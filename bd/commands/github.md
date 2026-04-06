# `bd github`

**Command:** `bd github`  
**Slug:** `github`

## Help Output

```
Commands for syncing issues between beads and GitHub.

Configuration can be set via 'bd config' or environment variables:
  github.token / GITHUB_TOKEN           - Personal access token
  github.owner / GITHUB_OWNER           - Repository owner
  github.repo / GITHUB_REPO             - Repository name
  github.repository / GITHUB_REPOSITORY - Combined "owner/repo" format
  github.url / GITHUB_API_URL           - Custom API URL (GitHub Enterprise)

Usage:
  bd github [command]

Available Commands:
  repos       List accessible GitHub repositories
  status      Show GitHub sync status
  sync        Sync issues with GitHub

Flags:
  -h, --help   help for github

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

Use "bd github [command] --help" for more information about a command.
```

## Sub-commands

- [`bd github repos`](./github-repos.md) — List accessible GitHub repositories
- [`bd github status`](./github-status.md) — Show GitHub sync status
- [`bd github sync`](./github-sync.md) — Sync issues with GitHub
