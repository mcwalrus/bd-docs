# `bd create`

**Purpose:** Creates a new issue or task in the beads issue tracker with an automatically generated unique identifier.

## When to use it

- Starting work on a new feature or bug fix
- Breaking down large tasks into smaller, trackable issues
- Creating issues with dependencies on existing work
- Adding tasks discovered during development or code review
- Setting up a backlog of work items for a project
- Creating placeholder issues for future work

## Key flags / options

| Flag | Description |
|------|-------------|
| `-t, --title` | Set the issue title (required) |
| `-d, --description` | Add a detailed description of the issue |
| `-p, --priority` | Set priority level (low, normal, high, critical) |
| `--depends-on` | Specify dependencies on other issue IDs |
| `--assignee` | Assign the issue to a specific person |
| `--tag` | Add tags for categorization (can be used multiple times) |

## Example workflows

**Basic issue creation:**
```bash
bd create -t "Fix login button styling" -d "Button appears misaligned on mobile devices"
```
Creates a simple issue with title and description. The system generates a unique ID automatically.

**Feature with dependencies:**
```bash
bd create -t "Add user dashboard" --depends-on issue-123 --tag feature --priority high
```
Creates a new feature that depends on completing issue-123, tagged as a feature with high priority.

**Quick task creation:**
```bash
bd create -t "Update README with new API endpoints"
```
Minimal syntax for simple tasks where just a title is sufficient to get started.

## Tips & gotchas

- Issue IDs are auto-generated, so don't try to specify them manually
- Dependencies must reference existing issue IDs; invalid references will cause creation to fail
- Tags are free-form but consider establishing team conventions for consistency
- The description flag supports multi-line text, but wrap longer descriptions in quotes
- Issues are immediately committed to git, so they're visible to the entire team

## Related commands

- **`bd list`** — View existing issues and their statuses
- **`bd show`** — Display detailed information about specific issues
- **`bd edit`** — Modify issue details after creation
- **`bd depends`** — Manage dependencies between issues