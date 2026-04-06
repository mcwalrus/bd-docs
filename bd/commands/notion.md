# `bd notion`

**Command:** `bd notion`  
**Slug:** `notion`

## Help Output

```
Commands for syncing issues between beads and Notion.

Usage:
  bd notion [command]

Available Commands:
  connect     Connect bd to an existing Notion database or data source
  init        Create a dedicated Beads database in Notion
  status      Show Notion sync status
  sync        Sync issues with Notion

Flags:
  -h, --help   help for notion

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

Use "bd notion [command] --help" for more information about a command.
```

## Sub-commands

- [`bd notion connect`](./notion-connect.md) — Connect bd to an existing Notion database or data source
- [`bd notion init`](./notion-init.md) — Create a dedicated Beads database in Notion
- [`bd notion status`](./notion-status.md) — Show Notion sync status
- [`bd notion sync`](./notion-sync.md) — Sync issues with Notion
