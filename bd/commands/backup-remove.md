# `bd backup remove`

**Command:** `bd backup remove`  
**Slug:** `backup-remove`

## Help Output

```
Remove the configured backup destination.

This unregisters the backup remote from Dolt and removes the local
backup configuration. The backup data at the destination is not deleted.

Usage:
  bd backup remove [flags]

Aliases:
  remove, rm

Flags:
  -h, --help   help for remove

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
```
