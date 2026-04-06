# backup-status

**Purpose** — Shows the current state of your backup configuration and the synchronization status between your local bd repository and configured backup locations.

## When to use it

• Check if backups are properly configured before starting work
• Verify that recent changes have been synchronized to backup locations
• Troubleshoot backup connectivity issues
• Monitor backup health as part of regular maintenance
• Confirm backup status before making critical changes to issues

## Key options

| Flag | Description |
|------|-------------|
| `--verbose` | Show detailed sync information for each backup location |
| `--check-remote` | Actively test connectivity to remote backup services |
| `--format=json` | Output status information in JSON format for scripting |

## Example workflows

**Quick status check:**
```bash
bd backup status
```
Shows a summary of backup configuration and last sync times—useful for a daily workflow check.

**Detailed backup inspection:**
```bash
bd backup status --verbose --check-remote
```
Provides comprehensive backup health information including remote connectivity tests, ideal when troubleshooting sync issues or setting up new backup locations.

**Automated monitoring:**
```bash
bd backup status --format=json | jq '.last_sync'
```
Extracts specific backup metrics for integration with monitoring scripts or CI/CD pipelines.

## Tips & gotchas

• Status checks don't trigger synchronization—use `bd backup sync` if you need to update backups
• Remote connectivity tests may take several seconds depending on your backup service
• JSON output format is stable and recommended for scripting and automation
• Some backup services may show "pending" status during their own maintenance windows

## Related commands

• `bd backup sync` — Manually synchronize changes to backup locations
• `bd backup configure` — Set up or modify backup destination settings
• `bd status` — View overall repository status including local changes
• `bd log` — Review recent activity that may need backing up