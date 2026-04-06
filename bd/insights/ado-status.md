# `bd ado status`

**Purpose**: Displays the Azure DevOps (ADO) synchronization status for issues in the current bd repository.

## When to use it

- Check which local bd issues are synced with Azure DevOps work items
- Verify sync status before pushing changes to ADO
- Troubleshoot sync issues or mismatched items
- Review ADO integration health after configuration changes
- Audit which issues need manual ADO sync intervention

## Key flags / options

| Flag | Description |
|------|-------------|
| `--all` | Show status for all issues, including those without ADO links |
| `--json` | Output status information in JSON format for scripting |
| `--verbose` | Display detailed sync metadata and timestamps |

## Example workflows

**Check overall sync status:**
```bash
bd ado status
```
Quick overview of which issues are synced, pending, or have sync conflicts with your ADO project.

**Generate detailed report for CI/CD:**
```bash
bd ado status --json --all > ado-sync-report.json
```
Exports comprehensive sync status in machine-readable format, useful for automated workflows or dashboard integrations.

**Debug specific sync issues:**
```bash
bd ado status --verbose
```
Shows detailed sync metadata including last sync timestamps, ADO work item IDs, and any error states to help diagnose sync problems.

## Tips & gotchas

- Status reflects the last attempted sync, not real-time ADO state
- Issues created locally but not yet pushed to ADO will show as "unsynced"
- Network connectivity issues may cause status to appear stale
- The command only shows status for issues in the current repository's ADO configuration
- Status may lag behind ADO changes made outside of bd until next sync

## Related commands

- `bd ado sync` — Actually synchronize issues with Azure DevOps
- `bd ado configure` — Set up or modify ADO integration settings
- `bd list` — View local issues that might need ADO sync
- `bd ado push` — Push specific issues to Azure DevOps