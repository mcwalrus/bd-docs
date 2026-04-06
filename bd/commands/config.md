# `bd config`

**Command:** `bd config`  
**Slug:** `config`

## Help Output

```
Manage configuration settings for external integrations and preferences.

Configuration is stored per-project in the beads database and is version-control-friendly.

Common namespaces:
  - jira.*            Jira integration settings
  - linear.*          Linear integration settings
  - github.*          GitHub integration settings
  - custom.*          Custom integration settings
  - status.*          Issue status configuration
  - doctor.suppress.* Suppress specific bd doctor warnings (GH#1095)

Custom Status States:
  You can define custom status states for multi-step pipelines using the
  status.custom config key. Statuses should be comma-separated.

  Example:
    bd config set status.custom "awaiting_review,awaiting_testing,awaiting_docs"

  This enables issues to use statuses like 'awaiting_review' in addition to
  the built-in statuses (open, in_progress, blocked, deferred, closed).

Suppressing Doctor Warnings:
  Suppress specific bd doctor warnings by check name slug:
    bd config set doctor.suppress.pending-migrations true
    bd config set doctor.suppress.git-hooks true
  Check names are converted to slugs: "Git Hooks" → "git-hooks".
  Only warnings are suppressed (errors and passing checks always show).
  To unsuppress: bd config unset doctor.suppress.<slug>

Examples:
  bd config set jira.url "https://company.atlassian.net"
  bd config set jira.project "PROJ"
  bd config set status.custom "awaiting_review,awaiting_testing"
  bd config set doctor.suppress.pending-migrations true
  bd config get jira.url
  bd config list
  bd config unset jira.url

Usage:
  bd config [command]

Available Commands:
  get         Get a configuration value
  list        List all configuration
  set         Set a configuration value
  set-many    Set multiple configuration values in one operation
  unset       Delete a configuration value
  validate    Validate sync-related configuration

Flags:
  -h, --help   help for config

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

Use "bd config [command] --help" for more information about a command.
```

## Sub-commands

- [`bd config get`](./config-get.md) — Get a configuration value
- [`bd config list`](./config-list.md) — List all configuration
- [`bd config set`](./config-set.md) — Set a configuration value
- [`bd config set-many`](./config-set-many.md) — Set multiple configuration values in one operation
- [`bd config unset`](./config-unset.md) — Delete a configuration value
- [`bd config validate`](./config-validate.md) — Validate sync-related configuration
