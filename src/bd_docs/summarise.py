"""
summarise.py — Phase 3
======================
Reads all files under bd/commands/ and bd/insights/ and produces:

    <out_dir>/bd/summary/all-commands.md   — every command page concatenated
                                              with a TOC
    <out_dir>/bd/summary/insights.md       — AI insight for every command,
                                              concatenated with a TOC and
                                              brief section headers

The summary files are designed to be readable as standalone documents and are
also useful as context to feed into an LLM.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from datetime import datetime, timezone

from rich.console import Console

console = Console()

# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

def _slug_to_title(slug: str) -> str:
    """Convert 'create-form' → 'bd create form'."""
    parts = slug.replace("-", " ").split()
    return "bd " + " ".join(parts)


def _extract_first_paragraph(md: str) -> str:
    """Pull the first non-heading, non-empty paragraph from Markdown."""
    lines = md.splitlines()
    buf: list[str] = []
    started = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            if started:
                break
            continue
        if stripped == "":
            if started:
                break
            continue
        buf.append(stripped)
        started = True
    return " ".join(buf)


def _anchor(slug: str) -> str:
    return slug.replace("-", "--").lower()


# ──────────────────────────────────────────────────────────────────────────────
# Build all-commands.md
# ──────────────────────────────────────────────────────────────────────────────

def _build_all_commands(commands_dir: Path, out_path: Path) -> int:
    files = sorted(commands_dir.glob("*.md"))
    if not files:
        console.print("[yellow]No command files found to summarise.[/yellow]")
        return 0

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    header = [
        "# bd — All Commands Reference",
        "",
        f"> Auto-generated on {now}  ",
        f"> Total commands: {len(files)}",
        "",
        "---",
        "",
        "## Table of Contents",
        "",
    ]

    toc_lines: list[str] = []
    sections: list[str] = []

    for f in files:
        slug = f.stem
        title = _slug_to_title(slug)
        anchor = _anchor(slug)
        toc_lines.append(f"- [`{title}`](#{anchor})")

        content = f.read_text(encoding="utf-8")
        # Re-level headings: h1→h2, h2→h3, etc. to nest inside summary
        releveled = re.sub(r"^(#{1,5})", lambda m: "#" + m.group(1), content, flags=re.MULTILINE)

        sections.append(f"---\n\n## {title}\n\n{releveled}\n")

    body = "\n".join(header + toc_lines + ["", "---", ""] + sections)
    out_path.write_text(body, encoding="utf-8")
    return len(files)


# ──────────────────────────────────────────────────────────────────────────────
# Build insights.md
# ──────────────────────────────────────────────────────────────────────────────

def _build_insights(insights_dir: Path, commands_dir: Path, out_path: Path) -> int:
    insight_by_slug = {f.stem: f for f in insights_dir.glob("*.md")}
    command_slugs = {f.stem for f in commands_dir.glob("*.md")}
    files = [insight_by_slug[slug] for slug in sorted(command_slugs) if slug in insight_by_slug]
    stale_count = len(set(insight_by_slug) - command_slugs)

    if not files:
        console.print(
            "[yellow]No insight files found. Run insights step first.[/yellow]"
        )
        return 0

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    header = [
        "# bd — AI Insights for All Commands",
        "",
        f"> Auto-generated on {now}  ",
        f"> Total insights: {len(files)}",
        "",
        "Each section explains how a `bd` command is practically useful,",
        "including real-world scenarios, key flags, and example workflows.",
        "",
        "---",
        "",
        "## Table of Contents",
        "",
    ]

    toc_lines: list[str] = []
    sections: list[str] = []

    for f in files:
        slug = f.stem
        title = _slug_to_title(slug)
        anchor = _anchor(slug)
        toc_lines.append(f"- [`{title}`](#{anchor})")

        content = f.read_text(encoding="utf-8")
        # Re-level so headings fit inside the summary structure
        releveled = re.sub(r"^(#{1,5})", lambda m: "#" + m.group(1), content, flags=re.MULTILINE)

        sections.append(f"---\n\n## {title}\n\n{releveled}\n")

    body = "\n".join(header + toc_lines + ["", "---", ""] + sections)
    out_path.write_text(body, encoding="utf-8")
    if stale_count:
        console.print(
            f"  [yellow]• Ignored {stale_count} stale insight files not in current command set[/yellow]"
        )
    return len(files)


# ──────────────────────────────────────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────────────────────────────────────

def run(out_dir: str = ".") -> None:
    root = Path(out_dir)
    commands_dir = root / "bd" / "commands"
    insights_dir = root / "bd" / "insights"
    summary_dir = root / "bd" / "summary"
    summary_dir.mkdir(parents=True, exist_ok=True)

    all_commands_path = summary_dir / "all-commands.md"
    insights_path = summary_dir / "insights.md"

    n_cmds = _build_all_commands(commands_dir, all_commands_path)
    console.print(
        f"  [green]✓[/green] {all_commands_path.relative_to(root)} "
        f"({n_cmds} commands)"
    )

    n_insights = _build_insights(insights_dir, commands_dir, insights_path)
    if n_insights:
        console.print(
            f"  [green]✓[/green] {insights_path.relative_to(root)} "
            f"({n_insights} insights)"
        )

    console.print(f"\n[bold green]Summary files written to {summary_dir}[/bold green]")


def main() -> None:
    parser = argparse.ArgumentParser(description="Flatten bd docs into summary files.")
    parser.add_argument("--out-dir", default=".")
    args = parser.parse_args()
    run(out_dir=args.out_dir)


if __name__ == "__main__":
    main()
