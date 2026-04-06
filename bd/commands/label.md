# `bd label`

**Command:** `bd label`  
**Slug:** `label`

## Help Output

```
Manage issue labels

Usage:
  bd label [command]

Available Commands:
  add         Add a label to one or more issues
  list        List labels for an issue
  list-all    List all unique labels in the database
  propagate   Propagate a label from a parent issue to all its children
  remove      Remove a label from one or more issues

Flags:
  -h, --help   help for label

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

Use "bd label [command] --help" for more information about a command.
```

## Sub-commands

- [`bd label add`](./label-add.md) — Add a label to one or more issues
- [`bd label list`](./label-list.md) — List labels for an issue
- [`bd label list-all`](./label-list-all.md) — List all unique labels in the database
- [`bd label propagate`](./label-propagate.md) — Propagate a label from a parent issue to all its children
- [`bd label remove`](./label-remove.md) — Remove a label from one or more issues
