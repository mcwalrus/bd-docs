# `bd backup`

**Command:** `bd backup`  
**Slug:** `backup`

## Help Output

```
Back up your beads database for off-machine recovery.

Commands:
  bd backup init <path>    Set up a backup destination (filesystem or DoltHub)
  bd backup sync           Push to configured backup destination
  bd backup restore [path] Restore from a backup directory
  bd backup remove         Remove backup destination
  bd backup status         Show backup status

DoltHub is recommended for cloud backup:
  bd backup init https://doltremoteapi.dolthub.com/<user>/<repo>
  Set DOLT_REMOTE_USER and DOLT_REMOTE_PASSWORD for authentication.

Usage:
  bd backup [command]

Available Commands:
  init        Set up a Dolt backup destination
  remove      Remove the configured backup destination
  restore     Restore database from a Dolt backup
  status      Show last backup status
  sync        Push database to configured Dolt backup

Flags:
  -h, --help   help for backup

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

Use "bd backup [command] --help" for more information about a command.
```

## Sub-commands

- [`bd backup init`](./backup-init.md) — Set up a Dolt backup destination
- [`bd backup remove`](./backup-remove.md) — Remove the configured backup destination
- [`bd backup restore`](./backup-restore.md) — Restore database from a Dolt backup
- [`bd backup status`](./backup-status.md) — Show last backup status
- [`bd backup sync`](./backup-sync.md) — Push database to configured Dolt backup
