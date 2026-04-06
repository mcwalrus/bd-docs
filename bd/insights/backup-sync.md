# bd backup sync

**Purpose**: Synchronizes your local issue data with configured backup destinations to ensure your beads repository state is safely stored elsewhere.

## When to use it

• After making significant changes to issues (creation, updates, or status changes)
• Before major project milestones or releases
• As part of automated CI/CD workflows to maintain backup consistency
• When switching between development environments
• Before performing potentially destructive operations on the repository
• On a scheduled basis for regular backup maintenance

## Key flags / options

| Flag | Description |
|------|-------------|
| `--dry-run` | Preview what would be synchronized without making actual changes |
| `--force` | Override safety checks and force synchronization even with conflicts |
| `--destination <name>` | Sync only to a specific configured backup destination |
| `--verbose` | Show detailed progress information during the sync process |

## Example workflows

**Basic sync to all destinations:**
```bash
bd backup sync
```
Pushes your current beads state to all configured backup locations, ensuring remote copies are up-to-date with local changes.

**Preview changes before syncing:**
```bash
bd backup sync --dry-run --verbose
```
Shows exactly what would be synchronized without making changes, useful for verifying backup state before committing to the operation.

**Emergency sync with conflict resolution:**
```bash
bd backup sync --force --destination production
```
Forces synchronization to a specific backup destination, overriding any detected conflicts - typically used when you're confident local state should take precedence.

## Tips & gotchas

The sync operation respects your git history, so ensure your beads changes are committed before syncing. Uncommitted modifications may not be included in the backup. If you encounter sync conflicts, examine the conflicting state carefully before using `--force`, as this can overwrite important backup data. The command will fail gracefully if backup destinations are unreachable, allowing you to continue working offline.

## Related commands

• `bd backup add` - Configure new backup destinations
• `bd backup status` - Check current backup configuration and sync status  
• `bd status` - Review local issue state before backing up
• `bd commit` - Ensure changes are committed before synchronization