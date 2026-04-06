# bd ado

**Purpose** — Manages synchronization and integration between bd (beads) and Azure DevOps work items.

## When to use it

• Working in teams that use Azure DevOps for project management
• Need to sync local bd issues with remote Azure DevOps work items
• Want to check connectivity and sync status with Azure DevOps
• Managing multiple Azure DevOps projects from a single repository
• Bridging between local development workflow and enterprise tooling
• Maintaining traceability between code changes and work items

## Key flags / options

Since this is a parent command, flags are handled by the sub-commands:
- `projects` — Lists all accessible Azure DevOps projects
- `status` — Shows current sync configuration and connection state
- `sync` — Performs bidirectional synchronization of issues

## Example workflows

**Check Azure DevOps connectivity:**
```bash
bd ado status
bd ado projects
```
Verify your Azure DevOps connection is working and see which projects you can access before attempting any sync operations.

**Initial setup and sync:**
```bash
bd ado projects  # Find your project
bd ado sync      # Perform initial sync
bd ado status    # Verify sync completed successfully
```
Common workflow when first connecting a bd repository to an existing Azure DevOps project with work items.

**Regular maintenance:**
```bash
bd ado sync
bd status        # Check local bd state
```
Periodic sync to keep local issues aligned with remote work items, typically run before starting new work or during standup preparation.

## Tips & gotchas

• Run `bd ado status` first to ensure proper Azure DevOps authentication and project access before attempting sync operations
• The sync process is bidirectional — changes in either bd or Azure DevOps will be reflected in both systems
• Large projects may take time to sync initially; subsequent syncs are typically faster due to incremental updates
• Authentication tokens may expire; check status if sync operations start failing

## Related commands

• `bd status` — Check overall bd repository state after Azure DevOps sync
• `bd list` — View synced issues locally after running ado sync  
• `bd show` — Examine individual issues that may have been updated from Azure DevOps
• `bd new` — Create issues that can be synced to Azure DevOps work items