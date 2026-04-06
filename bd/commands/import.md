# `bd import`

**Command:** `bd import`  
**Slug:** `import`

## Help Output

```
Import issues from a JSONL file (newline-delimited JSON) into the database.

If no file is specified, imports from .beads/issues.jsonl (the git-tracked
export). This is the incremental counterpart to 'bd export': new issues are
created and existing issues are updated (upsert semantics).

Memory records (lines with "_type":"memory") are automatically detected and
imported as persistent memories (equivalent to 'bd remember'). This makes
'bd export | bd import' a full round-trip for both issues and memories.

This command makes the git-tracked JSONL portable again — after 'git pull'
brings new issues, 'bd import' loads them into the local Dolt database.

EXAMPLES:
  bd import                        # Import from .beads/issues.jsonl
  bd import backup.jsonl           # Import from a specific file
  bd import --dry-run              # Show what would be imported

Usage:
  bd import [file] [flags]

Flags:
      --dry-run   Show what would be imported without importing
  -h, --help      help for import

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
