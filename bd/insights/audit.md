# bd audit

**Purpose** — Create and manage audit trail entries for issues, providing accountability and tracking of administrative actions.

## When to use it

• After making manual changes to issue files that need documentation
• When updating issue metadata outside of normal bd workflows
• To record external decisions or actions that affect issue status
• During issue triage or bulk operations for compliance tracking
• When integrating with external systems that require audit trails
• To add retrospective documentation for undocumented changes

## Key flags / options

This is a parent command with two sub-commands:

| Sub-command | Description |
|-------------|-------------|
| `record` | Create a new audit interaction entry with timestamp and details |
| `label` | Add a label reference to an existing interaction for categorization |

## Example workflows

**Recording a manual fix:**
```bash
# Document a manual correction made to an issue
bd audit record "Fixed malformed JSON in issue metadata after git merge conflict"
```
This creates an audit entry explaining why the issue file was manually edited, maintaining transparency in the issue history.

**Labeling audit entries:**
```bash
# Add a label to categorize a previous audit entry
bd audit label maintenance
```
Apply labels to audit interactions for better organization and filtering during issue reviews.

**Compliance documentation:**
```bash
# Record external decision affecting issue
bd audit record "Issue closed per security review meeting on 2024-01-15"
bd audit label compliance security-review
```
Document external processes and decisions that impact issue lifecycle for audit compliance.

## Tips & gotchas

• Audit entries are immutable once created — plan your message carefully
• Labels must reference existing interaction entries, not arbitrary text
• Audit trails are stored in the git history, so they persist across branches
• Use descriptive messages since audit entries may be reviewed months later
• Consider establishing team conventions for audit message formats

## Related commands

• **bd log** — View complete issue history including audit entries
• **bd label** — Manage labels that can be applied to audit interactions  
• **bd show** — Display issue details including audit trail
• **bd edit** — Make tracked changes that automatically create audit entries