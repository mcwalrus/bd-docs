# bd blocked

## Purpose
List all issues that are currently blocked by dependencies that haven't been completed yet.

## When to use it
• **Unblocking workflow planning** — identify which issues can't proceed until dependencies are resolved
• **Sprint planning** — understand what work is actually available to start
• **Dependency chain analysis** — visualize bottlenecks in your development pipeline
• **Team coordination** — see which issues are waiting on other team members' work
• **Project status reviews** — quickly assess what's stuck and why

## Key flags / options
This command appears to have a minimal interface focused on simplicity, likely displaying blocked issues without additional configuration options.

## Example workflows

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

## Tips & gotchas
• **Transitive dependencies** — An issue may appear blocked even if its direct dependency is complete, due to deeper dependency chains
• **Stale dependencies** — Issues may remain in blocked status if dependency relationships weren't properly updated when work was completed
• **Empty output is good news** — No output means all issues have their dependencies satisfied and work can proceed freely
• **Use with `bd deps`** — Cross-reference with dependency visualization commands to understand the full blocking relationship tree

## Related commands
• **`bd deps`** — visualize dependency relationships to understand why issues are blocked
• **`bd status`** — see overall project status including active and completed work
• **`bd list`** — view all issues to identify potential work that could unblock others
• **`bd show`** — examine specific blocked issues to understand their dependency requirements