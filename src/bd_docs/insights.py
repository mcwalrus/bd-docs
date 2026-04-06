"""
insights.py — Phase 2
=====================
For every Markdown file under bd/commands/, calls the Anthropic API to produce
a practical "how this command is useful" insight and writes it to:

    <out_dir>/bd/insights/<same-slug>.md

Runs up to `concurrency` API calls in parallel using asyncio + threading so
the process is fast even with hundreds of commands.
"""

from __future__ import annotations

import argparse
import os
import re
import textwrap
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import anthropic
from rich.console import Console
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    SpinnerColumn,
    TaskID,
    TextColumn,
    TimeElapsedColumn,
)

console = Console()

# ──────────────────────────────────────────────────────────────────────────────
# Prompt
# ──────────────────────────────────────────────────────────────────────────────

SYSTEM_PROMPT = textwrap.dedent("""
    You are a technical writer and developer-experience expert.
    You are documenting `bd` (beads), a lightweight, git-native issue tracker
    with first-class dependency support designed for use inside coding projects
    and with AI agents.

    Given the raw --help output for a bd command, write a concise, practical
    Markdown insight document explaining:

    1. **Purpose** — what this command does in one sentence.
    2. **When to use it** — concrete scenarios (bullet list, ≤6 items).
    3. **Key flags / options** — the most important flags with a one-line
       explanation for each (table format preferred).
    4. **Example workflows** — 2–3 short shell snippets showing real usage
       with brief prose explaining each.
    5. **Tips & gotchas** — any non-obvious behaviour or common mistakes.
    6. **Related commands** — mention 2–4 commands that are commonly used
       alongside this one.

    Keep the total length between 300 and 600 words.
    Use clear, direct language aimed at a developer audience.
    Do NOT reproduce the raw help text verbatim — synthesise it.
    Format output as clean Markdown starting with a level-1 heading.
""").strip()


def _make_user_prompt(slug: str, help_md_content: str) -> str:
    # Strip the fenced help block so we give raw help text
    raw_help = re.sub(r"```.*?```", "", help_md_content, flags=re.DOTALL).strip()
    return f"Command slug: `{slug}`\n\nHelp output:\n\n{raw_help}"


# ──────────────────────────────────────────────────────────────────────────────
# API call (blocking — runs in thread pool)
# ──────────────────────────────────────────────────────────────────────────────

def _call_api(client: anthropic.Anthropic, slug: str, help_content: str) -> str:
    """Blocking call to Anthropic. Returns insight Markdown."""
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": _make_user_prompt(slug, help_content),
            }
        ],
    )
    return message.content[0].text


def _insight_markdown(slug: str, insight: str) -> str:
    return insight  # Already well-formed Markdown from the model


# ──────────────────────────────────────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────────────────────────────────────

def run(out_dir: str = ".", concurrency: int = 5) -> None:
    root = Path(out_dir)
    commands_dir = root / "bd" / "commands"
    insights_dir = root / "bd" / "insights"
    insights_dir.mkdir(parents=True, exist_ok=True)

    command_files = sorted(commands_dir.glob("*.md"))
    if not command_files:
        console.print(
            "[yellow]No command files found. Run harvest first.[/yellow]"
        )
        return

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        console.print(
            "[red]ANTHROPIC_API_KEY not set. Export it before running insights.[/red]"
        )
        return

    client = anthropic.Anthropic(api_key=api_key)

    console.print(
        f"[cyan]Generating insights for {len(command_files)} commands "
        f"(concurrency={concurrency})…[/cyan]\n"
    )

    errors: list[str] = []
    generated_slugs: set[str] = set()

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        TimeElapsedColumn(),
        console=console,
        transient=False,
    ) as progress:
        task = progress.add_task("Insights", total=len(command_files))

        with ThreadPoolExecutor(max_workers=concurrency) as executor:
            future_to_file = {
                executor.submit(
                    _call_api,
                    client,
                    f.stem,
                    f.read_text(encoding="utf-8"),
                ): f
                for f in command_files
            }

            for future in as_completed(future_to_file):
                src_file = future_to_file[future]
                slug = src_file.stem
                try:
                    insight = future.result()
                    out_path = insights_dir / f"{slug}.md"
                    out_path.write_text(_insight_markdown(slug, insight), encoding="utf-8")
                    generated_slugs.add(slug)
                    progress.advance(task)
                except Exception as exc:  # noqa: BLE001
                    errors.append(f"{slug}: {exc}")
                    progress.advance(task)

    # Remove stale insights when command pages were removed/renamed.
    removed = 0
    for path in insights_dir.glob("*.md"):
        if path.stem not in generated_slugs:
            path.unlink()
            removed += 1
    if removed:
        console.print(f"[yellow]Removed {removed} stale insight files.[/yellow]")

    if errors:
        console.print(f"\n[red]Errors ({len(errors)}):[/red]")
        for e in errors:
            console.print(f"  [red]• {e}[/red]")
    else:
        console.print(
            f"\n[bold green]✓ {len(command_files)} insight files written.[/bold green]"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate AI insights for bd commands.")
    parser.add_argument("--out-dir", default=".")
    parser.add_argument("--concurrency", type=int, default=5)
    args = parser.parse_args()
    run(out_dir=args.out_dir, concurrency=args.concurrency)


if __name__ == "__main__":
    main()
