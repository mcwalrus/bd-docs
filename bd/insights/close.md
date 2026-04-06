# Close Command

**Purpose:** Marks one or more issues as closed by setting their status to "closed" and recording the closure timestamp.

## When to use it

• Issue is completely resolved and no further work is needed
• Bug has been fixed and tested
• Feature has been implemented and merged
• Issue was a duplicate or invalid and should be archived
• Dependencies are satisfied and the issue can be considered done
• Need to clean up completed work from active issue lists

## Key flags / options

| Flag | Description |
|------|-------------|
| `--message`, `-m` | Add a closure message explaining why the issue was closed |
| `--bulk` | Close multiple issues by providing a list of issue IDs |
| `--force` | Close issue even if it has open dependencies |

## Example workflows

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

## Tips & gotchas

• Closed issues remain in the git history and can be reopened if needed
• Closing an issue with open dependencies requires the `--force` flag as a safety measure
• The closure timestamp is automatically recorded for tracking and reporting purposes
• Consider adding meaningful closure messages to help future developers understand the resolution
• Closed issues are filtered out of most list commands by default but can still be queried

## Related commands

• `bd open` — Reopen a previously closed issue
• `bd list` — View active issues (excludes closed by default)
• `bd status` — Check the current state of an issue before closing
• `bd comment` — Add final notes before closing an issue