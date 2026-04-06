# bd backup init

**Purpose** — Initialize a remote backup repository for syncing beads data to external Git hosting.

## When to use it

- Setting up your first backup for a beads project to prevent data loss
- Creating redundancy for critical issue tracking data before major changes
- Enabling team collaboration by establishing a shared remote repository
- Preparing for CI/CD integration that needs access to issue data
- Migrating from local-only beads usage to a distributed workflow

## Key flags / options

| Flag | Description |
|------|-------------|
| `--remote URL` | Specify the Git remote URL for the backup repository |
| `--branch NAME` | Set the target branch for backup sync (default: main) |
| `--force` | Overwrite existing backup configuration without confirmation |

## Example workflows

**Basic backup setup:**
```bash
bd backup init --remote git@github.com:myorg/myproject-beads.git
```
Creates a backup configuration pointing to a GitHub repository, automatically setting up the remote connection for future sync operations.

**Custom branch backup:**
```bash
bd backup init --remote https://gitlab.com/team/issues.git --branch beads-data
```
Initializes backup to a specific branch, useful when you want to keep beads data separate from your main codebase or share across multiple projects.

**Reconfiguring existing backup:**
```bash
bd backup init --remote git@newhost.com:backup/beads.git --force
```
Updates an existing backup configuration to point to a new remote, bypassing confirmation prompts.

## Tips & gotchas

- The remote repository should be empty or dedicated to beads data—this isn't meant for mixing with application code
- Ensure your Git credentials are configured before running, as the command will test the remote connection
- The backup branch will be created automatically if it doesn't exist on the remote
- Configuration is stored in `.beads/config` and affects all subsequent backup operations

## Related commands

- `bd backup sync` — Push local beads data to the configured backup remote
- `bd backup pull` — Retrieve and merge beads data from the backup remote  
- `bd backup status` — Check the current backup configuration and sync state
- `bd init` — Initialize a new beads project (typically run before backup setup)