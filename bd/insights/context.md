# bd context

**Purpose** — Displays the current bead (issue) context and allows switching between different beads for focused work.

## When to use it

• Check which bead you're currently working on
• Switch context to a different bead when starting new work
• View the current bead's details before making commits
• Reset context when you want to work without a specific bead focus
• Confirm context changes after running other bd commands
• Get oriented when returning to a project after time away

## Key flags / options

| Flag | Description |
|------|-------------|
| `--clear` | Clear the current context (work without a specific bead) |
| `--show` | Display current context information (default behavior) |

## Example workflows

**Check current context:**
```bash
bd context
# Shows: Currently working on bead #42: "Fix login validation bug"
```
This helps you confirm which issue you're focused on before making commits or changes.

**Switch to a different bead:**
```bash
bd context 15
# Switches context to bead #15
bd context
# Shows: Currently working on bead #15: "Add user profile page"
```
Useful when you need to pause work on one issue and start another.

**Clear context for general work:**
```bash
bd context --clear
bd context
# Shows: No current bead context
```
Ideal when doing maintenance work or changes that don't relate to a specific tracked issue.

## Tips & gotchas

• Context persists across terminal sessions — you don't need to re-set it each time
• Some bd commands automatically update context (like `bd new` sets context to the newly created bead)
• Working with context helps maintain clean commit messages and proper issue tracking
• Context doesn't restrict which files you can edit — it's purely organizational

## Related commands

• `bd new` — creates a new bead and automatically sets it as current context
• `bd show` — displays detailed information about the current context bead
• `bd list` — view all beads to help choose which one to set as context
• `bd commit` — uses current context to enhance commit messages with bead references