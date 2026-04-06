# bd children

**Purpose** — Displays all issues that depend on (are children of) a specified issue, showing the dependency hierarchy.

## When to use it

• **Tracking blockers** — See what work is waiting on a particular issue to be resolved
• **Planning releases** — Understand which features depend on core infrastructure changes
• **Code review workflow** — Check what pull requests are blocked by a specific fix
• **Sprint planning** — Identify work that will become available once a milestone is completed
• **Dependency analysis** — Visualize the impact scope of completing an issue

## Key flags / options

| Flag | Description |
|------|-------------|
| `--recursive` | Show all descendants, not just direct children |
| `--format` | Output format (table, json, list) |
| `--status` | Filter children by status (open, closed, all) |

## Example workflows

**Check direct dependencies:**
```bash
bd children feature-auth-system
# Shows: login-ui, password-reset, oauth-integration
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

## Tips & gotchas

**Empty results are normal** — Many leaf issues have no children; this indicates work that doesn't block other tasks.

**Status filtering matters** — Use `--status=open` to focus on actionable items, or `--status=all` for complete historical context.

**Recursive can be overwhelming** — Start with direct children first; use `--recursive` only when you need the full dependency tree.

## Related commands

• **`bd depends`** — Show what the current issue depends on (parent direction)
• **`bd graph`** — Visualize the complete dependency network graphically  
• **`bd list --blocked`** — Find all issues waiting on dependencies
• **`bd tree`** — Display hierarchical view of issue relationships