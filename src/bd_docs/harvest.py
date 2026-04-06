"""
harvest.py — Phase 1
====================
Walks the bd command tree by running `bd <cmd> --help` for every command and
sub-command, then writes structured Markdown files to:

    <out_dir>/bd/commands/<command>.md
    <out_dir>/bd/commands/<command>-<subcommand>.md
    ...

Subcommand discovery is done by parsing the "Available Commands:" or
"[command]" sections from each help output, so no hard-coded command list is
needed — the tree is discovered dynamically.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

_COMMAND_LINE_RE = re.compile(r"^\s{2}(\S+)\s{2,}(.+)$")
_GENERIC_SECTION_HEADER_RE = re.compile(r"^[A-Z][A-Za-z0-9 ()/_-]+:$")
_VALID_COMMAND_RE = re.compile(r"^[a-z0-9][a-z0-9:-]*$")
_NON_COMMAND_SECTION_KEYWORDS = {
    "usage",
    "flag",
    "flags",
    "global flags",
    "options",
    "arguments",
    "args",
    "example",
    "examples",
    "aliases",
}


def _run_help(bd_path: str, args: list[str]) -> str:
    """Run `bd [args...] --help` and return stdout+stderr merged."""
    cmd = [bd_path, *args, "--help"]
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=15,
        )
        return (result.stdout + result.stderr).strip()
    except (subprocess.TimeoutExpired, FileNotFoundError) as exc:
        console.print(f"[red]ERROR running {' '.join(cmd)}: {exc}[/red]")
        return ""


def _usage_matches_chain(help_text: str, cmd_chain: list[str]) -> bool:
    """
    Return True when `Usage:` appears to correspond to the exact command chain.

    This prevents recursing through pseudo-subcommands where `bd` falls back to
    a parent help page (e.g. `bd gate human --help` returning `bd gate [command]`).
    """
    in_usage = False
    for raw_line in help_text.splitlines():
        line = raw_line.strip()
        if line == "Usage:":
            in_usage = True
            continue
        if not in_usage:
            continue
        if not line:
            # End of usage block.
            break
        if not line.startswith("bd "):
            continue
        usage_tokens = line.split()
        # Compare only concrete command tokens and ignore placeholders like [flags].
        concrete = [tok for tok in usage_tokens[1:] if not tok.startswith("[") and not tok.startswith("<")]
        return concrete == cmd_chain
    return False


def _init_cache_file(cache_path: Path) -> None:
    if cache_path.exists():
        return
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text('{"checked_commands": {}}\n', encoding="utf-8")


def _update_cache(cache_path: Path, key: str, slug: str, status: str, reason: str = "") -> None:
    """Record command checks in cache, preferring jq for updates."""
    checked_at = datetime.now(timezone.utc).isoformat()
    _init_cache_file(cache_path)

    jq_cmd = [
        "jq",
        "--arg",
        "key",
        key,
        "--arg",
        "slug",
        slug,
        "--arg",
        "status",
        status,
        "--arg",
        "reason",
        reason,
        "--arg",
        "checked_at",
        checked_at,
        (
            ".checked_commands[$key] = "
            "{slug:$slug,status:$status,reason:$reason,checked_at:$checked_at}"
        ),
        str(cache_path),
    ]
    tmp_path = cache_path.with_suffix(".tmp")
    try:
        with tmp_path.open("w", encoding="utf-8") as tmp:
            result = subprocess.run(jq_cmd, check=True, capture_output=True, text=True)
            tmp.write(result.stdout)
        tmp_path.replace(cache_path)
        return
    except Exception:  # noqa: BLE001
        if tmp_path.exists():
            tmp_path.unlink()

    # Fallback: update with Python if jq is unavailable.
    data = json.loads(cache_path.read_text(encoding="utf-8"))
    checked = data.setdefault("checked_commands", {})
    checked[key] = {
        "slug": slug,
        "status": status,
        "reason": reason,
        "checked_at": checked_at,
    }
    cache_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def _is_valid_command_token(token: str) -> bool:
    """
    Accept only real command tokens.

    Reject flags / placeholders such as:
      --json, -h, <id>, [command], command..., COMMAND
    """
    if not token:
        return False
    if token.startswith("-") or "--" in token:
        return False
    if any(ch in token for ch in "<>[](){}=,"):
        return False
    if token.endswith("..."):
        return False
    if token.lower() in {"help", "completion"}:
        return False
    return bool(_VALID_COMMAND_RE.fullmatch(token))


def _is_command_section_header(header: str) -> bool:
    """Return True if a section header likely contains command listings."""
    cleaned = header.rstrip(":").strip().lower()
    return not any(keyword in cleaned for keyword in _NON_COMMAND_SECTION_KEYWORDS)


def _parse_subcommands(help_text: str, *, allow_fallback_sections: bool = False) -> list[tuple[str, str]]:
    """
    Extract only real sub-commands from command-list sections.
    """
    subs: list[tuple[str, str]] = []
    has_available_commands = "Available Commands:" in help_text
    in_command_section = False

    for line in help_text.splitlines():
        stripped = line.rstrip()
        if _GENERIC_SECTION_HEADER_RE.match(stripped):
            if has_available_commands:
                in_command_section = stripped == "Available Commands:"
            elif allow_fallback_sections:
                in_command_section = _is_command_section_header(stripped)
            else:
                in_command_section = False
            continue

        if in_command_section:
            m = _COMMAND_LINE_RE.match(line)
            if m:
                name, desc = m.group(1), m.group(2).strip()
                if _is_valid_command_token(name):
                    subs.append((name, desc))
    return subs


def _markdown_for(
    cmd_chain: list[str],
    help_text: str,
    subcommands: list[tuple[str, str]],
) -> str:
    """Render a Markdown document for a command."""
    title = " ".join(cmd_chain)
    slug = "-".join(cmd_chain)

    lines: list[str] = [
        f"# `bd {title}`",
        "",
        f"**Command:** `bd {title}`  ",
        f"**Slug:** `{slug}`",
        "",
        "## Help Output",
        "",
        "```",
        help_text,
        "```",
        "",
    ]

    if subcommands:
        lines += ["## Sub-commands", ""]
        for name, desc in subcommands:
            sub_slug = f"{slug}-{name}"
            lines.append(f"- [`bd {title} {name}`](./{sub_slug}.md) — {desc}")
        lines.append("")

    return "\n".join(lines)


# ──────────────────────────────────────────────────────────────────────────────
# Recursive walker
# ──────────────────────────────────────────────────────────────────────────────

def _walk(
    bd_path: str,
    cmd_chain: list[str],
    out_dir: Path,
    cache_path: Path,
    visited: set[str],
    generated_slugs: set[str],
    depth: int = 0,
    max_depth: int = 4,
) -> int:
    """Recursively harvest help for cmd_chain and all children."""
    if depth > max_depth:
        return 0

    key = " ".join(cmd_chain)
    slug = "-".join(cmd_chain)

    if key in visited:
        _update_cache(cache_path, key, slug, "skipped", "already-visited")
        return 0
    visited.add(key)

    help_text = _run_help(bd_path, cmd_chain)
    if not help_text:
        _update_cache(cache_path, key, slug, "error", "help-command-failed")
        return 0
    if not _usage_matches_chain(help_text, cmd_chain):
        _update_cache(cache_path, key, slug, "skipped", "usage-mismatch")
        return 0

    subcommands = _parse_subcommands(help_text)

    md_path = out_dir / f"{slug}.md"
    md_path.write_text(_markdown_for(cmd_chain, help_text, subcommands), encoding="utf-8")
    generated_slugs.add(slug)
    _update_cache(cache_path, key, slug, "checked", "")
    console.print(f"  [green]✓[/green] {md_path.relative_to(out_dir.parent.parent)}")

    count = 1
    for name, _desc in subcommands:
        count += _walk(
            bd_path,
            cmd_chain + [name],
            out_dir,
            cache_path,
            visited,
            generated_slugs,
            depth + 1,
            max_depth,
        )

    return count


# ──────────────────────────────────────────────────────────────────────────────
# Top-level help — discover root commands
# ──────────────────────────────────────────────────────────────────────────────

def _discover_root_commands(bd_path: str) -> list[tuple[str, str]]:
    """Parse `bd --help` to get the top-level command list."""
    help_text = _run_help(bd_path, [])
    if not help_text:
        console.print("[red]Could not run bd --help. Is bd installed and on PATH?[/red]")
        sys.exit(1)
    return _parse_subcommands(help_text, allow_fallback_sections=True)


# ──────────────────────────────────────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────────────────────────────────────

def run(bd_path: str = "bd", out_dir: str = ".") -> None:
    root = Path(out_dir)
    commands_dir = root / "bd" / "commands"
    cache_path = root / "bd" / ".cache" / "harvest-checked-commands.json"
    commands_dir.mkdir(parents=True, exist_ok=True)
    _init_cache_file(cache_path)

    console.print(f"[cyan]bd executable:[/cyan] {bd_path}")
    console.print(f"[cyan]Output dir:   [/cyan] {commands_dir}\n")

    # Write root help
    root_help = _run_help(bd_path, [])
    root_commands = _parse_subcommands(root_help, allow_fallback_sections=True)
    root_md = commands_dir / "index.md"
    root_md.write_text(_markdown_for([""], root_help, root_commands).replace("# `bd `", "# `bd`"), encoding="utf-8")
    _update_cache(cache_path, "bd", "index", "checked", "")
    console.print(f"  [green]✓[/green] {root_md.relative_to(root)}")

    visited: set[str] = set()
    generated_slugs: set[str] = {"index"}
    total = 1  # root

    for name, _desc in root_commands:
        total += _walk(bd_path, [name], commands_dir, cache_path, visited, generated_slugs)

    # Remove stale generated files from prior runs.
    removed = 0
    for path in commands_dir.glob("*.md"):
        if path.stem not in generated_slugs:
            path.unlink()
            removed += 1
    if removed:
        console.print(f"  [yellow]• Removed {removed} stale command pages[/yellow]")
    console.print(f"  [cyan]Cache:[/cyan] {cache_path.relative_to(root)}")

    console.print(f"\n[bold green]Harvested {total} command pages.[/bold green]")


def main() -> None:
    parser = argparse.ArgumentParser(description="Harvest bd help text into Markdown files.")
    parser.add_argument("--bd-path", default="bd")
    parser.add_argument("--out-dir", default=".")
    args = parser.parse_args()
    run(bd_path=args.bd_path, out_dir=args.out_dir)


if __name__ == "__main__":
    main()
