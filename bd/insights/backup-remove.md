# bd backup remove

**Purpose**: Removes previously created backup snapshots of your bd issue tracker state.

## When to use it

- Clean up old backups after successful migrations or major changes
- Free up disk space by removing unnecessary backup files
- Remove corrupted or incomplete backup snapshots
- Maintain a tidy backup history by keeping only recent snapshots
- Clear backups before archiving or transferring a project

## Key flags / options

Since no help output was provided, this command likely follows bd's standard pattern of accepting backup identifiers or timestamps to specify which backups to remove.

## Example workflows

**Remove a specific backup:**
```bash
bd backup remove backup-2024-01-15-143022
```
Clean up a backup created before a major refactoring that's no longer needed.

**Interactive cleanup:**
```bash
bd backup list
bd backup remove backup-2024-01-10-091543
```
First review available backups, then remove the ones you no longer need.

**Bulk cleanup (if supported):**
```bash
bd backup remove --older-than=30d
```
Remove all backups older than 30 days to maintain a rolling backup window.

## Tips & gotchas

- **No undo**: Once removed, backup snapshots cannot be recovered—ensure you don't need them before deletion
- **Verify first**: Use `bd backup list` to confirm you're removing the correct backup
- **Keep recent backups**: Always maintain at least one recent backup before removing others
- **Storage location**: Backups are typically stored in `.bd/backups/` but removal is handled through bd commands, not direct file deletion

## Related commands

- **`bd backup create`** — Create new backup snapshots before making changes
- **`bd backup list`** — View available backups to identify candidates for removal  
- **`bd backup restore`** — Restore from a backup (verify you have alternatives before removing)
- **`bd backup verify`** — Check backup integrity before deciding to remove