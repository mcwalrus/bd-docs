# bd backup

**Purpose** — Manages database backups to Dolt remote repositories for your bd issue tracker.

## When to use it

• Setting up automated backups for your issue database
• Restoring from backups after data corruption or accidental changes
• Syncing issue data across multiple development environments
• Creating redundant copies of critical project tracking data
• Migrating bd databases between systems or team members
• Implementing disaster recovery for long-running projects

## Key commands

| Command | Purpose |
|---------|---------|
| `bd backup init` | Configure a new Dolt remote as backup destination |
| `bd backup sync` | Push current database state to the backup remote |
| `bd backup restore` | Pull and restore database from backup remote |
| `bd backup status` | Check when last backup was performed |
| `bd backup remove` | Disconnect the current backup configuration |

## Example workflows

**Set up team backup repository:**
```bash
bd backup init --remote https://dolthub.com/myteam/project-issues
bd backup sync
```
Creates a backup destination and performs the initial sync to share your issue database with the team.

**Restore from backup after corruption:**
```bash
bd backup status  # Check last backup date
bd backup restore --force
```
Overwrites your local database with the latest backup version, useful when local data becomes corrupted.

**Regular maintenance sync:**
```bash
bd backup sync
```
Pushes recent issue updates to the backup remote, typically run after major milestones or daily as part of automated workflows.

## Tips & gotchas

• The backup system requires Dolt to be installed and configured separately from bd
• Initial `backup init` may require authentication credentials for your Dolt remote
• `backup restore` is destructive and will overwrite local changes unless you use appropriate flags
• Backup operations can be slow for large issue databases, especially on first sync
• Consider running `backup status` before `restore` to understand what you're reverting to

## Related commands

• `bd init` — Initialize the local database that backups will preserve
• `bd export` — Alternative data export method for non-Dolt destinations  
• `bd import` — Import issues when migrating between backup systems
• `bd status` — Check local database state before/after backup operations