# bd backup restore

**Purpose**: Restores a bd repository from a previously created backup, recovering all beads, metadata, and configuration.

## When to use it

- Recovering from catastrophic data loss or corruption
- Setting up bd in a new environment from an existing backup
- Testing backup integrity by performing restore operations
- Migrating bd data between different systems or repositories
- Rolling back to a known good state after problematic changes

## Key flags / options

| Flag | Description |
|------|-------------|
| `--force` | Overwrite existing bd data without confirmation prompts |
| `--verify` | Validate backup integrity before restoring |
| `--partial` | Restore only specific components (beads, config, etc.) |
| `--dry-run` | Preview what would be restored without making changes |

## Example workflows

**Basic restore from backup file:**
```bash
bd backup restore my-project-backup.tar.gz
```
Restores the entire bd repository from a compressed backup archive, prompting for confirmation if existing data would be overwritten.

**Safe restore with verification:**
```bash
bd backup restore --verify --dry-run backup-2024-01-15.tar.gz
bd backup restore --verify backup-2024-01-15.tar.gz
```
First previews the restore operation and validates backup integrity, then performs the actual restore with confidence.

**Force restore in automated environments:**
```bash
bd backup restore --force production-backup.tar.gz
```
Performs an unattended restore, automatically overwriting any existing bd data—useful for deployment scripts or disaster recovery automation.

## Tips & gotchas

- Always verify backup integrity before restoring, especially for critical data recovery scenarios
- The restore process overwrites existing bd data by default—use `--dry-run` first to preview changes
- Restored beads maintain their original IDs and dependency relationships, ensuring consistency
- Git history and commits are preserved during restore, maintaining full project traceability
- Large backups may take time to restore; consider using `--partial` for incremental recovery

## Related commands

- `bd backup create` — Create backups that can later be restored
- `bd init` — Initialize a new bd repository (often used before restore)
- `bd status` — Verify repository state after restore completion
- `bd validate` — Check repository integrity post-restore