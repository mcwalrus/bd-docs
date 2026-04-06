# bd branch

**Purpose:** Creates a new git branch for working on a specific issue, automatically setting up branch naming and issue context.

## When to use it

- Starting work on a tagged issue that needs code changes
- Creating feature branches with consistent naming conventions
- Setting up isolated development environments for specific beads
- Beginning work on issues that require collaboration or review
- Preparing branches for pull requests linked to tracked issues

## Key flags / options

| Flag | Description |
|------|-------------|
| `--issue-id` | Specify the issue ID to create a branch for |
| `--name` | Override the default branch name pattern |
| `--base` | Set the base branch (defaults to current branch) |
| `--push` | Automatically push the new branch to remote |

## Example workflows

**Basic issue branch creation:**
```bash
bd branch --issue-id 42
git checkout issue-42-implement-user-auth
```
Creates and checks out a new branch following bd's naming convention, linking it to issue #42.

**Custom branch with remote push:**
```bash
bd branch --issue-id 15 --name feature/payment-gateway --push
```
Creates a custom-named branch for issue #15 and immediately pushes it to the remote repository.

**Branch from specific base:**
```bash
bd branch --issue-id 8 --base develop
git log --oneline -5
```
Creates an issue branch starting from the `develop` branch instead of the current branch, useful for feature work that needs to be based on the latest development state.

## Tips & gotchas

- Branch names automatically include the issue ID and a sanitized version of the issue title
- The command fails if you have uncommitted changes unless you stash them first
- bd tracks which branches are associated with which issues for better workflow integration
- Creating a branch doesn't automatically assign the issue to you—use `bd assign` separately if needed
- The branch creation updates local issue metadata to track the association

## Related commands

- `bd list` — Find issue IDs before creating branches
- `bd assign` — Assign issues to yourself when starting work
- `bd status` — Check which issues have active branches
- `bd close` — Complete and close issues when merging branches