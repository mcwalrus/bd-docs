# bd ado sync

**Purpose:** Synchronizes issues between your bd repository and an Azure DevOps (ADO) organization, enabling bidirectional data flow between local and remote issue tracking.

## When to use it

• **Team collaboration** — Keep bd issues in sync with ADO work items for teams using Azure DevOps
• **Migration workflows** — Transfer existing ADO work items into bd or export bd issues to ADO
• **Hybrid workflows** — Maintain local bd tracking while participating in organization-wide ADO processes
• **Reporting integration** — Ensure bd changes appear in ADO dashboards and reporting tools
• **Cross-tool development** — Work locally with bd while maintaining ADO compatibility for stakeholders

## Key options

| Flag | Description |
|------|-------------|
| `--dry-run` | Preview sync operations without making changes |
| `--direction` | Control sync direction (pull, push, or bidirectional) |
| `--organization` | Specify ADO organization URL or identifier |
| `--project` | Target ADO project for synchronization |
| `--auth-token` | ADO personal access token for authentication |

## Example workflows

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

## Tips & gotchas

• **Authentication required** — ADO sync requires a valid personal access token with work item read/write permissions
• **Dependency mapping** — bd's native dependency relationships may not translate perfectly to ADO work item links
• **State conflicts** — Use `--dry-run` first to identify potential conflicts between bd issue states and ADO work item states
• **Network dependency** — Sync operations require active internet connection to ADO servers
• **Rate limiting** — Large repositories may hit ADO API rate limits; the command automatically handles retries

## Related commands

• **`bd sync`** — Generic sync command for other integrations (GitHub, GitLab)
• **`bd export`** — Export bd issues to various formats for one-way data transfer
• **`bd import`** — Import issues from external sources into bd
• **`bd status`** — Check current sync state and identify unsynchronized changes