# bd comments

**Purpose** — Manage comments on issues within your beads issue tracker.

## When to use it

• Add clarifications or updates to existing issues without modifying the original description
• Provide feedback or suggestions during code review discussions
• Document progress updates or status changes on long-running issues
• Share additional context or links discovered after issue creation
• Facilitate team discussions around specific problems or features
• Log resolution details when closing complex issues

## Key flags / options

This command serves as a parent for comment-related operations. Individual subcommands have their own specific flags and options.

## Example workflows

**Adding a comment to an issue:**
```bash
bd comments add ISSUE-123 "Found the root cause - it's related to the database connection pooling"
```
This adds a new comment to issue ISSUE-123 with the specified message, useful for sharing discoveries during investigation.

**Adding a multi-line comment:**
```bash
bd comments add ISSUE-456 -m "Tested the proposed fix" -m "Works on staging environment" -m "Ready for production deployment"
```
Use multiple `-m` flags to create structured comments with multiple paragraphs or bullet points.

## Tips & gotchas

• Comments are stored as git objects, so they benefit from git's history and backup mechanisms
• Unlike issue descriptions, comments can be added by anyone with write access to the repository
• Comments maintain chronological order and are immutable once created
• Consider using comments for temporary notes that don't warrant editing the main issue description

## Related commands

• `bd show` — View an issue with all its comments in formatted output
• `bd list` — Find issues that might need commenting or follow-up
• `bd edit` — Modify the main issue description when comments reveal need for updates
• `bd close` — Often used after adding final resolution comments