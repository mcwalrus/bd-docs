# bd-docs

Produces `bd` commands flattened.

Generate structured Markdown documentation and AI-powered insights for every
command in the [`bd`](https://github.com/beads-sh/beads) (beads) issue tracker.

## What it produces

```
bd/
├── commands/
│   ├── index.md              ← root `bd --help`
│   ├── create.md
│   ├── create-form.md        ← sub-command
│   ├── epic.md
│   ├── epic-list.md          ← nested sub-command
│   └── …
├── insights/
│   ├── create.md             ← AI explanation of how to use create
│   ├── create-form.md
│   └── …
└── summary/
    ├── all-commands.md       ← every command page in one file (with TOC)
    └── insights.md           ← every insight in one file (with TOC)
```

## Prerequisites

- Python ≥ 3.11
- [`uv`](https://docs.astral.sh/uv/) installed (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- `bd` on your `PATH` (or specify `--bd-path`)
- `jq` installed (used to update harvest cache state)
- `ANTHROPIC_API_KEY` set in your environment (for the insights step)

## Quick start

```bash
# 1. Clone / cd into the project
cd bd-docs

# 2. Create a virtual environment and install deps (uv handles everything)
uv sync

# 3. Export your API key
export ANTHROPIC_API_KEY="sk-ant-…"

# 4. Run the full pipeline (all three phases)
uv run bd-docs

# The output lands in ./bd/ inside the current directory.
```

## Running individual phases

```bash
# Phase 1 — harvest bd help text → bd/commands/*.md
uv run bd-harvest

# Phase 2 — AI insights → bd/insights/*.md
uv run bd-insights

# Phase 3 — flatten → bd/summary/all-commands.md + bd/summary/insights.md
uv run bd-summarise
```

## Harvest cache

`bd-harvest` tracks every checked command chain in:

`bd/.cache/harvest-checked-commands.json`

The cache is updated using `jq` and records:
- command key (for example, `gate resolve`)
- slug (for example, `gate-resolve`)
- status (`checked`, `skipped`, or `error`)
- reason (for skipped/error states)
- timestamp

## Options

### `bd-docs` (full pipeline)

| Flag | Default | Description |
|------|---------|-------------|
| `--steps` | `all` | Which steps to run: `harvest`, `insights`, `summarise`, or `all` |
| `--bd-path` | `bd` | Path to the bd executable |
| `--out-dir` | `.` | Root directory for all output |
| `--concurrency` | `5` | Parallel Anthropic API calls during insights phase |

### `bd-harvest`

| Flag | Default | Description |
|------|---------|-------------|
| `--bd-path` | `bd` | Path to the bd executable |
| `--out-dir` | `.` | Root output directory |

### `bd-insights`

| Flag | Default | Description |
|------|---------|-------------|
| `--out-dir` | `.` | Root output directory |
| `--concurrency` | `5` | Parallel API calls |

### `bd-summarise`

| Flag | Default | Description |
|------|---------|-------------|
| `--out-dir` | `.` | Root output directory |

## Examples

```bash
# Use a bd binary that's not on PATH
uv run bd-docs --bd-path ~/bin/bd --out-dir ~/my-bd-docs

# Only run harvest (no API key needed)
uv run bd-docs --steps harvest

# Regenerate insights at higher concurrency
uv run bd-docs --steps insights --concurrency 10

# Only rebuild summaries after adding new insights manually
uv run bd-docs --steps summarise
```

## Architecture

```
src/bd_docs/
├── __init__.py
├── main.py        ← orchestrator (bd-docs entry point)
├── harvest.py     ← phase 1: run bd --help recursively
├── insights.py    ← phase 2: Anthropic API calls
└── summarise.py   ← phase 3: flatten into summary files
```

**harvest.py** discovers the command tree dynamically — it parses the help
output of each command to find sub-commands, so it works even if `bd` adds new
commands in the future.

**insights.py** uses a `ThreadPoolExecutor` to run multiple Anthropic API calls
concurrently, keeping wall-clock time low even with 100+ commands.

**summarise.py** re-levels Markdown headings so each command section nests
cleanly inside the summary documents.

## Tips

- The `bd/commands/` output is checked-in-friendly — commit it to your repo as
  living documentation.
- The `bd/summary/all-commands.md` file is ideal as a context document to paste
  into an AI assistant before asking questions about `bd`.
- Re-run with `--steps insights` after a `bd` upgrade to refresh the AI
  insights without re-harvesting.
