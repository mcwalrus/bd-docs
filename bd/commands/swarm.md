# `bd swarm`

**Command:** `bd swarm`  
**Slug:** `swarm`

## Help Output

```
Swarm management commands for coordinating parallel work on epics.

A swarm is a structured body of work defined by an epic and its children,
with dependencies forming a DAG (directed acyclic graph) of work.

Usage:
  bd swarm [command]

Available Commands:
  create      Create a swarm molecule from an epic
  list        List all swarm molecules
  status      Show current swarm status
  validate    Validate epic structure for swarming

Flags:
  -h, --help   help for swarm

Global Flags:
      --actor string              Actor name for audit trail (default: $BEADS_ACTOR, git user.name, $USER)
      --db string                 Database path (default: auto-discover .beads/*.db)
      --dolt-auto-commit string   Dolt auto-commit policy (off|on|batch). 'on': commit after each write. 'batch': defer commits to bd dolt commit; uncommitted changes persist in the working set until then. SIGTERM/SIGHUP flush pending batch commits. Default: off. Override via config key dolt.auto-commit
      --json                      Output in JSON format
      --profile                   Generate CPU profile for performance analysis
  -q, --quiet                     Suppress non-essential output (errors only)
      --readonly                  Read-only mode: block write operations (for worker sandboxes)
      --sandbox                   Sandbox mode: disables auto-sync
  -v, --verbose                   Enable verbose/debug output

Use "bd swarm [command] --help" for more information about a command.
```

## Sub-commands

- [`bd swarm create`](./swarm-create.md) — Create a swarm molecule from an epic
- [`bd swarm list`](./swarm-list.md) — List all swarm molecules
- [`bd swarm status`](./swarm-status.md) — Show current swarm status
- [`bd swarm validate`](./swarm-validate.md) — Validate epic structure for swarming
