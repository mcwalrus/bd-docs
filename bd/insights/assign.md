# bd assign

## Purpose
Assigns issues to specific users or teams for ownership and accountability tracking within the beads issue tracker.

## When to use it
• Delegating work on specific issues to team members
• Taking ownership of an issue you plan to work on
• Reassigning issues when team responsibilities change
• Setting up initial assignments during sprint planning
• Tracking who is responsible for issue resolution
• Managing workload distribution across the team

## Key flags / options
| Flag | Description |
|------|-------------|
| `--user` | Specify the username or ID to assign the issue to |
| `--unassign` | Remove current assignment from the issue |
| `--list` | Show all currently assigned issues and their assignees |
| `--me` | Assign the issue to yourself (shortcut) |

## Example workflows

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

## Tips & gotchas
• Assignments are stored in git, so they're versioned and shared across the team automatically
• Use `bd list --assignee <user>` to check someone's current workload before assigning more issues
• The `--me` flag uses your git configuration to determine your identity
• Unassigning an issue doesn't delete assignment history — it's preserved in git commits
• Assignment changes trigger notifications if your team has hooks configured

## Related commands
• `bd list` — View assigned issues and filter by assignee
• `bd status` — Check overall project health including assignment distribution
• `bd comment` — Add notes when reassigning with context
• `bd dependencies` — Review issue dependencies before assignment changes