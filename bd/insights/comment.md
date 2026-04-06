# comment

**Purpose:** Add comments to existing issues for updates, clarifications, or status changes.

## When to use it

- Update stakeholders on progress without changing issue status
- Ask clarifying questions on someone else's issue
- Document workarounds or partial solutions
- Record debugging findings or investigation results
- Leave notes for future reference during code review
- Provide feedback on proposed solutions

## Key flags / options

| Flag | Description |
|------|-------------|
| `--message` / `-m` | Specify comment text directly on command line |
| `--file` / `-f` | Read comment content from a file |
| `--editor` | Open default editor to compose comment |

## Example workflows

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

## Tips & gotchas

- Comments are stored as separate Git commits, so they preserve full history and attribution
- Use meaningful comment messages since they become part of your Git log
- Comments support Markdown formatting for code blocks, links, and emphasis
- Consider using `bd show` first to review existing comments before adding your own
- Comments are immutable once added (follows Git's append-only model)

## Related commands

- `bd show` — View issue details and existing comments before adding new ones
- `bd edit` — Modify the issue description or metadata rather than adding comments
- `bd list` — Find issues that need commenting or follow-up
- `bd assign` — Change issue ownership, often done alongside status comments