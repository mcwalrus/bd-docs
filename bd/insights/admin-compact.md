# bd admin compact

**Purpose** — Removes unused blobs and reduces repository size by cleaning up orphaned issue data and optimizing storage.

## When to use it

• After deleting many issues or comments to reclaim disk space
• Before archiving or backing up a project repository
• When repository size has grown unexpectedly large
• As part of regular maintenance on long-running projects
• Before migrating issues to a different system
• When experiencing performance issues due to repository bloat

## Key flags / options

| Flag | Description |
|------|-------------|
| `--dry-run` | Preview what would be removed without making changes |
| `--force` | Skip confirmation prompts for automated scripts |
| `--verbose` | Show detailed output of cleanup operations |

## Example workflows

**Basic cleanup after issue deletion:**
```bash
bd admin compact --dry-run
# Review what will be cleaned up
bd admin compact
# Confirm and proceed with actual cleanup
```

**Automated maintenance in CI/CD:**
```bash
bd admin compact --force --verbose
# Clean up repository size in automated workflows
# Verbose output helps with debugging if needed
```

**Pre-migration cleanup:**
```bash
bd admin compact --dry-run --verbose
# Get detailed view of repository bloat
bd admin compact --force
# Clean repository before exporting data
```

## Tips & gotchas

• Always run with `--dry-run` first to preview changes — compacting is irreversible
• This command only affects bd's internal data structures, not your main git repository
• Compacting is safe to run anytime but provides most benefit after bulk deletions
• Large repositories may take several minutes to compact completely
• The command preserves all active issues and their full history

## Related commands

• **`bd status`** — Check repository health before compacting
• **`bd admin stats`** — View repository size metrics to determine if compacting is needed
• **`bd admin backup`** — Create backups before major maintenance operations
• **`bd admin migrate`** — Often used after compacting when moving between systems