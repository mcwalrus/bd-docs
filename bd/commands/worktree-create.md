# `bd worktree create`

**Command:** `bd worktree create`  
**Slug:** `worktree-create`

## Help Output

```
Create a git worktree with proper beads configuration.

This command:
1. Creates a git worktree at ./<name> (or specified path)
2. Sets up .beads/redirect pointing to the main repository's .beads
3. Adds the worktree path to .gitignore (if inside repo root)

The worktree will share the same beads database as the main repository,
ensuring consistent issue state across all worktrees.

Examples:
  bd worktree create feature-auth           # Create at ./feature-auth
  bd worktree create bugfix --branch fix-1  # Create with branch name
  bd worktree create ../agents/worker-1     # Create at relative path

Usage:
  bd worktree create <name> [--branch=<branch>] [flags]

Flags:
      --branch string   Branch name for the worktree (default: same as name)
  -h, --help            help for create

Global Flags:
      --actor string              Actor name for audit trail (default: $BEADS_ACTOR, git user.name, $USER)
      --db string                 Database path (default: auto-discover .beads/*.db)
      --dolt-auto-commit string   Dolt auto-commit policy (off|on|batch). 'on': commit after each write. 'batch': defer commits to bd dolt commit; uncommitted changes persist in the working set until then. SIGTERM/SIGHUP flush pending batch commits. Default: off. Override via config key dolt.auto-commit
      --json                      Output in JSON format
      --profile                   Generate CPU profile for performance analysis
  -q, --quiet                     Suppress non-essential output (errors only)
      --readonly                  Read-only mode: block write operations (for worker sandboxes)
      --sandbox                   Sandbox mode: disables auto-sync
  -v, --verbose                   Enable verbose/debug output
```
