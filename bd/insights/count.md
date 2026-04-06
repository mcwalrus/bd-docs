# `bd count`

**Purpose:** Displays a summary count of issues grouped by status, providing a quick overview of your project's issue distribution.

## When to use it

- Get a quick project health snapshot during standup meetings
- Check how many issues are ready for work vs. in progress vs. completed
- Monitor progress before releases or milestones
- Generate high-level metrics for team reporting
- Verify issue status distribution after bulk status updates

## Key flags / options

| Flag | Description |
|------|-------------|
| `--status` | Filter count to specific status(es) only |
| `--format` | Output format (table, json, csv) for integration with other tools |
| `--include-deps` | Include dependency counts in the summary |

## Example workflows

**Quick project overview:**
```bash
bd count
# Shows: Open: 12, In Progress: 4, Done: 23, Blocked: 2
# Perfect for daily standups or sprint planning
```

**Status-specific counting:**
```bash
bd count --status open,blocked
# Focus on actionable issues that need attention
# Useful when prioritizing work or identifying bottlenecks
```

**Integration with reporting:**
```bash
bd count --format json | jq '.open + .in_progress'
# Calculate total active work items for burndown charts
# Combine with CI/CD pipelines for automated reporting
```

## Tips & gotchas

- Counts reflect the current state of your git repository — make sure you're on the right branch and have pulled recent changes
- The command respects any existing issue filters you've set, so results may be scoped if you've previously filtered your view
- Status names are case-sensitive and must match exactly as defined in your project configuration
- Large repositories with thousands of issues may take a moment to process the count

## Related commands

- **`bd list`** — See the actual issues behind these counts
- **`bd status`** — View or modify individual issue statuses
- **`bd show`** — Drill down into specific issues for details
- **`bd filter`** — Narrow down which issues are included in counts