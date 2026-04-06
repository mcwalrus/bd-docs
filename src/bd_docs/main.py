"""
bd-docs: Full pipeline — harvest → insights → summarise
Run all three phases in sequence, or individual scripts separately.
"""

import sys
from rich.console import Console
from rich.panel import Panel

console = Console()


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        prog="bd-docs",
        description="Generate bd command docs, AI insights, and summary files.",
    )
    parser.add_argument(
        "--steps",
        nargs="+",
        choices=["harvest", "insights", "summarise", "all"],
        default=["all"],
        help="Which steps to run (default: all)",
    )
    parser.add_argument(
        "--bd-path",
        default="bd",
        help="Path to the bd executable (default: bd)",
    )
    parser.add_argument(
        "--out-dir",
        default=".",
        help="Root output directory (default: current dir). Subdirs bd/commands, bd/insights, bd/summary created inside.",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=5,
        help="Max parallel Anthropic API calls for insights (default: 5)",
    )
    args = parser.parse_args()

    steps = args.steps
    if "all" in steps:
        steps = ["harvest", "insights", "summarise"]

    console.print(
        Panel.fit(
            "[bold cyan]bd-docs[/bold cyan]  •  beads command documentation generator",
            border_style="cyan",
        )
    )

    if "harvest" in steps:
        console.rule("[bold]Step 1 — Harvest help text[/bold]")
        from bd_docs.harvest import run as harvest_run
        harvest_run(bd_path=args.bd_path, out_dir=args.out_dir)

    if "insights" in steps:
        console.rule("[bold]Step 2 — Generate AI insights[/bold]")
        from bd_docs.insights import run as insights_run
        insights_run(out_dir=args.out_dir, concurrency=args.concurrency)

    if "summarise" in steps:
        console.rule("[bold]Step 3 — Build summary files[/bold]")
        from bd_docs.summarise import run as summarise_run
        summarise_run(out_dir=args.out_dir)

    console.print("\n[bold green]✓ Done![/bold green]")


if __name__ == "__main__":
    main()
