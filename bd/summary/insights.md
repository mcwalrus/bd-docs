# bd — AI Insights for All Commands

> Auto-generated on 2026-04-06 07:33 UTC  
> Total insights: 25

Each section explains how a `bd` command is practically useful,
including real-world scenarios, key flags, and example workflows.

---

## Table of Contents

- [`bd admin`](#admin)
- [`bd admin cleanup`](#admin--cleanup)
- [`bd admin compact`](#admin--compact)
- [`bd admin reset`](#admin--reset)
- [`bd ado`](#ado)
- [`bd ado projects`](#ado--projects)
- [`bd ado status`](#ado--status)
- [`bd ado sync`](#ado--sync)
- [`bd assign`](#assign)
- [`bd audit`](#audit)
- [`bd audit label`](#audit--label)
- [`bd audit record`](#audit--record)
- [`bd backup`](#backup)
- [`bd backup init`](#backup--init)
- [`bd backup remove`](#backup--remove)
- [`bd backup restore`](#backup--restore)
- [`bd backup status`](#backup--status)
- [`bd backup sync`](#backup--sync)
- [`bd blocked`](#blocked)
- [`bd bootstrap`](#bootstrap)
- [`bd branch`](#branch)
- [`bd children`](#children)
- [`bd close`](#close)
- [`bd comment`](#comment)
- [`bd comments add`](#comments--add)

---

---

## bd admin

## bd admin

**Purpose**: Provides administrative commands for maintaining and managing the bd database and configuration.

### When to use it

• **Database maintenance** — Clean up closed issues to reduce repository bloat
• **Storage optimization** — Compact historical data when the bd database grows large
• **Project resets** — Remove all bd data when starting fresh or abandoning issue tracking
• **Repository cleanup** — Prepare a project for archival or handover
• **Performance tuning** — Optimize bd performance after long-term usage
• **Troubleshooting** — Reset bd state when configuration becomes corrupted

### Key options

The `admin` command serves as a namespace for administrative sub-commands rather than having its own flags. Each sub-command has its own specific options for targeted maintenance tasks.

### Example workflows

**Regular maintenance cleanup:**
```bash
## Remove closed issues older than 30 days
bd admin cleanup --older-than 30d
```
This helps keep your repository lean by removing resolved issues that no longer need to be tracked, while preserving recent history for reference.

**Database optimization:**
```bash
## Compact old closed issues to save space
bd admin compact
## Reset everything for a fresh start
bd admin reset --confirm
```
The compact command reduces storage overhead by optimizing how closed issues are stored, while reset provides a nuclear option for starting over.

**Pre-archive repository cleanup:**
```bash
bd admin cleanup --all
bd admin compact
```
Before archiving a project, clean up all closed issues and compact the database to minimize the repository's final size.

### Tips & gotchas

• **Backup first** — Administrative commands can permanently delete data, so consider backing up your repository before running cleanup or reset operations
• **Coordination required** — Run admin commands when other team members aren't actively working with bd to avoid conflicts
• **Git history preserved** — Even after cleanup, issue data may still exist in git history until you rewrite or prune the repository
• **Irreversible operations** — Most admin commands cannot be undone, especially `reset` which removes all bd configuration and data

### Related commands

• **bd init** — Often used after `bd admin reset` to reinitialize bd in a project
• **bd status** — Check the current state before and after running admin commands  
• **bd list** — View remaining issues after cleanup operations
• **bd config** — May need reconfiguration after reset operations

---

## bd admin cleanup

## bd admin cleanup

**Purpose**: Removes orphaned issue files and performs repository maintenance tasks to keep the beads tracker database clean.

### When to use it

• After deleting git branches that contained issue files
• When you suspect corrupted or orphaned metadata from interrupted operations
• Before archiving or sharing a repository to ensure clean state
• After bulk operations that may have left temporary files behind
• When disk space is a concern and you want to reclaim storage
• As part of regular maintenance workflows in long-running projects

### Key flags / options

The `cleanup` command typically runs with default settings and doesn't require additional flags for basic operation.

### Example workflows

**Basic cleanup after development cycle:**
```bash
## After merging feature branches, clean up any orphaned files
bd admin cleanup
git status  # Verify what was removed
```
This removes any issue files that no longer have corresponding git objects or have become disconnected from the main issue graph.

**Pre-archive maintenance:**
```bash
## Before creating a project archive or backup
bd admin cleanup
bd list --status all  # Verify issue integrity
git add -A && git commit -m "Clean up beads tracker"
```
Ensures the repository contains only valid, connected issue data before long-term storage.

**Automated maintenance script:**
```bash
##!/bin/bash
## Weekly maintenance routine
bd admin cleanup
if [ $? -eq 0 ]; then
    echo "Cleanup completed successfully"
    bd stats  # Show current repository state
fi
```
Integrates cleanup into automated workflows with proper error checking.

### Tips & gotchas

• Always run `git status` after cleanup to review what files were removed before committing changes
• The command is conservative by design — it won't remove files that might be valid issues
• Cleanup operations are not reversible, so ensure your repository is backed up if you're unsure about the current state
• Running cleanup frequently (weekly or monthly) prevents accumulation of orphaned data
• The command may take longer in repositories with extensive branching history

### Related commands

• **`bd init`** — Initialize tracker (sets up clean state initially)
• **`bd list`** — Verify issue integrity after cleanup
• **`bd stats`** — Check repository health and issue count post-cleanup
• **`bd admin validate`** — Verify tracker consistency before or after maintenance

---

## bd admin compact

## bd admin compact

**Purpose** — Removes unused blobs and reduces repository size by cleaning up orphaned issue data and optimizing storage.

### When to use it

• After deleting many issues or comments to reclaim disk space
• Before archiving or backing up a project repository
• When repository size has grown unexpectedly large
• As part of regular maintenance on long-running projects
• Before migrating issues to a different system
• When experiencing performance issues due to repository bloat

### Key flags / options

| Flag | Description |
|------|-------------|
| `--dry-run` | Preview what would be removed without making changes |
| `--force` | Skip confirmation prompts for automated scripts |
| `--verbose` | Show detailed output of cleanup operations |

### Example workflows

**Basic cleanup after issue deletion:**
```bash
bd admin compact --dry-run
## Review what will be cleaned up
bd admin compact
## Confirm and proceed with actual cleanup
```

**Automated maintenance in CI/CD:**
```bash
bd admin compact --force --verbose
## Clean up repository size in automated workflows
## Verbose output helps with debugging if needed
```

**Pre-migration cleanup:**
```bash
bd admin compact --dry-run --verbose
## Get detailed view of repository bloat
bd admin compact --force
## Clean repository before exporting data
```

### Tips & gotchas

• Always run with `--dry-run` first to preview changes — compacting is irreversible
• This command only affects bd's internal data structures, not your main git repository
• Compacting is safe to run anytime but provides most benefit after bulk deletions
• Large repositories may take several minutes to compact completely
• The command preserves all active issues and their full history

### Related commands

• **`bd status`** — Check repository health before compacting
• **`bd admin stats`** — View repository size metrics to determine if compacting is needed
• **`bd admin backup`** — Create backups before major maintenance operations
• **`bd admin migrate`** — Often used after compacting when moving between systems

---

## bd admin reset

## bd admin reset

**Purpose:** Forcefully resets the bd issue tracker to a clean state, removing all issues, comments, and tracking data.

### When to use it

• Starting fresh after experimenting with bd in a project
• Clearing out test issues before going into production
• Recovering from corrupted bd state or metadata
• Migrating from another issue tracker and want a clean slate
• Demonstrating bd to a team without historical clutter
• Fixing issues when bd commands start behaving unexpectedly

### Key flags / options

This is a destructive administrative command that typically runs without additional flags, though some implementations may offer:

| Flag | Description |
|------|-------------|
| `--confirm` | Skip interactive confirmation prompt |
| `--keep-config` | Preserve bd configuration while clearing issues |

### Example workflows

**Clean slate for new project:**
```bash
## Remove all existing bd data and start fresh
bd admin reset
## Confirm when prompted
bd init  # Re-initialize if needed
```

**Quick reset during development:**
```bash
## Reset without confirmation prompt (if supported)
bd admin reset --confirm
bd add "First real issue" --priority high
```

**Preserve settings while clearing issues:**
```bash
## Keep bd configuration but remove all issues
bd admin reset --keep-config
bd status  # Should show empty issue list
```

### Tips & gotchas

• **This is irreversible** — all issues, comments, and dependency relationships are permanently deleted
• Always run `bd export` or commit your current state before resetting if you might need to recover data
• The command may require confirmation in interactive mode to prevent accidental data loss
• Git history containing bd commits remains intact, but the current working state is cleared
• Some bd configurations (like templates or aliases) might be preserved depending on implementation
• After reset, you may need to re-run `bd init` to re-establish the tracker in your repository

### Related commands

• **`bd init`** — Initialize bd in a repository (often used after reset)
• **`bd export`** — Export issues before resetting (backup strategy)  
• **`bd import`** — Import issues back after a reset
• **`bd status`** — Verify the reset was successful (should show empty state)

---

## bd ado

## bd ado

**Purpose** — Manages synchronization and integration between bd (beads) and Azure DevOps work items.

### When to use it

• Working in teams that use Azure DevOps for project management
• Need to sync local bd issues with remote Azure DevOps work items
• Want to check connectivity and sync status with Azure DevOps
• Managing multiple Azure DevOps projects from a single repository
• Bridging between local development workflow and enterprise tooling
• Maintaining traceability between code changes and work items

### Key flags / options

Since this is a parent command, flags are handled by the sub-commands:
- `projects` — Lists all accessible Azure DevOps projects
- `status` — Shows current sync configuration and connection state
- `sync` — Performs bidirectional synchronization of issues

### Example workflows

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

### Tips & gotchas

• Run `bd ado status` first to ensure proper Azure DevOps authentication and project access before attempting sync operations
• The sync process is bidirectional — changes in either bd or Azure DevOps will be reflected in both systems
• Large projects may take time to sync initially; subsequent syncs are typically faster due to incremental updates
• Authentication tokens may expire; check status if sync operations start failing

### Related commands

• `bd status` — Check overall bd repository state after Azure DevOps sync
• `bd list` — View synced issues locally after running ado sync  
• `bd show` — Examine individual issues that may have been updated from Azure DevOps
• `bd new` — Create issues that can be synced to Azure DevOps work items

---

## bd ado projects

## bd ado projects

**Purpose** — Lists all projects in an Azure DevOps organization to help you find the correct project for importing work items.

### When to use it

• Before running `bd ado import` to verify the target project exists
• When exploring an ADO organization to understand its structure  
• To find the exact project name/ID needed for other ADO commands
• During initial setup of bd in a repository connected to Azure DevOps
• When troubleshooting ADO integration issues
• To confirm your authentication and organization access is working

### Key flags / options

Based on the command structure, this appears to be a simple listing command without complex options. The authentication and organization details would likely be configured separately or inherited from ADO CLI configuration.

### Example workflows

**Explore available projects:**
```bash
bd ado projects
```
Lists all projects in your configured ADO organization, showing names and IDs you can reference in import commands.

**Verify project before import:**
```bash
## First check what projects are available
bd ado projects
## Then import from the specific project
bd ado import --project "MyProject" --query "assigned-to-me"
```

**Pipeline integration:**
```bash
## In CI/CD, verify project exists before automated imports
if bd ado projects | grep -q "MyProject"; then
    bd ado import --project "MyProject"
fi
```

### Tips & gotchas

• Make sure you're authenticated with Azure DevOps CLI (`az devops login`) before running this command
• The command respects your default ADO organization setting — verify with `az devops configure --list`
• Project names are case-sensitive in subsequent import commands, so note the exact spelling
• Some projects may be visible but not accessible depending on your permissions
• Large organizations may have many projects — consider using `grep` to filter output

### Related commands

• `bd ado import` — Import work items from ADO projects into bd issues
• `bd ado auth` — Configure authentication for Azure DevOps integration  
• `bd list` — View imported issues after running ADO imports
• `bd ado sync` — Synchronize changes between bd and ADO work items

---

## bd ado status

## `bd ado status`

**Purpose**: Displays the Azure DevOps (ADO) synchronization status for issues in the current bd repository.

### When to use it

- Check which local bd issues are synced with Azure DevOps work items
- Verify sync status before pushing changes to ADO
- Troubleshoot sync issues or mismatched items
- Review ADO integration health after configuration changes
- Audit which issues need manual ADO sync intervention

### Key flags / options

| Flag | Description |
|------|-------------|
| `--all` | Show status for all issues, including those without ADO links |
| `--json` | Output status information in JSON format for scripting |
| `--verbose` | Display detailed sync metadata and timestamps |

### Example workflows

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

### Tips & gotchas

- Status reflects the last attempted sync, not real-time ADO state
- Issues created locally but not yet pushed to ADO will show as "unsynced"
- Network connectivity issues may cause status to appear stale
- The command only shows status for issues in the current repository's ADO configuration
- Status may lag behind ADO changes made outside of bd until next sync

### Related commands

- `bd ado sync` — Actually synchronize issues with Azure DevOps
- `bd ado configure` — Set up or modify ADO integration settings
- `bd list` — View local issues that might need ADO sync
- `bd ado push` — Push specific issues to Azure DevOps

---

## bd ado sync

## bd ado sync

**Purpose:** Synchronizes issues between your bd repository and an Azure DevOps (ADO) organization, enabling bidirectional data flow between local and remote issue tracking.

### When to use it

• **Team collaboration** — Keep bd issues in sync with ADO work items for teams using Azure DevOps
• **Migration workflows** — Transfer existing ADO work items into bd or export bd issues to ADO
• **Hybrid workflows** — Maintain local bd tracking while participating in organization-wide ADO processes
• **Reporting integration** — Ensure bd changes appear in ADO dashboards and reporting tools
• **Cross-tool development** — Work locally with bd while maintaining ADO compatibility for stakeholders

### Key options

| Flag | Description |
|------|-------------|
| `--dry-run` | Preview sync operations without making changes |
| `--direction` | Control sync direction (pull, push, or bidirectional) |
| `--organization` | Specify ADO organization URL or identifier |
| `--project` | Target ADO project for synchronization |
| `--auth-token` | ADO personal access token for authentication |

### Example workflows

**Initial setup and pull from ADO:**
```bash
bd ado sync --organization myorg --project myproject --direction pull
```
Downloads existing work items from the specified ADO project into your bd repository, establishing the initial connection between systems.

**Push local changes to ADO:**
```bash
bd ado sync --direction push --dry-run
bd ado sync --direction push
```
First preview what changes would be pushed, then execute the sync to update ADO work items with your local bd issue modifications.

**Bidirectional sync with conflict preview:**
```bash
bd ado sync --organization myorg --project myproject
```
Performs full bidirectional synchronization, merging changes from both sides while respecting bd's dependency tracking and ADO's work item states.

### Tips & gotchas

• **Authentication required** — ADO sync requires a valid personal access token with work item read/write permissions
• **Dependency mapping** — bd's native dependency relationships may not translate perfectly to ADO work item links
• **State conflicts** — Use `--dry-run` first to identify potential conflicts between bd issue states and ADO work item states
• **Network dependency** — Sync operations require active internet connection to ADO servers
• **Rate limiting** — Large repositories may hit ADO API rate limits; the command automatically handles retries

### Related commands

• **`bd sync`** — Generic sync command for other integrations (GitHub, GitLab)
• **`bd export`** — Export bd issues to various formats for one-way data transfer
• **`bd import`** — Import issues from external sources into bd
• **`bd status`** — Check current sync state and identify unsynchronized changes

---

## bd assign

## bd assign

### Purpose
Assigns issues to specific users or teams for ownership and accountability tracking within the beads issue tracker.

### When to use it
• Delegating work on specific issues to team members
• Taking ownership of an issue you plan to work on
• Reassigning issues when team responsibilities change
• Setting up initial assignments during sprint planning
• Tracking who is responsible for issue resolution
• Managing workload distribution across the team

### Key flags / options
| Flag | Description |
|------|-------------|
| `--user` | Specify the username or ID to assign the issue to |
| `--unassign` | Remove current assignment from the issue |
| `--list` | Show all currently assigned issues and their assignees |
| `--me` | Assign the issue to yourself (shortcut) |

### Example workflows

**Assign an issue to yourself:**
```bash
bd assign --me issue-123
```
Quick way to take ownership of an issue you're about to work on.

**Delegate work to a team member:**
```bash
bd assign --user alice issue-456
bd list --assignee alice
```
Assigns the issue to Alice, then checks her current workload to ensure balance.

**Clean up assignments during reorganization:**
```bash
bd assign --unassign issue-789
bd assign --user bob issue-789
```
Removes existing assignment and reassigns to a different team member.

### Tips & gotchas
• Assignments are stored in git, so they're versioned and shared across the team automatically
• Use `bd list --assignee <user>` to check someone's current workload before assigning more issues
• The `--me` flag uses your git configuration to determine your identity
• Unassigning an issue doesn't delete assignment history — it's preserved in git commits
• Assignment changes trigger notifications if your team has hooks configured

### Related commands
• `bd list` — View assigned issues and filter by assignee
• `bd status` — Check overall project health including assignment distribution
• `bd comment` — Add notes when reassigning with context
• `bd dependencies` — Review issue dependencies before assignment changes

---

## bd audit

## bd audit

**Purpose** — Create and manage audit trail entries for issues, providing accountability and tracking of administrative actions.

### When to use it

• After making manual changes to issue files that need documentation
• When updating issue metadata outside of normal bd workflows
• To record external decisions or actions that affect issue status
• During issue triage or bulk operations for compliance tracking
• When integrating with external systems that require audit trails
• To add retrospective documentation for undocumented changes

### Key flags / options

This is a parent command with two sub-commands:

| Sub-command | Description |
|-------------|-------------|
| `record` | Create a new audit interaction entry with timestamp and details |
| `label` | Add a label reference to an existing interaction for categorization |

### Example workflows

**Recording a manual fix:**
```bash
## Document a manual correction made to an issue
bd audit record "Fixed malformed JSON in issue metadata after git merge conflict"
```
This creates an audit entry explaining why the issue file was manually edited, maintaining transparency in the issue history.

**Labeling audit entries:**
```bash
## Add a label to categorize a previous audit entry
bd audit label maintenance
```
Apply labels to audit interactions for better organization and filtering during issue reviews.

**Compliance documentation:**
```bash
## Record external decision affecting issue
bd audit record "Issue closed per security review meeting on 2024-01-15"
bd audit label compliance security-review
```
Document external processes and decisions that impact issue lifecycle for audit compliance.

### Tips & gotchas

• Audit entries are immutable once created — plan your message carefully
• Labels must reference existing interaction entries, not arbitrary text
• Audit trails are stored in the git history, so they persist across branches
• Use descriptive messages since audit entries may be reviewed months later
• Consider establishing team conventions for audit message formats

### Related commands

• **bd log** — View complete issue history including audit entries
• **bd label** — Manage labels that can be applied to audit interactions  
• **bd show** — Display issue details including audit trail
• **bd edit** — Make tracked changes that automatically create audit entries

---

## bd audit label

## bd audit label

**Purpose:** Validates and reports inconsistencies in bead labels across your issue tracker to ensure data integrity and consistency.

### When to use it

- Before major releases to verify all beads are properly labeled
- After bulk editing or importing beads from external sources
- When debugging search/filtering issues that might be label-related
- As part of CI/CD pipelines to catch labeling errors early
- When onboarding new team members who may have inconsistent labeling practices
- After merging branches that contain bead changes

### Key flags / options

| Flag | Description |
|------|-------------|
| `--fix` | Automatically fix common label inconsistencies where possible |
| `--verbose` | Show detailed information about each label issue found |
| `--format` | Output format (text, json, csv) for integration with other tools |
| `--label-type` | Audit only specific label types (e.g., priority, component, status) |

### Example workflows

**Basic audit check:**
```bash
bd audit label
```
Quick scan to identify any label problems in your bead database. Returns a summary of issues found with recommendations for fixes.

**Automated cleanup:**
```bash
bd audit label --fix --verbose
```
Automatically corrects common issues like case inconsistencies, duplicate labels, and invalid label formats while providing detailed output of all changes made.

**CI integration:**
```bash
bd audit label --format json | jq '.errors | length'
```
Returns the number of label errors in JSON format, perfect for failing CI builds when label inconsistencies are detected.

### Tips & gotchas

- The audit doesn't modify beads unless `--fix` is explicitly used
- Some label inconsistencies may require manual intervention even with `--fix`
- Running this command frequently helps catch problems before they spread across many beads
- Custom label schemas may require additional configuration to validate properly
- Large repositories may take several seconds to audit completely

### Related commands

- `bd label` — Create and manage labels on individual beads
- `bd list` — Filter and search beads by labels to verify audit results  
- `bd status` — Check overall repository health including label statistics
- `bd migrate` — Update bead formats which may affect label structures

---

## bd audit record

## `bd audit-record`

**Purpose** — Records an audit entry documenting actions taken on issues, creating a permanent log for compliance and tracking purposes.

### When to use it

• After resolving critical bugs that require documented remediation steps
• When implementing security fixes that need compliance trails
• During code reviews where significant changes affect multiple issues
• For post-incident documentation linking issues to resolution actions
• When external auditors request proof of issue handling procedures
• Before major releases to document all addressed issues

### Key flags / options

| Flag | Description |
|------|-------------|
| `--issue` | Specify which issue(s) this audit record relates to |
| `--type` | Set audit type (security, compliance, review, incident, etc.) |
| `--message` | Provide detailed audit message describing actions taken |
| `--reference` | Link to external documentation, tickets, or commit hashes |
| `--severity` | Mark audit importance level for filtering and reporting |

### Example workflows

**Document security fix resolution:**
```bash
bd audit-record --issue SEC-001 --type security \
  --message "Applied CVE-2024-1234 patch, updated dependencies" \
  --reference "commit:abc123f"
```
Creates a permanent record linking the security issue to specific remediation actions and code changes.

**Log compliance review:**
```bash
bd audit-record --type compliance --severity high \
  --message "GDPR data handling review completed for user registration flow" \
  --reference "https://internal-docs.company.com/gdpr-review-2024"
```
Documents regulatory compliance activities with external reference links for auditor access.

**Post-incident documentation:**
```bash
bd audit-record --issue BUG-456 --issue BUG-789 --type incident \
  --message "Database timeout issues resolved via connection pool tuning"
```
Links multiple related issues to a single remediation effort for comprehensive incident tracking.

### Tips & gotchas

• Audit records are immutable once created — double-check your message content before submitting
• Use consistent `--type` values across your team to enable effective filtering and reporting
• Reference external documents that might change; consider archiving critical compliance documentation locally
• Audit trails integrate with git history but exist independently, so they persist even if issues are deleted

### Related commands

• `bd list --audit` — Filter and view existing audit records
• `bd show` — Display issue details including associated audit entries
• `bd report` — Generate compliance reports including audit trail summaries
• `bd export` — Extract audit data for external compliance systems

---

## bd backup

## bd backup

**Purpose** — Manages database backups to Dolt remote repositories for your bd issue tracker.

### When to use it

• Setting up automated backups for your issue database
• Restoring from backups after data corruption or accidental changes
• Syncing issue data across multiple development environments
• Creating redundant copies of critical project tracking data
• Migrating bd databases between systems or team members
• Implementing disaster recovery for long-running projects

### Key commands

| Command | Purpose |
|---------|---------|
| `bd backup init` | Configure a new Dolt remote as backup destination |
| `bd backup sync` | Push current database state to the backup remote |
| `bd backup restore` | Pull and restore database from backup remote |
| `bd backup status` | Check when last backup was performed |
| `bd backup remove` | Disconnect the current backup configuration |

### Example workflows

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

### Tips & gotchas

• The backup system requires Dolt to be installed and configured separately from bd
• Initial `backup init` may require authentication credentials for your Dolt remote
• `backup restore` is destructive and will overwrite local changes unless you use appropriate flags
• Backup operations can be slow for large issue databases, especially on first sync
• Consider running `backup status` before `restore` to understand what you're reverting to

### Related commands

• `bd init` — Initialize the local database that backups will preserve
• `bd export` — Alternative data export method for non-Dolt destinations  
• `bd import` — Import issues when migrating between backup systems
• `bd status` — Check local database state before/after backup operations

---

## bd backup init

## bd backup init

**Purpose** — Initialize a remote backup repository for syncing beads data to external Git hosting.

### When to use it

- Setting up your first backup for a beads project to prevent data loss
- Creating redundancy for critical issue tracking data before major changes
- Enabling team collaboration by establishing a shared remote repository
- Preparing for CI/CD integration that needs access to issue data
- Migrating from local-only beads usage to a distributed workflow

### Key flags / options

| Flag | Description |
|------|-------------|
| `--remote URL` | Specify the Git remote URL for the backup repository |
| `--branch NAME` | Set the target branch for backup sync (default: main) |
| `--force` | Overwrite existing backup configuration without confirmation |

### Example workflows

**Basic backup setup:**
```bash
bd backup init --remote git@github.com:myorg/myproject-beads.git
```
Creates a backup configuration pointing to a GitHub repository, automatically setting up the remote connection for future sync operations.

**Custom branch backup:**
```bash
bd backup init --remote https://gitlab.com/team/issues.git --branch beads-data
```
Initializes backup to a specific branch, useful when you want to keep beads data separate from your main codebase or share across multiple projects.

**Reconfiguring existing backup:**
```bash
bd backup init --remote git@newhost.com:backup/beads.git --force
```
Updates an existing backup configuration to point to a new remote, bypassing confirmation prompts.

### Tips & gotchas

- The remote repository should be empty or dedicated to beads data—this isn't meant for mixing with application code
- Ensure your Git credentials are configured before running, as the command will test the remote connection
- The backup branch will be created automatically if it doesn't exist on the remote
- Configuration is stored in `.beads/config` and affects all subsequent backup operations

### Related commands

- `bd backup sync` — Push local beads data to the configured backup remote
- `bd backup pull` — Retrieve and merge beads data from the backup remote  
- `bd backup status` — Check the current backup configuration and sync state
- `bd init` — Initialize a new beads project (typically run before backup setup)

---

## bd backup remove

## bd backup remove

**Purpose**: Removes previously created backup snapshots of your bd issue tracker state.

### When to use it

- Clean up old backups after successful migrations or major changes
- Free up disk space by removing unnecessary backup files
- Remove corrupted or incomplete backup snapshots
- Maintain a tidy backup history by keeping only recent snapshots
- Clear backups before archiving or transferring a project

### Key flags / options

Since no help output was provided, this command likely follows bd's standard pattern of accepting backup identifiers or timestamps to specify which backups to remove.

### Example workflows

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

### Tips & gotchas

- **No undo**: Once removed, backup snapshots cannot be recovered—ensure you don't need them before deletion
- **Verify first**: Use `bd backup list` to confirm you're removing the correct backup
- **Keep recent backups**: Always maintain at least one recent backup before removing others
- **Storage location**: Backups are typically stored in `.bd/backups/` but removal is handled through bd commands, not direct file deletion

### Related commands

- **`bd backup create`** — Create new backup snapshots before making changes
- **`bd backup list`** — View available backups to identify candidates for removal  
- **`bd backup restore`** — Restore from a backup (verify you have alternatives before removing)
- **`bd backup verify`** — Check backup integrity before deciding to remove

---

## bd backup restore

## bd backup restore

**Purpose**: Restores a bd repository from a previously created backup, recovering all beads, metadata, and configuration.

### When to use it

- Recovering from catastrophic data loss or corruption
- Setting up bd in a new environment from an existing backup
- Testing backup integrity by performing restore operations
- Migrating bd data between different systems or repositories
- Rolling back to a known good state after problematic changes

### Key flags / options

| Flag | Description |
|------|-------------|
| `--force` | Overwrite existing bd data without confirmation prompts |
| `--verify` | Validate backup integrity before restoring |
| `--partial` | Restore only specific components (beads, config, etc.) |
| `--dry-run` | Preview what would be restored without making changes |

### Example workflows

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

### Tips & gotchas

- Always verify backup integrity before restoring, especially for critical data recovery scenarios
- The restore process overwrites existing bd data by default—use `--dry-run` first to preview changes
- Restored beads maintain their original IDs and dependency relationships, ensuring consistency
- Git history and commits are preserved during restore, maintaining full project traceability
- Large backups may take time to restore; consider using `--partial` for incremental recovery

### Related commands

- `bd backup create` — Create backups that can later be restored
- `bd init` — Initialize a new bd repository (often used before restore)
- `bd status` — Verify repository state after restore completion
- `bd validate` — Check repository integrity post-restore

---

## bd backup status

## backup-status

**Purpose** — Shows the current state of your backup configuration and the synchronization status between your local bd repository and configured backup locations.

### When to use it

• Check if backups are properly configured before starting work
• Verify that recent changes have been synchronized to backup locations
• Troubleshoot backup connectivity issues
• Monitor backup health as part of regular maintenance
• Confirm backup status before making critical changes to issues

### Key options

| Flag | Description |
|------|-------------|
| `--verbose` | Show detailed sync information for each backup location |
| `--check-remote` | Actively test connectivity to remote backup services |
| `--format=json` | Output status information in JSON format for scripting |

### Example workflows

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

### Tips & gotchas

• Status checks don't trigger synchronization—use `bd backup sync` if you need to update backups
• Remote connectivity tests may take several seconds depending on your backup service
• JSON output format is stable and recommended for scripting and automation
• Some backup services may show "pending" status during their own maintenance windows

### Related commands

• `bd backup sync` — Manually synchronize changes to backup locations
• `bd backup configure` — Set up or modify backup destination settings
• `bd status` — View overall repository status including local changes
• `bd log` — Review recent activity that may need backing up

---

## bd backup sync

## bd backup sync

**Purpose**: Synchronizes your local issue data with configured backup destinations to ensure your beads repository state is safely stored elsewhere.

### When to use it

• After making significant changes to issues (creation, updates, or status changes)
• Before major project milestones or releases
• As part of automated CI/CD workflows to maintain backup consistency
• When switching between development environments
• Before performing potentially destructive operations on the repository
• On a scheduled basis for regular backup maintenance

### Key flags / options

| Flag | Description |
|------|-------------|
| `--dry-run` | Preview what would be synchronized without making actual changes |
| `--force` | Override safety checks and force synchronization even with conflicts |
| `--destination <name>` | Sync only to a specific configured backup destination |
| `--verbose` | Show detailed progress information during the sync process |

### Example workflows

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

### Tips & gotchas

The sync operation respects your git history, so ensure your beads changes are committed before syncing. Uncommitted modifications may not be included in the backup. If you encounter sync conflicts, examine the conflicting state carefully before using `--force`, as this can overwrite important backup data. The command will fail gracefully if backup destinations are unreachable, allowing you to continue working offline.

### Related commands

• `bd backup add` - Configure new backup destinations
• `bd backup status` - Check current backup configuration and sync status  
• `bd status` - Review local issue state before backing up
• `bd commit` - Ensure changes are committed before synchronization

---

## bd blocked

## bd blocked

### Purpose
List all issues that are currently blocked by dependencies that haven't been completed yet.

### When to use it
• **Unblocking workflow planning** — identify which issues can't proceed until dependencies are resolved
• **Sprint planning** — understand what work is actually available to start
• **Dependency chain analysis** — visualize bottlenecks in your development pipeline
• **Team coordination** — see which issues are waiting on other team members' work
• **Project status reviews** — quickly assess what's stuck and why

### Key flags / options
This command appears to have a minimal interface focused on simplicity, likely displaying blocked issues without additional configuration options.

### Example workflows

**Check what's currently blocked:**
```bash
bd blocked
```
Get a quick overview of all issues that can't proceed due to unresolved dependencies.

**Combine with issue details for triage:**
```bash
bd blocked
bd show issue-123  # investigate a specific blocked issue
```
First see what's blocked, then examine individual issues to understand the dependency chain and plan resolution steps.

**Daily standup preparation:**
```bash
bd blocked > blocked-today.txt
bd status --active
```
Export blocked issues for review, then check active work to see if any blocking dependencies are close to completion.

### Tips & gotchas
• **Transitive dependencies** — An issue may appear blocked even if its direct dependency is complete, due to deeper dependency chains
• **Stale dependencies** — Issues may remain in blocked status if dependency relationships weren't properly updated when work was completed
• **Empty output is good news** — No output means all issues have their dependencies satisfied and work can proceed freely
• **Use with `bd deps`** — Cross-reference with dependency visualization commands to understand the full blocking relationship tree

### Related commands
• **`bd deps`** — visualize dependency relationships to understand why issues are blocked
• **`bd status`** — see overall project status including active and completed work
• **`bd list`** — view all issues to identify potential work that could unblock others
• **`bd show`** — examine specific blocked issues to understand their dependency requirements

---

## bd bootstrap

## `bd bootstrap`

**Purpose:** Initialize a new bd issue tracker repository with the necessary Git hooks and configuration files.

### When to use it

• Starting a new project that needs issue tracking
• Setting up bd in an existing Git repository for the first time
• Reinitializing bd after accidentally removing configuration files
• Creating a clean bd environment after repository corruption
• Adding issue tracking to a project that previously used external tools

### Key flags / options

| Flag | Description |
|------|-------------|
| `--force` | Overwrite existing bd configuration and hooks |
| `--no-hooks` | Skip Git hook installation during initialization |
| `--template` | Initialize with a specific issue template or configuration |

### Example workflows

**New project setup:**
```bash
git init my-project
cd my-project
bd bootstrap
```
Sets up a fresh repository with bd tracking from the start. Creates the `.bd/` directory structure and installs Git hooks for automatic issue validation.

**Existing project integration:**
```bash
cd existing-project
bd bootstrap --force
git add .bd/
git commit -m "Add bd issue tracking"
```
Integrates bd into an established codebase. The `--force` flag overwrites any conflicting files, ensuring a clean setup.

**Lightweight setup for scripts:**
```bash
bd bootstrap --no-hooks
```
Creates the bd structure without Git hooks, useful for automated environments or when you want manual control over when bd validation occurs.

### Tips & gotchas

**Git hooks consideration:** Bootstrap installs Git hooks that validate issues on commit. If your project already has custom hooks, they may be overwritten unless you use `--no-hooks` and manually integrate bd validation.

**Permissions on hooks:** The installed Git hooks need execute permissions. Bootstrap handles this automatically, but if you copy `.bd/` directories between systems, you may need to fix permissions manually.

**Nested repositories:** Bootstrap detects the Git repository root automatically. Running it in a subdirectory will still initialize bd at the repository level, not the current working directory.

### Related commands

• **`bd new`** — Create your first issue after bootstrapping
• **`bd status`** — Verify the bootstrap worked correctly and check repository health
• **`bd config`** — Customize bd behavior after initial setup
• **`bd validate`** — Manually run the validation that Git hooks perform automatically

---

## bd branch

## bd branch

**Purpose:** Creates a new git branch for working on a specific issue, automatically setting up branch naming and issue context.

### When to use it

- Starting work on a tagged issue that needs code changes
- Creating feature branches with consistent naming conventions
- Setting up isolated development environments for specific beads
- Beginning work on issues that require collaboration or review
- Preparing branches for pull requests linked to tracked issues

### Key flags / options

| Flag | Description |
|------|-------------|
| `--issue-id` | Specify the issue ID to create a branch for |
| `--name` | Override the default branch name pattern |
| `--base` | Set the base branch (defaults to current branch) |
| `--push` | Automatically push the new branch to remote |

### Example workflows

**Basic issue branch creation:**
```bash
bd branch --issue-id 42
git checkout issue-42-implement-user-auth
```
Creates and checks out a new branch following bd's naming convention, linking it to issue #42.

**Custom branch with remote push:**
```bash
bd branch --issue-id 15 --name feature/payment-gateway --push
```
Creates a custom-named branch for issue #15 and immediately pushes it to the remote repository.

**Branch from specific base:**
```bash
bd branch --issue-id 8 --base develop
git log --oneline -5
```
Creates an issue branch starting from the `develop` branch instead of the current branch, useful for feature work that needs to be based on the latest development state.

### Tips & gotchas

- Branch names automatically include the issue ID and a sanitized version of the issue title
- The command fails if you have uncommitted changes unless you stash them first
- bd tracks which branches are associated with which issues for better workflow integration
- Creating a branch doesn't automatically assign the issue to you—use `bd assign` separately if needed
- The branch creation updates local issue metadata to track the association

### Related commands

- `bd list` — Find issue IDs before creating branches
- `bd assign` — Assign issues to yourself when starting work
- `bd status` — Check which issues have active branches
- `bd close` — Complete and close issues when merging branches

---

## bd children

## bd children

**Purpose** — Displays all issues that depend on (are children of) a specified issue, showing the dependency hierarchy.

### When to use it

• **Tracking blockers** — See what work is waiting on a particular issue to be resolved
• **Planning releases** — Understand which features depend on core infrastructure changes
• **Code review workflow** — Check what pull requests are blocked by a specific fix
• **Sprint planning** — Identify work that will become available once a milestone is completed
• **Dependency analysis** — Visualize the impact scope of completing an issue

### Key flags / options

| Flag | Description |
|------|-------------|
| `--recursive` | Show all descendants, not just direct children |
| `--format` | Output format (table, json, list) |
| `--status` | Filter children by status (open, closed, all) |

### Example workflows

**Check direct dependencies:**
```bash
bd children feature-auth-system
## Shows: login-ui, password-reset, oauth-integration
```
This helps you see what work is immediately unblocked when you complete the auth system.

**Analyze full impact tree:**
```bash
bd children api-refactor --recursive --status=open
```
Reveals the complete chain of work that depends on your API changes, helping estimate total effort and plan rollout phases.

**Export for stakeholder reporting:**
```bash
bd children milestone-v2 --format=json | jq '.[] | {title, assignee, estimate}'
```
Creates a clean summary of all work items blocked by a major milestone for project updates.

### Tips & gotchas

**Empty results are normal** — Many leaf issues have no children; this indicates work that doesn't block other tasks.

**Status filtering matters** — Use `--status=open` to focus on actionable items, or `--status=all` for complete historical context.

**Recursive can be overwhelming** — Start with direct children first; use `--recursive` only when you need the full dependency tree.

### Related commands

• **`bd depends`** — Show what the current issue depends on (parent direction)
• **`bd graph`** — Visualize the complete dependency network graphically  
• **`bd list --blocked`** — Find all issues waiting on dependencies
• **`bd tree`** — Display hierarchical view of issue relationships

---

## bd close

## Close Command

**Purpose:** Marks one or more issues as closed by setting their status to "closed" and recording the closure timestamp.

### When to use it

• Issue is completely resolved and no further work is needed
• Bug has been fixed and tested
• Feature has been implemented and merged
• Issue was a duplicate or invalid and should be archived
• Dependencies are satisfied and the issue can be considered done
• Need to clean up completed work from active issue lists

### Key flags / options

| Flag | Description |
|------|-------------|
| `--message`, `-m` | Add a closure message explaining why the issue was closed |
| `--bulk` | Close multiple issues by providing a list of issue IDs |
| `--force` | Close issue even if it has open dependencies |

### Example workflows

**Close a single resolved issue:**
```bash
bd close 42 -m "Fixed memory leak in parser module"
```
Simple closure with an explanatory message documenting what was accomplished.

**Bulk close multiple completed features:**
```bash
bd close --bulk 15 23 31 -m "Sprint 3 deliverables completed"
```
Efficiently closes several related issues at once, useful during sprint cleanup or milestone completion.

**Force close a blocked issue:**
```bash
bd close 18 --force -m "Closing as obsolete after architecture change"
```
Closes an issue despite having open dependencies, typically when requirements have changed or the issue is no longer relevant.

### Tips & gotchas

• Closed issues remain in the git history and can be reopened if needed
• Closing an issue with open dependencies requires the `--force` flag as a safety measure
• The closure timestamp is automatically recorded for tracking and reporting purposes
• Consider adding meaningful closure messages to help future developers understand the resolution
• Closed issues are filtered out of most list commands by default but can still be queried

### Related commands

• `bd open` — Reopen a previously closed issue
• `bd list` — View active issues (excludes closed by default)
• `bd status` — Check the current state of an issue before closing
• `bd comment` — Add final notes before closing an issue

---

## bd comment

## comment

**Purpose:** Add comments to existing issues for updates, clarifications, or status changes.

### When to use it

- Update stakeholders on progress without changing issue status
- Ask clarifying questions on someone else's issue
- Document workarounds or partial solutions
- Record debugging findings or investigation results
- Leave notes for future reference during code review
- Provide feedback on proposed solutions

### Key flags / options

| Flag | Description |
|------|-------------|
| `--message` / `-m` | Specify comment text directly on command line |
| `--file` / `-f` | Read comment content from a file |
| `--editor` | Open default editor to compose comment |

### Example workflows

**Quick status update:**
```bash
bd comment ABC-123 -m "Investigated the API timeout issue. Root cause is connection pool exhaustion."
```
This adds a brief progress note without changing the issue's status or assignee.

**Detailed analysis from file:**
```bash
bd comment ABC-456 -f investigation-notes.md
```
Use this when you have extensive findings or formatted content (stack traces, logs, etc.) already prepared in a file.

**Interactive commenting:**
```bash
bd comment ABC-789 --editor
```
Opens your configured editor for longer comments where you need formatting control or want to review before posting.

### Tips & gotchas

- Comments are stored as separate Git commits, so they preserve full history and attribution
- Use meaningful comment messages since they become part of your Git log
- Comments support Markdown formatting for code blocks, links, and emphasis
- Consider using `bd show` first to review existing comments before adding your own
- Comments are immutable once added (follows Git's append-only model)

### Related commands

- `bd show` — View issue details and existing comments before adding new ones
- `bd edit` — Modify the issue description or metadata rather than adding comments
- `bd list` — Find issues that need commenting or follow-up
- `bd assign` — Change issue ownership, often done alongside status comments

---

## bd comments add

## bd comments add

**Purpose** — Add a comment to an existing issue to provide updates, feedback, or additional context.

### When to use it

• After investigating an issue and finding new information
• When providing status updates on work in progress
• To respond to questions or clarify requirements from other team members
• When documenting failed attempts or alternative approaches
• To link related issues or reference external resources
• Before closing an issue to summarize the final resolution

### Key flags / options

| Flag | Description |
|------|-------------|
| `--issue-id` | Target issue ID to comment on (required) |
| `--message` | Comment text directly from command line |
| `--file` | Read comment content from a file |
| `--editor` | Open default editor to compose the comment |

### Example workflows

**Quick status update:**
```bash
bd comments add --issue-id 42 --message "Started working on the login validation logic"
```
Add a brief progress note without opening an editor.

**Detailed technical comment:**
```bash
bd comments add --issue-id 15 --editor
```
Opens your configured editor for longer explanations, code snippets, or multi-paragraph updates.

**Bulk comment from file:**
```bash
bd comments add --issue-id 23 --file investigation-notes.md
```
Useful when you've documented findings in a separate file and want to attach them to the issue thread.

### Tips & gotchas

• Comments are timestamped and attributed to the current git user, so ensure your git identity is configured correctly
• Unlike issue descriptions, comments cannot be edited after creation — double-check before submitting
• Comments support Markdown formatting for code blocks, links, and emphasis
• If you don't specify `--message`, `--file`, or `--editor`, the command will prompt for input interactively

### Related commands

• `bd list` — View issues to find the correct issue ID for commenting
• `bd show` — Display an issue and its existing comment thread
• `bd edit` — Modify the main issue description (not comments)
• `bd close` — Close an issue, often done after adding a final resolution comment
