# bd admin

**Purpose**: Provides administrative commands for maintaining and managing the bd database and configuration.

## When to use it

• **Database maintenance** — Clean up closed issues to reduce repository bloat
• **Storage optimization** — Compact historical data when the bd database grows large
• **Project resets** — Remove all bd data when starting fresh or abandoning issue tracking
• **Repository cleanup** — Prepare a project for archival or handover
• **Performance tuning** — Optimize bd performance after long-term usage
• **Troubleshooting** — Reset bd state when configuration becomes corrupted

## Key options

The `admin` command serves as a namespace for administrative sub-commands rather than having its own flags. Each sub-command has its own specific options for targeted maintenance tasks.

## Example workflows

**Regular maintenance cleanup:**
```bash
# Remove closed issues older than 30 days
bd admin cleanup --older-than 30d
```
This helps keep your repository lean by removing resolved issues that no longer need to be tracked, while preserving recent history for reference.

**Database optimization:**
```bash
# Compact old closed issues to save space
bd admin compact
# Reset everything for a fresh start
bd admin reset --confirm
```
The compact command reduces storage overhead by optimizing how closed issues are stored, while reset provides a nuclear option for starting over.

**Pre-archive repository cleanup:**
```bash
bd admin cleanup --all
bd admin compact
```
Before archiving a project, clean up all closed issues and compact the database to minimize the repository's final size.

## Tips & gotchas

• **Backup first** — Administrative commands can permanently delete data, so consider backing up your repository before running cleanup or reset operations
• **Coordination required** — Run admin commands when other team members aren't actively working with bd to avoid conflicts
• **Git history preserved** — Even after cleanup, issue data may still exist in git history until you rewrite or prune the repository
• **Irreversible operations** — Most admin commands cannot be undone, especially `reset` which removes all bd configuration and data

## Related commands

• **bd init** — Often used after `bd admin reset` to reinitialize bd in a project
• **bd status** — Check the current state before and after running admin commands  
• **bd list** — View remaining issues after cleanup operations
• **bd config** — May need reconfiguration after reset operations