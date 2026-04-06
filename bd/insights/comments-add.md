# bd comments add

**Purpose** — Add a comment to an existing issue to provide updates, feedback, or additional context.

## When to use it

• After investigating an issue and finding new information
• When providing status updates on work in progress
• To respond to questions or clarify requirements from other team members
• When documenting failed attempts or alternative approaches
• To link related issues or reference external resources
• Before closing an issue to summarize the final resolution

## Key flags / options

| Flag | Description |
|------|-------------|
| `--issue-id` | Target issue ID to comment on (required) |
| `--message` | Comment text directly from command line |
| `--file` | Read comment content from a file |
| `--editor` | Open default editor to compose the comment |

## Example workflows

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

## Tips & gotchas

• Comments are timestamped and attributed to the current git user, so ensure your git identity is configured correctly
• Unlike issue descriptions, comments cannot be edited after creation — double-check before submitting
• Comments support Markdown formatting for code blocks, links, and emphasis
• If you don't specify `--message`, `--file`, or `--editor`, the command will prompt for input interactively

## Related commands

• `bd list` — View issues to find the correct issue ID for commenting
• `bd show` — Display an issue and its existing comment thread
• `bd edit` — Modify the main issue description (not comments)
• `bd close` — Close an issue, often done after adding a final resolution comment