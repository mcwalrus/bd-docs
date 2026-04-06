# bd — All Commands Reference

> Auto-generated on 2026-04-06 07:33 UTC  
> Total commands: 228

---

## Table of Contents

- [`bd admin cleanup`](#admin--cleanup)
- [`bd admin compact`](#admin--compact)
- [`bd admin reset`](#admin--reset)
- [`bd admin`](#admin)
- [`bd ado projects`](#ado--projects)
- [`bd ado status`](#ado--status)
- [`bd ado sync`](#ado--sync)
- [`bd ado`](#ado)
- [`bd assign`](#assign)
- [`bd audit label`](#audit--label)
- [`bd audit record`](#audit--record)
- [`bd audit`](#audit)
- [`bd backup init`](#backup--init)
- [`bd backup remove`](#backup--remove)
- [`bd backup restore`](#backup--restore)
- [`bd backup status`](#backup--status)
- [`bd backup sync`](#backup--sync)
- [`bd backup`](#backup)
- [`bd blocked`](#blocked)
- [`bd bootstrap`](#bootstrap)
- [`bd branch`](#branch)
- [`bd children`](#children)
- [`bd close`](#close)
- [`bd comment`](#comment)
- [`bd comments add`](#comments--add)
- [`bd comments`](#comments)
- [`bd compact`](#compact)
- [`bd config get`](#config--get)
- [`bd config list`](#config--list)
- [`bd config set many`](#config--set--many)
- [`bd config set`](#config--set)
- [`bd config unset`](#config--unset)
- [`bd config validate`](#config--validate)
- [`bd config`](#config)
- [`bd context`](#context)
- [`bd cook`](#cook)
- [`bd count`](#count)
- [`bd create form`](#create--form)
- [`bd create`](#create)
- [`bd defer`](#defer)
- [`bd delete`](#delete)
- [`bd dep add`](#dep--add)
- [`bd dep cycles`](#dep--cycles)
- [`bd dep list`](#dep--list)
- [`bd dep relate`](#dep--relate)
- [`bd dep remove`](#dep--remove)
- [`bd dep tree`](#dep--tree)
- [`bd dep unrelate`](#dep--unrelate)
- [`bd dep`](#dep)
- [`bd diff`](#diff)
- [`bd doctor`](#doctor)
- [`bd dolt commit`](#dolt--commit)
- [`bd dolt killall`](#dolt--killall)
- [`bd dolt pull`](#dolt--pull)
- [`bd dolt push`](#dolt--push)
- [`bd dolt remote add`](#dolt--remote--add)
- [`bd dolt remote list`](#dolt--remote--list)
- [`bd dolt remote remove`](#dolt--remote--remove)
- [`bd dolt remote`](#dolt--remote)
- [`bd dolt set`](#dolt--set)
- [`bd dolt show`](#dolt--show)
- [`bd dolt start`](#dolt--start)
- [`bd dolt status`](#dolt--status)
- [`bd dolt stop`](#dolt--stop)
- [`bd dolt test`](#dolt--test)
- [`bd dolt`](#dolt)
- [`bd duplicates`](#duplicates)
- [`bd edit`](#edit)
- [`bd epic status`](#epic--status)
- [`bd epic`](#epic)
- [`bd export`](#export)
- [`bd federation add peer`](#federation--add--peer)
- [`bd federation list peers`](#federation--list--peers)
- [`bd federation`](#federation)
- [`bd flatten`](#flatten)
- [`bd forget`](#forget)
- [`bd formula convert`](#formula--convert)
- [`bd formula list`](#formula--list)
- [`bd formula show`](#formula--show)
- [`bd formula`](#formula)
- [`bd gate add waiter`](#gate--add--waiter)
- [`bd gate check`](#gate--check)
- [`bd gate discover`](#gate--discover)
- [`bd gate list`](#gate--list)
- [`bd gate resolve`](#gate--resolve)
- [`bd gate show`](#gate--show)
- [`bd gate`](#gate)
- [`bd gc`](#gc)
- [`bd github repos`](#github--repos)
- [`bd github status`](#github--status)
- [`bd github sync`](#github--sync)
- [`bd github`](#github)
- [`bd gitlab projects`](#gitlab--projects)
- [`bd gitlab status`](#gitlab--status)
- [`bd gitlab sync`](#gitlab--sync)
- [`bd gitlab`](#gitlab)
- [`bd graph check`](#graph--check)
- [`bd graph`](#graph)
- [`bd history`](#history)
- [`bd hooks install`](#hooks--install)
- [`bd hooks list`](#hooks--list)
- [`bd hooks run`](#hooks--run)
- [`bd hooks uninstall`](#hooks--uninstall)
- [`bd hooks`](#hooks)
- [`bd human dismiss`](#human--dismiss)
- [`bd human list`](#human--list)
- [`bd human respond`](#human--respond)
- [`bd human stats`](#human--stats)
- [`bd human`](#human)
- [`bd import`](#import)
- [`bd index`](#index)
- [`bd info`](#info)
- [`bd init`](#init)
- [`bd jira status`](#jira--status)
- [`bd jira sync`](#jira--sync)
- [`bd jira`](#jira)
- [`bd kv clear`](#kv--clear)
- [`bd kv get`](#kv--get)
- [`bd kv list`](#kv--list)
- [`bd kv set`](#kv--set)
- [`bd kv`](#kv)
- [`bd label add`](#label--add)
- [`bd label list all`](#label--list--all)
- [`bd label list`](#label--list)
- [`bd label propagate`](#label--propagate)
- [`bd label remove`](#label--remove)
- [`bd label`](#label)
- [`bd linear status`](#linear--status)
- [`bd linear sync`](#linear--sync)
- [`bd linear teams`](#linear--teams)
- [`bd linear`](#linear)
- [`bd link`](#link)
- [`bd lint`](#lint)
- [`bd list`](#list)
- [`bd memories`](#memories)
- [`bd merge slot acquire`](#merge--slot--acquire)
- [`bd merge slot check`](#merge--slot--check)
- [`bd merge slot create`](#merge--slot--create)
- [`bd merge slot release`](#merge--slot--release)
- [`bd merge slot`](#merge--slot)
- [`bd migrate hooks`](#migrate--hooks)
- [`bd migrate issues`](#migrate--issues)
- [`bd migrate sync`](#migrate--sync)
- [`bd migrate`](#migrate)
- [`bd mol bond`](#mol--bond)
- [`bd mol burn`](#mol--burn)
- [`bd mol current`](#mol--current)
- [`bd mol distill`](#mol--distill)
- [`bd mol pour`](#mol--pour)
- [`bd mol progress`](#mol--progress)
- [`bd mol seed`](#mol--seed)
- [`bd mol show`](#mol--show)
- [`bd mol squash`](#mol--squash)
- [`bd mol stale`](#mol--stale)
- [`bd mol wisp create`](#mol--wisp--create)
- [`bd mol wisp gc`](#mol--wisp--gc)
- [`bd mol wisp list`](#mol--wisp--list)
- [`bd mol wisp`](#mol--wisp)
- [`bd mol`](#mol)
- [`bd note`](#note)
- [`bd notion connect`](#notion--connect)
- [`bd notion init`](#notion--init)
- [`bd notion status`](#notion--status)
- [`bd notion sync`](#notion--sync)
- [`bd notion`](#notion)
- [`bd onboard`](#onboard)
- [`bd orphans`](#orphans)
- [`bd preflight`](#preflight)
- [`bd prime`](#prime)
- [`bd priority`](#priority)
- [`bd promote`](#promote)
- [`bd purge`](#purge)
- [`bd q`](#q)
- [`bd query`](#query)
- [`bd quickstart`](#quickstart)
- [`bd ready`](#ready)
- [`bd recall`](#recall)
- [`bd rename prefix`](#rename--prefix)
- [`bd rename`](#rename)
- [`bd reopen`](#reopen)
- [`bd repo add`](#repo--add)
- [`bd repo list`](#repo--list)
- [`bd repo remove`](#repo--remove)
- [`bd repo sync`](#repo--sync)
- [`bd repo`](#repo)
- [`bd restore`](#restore)
- [`bd rules audit`](#rules--audit)
- [`bd rules compact`](#rules--compact)
- [`bd rules`](#rules)
- [`bd search`](#search)
- [`bd set state`](#set--state)
- [`bd setup`](#setup)
- [`bd ship`](#ship)
- [`bd show`](#show)
- [`bd sql`](#sql)
- [`bd stale`](#stale)
- [`bd state list`](#state--list)
- [`bd state`](#state)
- [`bd status`](#status)
- [`bd statuses`](#statuses)
- [`bd swarm create`](#swarm--create)
- [`bd swarm list`](#swarm--list)
- [`bd swarm status`](#swarm--status)
- [`bd swarm validate`](#swarm--validate)
- [`bd swarm`](#swarm)
- [`bd tag`](#tag)
- [`bd todo add`](#todo--add)
- [`bd todo done`](#todo--done)
- [`bd todo list`](#todo--list)
- [`bd todo`](#todo)
- [`bd types`](#types)
- [`bd undefer`](#undefer)
- [`bd update`](#update)
- [`bd upgrade ack`](#upgrade--ack)
- [`bd upgrade review`](#upgrade--review)
- [`bd upgrade status`](#upgrade--status)
- [`bd upgrade`](#upgrade)
- [`bd vc commit`](#vc--commit)
- [`bd vc merge`](#vc--merge)
- [`bd vc status`](#vc--status)
- [`bd vc`](#vc)
- [`bd version`](#version)
- [`bd where`](#where)
- [`bd worktree create`](#worktree--create)
- [`bd worktree info`](#worktree--info)
- [`bd worktree list`](#worktree--list)
- [`bd worktree remove`](#worktree--remove)
- [`bd worktree`](#worktree)

---

---

## bd admin cleanup

## `bd admin cleanup`

**Command:** `bd admin cleanup`  
**Slug:** `admin-cleanup`

### Help Output

```
Delete closed issues to reduce database size.

This command permanently removes closed issues from the database.

NOTE: This command only manages issue lifecycle (closed -> deleted). For general
health checks and automatic repairs, use 'bd doctor --fix' instead.

By default, deletes ALL closed issues. Use --older-than to only delete
issues closed before a certain date.

EXAMPLES:
  bd admin cleanup --force                          # Delete all closed issues
  bd admin cleanup --older-than 30 --force          # Only issues closed 30+ days ago
  bd admin cleanup --ephemeral --force              # Only closed wisps (transient molecules)
  bd admin cleanup --dry-run                        # Preview what would be deleted

SAFETY:
- Requires --force flag to actually delete (unless --dry-run)
- Supports --cascade to delete dependents
- Shows preview of what will be deleted
- Use --json for programmatic output

SEE ALSO:
  bd doctor --fix    Automatic health checks and repairs (recommended for routine maintenance)
  bd admin compact   Compact old closed issues to save space

Usage:
  bd admin cleanup [flags]

Flags:
      --cascade          Recursively delete all dependent issues
      --dry-run          Preview what would be deleted without making changes
      --ephemeral        Only delete closed wisps (transient molecules)
  -f, --force            Actually delete (without this flag, shows error)
  -h, --help             help for cleanup
      --older-than int   Only delete issues closed more than N days ago (0 = all closed issues)

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


---

## bd admin compact

## `bd admin compact`

**Command:** `bd admin compact`  
**Slug:** `admin-compact`

### Help Output

```
Compact old closed issues using semantic summarization.

Compaction reduces database size by summarizing closed issues that are no longer
actively referenced. This is permanent graceful decay - original content is discarded.

Modes:
  - Analyze: Export candidates for agent review (no API key needed)
  - Apply: Accept agent-provided summary (no API key needed)
  - Auto: AI-powered compaction (requires ANTHROPIC_API_KEY or ai.api_key, legacy)
  - Dolt: Run Dolt garbage collection (for Dolt-backend repositories)

Tiers:
  - Tier 1: Semantic compression (30 days closed, 70% reduction)
  - Tier 2: Ultra compression (90 days closed, 95% reduction)

Dolt Garbage Collection:
  With auto-commit per mutation, Dolt commit history grows over time. Use
  --dolt to run Dolt garbage collection and reclaim disk space.

  --dolt: Run Dolt GC on .beads/dolt directory to free disk space.
          This removes unreachable commits and compacts storage.

Examples:
  # Dolt garbage collection
  bd compact --dolt                        # Run Dolt GC
  bd compact --dolt --dry-run              # Preview without running GC

  # Agent-driven workflow (recommended)
  bd compact --analyze --json              # Get candidates with full content
  bd compact --apply --id bd-42 --summary summary.txt
  bd compact --apply --id bd-42 --summary - < summary.txt

  # Legacy AI-powered workflow
  bd compact --auto --dry-run              # Preview candidates
  bd compact --auto --all                  # Compact all eligible issues
  bd compact --auto --id bd-42             # Compact specific issue

  # Statistics
  bd compact --stats                       # Show statistics


Usage:
  bd admin compact [flags]

Flags:
      --actor string     Actor name for audit trail (default "agent")
      --all              Process all candidates
      --analyze          Analyze mode: export candidates for agent review
      --apply            Apply mode: accept agent-provided summary
      --auto             Auto mode: AI-powered compaction (legacy)
      --batch-size int   Issues per batch (default 10)
      --dolt             Dolt mode: run Dolt garbage collection on .beads/dolt
      --dry-run          Preview without compacting
      --force            Force compact (bypass checks, requires --id)
  -h, --help             help for compact
      --id string        Compact specific issue
      --json             Output JSON format
      --limit int        Limit number of candidates (0 = no limit)
      --stats            Show compaction statistics
      --summary string   Path to summary file (use '-' for stdin)
      --tier int         Compaction tier (1 or 2) (default 1)
      --workers int      Parallel workers (default 5)

Global Flags:
      --db string                 Database path (default: auto-discover .beads/*.db)
      --dolt-auto-commit string   Dolt auto-commit policy (off|on|batch). 'on': commit after each write. 'batch': defer commits to bd dolt commit; uncommitted changes persist in the working set until then. SIGTERM/SIGHUP flush pending batch commits. Default: off. Override via config key dolt.auto-commit
      --profile                   Generate CPU profile for performance analysis
  -q, --quiet                     Suppress non-essential output (errors only)
      --readonly                  Read-only mode: block write operations (for worker sandboxes)
      --sandbox                   Sandbox mode: disables auto-sync
  -v, --verbose                   Enable verbose/debug output
```


---

## bd admin reset

## `bd admin reset`

**Command:** `bd admin reset`  
**Slug:** `admin-reset`

### Help Output

```
Reset beads to an uninitialized state, removing all local data.

This command removes:
  - The .beads directory (database, JSONL, config)
  - Git hooks installed by bd
  - Sync branch worktrees

By default, shows what would be deleted (dry-run mode).
Use --force to actually perform the reset.

Examples:
  bd reset              # Show what would be deleted
  bd reset --force      # Actually delete everything

Usage:
  bd admin reset [flags]

Flags:
      --force   Actually perform the reset (required)
  -h, --help    help for reset

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


---

## bd admin

## `bd admin`

**Command:** `bd admin`  
**Slug:** `admin`

### Help Output

```
Administrative commands for beads database maintenance.

These commands are for advanced users and should be used carefully:
  cleanup   Delete closed issues (issue lifecycle)
  compact   Compact old closed issues to save space (storage optimization)
  reset     Remove all beads data and configuration (full reset)

For routine maintenance, prefer 'bd doctor --fix' which handles common repairs
automatically. Use these admin commands for targeted database operations.

Usage:
  bd admin [command]

Available Commands:
  cleanup     Delete closed issues to reduce database size
  compact     Compact old closed issues to save space
  reset       Remove all beads data and configuration

Flags:
  -h, --help   help for admin

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

Use "bd admin [command] --help" for more information about a command.
```

### Sub-commands

- [`bd admin cleanup`](./admin-cleanup.md) — Delete closed issues to reduce database size
- [`bd admin compact`](./admin-compact.md) — Compact old closed issues to save space
- [`bd admin reset`](./admin-reset.md) — Remove all beads data and configuration


---

## bd ado projects

## `bd ado projects`

**Command:** `bd ado projects`  
**Slug:** `ado-projects`

### Help Output

```
List Azure DevOps projects that the configured token has access to.

Usage:
  bd ado projects [flags]

Flags:
  -h, --help   help for projects

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


---

## bd ado status

## `bd ado status`

**Command:** `bd ado status`  
**Slug:** `ado-status`

### Help Output

```
Display current Azure DevOps configuration and sync status.

Usage:
  bd ado status [flags]

Flags:
  -h, --help   help for status

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


---

## bd ado sync

## `bd ado sync`

**Command:** `bd ado sync`  
**Slug:** `ado-sync`

### Help Output

```
Synchronize issues between beads and Azure DevOps.

By default, performs bidirectional sync:
- Pulls new/updated work items from Azure DevOps to beads
- Pushes local beads issues to Azure DevOps

Use --pull-only or --push-only to limit direction.

Filters (--area-path, --iteration-path, --types, --states) restrict
which work items are synced. On pull, they limit the WIQL query. On push,
--types and --states filter local beads before pushing to ADO. Use
--no-create with push to skip creating new ADO work items (only update
existing linked items). Filters can also be persisted via config:
  ado.filter.area_path, ado.filter.iteration_path,
  ado.filter.types, ado.filter.states
CLI flags override config values when both are set.

Usage:
  bd ado sync [flags]

Flags:
      --area-path string        Filter to ADO area path (e.g., "Project\Team")
      --bootstrap-match         Enable heuristic matching for first sync
      --dry-run                 Show what would be synced without making changes
  -h, --help                    help for sync
      --iteration-path string   Filter to ADO iteration path (e.g., "Project\Sprint 1")
      --no-create               Never create new items in either direction (pull or push)
      --prefer-ado              On conflict, use Azure DevOps version
      --prefer-local            On conflict, keep local beads version
      --prefer-newer            On conflict, use most recent version (default)
      --project strings         Project name(s) to sync (overrides configured project/projects)
      --pull-only               Only pull issues from Azure DevOps
      --push-only               Only push issues to Azure DevOps
      --reconcile               Force reconciliation scan for deleted items
      --states string           Filter to ADO states, comma-separated (e.g., "New,Active,Resolved")
      --types string            Filter to work item types, comma-separated (e.g., "Bug,Task,User Story")

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


---

## bd ado

## `bd ado`

**Command:** `bd ado`  
**Slug:** `ado`

### Help Output

```
Commands for syncing issues between beads and Azure DevOps.

Configuration can be set via 'bd config' or environment variables:
  ado.org / AZURE_DEVOPS_ORG              - Organization name
  ado.project / AZURE_DEVOPS_PROJECT      - Project name (single)
  ado.projects / AZURE_DEVOPS_PROJECTS    - Project names (comma-separated)
  ado.pat / AZURE_DEVOPS_PAT              - Personal access token
  ado.url / AZURE_DEVOPS_URL              - Custom base URL (on-prem)

Usage:
  bd ado [command]

Available Commands:
  projects    List accessible Azure DevOps projects
  status      Show Azure DevOps sync status
  sync        Sync issues with Azure DevOps

Flags:
  -h, --help   help for ado

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

Use "bd ado [command] --help" for more information about a command.
```

### Sub-commands

- [`bd ado projects`](./ado-projects.md) — List accessible Azure DevOps projects
- [`bd ado status`](./ado-status.md) — Show Azure DevOps sync status
- [`bd ado sync`](./ado-sync.md) — Sync issues with Azure DevOps


---

## bd assign

## `bd assign`

**Command:** `bd assign`  
**Slug:** `assign`

### Help Output

```
Assign an issue to someone.

Shorthand for 'bd update <id> --assignee <name>'.

Examples:
  bd assign bd-123 alice
  bd assign bd-123 ""      # unassign

Usage:
  bd assign <id> <name> [flags]

Flags:
  -h, --help   help for assign

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


---

## bd audit label

## `bd audit label`

**Command:** `bd audit label`  
**Slug:** `audit-label`

### Help Output

```
Append a label entry referencing an existing interaction

Usage:
  bd audit label <entry-id> [flags]

Flags:
  -h, --help            help for label
      --label string    Label value (e.g. "good" or "bad")
      --reason string   Reason for label

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


---

## bd audit record

## `bd audit record`

**Command:** `bd audit record`  
**Slug:** `audit-record`

### Help Output

```
Append an audit interaction entry

Usage:
  bd audit record [flags]

Flags:
      --error string       Error string (llm_call/tool_call)
      --exit-code int      Exit code (tool_call) (default -1)
  -h, --help               help for record
      --issue-id string    Related issue id (bd-...)
      --kind string        Entry kind (e.g. llm_call, tool_call, label)
      --model string       Model name (llm_call)
      --prompt string      Prompt text (llm_call)
      --response string    Response text (llm_call)
      --stdin              Read a JSON object from stdin (must match audit.Entry schema)
      --tool-name string   Tool name (tool_call)

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


---

## bd audit

## `bd audit`

**Command:** `bd audit`  
**Slug:** `audit`

### Help Output

```
Audit log entries are appended to .beads/interactions.jsonl.

Each line is one event. This file is intended to be versioned in git and used for:
- auditing ("why did the agent do that?")
- dataset generation (SFT/RL fine-tuning)

Entries are append-only. Labeling creates a new "label" entry that references a parent entry.

Usage:
  bd audit [command]

Available Commands:
  label       Append a label entry referencing an existing interaction
  record      Append an audit interaction entry

Flags:
  -h, --help   help for audit

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

Use "bd audit [command] --help" for more information about a command.
```

### Sub-commands

- [`bd audit label`](./audit-label.md) — Append a label entry referencing an existing interaction
- [`bd audit record`](./audit-record.md) — Append an audit interaction entry


---

## bd backup init

## `bd backup init`

**Command:** `bd backup init`  
**Slug:** `backup-init`

### Help Output

```
Configure a filesystem path or URL as a backup destination.

The path can be a local directory (external drive, NAS, Dropbox folder) or a
DoltHub remote URL. If the destination was previously configured, it is
updated to the new path.

Filesystem examples:
  bd backup add /mnt/usb/beads-backup
  bd backup add ~/Dropbox/beads-backup

DoltHub (recommended for cloud backup):
  bd backup add https://doltremoteapi.dolthub.com/myuser/beads-backup

After adding, run 'bd backup sync' to push your data.

Usage:
  bd backup init <path> [flags]

Aliases:
  init, add

Flags:
  -h, --help   help for init

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


---

## bd backup remove

## `bd backup remove`

**Command:** `bd backup remove`  
**Slug:** `backup-remove`

### Help Output

```
Remove the configured backup destination.

This unregisters the backup remote from Dolt and removes the local
backup configuration. The backup data at the destination is not deleted.

Usage:
  bd backup remove [flags]

Aliases:
  remove, rm

Flags:
  -h, --help   help for remove

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


---

## bd backup restore

## `bd backup restore`

**Command:** `bd backup restore`  
**Slug:** `backup-restore`

### Help Output

```
Restore the beads database from a Dolt-native backup.

By default, reads from .beads/backup/ (or the configured backup directory).
Optionally specify a path to a directory containing a Dolt backup.

Use --force to overwrite an existing database with the backup contents.

The database must already be initialized (run 'bd init' first if needed).
To initialize and restore in one step, use: bd init && bd backup restore

Usage:
  bd backup restore [path] [flags]

Flags:
      --force   Overwrite existing database with backup contents
  -h, --help    help for restore

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


---

## bd backup status

## `bd backup status`

**Command:** `bd backup status`  
**Slug:** `backup-status`

### Help Output

```
Show last backup status

Usage:
  bd backup status [flags]

Flags:
  -h, --help   help for status

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


---

## bd backup sync

## `bd backup sync`

**Command:** `bd backup sync`  
**Slug:** `backup-sync`

### Help Output

```
Sync the current beads database to the configured Dolt backup destination.

This pushes the entire database state (all branches, full history) to the
backup location configured with 'bd backup init'.

The backup is atomic — if the sync fails, the previous backup state is preserved.

Run 'bd backup init <path>' first to configure a destination.

Usage:
  bd backup sync [flags]

Flags:
  -h, --help   help for sync

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


---

## bd backup

## `bd backup`

**Command:** `bd backup`  
**Slug:** `backup`

### Help Output

```
Back up your beads database for off-machine recovery.

Commands:
  bd backup init <path>    Set up a backup destination (filesystem or DoltHub)
  bd backup sync           Push to configured backup destination
  bd backup restore [path] Restore from a backup directory
  bd backup remove         Remove backup destination
  bd backup status         Show backup status

DoltHub is recommended for cloud backup:
  bd backup init https://doltremoteapi.dolthub.com/<user>/<repo>
  Set DOLT_REMOTE_USER and DOLT_REMOTE_PASSWORD for authentication.

Usage:
  bd backup [command]

Available Commands:
  init        Set up a Dolt backup destination
  remove      Remove the configured backup destination
  restore     Restore database from a Dolt backup
  status      Show last backup status
  sync        Push database to configured Dolt backup

Flags:
  -h, --help   help for backup

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

Use "bd backup [command] --help" for more information about a command.
```

### Sub-commands

- [`bd backup init`](./backup-init.md) — Set up a Dolt backup destination
- [`bd backup remove`](./backup-remove.md) — Remove the configured backup destination
- [`bd backup restore`](./backup-restore.md) — Restore database from a Dolt backup
- [`bd backup status`](./backup-status.md) — Show last backup status
- [`bd backup sync`](./backup-sync.md) — Push database to configured Dolt backup


---

## bd blocked

## `bd blocked`

**Command:** `bd blocked`  
**Slug:** `blocked`

### Help Output

```
Show blocked issues

Usage:
  bd blocked [flags]

Flags:
  -h, --help            help for blocked
      --parent string   Filter to descendants of this bead/epic

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


---

## bd bootstrap

## `bd bootstrap`

**Command:** `bd bootstrap`  
**Slug:** `bootstrap`

### Help Output

```
Bootstrap sets up the beads database without destroying existing data.
Unlike 'bd init --force', bootstrap will never delete existing issues.

Bootstrap auto-detects the right action:
  • If sync.git-remote is configured: clones from the remote
  • If .beads/backup/*.jsonl exists: restores from backup
  • If .beads/issues.jsonl exists: imports from git-tracked JSONL
  • If no database exists: creates a fresh one
  • If database already exists: validates and reports status

This is the recommended command for:
  • Setting up beads on a fresh clone
  • Recovering after moving to a new machine
  • Repairing a broken database configuration

Non-interactive mode (--non-interactive, --yes/-y, or BD_NON_INTERACTIVE=1):
  Skips the confirmation prompt before executing the bootstrap plan.
  Also auto-detected when stdin is not a terminal or CI=true is set.

Examples:
  bd bootstrap              # Auto-detect and set up
  bd bootstrap --dry-run    # Show what would be done
  bd bootstrap --json       # Output plan as JSON
  bd bootstrap --yes        # Skip confirmation prompt


Usage:
  bd bootstrap [flags]

Flags:
      --dry-run           Show what would be done without doing it
  -h, --help              help for bootstrap
      --non-interactive   Alias for --yes
  -y, --yes               Skip confirmation prompts (for CI/automation)

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


---

## bd branch

## `bd branch`

**Command:** `bd branch`  
**Slug:** `branch`

### Help Output

```
List all branches or create a new branch.

This command requires the Dolt storage backend. Without arguments,
it lists all branches. With an argument, it creates a new branch.

Examples:
  bd branch                    # List all branches
  bd branch feature-xyz        # Create a new branch named feature-xyz

Usage:
  bd branch [name] [flags]

Flags:
  -h, --help   help for branch

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


---

## bd children

## `bd children`

**Command:** `bd children`  
**Slug:** `children`

### Help Output

```
List all beads that are children of the specified parent bead.

This is a convenience alias for 'bd list --parent <id> --status all'.
Unlike plain 'bd list', children includes closed issues by default,
since the primary use case is inspecting all work under a parent.

Examples:
  bd children hq-abc123        # List all children of hq-abc123
  bd children hq-abc123 --json # List children in JSON format
  bd children hq-abc123 --pretty # Show children in tree format

Usage:
  bd children <parent-id> [flags]

Flags:
  -h, --help   help for children

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


---

## bd close

## `bd close`

**Command:** `bd close`  
**Slug:** `close`

### Help Output

```
Close one or more issues.

If no issue ID is provided, closes the last touched issue (from most recent
create, update, show, or close operation).

Usage:
  bd close [id...] [flags]

Aliases:
  close, done

Flags:
      --claim-next       Automatically claim the next highest priority available issue
      --continue         Auto-advance to next step in molecule
  -f, --force            Force close pinned issues or unsatisfied gates
  -h, --help             help for close
      --no-auto          With --continue, show next step but don't claim it
  -r, --reason string    Reason for closing
      --session string   Claude Code session ID (or set CLAUDE_SESSION_ID env var)
      --suggest-next     Show newly unblocked issues after closing

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


---

## bd comment

## `bd comment`

**Command:** `bd comment`  
**Slug:** `comment`

### Help Output

```
Add a comment to an issue.

Shorthand for 'bd comments add <id> "text"'.

Examples:
  bd comment bd-123 "Working on this now"
  bd comment bd-123 Working on this now
  echo "comment from pipe" | bd comment bd-123 --stdin
  bd comment bd-123 --file notes.txt

Usage:
  bd comment <id> [text...] [flags]

Flags:
      --file string   Read comment text from file
  -h, --help          help for comment
      --stdin         Read comment text from stdin

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


---

## bd comments add

## `bd comments add`

**Command:** `bd comments add`  
**Slug:** `comments-add`

### Help Output

```
Add a comment to an issue.

Examples:
  # Add a comment
  bd comments add bd-123 "Working on this now"

  # Add a comment from a file
  bd comments add bd-123 -f notes.txt

Usage:
  bd comments add [issue-id] [text] [flags]

Flags:
  -a, --author string   Add author to comment
  -f, --file string     Read comment text from file
  -h, --help            help for add

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


---

## bd comments

## `bd comments`

**Command:** `bd comments`  
**Slug:** `comments`

### Help Output

```
View or manage comments on an issue.

Examples:
  # List all comments on an issue
  bd comments bd-123

  # List comments in JSON format
  bd comments bd-123 --json

  # Add a comment
  bd comments add bd-123 "This is a comment"

  # Add a comment from a file
  bd comments add bd-123 -f notes.txt

Usage:
  bd comments [issue-id] [flags]
  bd comments [command]

Available Commands:
  add         Add a comment to an issue

Flags:
  -h, --help         help for comments
      --local-time   Show timestamps in local time instead of UTC

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

Use "bd comments [command] --help" for more information about a command.
```

### Sub-commands

- [`bd comments add`](./comments-add.md) — Add a comment to an issue


---

## bd compact

## `bd compact`

**Command:** `bd compact`  
**Slug:** `compact`

### Help Output

```
Squash Dolt commits older than N days into a single commit.

Recent commits (within the retention window) are preserved via cherry-pick.
This reduces Dolt storage overhead from auto-commit history while keeping
recent change tracking intact.

For semantic issue compaction (summarizing closed issues), use 'bd admin compact'.
For full history squash, use 'bd flatten'.

How it works:
  1. Identifies commits older than --days threshold
  2. Creates a squashed base commit from all old history
  3. Cherry-picks recent commits on top
  4. Swaps main branch to the compacted version
  5. Runs Dolt GC to reclaim space

Examples:
  bd compact --dry-run               # Preview: show commit breakdown
  bd compact --force                 # Squash commits older than 30 days
  bd compact --days 7 --force        # Keep only last 7 days of history
  bd compact --days 90 --force       # Conservative: squash 90+ day old commits

Usage:
  bd compact [flags]

Flags:
      --days int   Keep commits newer than N days (default 30)
      --dry-run    Preview without making changes
  -f, --force      Confirm commit squash
  -h, --help       help for compact

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


---

## bd config get

## `bd config get`

**Command:** `bd config get`  
**Slug:** `config-get`

### Help Output

```
Get a configuration value

Usage:
  bd config get <key> [flags]

Flags:
  -h, --help   help for get

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


---

## bd config list

## `bd config list`

**Command:** `bd config list`  
**Slug:** `config-list`

### Help Output

```
List all configuration

Usage:
  bd config list [flags]

Flags:
  -h, --help   help for list

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


---

## bd config set many

## `bd config set-many`

**Command:** `bd config set-many`  
**Slug:** `config-set-many`

### Help Output

```
Set multiple configuration values at once with a single auto-commit and auto-push.

Each argument must be in key=value format. All values are validated before
any writes occur. This is faster and less noisy than separate 'bd config set'
calls, especially in CI.

Examples:
  bd config set-many ado.state_map.open=New ado.state_map.closed=Closed
  bd config set-many jira.url=https://example.atlassian.net jira.project=PROJ

Usage:
  bd config set-many <key=value>... [flags]

Flags:
  -h, --help   help for set-many

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


---

## bd config set

## `bd config set`

**Command:** `bd config set`  
**Slug:** `config-set`

### Help Output

```
Set a configuration value

Usage:
  bd config set <key> <value> [flags]

Flags:
  -h, --help   help for set

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


---

## bd config unset

## `bd config unset`

**Command:** `bd config unset`  
**Slug:** `config-unset`

### Help Output

```
Delete a configuration value

Usage:
  bd config unset <key> [flags]

Flags:
  -h, --help   help for unset

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


---

## bd config validate

## `bd config validate`

**Command:** `bd config validate`  
**Slug:** `config-validate`

### Help Output

```
Validate sync-related configuration settings.

Checks:
  - federation.sovereignty is valid (T1, T2, T3, T4, or empty)
  - federation.remote is set for Dolt sync
  - Remote URL format is valid (dolthub://, gs://, s3://, file://)
  - routing.mode is valid (auto, maintainer, contributor, explicit)

Examples:
  bd config validate
  bd config validate --json

Usage:
  bd config validate [flags]

Flags:
  -h, --help   help for validate

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


---

## bd config

## `bd config`

**Command:** `bd config`  
**Slug:** `config`

### Help Output

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

### Sub-commands

- [`bd config get`](./config-get.md) — Get a configuration value
- [`bd config list`](./config-list.md) — List all configuration
- [`bd config set`](./config-set.md) — Set a configuration value
- [`bd config set-many`](./config-set-many.md) — Set multiple configuration values in one operation
- [`bd config unset`](./config-unset.md) — Delete a configuration value
- [`bd config validate`](./config-validate.md) — Validate sync-related configuration


---

## bd context

## `bd context`

**Command:** `bd context`  
**Slug:** `context`

### Help Output

```
Show the effective backend identity information including repository paths,
backend configuration, and sync settings.

This command reads directly from config files and does not require the
database to be open, making it useful for diagnostics in degraded states.

Examples:
  bd context           # Show context information
  bd context --json    # Output in JSON format


Usage:
  bd context [flags]

Flags:
  -h, --help   help for context

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


---

## bd cook

## `bd cook`

**Command:** `bd cook`  
**Slug:** `cook`

### Help Output

```
Cook transforms a .formula.json file into a proto.

By default, cook outputs the resolved formula as JSON to stdout for
ephemeral use. The output can be inspected, piped, or saved to a file.

Two cooking modes are available:
  COMPILE-TIME (default, --mode=compile):
    Produces a proto with {{variable}} placeholders intact.
    Use for: modeling, estimation, contractor handoff, planning.
    Variables are NOT substituted - the output shows the template structure.

  RUNTIME (--mode=runtime or when --var flags provided):
    Produces a fully-resolved proto with variables substituted.
    Use for: final validation before pour, seeing exact output.
    Requires all variables to have values (via --var or defaults).

Formulas are high-level workflow templates that support:
  - Variable definitions with defaults and validation
  - Step definitions that become issue hierarchies
  - Composition rules for bonding formulas together
  - Inheritance via extends

The --persist flag enables the legacy behavior of writing the proto
to the database. This is useful when you want to reuse the same
proto multiple times without re-cooking.

For most workflows, prefer ephemeral protos: pour and wisp commands
accept formula names directly and cook inline.

Examples:
  bd cook mol-feature.formula.json                    # Compile-time: keep {{vars}}
  bd cook mol-feature --var name=auth                 # Runtime: substitute vars
  bd cook mol-feature --mode=runtime --var name=auth  # Explicit runtime mode
  bd cook mol-feature --dry-run                       # Preview steps
  bd cook mol-release.formula.json --persist          # Write to database
  bd cook mol-release.formula.json --persist --force  # Replace existing

Output (default):
  JSON representation of the resolved formula with all steps.

Output (--persist):
  Creates a proto bead in the database with:
  - ID matching the formula name (e.g., mol-feature)
  - The "template" label for proto identification
  - Child issues for each step
  - Dependencies matching depends_on relationships

Usage:
  bd cook <formula-file> [flags]

Flags:
      --dry-run               Preview what would be created
      --force                 Replace existing proto if it exists (requires --persist)
  -h, --help                  help for cook
      --mode string           Cooking mode: compile (keep placeholders) or runtime (substitute vars)
      --persist               Persist proto to database (legacy behavior)
      --prefix string         Prefix to prepend to proto ID (e.g., 'gt-' creates 'gt-mol-feature')
      --search-path strings   Additional paths to search for formula inheritance
      --var stringArray       Variable substitution (key=value), enables runtime mode

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


---

## bd count

## `bd count`

**Command:** `bd count`  
**Slug:** `count`

### Help Output

```
Count issues matching the specified filters.

By default, returns the total count of issues matching the filters.
Use --by-* flags to group counts by different attributes.

Examples:
  bd count                          # Count all issues
  bd count --status open            # Count open issues
  bd count --by-status              # Group count by status
  bd count --by-priority            # Group count by priority
  bd count --by-type                # Group count by issue type
  bd count --by-assignee            # Group count by assignee
  bd count --by-label               # Group count by label
  bd count --assignee alice --by-status  # Count alice's issues by status


Usage:
  bd count [flags]

Flags:
  -a, --assignee string         Filter by assignee
      --by-assignee             Group count by assignee
      --by-label                Group count by label
      --by-priority             Group count by priority
      --by-status               Group count by status
      --by-type                 Group count by issue type
      --closed-after string     Filter issues closed after date (YYYY-MM-DD or RFC3339)
      --closed-before string    Filter issues closed before date (YYYY-MM-DD or RFC3339)
      --created-after string    Filter issues created after date (YYYY-MM-DD or RFC3339)
      --created-before string   Filter issues created before date (YYYY-MM-DD or RFC3339)
      --desc-contains string    Filter by description substring
      --empty-description       Filter issues with empty description
  -h, --help                    help for count
      --id string               Filter by specific issue IDs (comma-separated)
  -l, --label strings           Filter by labels (AND: must have ALL)
      --label-any strings       Filter by labels (OR: must have AT LEAST ONE)
      --no-assignee             Filter issues with no assignee
      --no-labels               Filter issues with no labels
      --notes-contains string   Filter by notes substring
  -p, --priority int            Filter by priority (0-4: 0=critical, 1=high, 2=medium, 3=low, 4=backlog)
      --priority-max int        Filter by maximum priority (inclusive)
      --priority-min int        Filter by minimum priority (inclusive)
  -s, --status string           Filter by stored status (open, in_progress, blocked, deferred, closed). Note: dependency-blocked issues use 'bd blocked'
      --title string            Filter by title text (case-insensitive substring match)
      --title-contains string   Filter by title substring
  -t, --type string             Filter by type (bug, feature, task, epic, chore, decision, merge-request, molecule, gate)
      --updated-after string    Filter issues updated after date (YYYY-MM-DD or RFC3339)
      --updated-before string   Filter issues updated before date (YYYY-MM-DD or RFC3339)

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


---

## bd create form

## `bd create-form`

**Command:** `bd create-form`  
**Slug:** `create-form`

### Help Output

```
Create a new issue using an interactive terminal form.

This command provides a user-friendly form interface for creating issues,
with fields for title, description, type, priority, labels, and more.

Use --parent to create a sub-issue under an existing parent issue.
The child will get an auto-generated hierarchical ID (e.g., parent-id.1).

The form uses keyboard navigation:
  - Tab/Shift+Tab: Move between fields
  - Enter: Submit the form (on the last field or submit button)
  - Ctrl+C: Cancel and exit
  - Arrow keys: Navigate within select fields

Usage:
  bd create-form [flags]

Flags:
  -h, --help            help for create-form
      --parent string   Parent issue ID for creating a hierarchical child (e.g., 'bd-a3f8e9')

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


---

## bd create

## `bd create`

**Command:** `bd create`  
**Slug:** `create`

### Help Output

```
Create a new issue (or batch from markdown/graph JSON)

Usage:
  bd create [title] [flags]

Aliases:
  create, new

Flags:
      --acceptance string       Acceptance criteria
      --append-notes string     Append to existing notes (with newline separator)
  -a, --assignee string         Assignee
      --body-file string        Read description from file (use - for stdin)
      --context string          Additional context for the issue
      --defer string            Defer until date (issue hidden from bd ready until then). Same formats as --due
      --deps strings            Dependencies in format 'type:id' or 'id' (e.g., 'discovered-from:bd-20,blocks:bd-15' or 'bd-20')
  -d, --description string      Issue description
      --design string           Design notes
      --design-file string      Read design from file (use - for stdin)
      --dry-run                 Preview what would be created without actually creating
      --due string              Due date/time. Formats: +6h, +1d, +2w, tomorrow, next monday, 2025-01-15
      --ephemeral               Create as ephemeral (short-lived, subject to TTL compaction)
  -e, --estimate int            Time estimate in minutes (e.g., 60 for 1 hour)
      --event-actor string      Entity URI who caused this event (requires --type=event)
      --event-category string   Event category (e.g., patrol.muted, agent.started) (requires --type=event)
      --event-payload string    Event-specific JSON data (requires --type=event)
      --event-target string     Entity URI or bead ID affected (requires --type=event)
      --external-ref string     External reference (e.g., 'gh-9', 'jira-ABC')
  -f, --file string             Create multiple issues from markdown file
      --force                   Force creation even if prefix doesn't match database prefix
      --graph string            Create a graph of issues with dependencies from JSON plan file
  -h, --help                    help for create
      --id string               Explicit issue ID (e.g., 'bd-42' for partitioning)
  -l, --labels strings          Labels (comma-separated)
      --metadata string         Set custom metadata (JSON string or @file.json to read from file)
      --mol-type string         Molecule type: swarm (multi-agent), patrol (recurring ops), work (default)
      --no-history              Skip Dolt commit history without making GC-eligible (for permanent agent beads)
      --no-inherit-labels       Don't inherit labels from parent issue
      --notes string            Additional notes
      --parent string           Parent issue ID for hierarchical child (e.g., 'bd-a3f8e9')
  -p, --priority string         Priority (0-4 or P0-P4, 0=highest) (default "2")
      --repo string             Target repository for issue (overrides auto-routing)
      --silent                  Output only the issue ID (for scripting)
      --skills string           Required skills for this issue
      --spec-id string          Link to specification document
      --stdin                   Read description from stdin (alias for --body-file -)
      --title string            Issue title (alternative to positional argument)
  -t, --type string             Issue type (bug|feature|task|epic|chore|decision); custom types require types.custom config; aliases: enhancement/feat→feature, dec/adr→decision (default "task")
      --validate                Validate description contains required sections for issue type
      --waits-for string        Spawner issue ID to wait for (creates waits-for dependency for fanout gate)
      --waits-for-gate string   Gate type: all-children (wait for all) or any-children (wait for first) (default "all-children")
      --wisp-type string        Wisp type for TTL-based compaction: heartbeat, ping, patrol, gc_report, recovery, error, escalation

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


---

## bd defer

## `bd defer`

**Command:** `bd defer`  
**Slug:** `defer`

### Help Output

```
Defer issues to put them on ice for later.

Deferred issues are deliberately set aside - not blocked by anything specific,
just postponed for future consideration. Unlike blocked issues, there's no
dependency keeping them from being worked. Unlike closed issues, they will
be revisited.

Deferred issues don't show in 'bd ready' but remain visible in 'bd list'.

Examples:
  bd defer bd-abc                  # Defer a single issue (status-based)
  bd defer bd-abc --until=tomorrow # Defer until specific time
  bd defer bd-abc bd-def           # Defer multiple issues

Usage:
  bd defer [id...] [flags]

Flags:
  -h, --help           help for defer
      --until string   Defer until specific time (e.g., +1h, tomorrow, next monday)

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


---

## bd delete

## `bd delete`

**Command:** `bd delete`  
**Slug:** `delete`

### Help Output

```
Delete one or more issues and clean up all references to them.
This command will:
1. Remove all dependency links (any type, both directions) involving the issues
2. Update text references to "[deleted:ID]" in directly connected issues
3. Permanently delete the issues from the database

This is a destructive operation that cannot be undone. Use with caution.

BATCH DELETION:
Delete multiple issues at once:
  bd delete bd-1 bd-2 bd-3 --force

Delete from file (one ID per line):
  bd delete --from-file deletions.txt --force

Preview before deleting:
  bd delete --from-file deletions.txt --dry-run

DEPENDENCY HANDLING:
Default: Fails if any issue has dependents not in deletion set
  bd delete bd-1 bd-2

Cascade: Recursively delete all dependents
  bd delete bd-1 --cascade --force

Force: Delete and orphan dependents
  bd delete bd-1 --force

Usage:
  bd delete <issue-id> [issue-id...] [flags]

Flags:
      --cascade            Recursively delete all dependent issues
      --dry-run            Preview what would be deleted without making changes
  -f, --force              Actually delete (without this flag, shows preview)
      --from-file string   Read issue IDs from file (one per line)
  -h, --help               help for delete

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


---

## bd dep add

## `bd dep add`

**Command:** `bd dep add`  
**Slug:** `dep-add`

### Help Output

```
Add a dependency between two issues.

The depends-on-id can be provided as:
  - A positional argument: bd dep add issue-123 issue-456
  - A flag: bd dep add issue-123 --blocked-by issue-456
  - A flag: bd dep add issue-123 --depends-on issue-456

The --blocked-by and --depends-on flags are aliases and both mean "issue-123
depends on (is blocked by) the specified issue."

The depends-on-id can be:
  - A local issue ID (e.g., bd-xyz)
  - An external reference: external:<project>:<capability>

External references are stored as-is and resolved at query time using
the external_projects config. They block the issue until the capability
is "shipped" in the target project.

Examples:
  bd dep add bd-42 bd-41                              # Positional args
  bd dep add bd-42 --blocked-by bd-41                 # Flag syntax (same effect)
  bd dep add bd-42 --depends-on bd-41                 # Alias (same effect)
  bd dep add gt-xyz external:beads:mol-run-assignee   # Cross-project dependency

Usage:
  bd dep add [issue-id] [depends-on-id] [flags]

Flags:
      --blocked-by string   Issue ID that blocks the first issue (alternative to positional arg)
      --depends-on string   Issue ID that the first issue depends on (alias for --blocked-by)
  -h, --help                help for add
  -t, --type string         Dependency type (blocks|tracks|related|parent-child|discovered-from|until|caused-by|validates|relates-to|supersedes) (default "blocks")

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


---

## bd dep cycles

## `bd dep cycles`

**Command:** `bd dep cycles`  
**Slug:** `dep-cycles`

### Help Output

```
Detect dependency cycles

Usage:
  bd dep cycles [flags]

Flags:
  -h, --help   help for cycles

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


---

## bd dep list

## `bd dep list`

**Command:** `bd dep list`  
**Slug:** `dep-list`

### Help Output

```
List dependencies or dependents of one or more issues with optional type filtering.

By default shows dependencies (what issues depend on). Use --direction to control:
  - down: Show dependencies (what this issue depends on) - default
  - up:   Show dependents (what depends on this issue)

Multiple IDs can be provided for batch dep listing. With --json, the output
is a flat array of dependency records across all requested issues.

Use --type to filter by dependency type (e.g., tracks, blocks, parent-child).

Examples:
  bd dep list gt-abc                     # Show what gt-abc depends on
  bd dep list gt-abc gt-def              # Batch: deps for both issues
  bd dep list gt-abc --direction=up      # Show what depends on gt-abc
  bd dep list gt-abc --direction=up -t tracks  # Show what tracks gt-abc (convoy tracking)

Usage:
  bd dep list [issue-id...] [flags]

Flags:
      --direction string   Direction: 'down' (dependencies), 'up' (dependents) (default "down")
  -h, --help               help for list
  -t, --type string        Filter by dependency type (e.g., tracks, blocks, parent-child)

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


---

## bd dep relate

## `bd dep relate`

**Command:** `bd dep relate`  
**Slug:** `dep-relate`

### Help Output

```
Create a loose 'see also' relationship between two issues.

The relates_to link is bidirectional - both issues will reference each other.
This enables knowledge graph connections without blocking or hierarchy.

Examples:
  bd relate bd-abc bd-xyz    # Link two related issues
  bd relate bd-123 bd-456    # Create see-also connection

Usage:
  bd dep relate <id1> <id2> [flags]

Flags:
  -h, --help   help for relate

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


---

## bd dep remove

## `bd dep remove`

**Command:** `bd dep remove`  
**Slug:** `dep-remove`

### Help Output

```
Remove a dependency

Usage:
  bd dep remove [issue-id] [depends-on-id] [flags]

Aliases:
  remove, rm

Flags:
  -h, --help   help for remove

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


---

## bd dep tree

## `bd dep tree`

**Command:** `bd dep tree`  
**Slug:** `dep-tree`

### Help Output

```
Show dependency tree rooted at the given issue.

By default, shows dependencies (what blocks this issue). Use --direction to control:
  - down: Show dependencies (what blocks this issue) - default
  - up:   Show dependents (what this issue blocks)
  - both: Show full graph in both directions

Examples:
  bd dep tree gt-0iqq                    # Show what blocks gt-0iqq
  bd dep tree gt-0iqq --direction=up     # Show what gt-0iqq blocks
  bd dep tree gt-0iqq --status=open      # Only show open issues
  bd dep tree gt-0iqq --depth=3          # Limit to 3 levels deep

Usage:
  bd dep tree [issue-id] [flags]

Flags:
      --direction string   Tree direction: 'down' (dependencies), 'up' (dependents), or 'both'
      --format string      Output format: 'mermaid' for Mermaid.js flowchart
  -h, --help               help for tree
  -d, --max-depth int      Maximum tree depth to display (safety limit) (default 50)
      --reverse            Show dependent tree (deprecated: use --direction=up)
      --show-all-paths     Show all paths to nodes (no deduplication for diamond dependencies)
      --status string      Filter to only show issues with this status (open, in_progress, blocked, deferred, closed)

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


---

## bd dep unrelate

## `bd dep unrelate`

**Command:** `bd dep unrelate`  
**Slug:** `dep-unrelate`

### Help Output

```
Remove a relates_to relationship between two issues.

Removes the link in both directions.

Example:
  bd unrelate bd-abc bd-xyz

Usage:
  bd dep unrelate <id1> <id2> [flags]

Flags:
  -h, --help   help for unrelate

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


---

## bd dep

## `bd dep`

**Command:** `bd dep`  
**Slug:** `dep`

### Help Output

```
Manage dependencies between issues.

When called with an issue ID and --blocks flag, creates a blocking dependency:
  bd dep <blocker-id> --blocks <blocked-id>

This is equivalent to:
  bd dep add <blocked-id> <blocker-id>

Examples:
  bd dep bd-xyz --blocks bd-abc    # bd-xyz blocks bd-abc
  bd dep add bd-abc bd-xyz         # Same as above (bd-abc depends on bd-xyz)

Usage:
  bd dep [issue-id] [flags]
  bd dep [command]

Available Commands:
  add         Add a dependency
  cycles      Detect dependency cycles
  list        List dependencies or dependents of one or more issues
  relate      Create a bidirectional relates_to link between issues
  remove      Remove a dependency
  tree        Show dependency tree
  unrelate    Remove a relates_to link between issues

Flags:
  -b, --blocks string   Issue ID that this issue blocks (shorthand for: bd dep add <blocked> <blocker>)
  -h, --help            help for dep

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

Use "bd dep [command] --help" for more information about a command.
```

### Sub-commands

- [`bd dep add`](./dep-add.md) — Add a dependency
- [`bd dep cycles`](./dep-cycles.md) — Detect dependency cycles
- [`bd dep list`](./dep-list.md) — List dependencies or dependents of one or more issues
- [`bd dep relate`](./dep-relate.md) — Create a bidirectional relates_to link between issues
- [`bd dep remove`](./dep-remove.md) — Remove a dependency
- [`bd dep tree`](./dep-tree.md) — Show dependency tree
- [`bd dep unrelate`](./dep-unrelate.md) — Remove a relates_to link between issues


---

## bd diff

## `bd diff`

**Command:** `bd diff`  
**Slug:** `diff`

### Help Output

```
Show the differences in issues between two commits or branches.

The refs can be:
- Commit hashes (e.g., abc123def)
- Branch names (e.g., main, feature-branch)
- Special refs like HEAD, HEAD~1

Examples:
  bd diff main feature-branch   # Compare main to feature branch
  bd diff HEAD~5 HEAD           # Show changes in last 5 commits
  bd diff abc123 def456         # Compare two specific commits

Usage:
  bd diff <from-ref> <to-ref> [flags]

Flags:
  -h, --help   help for diff

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


---

## bd doctor

## `bd doctor`

**Command:** `bd doctor`  
**Slug:** `doctor`

### Help Output

```
Sanity check the beads installation for the current directory or specified path.

This command checks:
  - If .beads/ directory exists
  - Database version and migration status
  - Schema compatibility (all required tables and columns present)
  - Whether using hash-based vs sequential IDs
  - If CLI version is current (checks GitHub releases)
  - If Claude plugin is current (when running in Claude Code)
  - File permissions
  - Circular dependencies
  - Git hooks (pre-commit, post-merge, pre-push)
  - .beads/.gitignore up to date
  - Metadata.json version tracking (LastBdVersion field)

Performance Mode (--perf):
  Run performance diagnostics on your database:
  - Times key operations (bd ready, bd list, bd show, etc.)
  - Collects system info (OS, arch, SQLite version, database stats)
  - Generates CPU profile for analysis
  - Outputs shareable report for bug reports

Export Mode (--output):
  Save diagnostics to a JSON file for historical analysis and bug reporting.
  Includes timestamp and platform info for tracking intermittent issues.

Specific Check Mode (--check):
  Run a specific check in detail. Available checks:
  - artifacts: Detect and optionally clean beads classic artifacts
    (stale JSONL, SQLite files, cruft .beads dirs). Use with --clean.
  - conventions: Check for convention drift (lint warnings, stale
    issues, orphaned issues). Advisory only - warns, never blocks.
  - pollution: Detect and optionally clean test issues from database
  - validate: Run focused data-integrity checks (duplicates, orphaned
    deps, test pollution, git conflicts). Use with --fix to auto-repair.

Deep Validation Mode (--deep):
  Validate full graph integrity. May be slow on large databases.
  Additional checks:
  - Parent consistency: All parent-child deps point to existing issues
  - Dependency integrity: All deps reference valid issues
  - Epic completeness: Find epics ready to close (all children closed)
  - Agent bead integrity: Agent beads have valid state values
  - Mail thread integrity: Thread IDs reference existing issues
  - Molecule integrity: Molecules have valid parent-child structures

Server Mode (--server):
  Run health checks for Dolt server mode connections (bd-dolt.2.3):
  - Server reachable: Can connect to configured host:port?
  - Dolt version: Is it a Dolt server (not vanilla MySQL)?
  - Database exists: Does the 'beads' database exist?
  - Schema compatible: Can query beads tables?
  - Connection pool: Pool health metrics

Migration Validation Mode (--migration):
  Run Dolt migration validation checks with machine-parseable output.
  Use --migration=pre before migration to verify readiness:
  - JSONL file exists and is valid (parseable, no corruption)
  - All JSONL issues are present in SQLite (or explains discrepancies)
  - No blocking issues prevent migration
  Use --migration=post after migration to verify completion:
  - Dolt database exists and is healthy
  - All issues from JSONL are present in Dolt
  - No data was lost during migration
  - Dolt database has no locks or uncommitted changes
  Combine with --json for machine-parseable output for automation.

Agent Mode (--agent):
  Output diagnostics designed for AI agent consumption. Instead of terse
  pass/fail messages, each issue includes:
  - Observed state: what the system actually looks like
  - Expected state: what it should look like
  - Explanation: full prose context about the issue and why it matters
  - Commands: exact remediation commands to run
  - Source files: where in the codebase to investigate further
  - Severity: blocking (prevents operation), degraded (partial function),
    or advisory (informational only)
  ZFC-compliant: Go observes and reports, the agent decides and acts.
  Combine with --json for structured agent-facing output.

Suppressing Warnings:
  Suppress specific warnings by setting doctor.suppress.<check-slug> config:
    bd config set doctor.suppress.pending-migrations true
    bd config set doctor.suppress.git-hooks true
  Check names are converted to slugs: "Git Hooks" → "git-hooks".
  Only warnings are suppressed; errors and passing checks always show.
  To unsuppress: bd config unset doctor.suppress.<slug>

Examples:
  bd doctor              # Check current directory
  bd doctor /path/to/repo # Check specific repository
  bd doctor --json       # Machine-readable output
  bd doctor --agent      # Agent-facing diagnostic output
  bd doctor --agent --json  # Structured agent diagnostics (JSON)
  bd doctor --fix        # Automatically fix issues (with confirmation)
  bd doctor --fix --yes  # Automatically fix issues (no confirmation)
  bd doctor --fix -i     # Confirm each fix individually
  bd doctor --fix --fix-child-parent  # Also fix child→parent deps (opt-in)
  bd doctor --fix --force # Force repair even when database can't be opened
  bd doctor --fix --source=jsonl # Rebuild database from JSONL (source of truth)
  bd doctor --dry-run    # Preview what --fix would do without making changes
  bd doctor --perf       # Performance diagnostics
  bd doctor --output diagnostics.json  # Export diagnostics to file
  bd doctor --check=artifacts           # Show classic artifacts (JSONL, SQLite, cruft dirs)
  bd doctor --check=artifacts --clean  # Delete safe-to-delete artifacts (with confirmation)
  bd doctor --check=conventions        # Convention drift check (lint, stale, orphans)
  bd doctor --check=pollution          # Show potential test issues
  bd doctor --check=pollution --clean  # Delete test issues (with confirmation)
  bd doctor --check=validate         # Data-integrity checks only
  bd doctor --check=validate --fix   # Auto-fix data-integrity issues
  bd doctor --deep             # Full graph integrity validation
  bd doctor --server           # Dolt server mode health checks
  bd doctor --migration=pre    # Validate readiness for Dolt migration
  bd doctor --migration=post   # Validate Dolt migration completed
  bd doctor --migration=pre --json  # Machine-parseable migration validation

Usage:
  bd doctor [path] [flags]

Flags:
      --agent                                   Agent-facing diagnostic mode: rich context for AI agents (ZFC-compliant)
      --check string                            Run specific check in detail (e.g., 'pollution')
      --check-health                            Quick health check for git hooks (silent on success)
      --clean                                   For pollution check: delete detected test issues
      --deep                                    Validate full graph integrity
      --dry-run                                 Preview fixes without making changes
      --fix                                     Automatically fix issues where possible
      --fix-child-parent                        Remove child→parent dependencies (opt-in)
  -h, --help                                    help for doctor
  -i, --interactive                             Confirm each fix individually
      --migration string                        Run Dolt migration validation: 'pre' (before migration) or 'post' (after migration)
      --orchestrator                            Running in orchestrator multi-workspace mode (routes.jsonl is expected, higher duplicate tolerance)
      --orchestrator-duplicates-threshold int   Duplicate tolerance threshold for orchestrator mode (wisps are ephemeral) (default 1000)
  -o, --output string                           Export diagnostics to JSON file
      --perf                                    Run performance diagnostics and generate CPU profile
      --server                                  Run Dolt server mode health checks (connectivity, version, schema)
  -v, --verbose                                 Show all checks (default shows only warnings/errors)
  -y, --yes                                     Skip confirmation prompt (for non-interactive use)

Global Flags:
      --actor string              Actor name for audit trail (default: $BEADS_ACTOR, git user.name, $USER)
      --db string                 Database path (default: auto-discover .beads/*.db)
      --dolt-auto-commit string   Dolt auto-commit policy (off|on|batch). 'on': commit after each write. 'batch': defer commits to bd dolt commit; uncommitted changes persist in the working set until then. SIGTERM/SIGHUP flush pending batch commits. Default: off. Override via config key dolt.auto-commit
      --json                      Output in JSON format
      --profile                   Generate CPU profile for performance analysis
  -q, --quiet                     Suppress non-essential output (errors only)
      --readonly                  Read-only mode: block write operations (for worker sandboxes)
      --sandbox                   Sandbox mode: disables auto-sync
```


---

## bd dolt commit

## `bd dolt commit`

**Command:** `bd dolt commit`  
**Slug:** `dolt-commit`

### Help Output

```
Create a Dolt commit from any uncommitted changes in the working set.

This is the primary commit point for batch mode. When auto-commit is set to
"batch", changes accumulate in the working set across multiple bd commands and
are committed together here with a descriptive summary message.

Also useful before push operations that require a clean working set, or when
auto-commit was off or changes were made externally.

For more options (--stdin, custom messages), see: bd vc commit

Usage:
  bd dolt commit [flags]

Flags:
  -h, --help             help for commit
  -m, --message string   Commit message (default: auto-generated)

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


---

## bd dolt killall

## `bd dolt killall`

**Command:** `bd dolt killall`  
**Slug:** `dolt-killall`

### Help Output

```
Find and kill orphan dolt sql-server processes not tracked by the
canonical PID file for the current repo's Dolt data directory.

Under an orchestrator, the canonical server lives at $GT_ROOT/.beads/. Any other
dolt sql-server processes using that shared data directory are considered
orphans and will be killed.

In standalone mode, only dolt sql-server processes using the current
project's Dolt data directory are eligible for cleanup. Other projects'
servers are preserved.

Usage:
  bd dolt killall [flags]

Flags:
  -h, --help   help for killall

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


---

## bd dolt pull

## `bd dolt pull`

**Command:** `bd dolt pull`  
**Slug:** `dolt-pull`

### Help Output

```
Pull commits from the configured Dolt remote into the local database.

Requires a Dolt remote to be configured in the database directory.
For Hosted Dolt, set DOLT_REMOTE_USER and DOLT_REMOTE_PASSWORD environment
variables for authentication.

Usage:
  bd dolt pull [flags]

Flags:
  -h, --help   help for pull

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


---

## bd dolt push

## `bd dolt push`

**Command:** `bd dolt push`  
**Slug:** `dolt-push`

### Help Output

```
Push local Dolt commits to the configured remote.

Requires a Dolt remote to be configured in the database directory.
For Hosted Dolt, set DOLT_REMOTE_USER and DOLT_REMOTE_PASSWORD environment
variables for authentication.

Use --force to overwrite remote changes (e.g., when the remote has
uncommitted changes in its working set).

Usage:
  bd dolt push [flags]

Flags:
      --force   Force push (overwrite remote changes)
  -h, --help    help for push

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


---

## bd dolt remote add

## `bd dolt remote add`

**Command:** `bd dolt remote add`  
**Slug:** `dolt-remote-add`

### Help Output

```
Add a Dolt remote (both SQL server and CLI)

Usage:
  bd dolt remote add <name> <url> [flags]

Flags:
  -h, --help   help for add

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


---

## bd dolt remote list

## `bd dolt remote list`

**Command:** `bd dolt remote list`  
**Slug:** `dolt-remote-list`

### Help Output

```
List configured Dolt remotes (SQL server + CLI)

Usage:
  bd dolt remote list [flags]

Flags:
  -h, --help   help for list

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


---

## bd dolt remote remove

## `bd dolt remote remove`

**Command:** `bd dolt remote remove`  
**Slug:** `dolt-remote-remove`

### Help Output

```
Remove a Dolt remote (both SQL server and CLI)

Usage:
  bd dolt remote remove <name> [flags]

Flags:
      --force   Force remove even when SQL and CLI URLs conflict
  -h, --help    help for remove

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


---

## bd dolt remote

## `bd dolt remote`

**Command:** `bd dolt remote`  
**Slug:** `dolt-remote`

### Help Output

```
Manage Dolt remotes for push/pull replication.

Subcommands:
  add <name> <url>   Add a new remote
  list               List all configured remotes
  remove <name>      Remove a remote

Usage:
  bd dolt remote [command]

Available Commands:
  add         Add a Dolt remote (both SQL server and CLI)
  list        List configured Dolt remotes (SQL server + CLI)
  remove      Remove a Dolt remote (both SQL server and CLI)

Flags:
  -h, --help   help for remote

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

Use "bd dolt remote [command] --help" for more information about a command.
```

### Sub-commands

- [`bd dolt remote add`](./dolt-remote-add.md) — Add a Dolt remote (both SQL server and CLI)
- [`bd dolt remote list`](./dolt-remote-list.md) — List configured Dolt remotes (SQL server + CLI)
- [`bd dolt remote remove`](./dolt-remote-remove.md) — Remove a Dolt remote (both SQL server and CLI)


---

## bd dolt set

## `bd dolt set`

**Command:** `bd dolt set`  
**Slug:** `dolt-set`

### Help Output

```
Set a Dolt configuration value in metadata.json.

Keys:
  database  Database name (default: issue prefix or "beads")
  host      Server host (default: 127.0.0.1)
  port      Server port (auto-detected; override with bd dolt set port <N>)
  user      MySQL user (default: root)
  data-dir  Custom dolt data directory (absolute path; default: .beads/dolt)

Use --update-config to also write to config.yaml for team-wide defaults.

Examples:
  bd dolt set database myproject
  bd dolt set host 192.168.1.100
  bd dolt set port 3307 --update-config
  bd dolt set data-dir /home/user/.beads-dolt/myproject

Usage:
  bd dolt set <key> <value> [flags]

Flags:
  -h, --help            help for set
      --update-config   Also write to config.yaml for team-wide defaults

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


---

## bd dolt show

## `bd dolt show`

**Command:** `bd dolt show`  
**Slug:** `dolt-show`

### Help Output

```
Show current Dolt configuration with connection status

Usage:
  bd dolt show [flags]

Flags:
  -h, --help   help for show

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


---

## bd dolt start

## `bd dolt start`

**Command:** `bd dolt start`  
**Slug:** `dolt-start`

### Help Output

```
Start a dolt sql-server for the current beads project.

The server runs in the background on a per-project port derived from the
project path. PID and logs are stored in .beads/.

The server auto-starts transparently when needed, so manual start is rarely
required. Use this command for explicit control or diagnostics.

Usage:
  bd dolt start [flags]

Flags:
  -h, --help   help for start

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


---

## bd dolt status

## `bd dolt status`

**Command:** `bd dolt status`  
**Slug:** `dolt-status`

### Help Output

```
Show the status of the dolt sql-server for the current project.

Displays whether the server is running, its PID, port, and data directory.

Usage:
  bd dolt status [flags]

Flags:
  -h, --help   help for status

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


---

## bd dolt stop

## `bd dolt stop`

**Command:** `bd dolt stop`  
**Slug:** `dolt-stop`

### Help Output

```
Stop the dolt sql-server managed by beads for the current project.

This sends a graceful shutdown signal. The server will restart automatically
on the next bd command unless auto-start is disabled.

Usage:
  bd dolt stop [flags]

Flags:
      --force   Force stop the server
  -h, --help    help for stop

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


---

## bd dolt test

## `bd dolt test`

**Command:** `bd dolt test`  
**Slug:** `dolt-test`

### Help Output

```
Test the connection to the configured Dolt server.

This verifies that:
  1. The server is reachable at the configured host:port
  2. The connection can be established

Use this before switching to server mode to ensure the server is running.

Usage:
  bd dolt test [flags]

Flags:
  -h, --help   help for test

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


---

## bd dolt

## `bd dolt`

**Command:** `bd dolt`  
**Slug:** `dolt`

### Help Output

```
Configure and manage Dolt database settings and server lifecycle.

Beads uses a dolt sql-server for all database operations. The server is
auto-started transparently when needed. Use these commands for explicit
control or diagnostics.

Server lifecycle:
  bd dolt start        Start the Dolt server for this project
  bd dolt stop         Stop the Dolt server for this project
  bd dolt status       Show Dolt server status

Configuration:
  bd dolt show         Show current Dolt configuration with connection test
  bd dolt set <k> <v>  Set a configuration value
  bd dolt test         Test server connection

Version control:
  bd dolt commit       Commit pending changes
  bd dolt push         Push commits to Dolt remote
  bd dolt pull         Pull commits from Dolt remote

Remote management:
  bd dolt remote add <name> <url>   Add a Dolt remote
  bd dolt remote list                List configured remotes
  bd dolt remote remove <name>       Remove a Dolt remote

Configuration keys for 'bd dolt set':
  database  Database name (default: issue prefix or "beads")
  host      Server host (default: 127.0.0.1)
  port      Server port (auto-detected; override with bd dolt set port <N>)
  user      MySQL user (default: root)
  data-dir  Custom dolt data directory (absolute path; default: .beads/dolt)

Flags for 'bd dolt set':
  --update-config  Also write to config.yaml for team-wide defaults

Examples:
  bd dolt set database myproject
  bd dolt set host 192.168.1.100 --update-config
  bd dolt set data-dir /home/user/.beads-dolt/myproject
  bd dolt test

Usage:
  bd dolt [command]

Available Commands:
  clean-databases Drop stale test databases from the Dolt server
  commit          Create a Dolt commit from pending changes
  killall         Kill all orphan Dolt server processes
  pull            Pull commits from Dolt remote
  push            Push commits to Dolt remote
  remote          Manage Dolt remotes
  set             Set a Dolt configuration value
  show            Show current Dolt configuration with connection status
  start           Start the Dolt SQL server for this project
  status          Show Dolt server status
  stop            Stop the Dolt SQL server for this project
  test            Test connection to Dolt server

Flags:
  -h, --help   help for dolt

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

Use "bd dolt [command] --help" for more information about a command.
```

### Sub-commands

- [`bd dolt commit`](./dolt-commit.md) — Create a Dolt commit from pending changes
- [`bd dolt killall`](./dolt-killall.md) — Kill all orphan Dolt server processes
- [`bd dolt pull`](./dolt-pull.md) — Pull commits from Dolt remote
- [`bd dolt push`](./dolt-push.md) — Push commits to Dolt remote
- [`bd dolt remote`](./dolt-remote.md) — Manage Dolt remotes
- [`bd dolt set`](./dolt-set.md) — Set a Dolt configuration value
- [`bd dolt show`](./dolt-show.md) — Show current Dolt configuration with connection status
- [`bd dolt start`](./dolt-start.md) — Start the Dolt SQL server for this project
- [`bd dolt status`](./dolt-status.md) — Show Dolt server status
- [`bd dolt stop`](./dolt-stop.md) — Stop the Dolt SQL server for this project
- [`bd dolt test`](./dolt-test.md) — Test connection to Dolt server


---

## bd duplicates

## `bd duplicates`

**Command:** `bd duplicates`  
**Slug:** `duplicates`

### Help Output

```
Find issues with identical content (title, description, design, acceptance criteria).
Groups issues by content hash and reports duplicates with suggested merge targets.
The merge target is chosen by:
1. Reference count (most referenced issue wins)
2. Lexicographically smallest ID if reference counts are equal
Only groups issues with matching status (open with open, closed with closed).
Example:
  bd duplicates                    # Show all duplicate groups
  bd duplicates --auto-merge       # Automatically merge all duplicates
  bd duplicates --dry-run          # Show what would be merged

Usage:
  bd duplicates [flags]

Flags:
      --auto-merge   Automatically merge all duplicates
      --dry-run      Show what would be merged without making changes
  -h, --help         help for duplicates

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


---

## bd edit

## `bd edit`

**Command:** `bd edit`  
**Slug:** `edit`

### Help Output

```
Edit an issue field using your configured $EDITOR.

By default, edits the description. Use flags to edit other fields.

Examples:
  bd edit bd-42                    # Edit description
  bd edit bd-42 --title            # Edit title
  bd edit bd-42 --design           # Edit design notes
  bd edit bd-42 --notes            # Edit notes
  bd edit bd-42 --acceptance       # Edit acceptance criteria

Usage:
  bd edit [id] [flags]

Flags:
      --acceptance    Edit the acceptance criteria
      --description   Edit the description (default)
      --design        Edit the design notes
  -h, --help          help for edit
      --notes         Edit the notes
      --title         Edit the title

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


---

## bd epic status

## `bd epic status`

**Command:** `bd epic status`  
**Slug:** `epic-status`

### Help Output

```
Show epic completion status

Usage:
  bd epic status [flags]

Flags:
      --eligible-only   Show only epics eligible for closure
  -h, --help            help for status

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


---

## bd epic

## `bd epic`

**Command:** `bd epic`  
**Slug:** `epic`

### Help Output

```
Epic management commands

Usage:
  bd epic [command]

Available Commands:
  close-eligible Close epics where all children are complete
  status         Show epic completion status

Flags:
  -h, --help   help for epic

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

Use "bd epic [command] --help" for more information about a command.
```

### Sub-commands

- [`bd epic status`](./epic-status.md) — Show epic completion status


---

## bd export

## `bd export`

**Command:** `bd export`  
**Slug:** `export`

### Help Output

```
Export all issues to JSONL (newline-delimited JSON) format.

Each line is a complete JSON object representing one issue, including its
labels, dependencies, and comment count.

This command is for issue export, migration, and interoperability. It does
not produce the JSONL backup snapshot used by 'bd backup restore'. For
supported backup/restore flows, use 'bd backup', 'bd backup export-git',
and 'bd backup restore'.

By default, exports only regular issues (excluding infrastructure beads
like agents, rigs, roles, and messages). Use --all to include everything.

Memories (from 'bd remember') are included by default. Use --no-memories
to exclude them.

EXAMPLES:
  bd export                              # Export issues + memories to stdout
  bd export -o backup.jsonl              # Export to file
  bd export --no-memories                # Export issues only
  bd export --all -o full.jsonl          # Include infra + templates + gates
  bd export --scrub -o clean.jsonl       # Exclude test/pollution records

Usage:
  bd export [flags]

Flags:
      --all             Include all records (infra, templates, gates)
  -h, --help            help for export
      --include-infra   Include infrastructure beads (agents, rigs, roles, messages)
      --no-memories     Exclude persistent memories from the export
  -o, --output string   Output file path (default: stdout)
      --scrub           Exclude test/pollution records

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


---

## bd federation add peer

## `bd federation add-peer`

**Command:** `bd federation add-peer`  
**Slug:** `federation-add-peer`

### Help Output

```
Add a new federation peer remote with optional SQL user authentication.

The URL can be:
  - dolthub://org/repo      DoltHub hosted repository
  - host:port/database      Direct dolt sql-server connection
  - file:///path/to/repo    Local file path (for testing)

Credentials are encrypted and stored locally. They are used automatically
when syncing with the peer. If --user is provided without --password,
you will be prompted for the password interactively.

Examples:
  bd federation add-peer town-beta dolthub://acme/town-beta-beads
  bd federation add-peer town-gamma 192.168.1.100:3306/beads --user sync-bot
  bd federation add-peer partner https://partner.example.com/beads --user admin --password secret

Usage:
  bd federation add-peer <name> <url> [flags]

Flags:
  -h, --help                 help for add-peer
  -p, --password string      SQL password (prompted if --user set without --password)
      --sovereignty string   Sovereignty tier (T1, T2, T3, T4)
  -u, --user string          SQL username for authentication

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


---

## bd federation list peers

## `bd federation list-peers`

**Command:** `bd federation list-peers`  
**Slug:** `federation-list-peers`

### Help Output

```
List configured federation peers

Usage:
  bd federation list-peers [flags]

Flags:
  -h, --help   help for list-peers

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


---

## bd federation

## `bd federation`

**Command:** `bd federation`  
**Slug:** `federation`

### Help Output

```
Manage peer-to-peer federation between Dolt-backed beads databases.

Federation enables synchronized issue tracking across multiple workspaces,
each maintaining their own Dolt database while sharing updates via remotes.

Requires the Dolt storage backend.

Usage:
  bd federation [command]

Available Commands:
  add-peer    Add a federation peer with optional SQL credentials
  list-peers  List configured federation peers
  remove-peer Remove a federation peer
  status      Show federation sync status
  sync        Synchronize with a peer town

Flags:
  -h, --help   help for federation

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

Use "bd federation [command] --help" for more information about a command.
```

### Sub-commands

- [`bd federation add-peer`](./federation-add-peer.md) — Add a federation peer with optional SQL credentials
- [`bd federation list-peers`](./federation-list-peers.md) — List configured federation peers
- [`bd federation status`](./federation-status.md) — Show federation sync status
- [`bd federation sync`](./federation-sync.md) — Synchronize with a peer town


---

## bd flatten

## `bd flatten`

**Command:** `bd flatten`  
**Slug:** `flatten`

### Help Output

```
Nuclear option: squash ALL Dolt commit history into a single commit.

This uses the Tim Sehn recipe:
  1. Create a new branch from the current state
  2. Soft-reset to the initial commit (preserving all data)
  3. Commit everything as a single snapshot
  4. Swap main branch to the new flattened branch
  5. Run Dolt GC to reclaim space from old history

This is irreversible — all commit history is lost. The resulting database
has exactly one commit containing all current data.

Use this when:
  - Your .beads/dolt directory has grown very large
  - You don't need commit-level history (time travel)
  - You want to start fresh with minimal storage

Examples:
  bd flatten --dry-run               # Preview: show commit count and disk usage
  bd flatten --force                 # Actually squash all history
  bd flatten --force --json          # JSON output

Usage:
  bd flatten [flags]

Flags:
      --dry-run   Preview without making changes
  -f, --force     Confirm irreversible history squash
  -h, --help      help for flatten

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


---

## bd forget

## `bd forget`

**Command:** `bd forget`  
**Slug:** `forget`

### Help Output

```
Remove a memory by its key.

Use 'bd memories' to see available keys.

Examples:
  bd forget dolt-phantoms
  bd forget auth-jwt

Usage:
  bd forget <key> [flags]

Flags:
  -h, --help   help for forget

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


---

## bd formula convert

## `bd formula convert`

**Command:** `bd formula convert`  
**Slug:** `formula-convert`

### Help Output

```
Convert formula files from JSON to TOML format.

TOML format provides better ergonomics:
  - Multi-line strings without \n escaping
  - Human-readable diffs
  - Comments allowed

The convert command reads a .formula.json file and outputs .formula.toml.
The original JSON file is preserved (use --delete to remove it).

Examples:
  bd formula convert shiny              # Convert shiny.formula.json to .toml
  bd formula convert ./my.formula.json  # Convert specific file
  bd formula convert --all              # Convert all JSON formulas
  bd formula convert shiny --delete     # Convert and remove JSON file
  bd formula convert shiny --stdout     # Print TOML to stdout

Usage:
  bd formula convert <formula-name|path> [--all] [flags]

Flags:
      --all      Convert all JSON formulas
      --delete   Delete JSON file after conversion
  -h, --help     help for convert
      --stdout   Print TOML to stdout instead of file

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


---

## bd formula list

## `bd formula list`

**Command:** `bd formula list`  
**Slug:** `formula-list`

### Help Output

```
List all formulas from search paths.

Search paths (in order of priority):
  1. .beads/formulas/ (project - highest priority)
  2. ~/.beads/formulas/ (user)
  3. $GT_ROOT/.beads/formulas/ (orchestrator, if GT_ROOT set)

Formulas in earlier paths shadow those with the same name in later paths.

Examples:
  bd formula list
  bd formula list --json
  bd formula list --type workflow
  bd formula list --type convoy

Usage:
  bd formula list [flags]

Flags:
  -h, --help          help for list
      --type string   Filter by type (workflow, expansion, aspect, convoy)

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


---

## bd formula show

## `bd formula show`

**Command:** `bd formula show`  
**Slug:** `formula-show`

### Help Output

```
Show detailed information about a formula.

Displays:
  - Formula metadata (name, type, description)
  - Variables with defaults and constraints
  - Steps with dependencies
  - Composition rules (extends, aspects, expansions)
  - Bond points for external composition

Examples:
  bd formula show shiny
  bd formula show rule-of-five
  bd formula show security-audit --json

Usage:
  bd formula show <formula-name> [flags]

Flags:
  -h, --help   help for show

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


---

## bd formula

## `bd formula`

**Command:** `bd formula`  
**Slug:** `formula`

### Help Output

```
Manage workflow formulas - the source layer for molecule templates.

Formulas are YAML/JSON files that define workflows with composition rules.
They are "cooked" into proto beads which can then be poured or wisped.

The Rig → Cook → Run lifecycle:
  - Rig: Compose formulas (extends, compose)
  - Cook: Transform to proto (bd cook expands macros, applies aspects)
  - Run: Agents execute poured mols or wisps

Search paths (in order):
  1. .beads/formulas/ (project)
  2. ~/.beads/formulas/ (user)
  3. $GT_ROOT/.beads/formulas/ (orchestrator, if GT_ROOT set)

Commands:
  list   List available formulas from all search paths
  show   Show formula details, steps, and composition rules

Usage:
  bd formula [command]

Available Commands:
  convert     Convert formula from JSON to TOML
  list        List available formulas
  show        Show formula details

Flags:
  -h, --help   help for formula

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

Use "bd formula [command] --help" for more information about a command.
```

### Sub-commands

- [`bd formula convert`](./formula-convert.md) — Convert formula from JSON to TOML
- [`bd formula list`](./formula-list.md) — List available formulas
- [`bd formula show`](./formula-show.md) — Show formula details


---

## bd gate add waiter

## `bd gate add-waiter`

**Command:** `bd gate add-waiter`  
**Slug:** `gate-add-waiter`

### Help Output

```
Register an agent as a waiter on a gate bead.

When the gate closes, the waiter will receive a wake notification via 'bd gate wake'.
The waiter is typically the worker's address (e.g., "my-project/workers/agent-1").

This is used by 'bd done --phase-complete' to register for gate wake notifications.

Usage:
  bd gate add-waiter <gate-id> <waiter> [flags]

Flags:
  -h, --help   help for add-waiter

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


---

## bd gate check

## `bd gate check`

**Command:** `bd gate check`  
**Slug:** `gate-check`

### Help Output

```
Evaluate gate conditions and automatically close resolved gates.

By default, checks all open gates. Use --type to filter by gate type.

Gate types:
  gh       - Check all GitHub gates (gh:run and gh:pr)
  gh:run   - Check GitHub Actions workflow runs
  gh:pr    - Check pull request merge status
  timer    - Check timer gates (auto-expire based on timeout)
  bead     - Check cross-rig bead gates
  all      - Check all gate types

GitHub gates use the 'gh' CLI to query status:
  - gh:run checks 'gh run view <id> --json status,conclusion'
  - gh:pr checks 'gh pr view <id> --json state,merged'

A gate is resolved when:
  - gh:run: status=completed AND conclusion=success
  - gh:pr: state=MERGED
  - timer: current time > created_at + timeout
  - bead: target bead status=closed

A gate is escalated when:
  - gh:run: status=completed AND conclusion in (failure, canceled)
  - gh:pr: state=CLOSED AND merged=false

Examples:
  bd gate check              # Check all gates
  bd gate check --type=gh    # Check only GitHub gates
  bd gate check --type=gh:run # Check only workflow run gates
  bd gate check --type=timer # Check only timer gates
  bd gate check --type=bead  # Check only cross-rig bead gates
  bd gate check --dry-run    # Show what would happen without changes
  bd gate check --escalate   # Escalate expired/failed gates

Usage:
  bd gate check [flags]

Flags:
      --dry-run       Show what would happen without making changes
  -e, --escalate      Escalate failed/expired gates
  -h, --help          help for check
  -l, --limit int     Limit results (default 100) (default 100)
  -t, --type string   Gate type to check (gh, gh:run, gh:pr, timer, bead, all)

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


---

## bd gate discover

## `bd gate discover`

**Command:** `bd gate discover`  
**Slug:** `gate-discover`

### Help Output

```
Discovers GitHub workflow run IDs for gates awaiting CI/CD completion.

This command finds open gates with await_type="gh:run" that don't have an await_id,
queries recent GitHub workflow runs, and matches them using heuristics:
  - Branch name matching
  - Commit SHA matching
  - Time proximity (runs within 5 minutes of gate creation)

Once matched, the gate's await_id is updated with the GitHub run ID, enabling
subsequent polling to check the run's status.

Examples:
  bd gate discover           # Auto-discover run IDs for all matching gates
  bd gate discover --dry-run # Preview what would be matched (no updates)
  bd gate discover --branch main --limit 10  # Only match runs on 'main' branch

Usage:
  bd gate discover [flags]

Flags:
  -b, --branch string      Filter runs by branch (default: current branch)
  -n, --dry-run            Preview mode: show matches without updating
  -h, --help               help for discover
  -l, --limit int          Max runs to query from GitHub (default 10)
  -a, --max-age duration   Max age for gate/run matching (default 30m0s)

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


---

## bd gate list

## `bd gate list`

**Command:** `bd gate list`  
**Slug:** `gate-list`

### Help Output

```
List all gate issues in the current beads database.

By default, shows only open gates. Use --all to include closed gates.

Usage:
  bd gate list [flags]

Flags:
  -a, --all         Show all gates including closed
  -h, --help        help for list
  -n, --limit int   Limit results (default 50) (default 50)

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


---

## bd gate resolve

## `bd gate resolve`

**Command:** `bd gate resolve`  
**Slug:** `gate-resolve`

### Help Output

```
Close a gate issue to unblock the step waiting on it.

This is equivalent to 'bd close <gate-id>' but with a more explicit name.
Use --reason to provide context for why the gate was resolved.

Usage:
  bd gate resolve <gate-id> [flags]

Flags:
  -h, --help            help for resolve
  -r, --reason string   Reason for resolving the gate

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


---

## bd gate show

## `bd gate show`

**Command:** `bd gate show`  
**Slug:** `gate-show`

### Help Output

```
Display details of a gate issue including its waiters.

This is similar to 'bd show' but validates that the issue is a gate.

Usage:
  bd gate show <gate-id> [flags]

Flags:
  -h, --help   help for show

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


---

## bd gate

## `bd gate`

**Command:** `bd gate`  
**Slug:** `gate`

### Help Output

```
Gates are async wait conditions that block workflow steps.

Gates are created automatically when a formula step has a gate field.
They must be closed (manually or via watchers) for the blocked step to proceed.

Gate types:
  human   - Requires manual bd close (Phase 1)
  timer   - Expires after timeout (Phase 2)
  gh:run  - Waits for GitHub workflow (Phase 3)
  gh:pr   - Waits for PR merge (Phase 3)
  bead    - Waits for cross-rig bead to close (Phase 4)

For bead gates, await_id format is <rig>:<bead-id> (e.g., "other-project:op-abc123").

Examples:
  bd gate list           # Show all open gates
  bd gate list --all     # Show all gates including closed
  bd gate check          # Evaluate all open gates
  bd gate check --type=bead  # Evaluate only bead gates
  bd gate resolve <id>   # Close a gate manually

Usage:
  bd gate [command]

Available Commands:
  add-waiter  Add a waiter to a gate
  check       Evaluate gates and close resolved ones
  discover    Discover await_id for gh:run gates
  list        List gate issues
  resolve     Manually resolve (close) a gate
  show        Show a gate issue

Flags:
  -h, --help   help for gate

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

Use "bd gate [command] --help" for more information about a command.
```

### Sub-commands

- [`bd gate add-waiter`](./gate-add-waiter.md) — Add a waiter to a gate
- [`bd gate check`](./gate-check.md) — Evaluate gates and close resolved ones
- [`bd gate discover`](./gate-discover.md) — Discover await_id for gh:run gates
- [`bd gate list`](./gate-list.md) — List gate issues
- [`bd gate resolve`](./gate-resolve.md) — Manually resolve (close) a gate
- [`bd gate show`](./gate-show.md) — Show a gate issue


---

## bd gc

## `bd gc`

**Command:** `bd gc`  
**Slug:** `gc`

### Help Output

```
Full lifecycle garbage collection for standalone Beads databases.

Runs three phases in sequence:
  1. DECAY   — Delete closed issues older than N days (default 90)
  2. COMPACT — Squash old Dolt commits into fewer commits (bd compact)
  3. GC      — Run Dolt garbage collection to reclaim disk space

Each phase can be skipped individually. Use --dry-run to preview all phases
without making changes.

Examples:
  bd gc                              # Full GC with defaults (90 day decay)
  bd gc --dry-run                    # Preview what would happen
  bd gc --older-than 30              # Decay issues closed 30+ days ago
  bd gc --skip-decay                 # Skip issue deletion, just compact+GC
  bd gc --skip-dolt                  # Skip Dolt GC, just decay+compact
  bd gc --force                      # Skip confirmation prompt

Usage:
  bd gc [flags]

Flags:
      --dry-run          Preview without making changes
  -f, --force            Skip confirmation prompts
  -h, --help             help for gc
      --older-than int   Delete closed issues older than N days (default 90)
      --skip-decay       Skip issue deletion phase
      --skip-dolt        Skip Dolt garbage collection phase

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


---

## bd github repos

## `bd github repos`

**Command:** `bd github repos`  
**Slug:** `github-repos`

### Help Output

```
List GitHub repositories that the configured token has access to.

Usage:
  bd github repos [flags]

Flags:
  -h, --help   help for repos

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


---

## bd github status

## `bd github status`

**Command:** `bd github status`  
**Slug:** `github-status`

### Help Output

```
Display current GitHub configuration and sync status.

Usage:
  bd github status [flags]

Flags:
  -h, --help   help for status

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


---

## bd github sync

## `bd github sync`

**Command:** `bd github sync`  
**Slug:** `github-sync`

### Help Output

```
Synchronize issues between beads and GitHub.

By default, performs bidirectional sync:
- Pulls new/updated issues from GitHub to beads
- Pushes local beads issues to GitHub

Use --pull-only or --push-only to limit direction.

Usage:
  bd github sync [flags]

Flags:
      --dry-run         Show what would be synced without making changes
  -h, --help            help for sync
      --prefer-github   On conflict, use GitHub version
      --prefer-local    On conflict, keep local beads version
      --prefer-newer    On conflict, use most recent version (default)
      --pull-only       Only pull issues from GitHub
      --push-only       Only push issues to GitHub

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


---

## bd github

## `bd github`

**Command:** `bd github`  
**Slug:** `github`

### Help Output

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

### Sub-commands

- [`bd github repos`](./github-repos.md) — List accessible GitHub repositories
- [`bd github status`](./github-status.md) — Show GitHub sync status
- [`bd github sync`](./github-sync.md) — Sync issues with GitHub


---

## bd gitlab projects

## `bd gitlab projects`

**Command:** `bd gitlab projects`  
**Slug:** `gitlab-projects`

### Help Output

```
List GitLab projects that the configured token has access to.

Usage:
  bd gitlab projects [flags]

Flags:
  -h, --help   help for projects

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


---

## bd gitlab status

## `bd gitlab status`

**Command:** `bd gitlab status`  
**Slug:** `gitlab-status`

### Help Output

```
Display current GitLab configuration and sync status.

Usage:
  bd gitlab status [flags]

Flags:
  -h, --help   help for status

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


---

## bd gitlab sync

## `bd gitlab sync`

**Command:** `bd gitlab sync`  
**Slug:** `gitlab-sync`

### Help Output

```
Synchronize issues between beads and GitLab.

By default, performs bidirectional sync:
- Pulls new/updated issues from GitLab to beads
- Pushes local beads issues to GitLab

Use --pull-only or --push-only to limit direction.

Usage:
  bd gitlab sync [flags]

Flags:
      --assignee string       Filter by assignee username
      --dry-run               Show what would be synced without making changes
      --exclude-type string   Exclude these issue types from sync (comma-separated)
  -h, --help                  help for sync
      --label string          Filter by labels (comma-separated, AND logic)
      --milestone string      Filter by milestone title
      --no-ephemeral          Exclude ephemeral/wisp issues from push (default: true) (default true)
      --prefer-gitlab         On conflict, use GitLab version
      --prefer-local          On conflict, keep local beads version
      --prefer-newer          On conflict, use most recent version (default)
      --project string        Filter to issues from this project ID (group mode)
      --pull-only             Only pull issues from GitLab
      --push-only             Only push issues to GitLab
      --type string           Only sync these issue types (comma-separated, e.g. 'epic,feature,task')

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


---

## bd gitlab

## `bd gitlab`

**Command:** `bd gitlab`  
**Slug:** `gitlab`

### Help Output

```
Commands for syncing issues between beads and GitLab.

Configuration can be set via 'bd config' or environment variables:
  gitlab.url / GITLAB_URL                         - GitLab instance URL
  gitlab.token / GITLAB_TOKEN                     - Personal access token
  gitlab.project_id / GITLAB_PROJECT_ID           - Project ID or path
  gitlab.group_id / GITLAB_GROUP_ID               - Group ID for group-level sync
  gitlab.default_project_id / GITLAB_DEFAULT_PROJECT_ID - Project for creating issues in group mode

Usage:
  bd gitlab [command]

Available Commands:
  projects    List accessible GitLab projects
  status      Show GitLab sync status
  sync        Sync issues with GitLab

Flags:
  -h, --help   help for gitlab

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

Use "bd gitlab [command] --help" for more information about a command.
```

### Sub-commands

- [`bd gitlab projects`](./gitlab-projects.md) — List accessible GitLab projects
- [`bd gitlab status`](./gitlab-status.md) — Show GitLab sync status
- [`bd gitlab sync`](./gitlab-sync.md) — Sync issues with GitLab


---

## bd graph check

## `bd graph check`

**Command:** `bd graph check`  
**Slug:** `graph-check`

### Help Output

```
Check the dependency graph for cycles, orphans, and other integrity issues.

Returns exit code 0 if the graph is clean, 1 if issues are found.

Usage:
  bd graph check [flags]

Flags:
  -h, --help   help for check

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


---

## bd graph

## `bd graph`

**Command:** `bd graph`  
**Slug:** `graph`

### Help Output

```
Display a visualization of an issue's dependency graph.

For epics, shows all children and their dependencies.
For regular issues, shows the issue and its direct dependencies.

With --all, shows all open issues grouped by connected component.

Display formats:
  (default)        DAG with columns and box-drawing edges (terminal-native)
  --box            ASCII boxes showing layers, more detailed
  --compact        Tree format, one line per issue, more scannable
  --dot            Graphviz DOT format (pipe to dot -Tsvg > graph.svg)
  --html           Self-contained interactive HTML with D3.js visualization

The graph shows execution order:
- Layer 0 / leftmost = no dependencies (can start immediately)
- Higher layers depend on lower layers
- Nodes in the same layer can run in parallel

Status icons: ○ open  ◐ in_progress  ● blocked  ✓ closed  ❄ deferred

Examples:
  bd graph issue-id              # Terminal DAG visualization (default)
  bd graph --box issue-id        # ASCII boxes with layer grouping
  bd graph --dot issue-id | dot -Tsvg > graph.svg  # SVG via Graphviz
  bd graph --dot issue-id | dot -Tpng > graph.png  # PNG via Graphviz
  bd graph --html issue-id > graph.html  # Interactive browser view
  bd graph --all --html > all.html       # All issues, interactive

Usage:
  bd graph [issue-id] [flags]
  bd graph [command]

Available Commands:
  check       Check dependency graph integrity

Flags:
      --all       Show graph for all open issues
      --box       ASCII boxes showing layers
      --compact   Tree format, one line per issue, more scannable
      --dot       Output Graphviz DOT format (pipe to: dot -Tsvg > graph.svg)
  -h, --help      help for graph
      --html      Output self-contained interactive HTML (redirect to file)

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

Use "bd graph [command] --help" for more information about a command.
```

### Sub-commands

- [`bd graph check`](./graph-check.md) — Check dependency graph integrity


---

## bd history

## `bd history`

**Command:** `bd history`  
**Slug:** `history`

### Help Output

```
Show the complete version history of an issue, including all commits
where the issue was modified.

Examples:
  bd history bd-123           # Show all history for issue bd-123
  bd history bd-123 --limit 5 # Show last 5 changes

Usage:
  bd history <id> [flags]

Flags:
  -h, --help        help for history
      --limit int   Limit number of history entries (0 = all)

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


---

## bd hooks install

## `bd hooks install`

**Command:** `bd hooks install`  
**Slug:** `hooks-install`

### Help Output

```
Install git hooks for beads integration.

By default, hooks are installed to .git/hooks/ in the current repository.
Use --beads to install to .beads/hooks/ (recommended for Dolt backend).
Use --shared to install to a versioned directory (.beads-hooks/) that can be
committed to git and shared with team members.

Hooks use section markers to coexist with existing hooks — any user content
outside the markers is preserved across installs and upgrades.

Installed hooks:
  - pre-commit: Run chained hooks before commit
  - post-merge: Run chained hooks after pull/merge
  - pre-push: Run chained hooks before push
  - post-checkout: Run chained hooks after branch checkout
  - prepare-commit-msg: Add agent identity trailers (for orchestrator agents)

Usage:
  bd hooks install [flags]

Flags:
      --beads    Install hooks to .beads/hooks/ (recommended for Dolt backend)
      --chain    Chain with existing hooks (run them before bd hooks)
      --force    Overwrite existing hooks without backup
  -h, --help     help for install
      --shared   Install hooks to .beads-hooks/ (versioned) instead of .git/hooks/

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


---

## bd hooks list

## `bd hooks list`

**Command:** `bd hooks list`  
**Slug:** `hooks-list`

### Help Output

```
Show the status of bd git hooks (installed, outdated, missing).

Usage:
  bd hooks list [flags]

Flags:
  -h, --help   help for list

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


---

## bd hooks run

## `bd hooks run`

**Command:** `bd hooks run`  
**Slug:** `hooks-run`

### Help Output

```
Execute the logic for a git hook. This command is typically called by
thin shim scripts installed in .git/hooks/.

Supported hooks:
  - pre-commit: Run chained hooks before commit
  - post-merge: Run chained hooks after pull/merge
  - pre-push: Run chained hooks before push
  - post-checkout: Run chained hooks after branch checkout
  - prepare-commit-msg: Add agent identity trailers for forensics

The thin shim pattern ensures hook logic is always in sync with the
installed bd version - upgrading bd automatically updates hook behavior.

Usage:
  bd hooks run <hook-name> [args...] [flags]

Flags:
  -h, --help   help for run

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


---

## bd hooks uninstall

## `bd hooks uninstall`

**Command:** `bd hooks uninstall`  
**Slug:** `hooks-uninstall`

### Help Output

```
Remove bd git hooks from .git/hooks/ directory.

Usage:
  bd hooks uninstall [flags]

Flags:
  -h, --help   help for uninstall

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


---

## bd hooks

## `bd hooks`

**Command:** `bd hooks`  
**Slug:** `hooks`

### Help Output

```
Install, uninstall, or list git hooks for beads integration.

The hooks provide:
- pre-commit: Run chained hooks before commit
- post-merge: Run chained hooks after pull/merge
- pre-push: Run chained hooks before push
- post-checkout: Run chained hooks after branch checkout
- prepare-commit-msg: Add agent identity trailers for forensics

Usage:
  bd hooks [command]

Available Commands:
  install     Install bd git hooks
  list        List installed git hooks status
  run         Execute a git hook (called by thin shims)
  uninstall   Uninstall bd git hooks

Flags:
  -h, --help   help for hooks

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

Use "bd hooks [command] --help" for more information about a command.
```

### Sub-commands

- [`bd hooks install`](./hooks-install.md) — Install bd git hooks
- [`bd hooks list`](./hooks-list.md) — List installed git hooks status
- [`bd hooks run`](./hooks-run.md) — Execute a git hook (called by thin shims)
- [`bd hooks uninstall`](./hooks-uninstall.md) — Uninstall bd git hooks


---

## bd human dismiss

## `bd human dismiss`

**Command:** `bd human dismiss`  
**Slug:** `human-dismiss`

### Help Output

```
Dismiss a human-needed bead permanently without responding.

The issue is closed with a "Dismissed" reason and optional note.

Examples:
  bd human dismiss bd-123
  bd human dismiss bd-123 --reason "No longer applicable"

Usage:
  bd human dismiss <issue-id> [flags]

Flags:
  -h, --help            help for dismiss
      --reason string   Reason for dismissal (optional)

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


---

## bd human list

## `bd human list`

**Command:** `bd human list`  
**Slug:** `human-list`

### Help Output

```
List all issues labeled with 'human' tag.

These are issues that require human intervention or input.

Examples:
  bd human list
  bd human list --status=open
  bd human list --json

Usage:
  bd human list [flags]

Flags:
  -h, --help            help for list
  -s, --status string   Filter by status (open, closed, etc.)

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


---

## bd human respond

## `bd human respond`

**Command:** `bd human respond`  
**Slug:** `human-respond`

### Help Output

```
Respond to a human-needed bead by adding a comment and closing it.

The response is added as a comment and the issue is closed with reason "Responded".

Examples:
  bd human respond bd-123 --response "Use OAuth2 for authentication"
  bd human respond bd-123 -r "Approved, proceed with implementation"

Usage:
  bd human respond <issue-id> [flags]

Flags:
  -h, --help              help for respond
  -r, --response string   Response text (required)

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


---

## bd human stats

## `bd human stats`

**Command:** `bd human stats`  
**Slug:** `human-stats`

### Help Output

```
Display summary statistics for human-needed beads.

Shows counts for total, pending (open), responded (closed without dismiss),
and dismissed beads.

Example:
  bd human stats

Usage:
  bd human stats [flags]

Flags:
  -h, --help   help for stats

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


---

## bd human

## `bd human`

**Command:** `bd human`  
**Slug:** `human`

### Help Output

```
Display a focused help menu showing only the most common commands.

bd has 70+ commands - many for AI agents, integrations, and advanced workflows.
This command shows the ~15 essential commands that human users need most often.

For the full command list, run: bd --help

SUBCOMMANDS:
  human list              List all human-needed beads (issues with 'human' label)
  human respond <id>      Respond to a human-needed bead (adds comment and closes)
  human dismiss <id>      Dismiss a human-needed bead permanently
  human stats             Show summary statistics for human-needed beads

Usage:
  bd human [flags]
  bd human [command]

Available Commands:
  dismiss     Dismiss a human-needed bead
  list        List all human-needed beads
  respond     Respond to a human-needed bead
  stats       Show summary statistics for human-needed beads

Flags:
  -h, --help   help for human

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

Use "bd human [command] --help" for more information about a command.
```

### Sub-commands

- [`bd human dismiss`](./human-dismiss.md) — Dismiss a human-needed bead
- [`bd human list`](./human-list.md) — List all human-needed beads
- [`bd human respond`](./human-respond.md) — Respond to a human-needed bead
- [`bd human stats`](./human-stats.md) — Show summary statistics for human-needed beads


---

## bd import

## `bd import`

**Command:** `bd import`  
**Slug:** `import`

### Help Output

```
Import issues from a JSONL file (newline-delimited JSON) into the database.

If no file is specified, imports from .beads/issues.jsonl (the git-tracked
export). This is the incremental counterpart to 'bd export': new issues are
created and existing issues are updated (upsert semantics).

Memory records (lines with "_type":"memory") are automatically detected and
imported as persistent memories (equivalent to 'bd remember'). This makes
'bd export | bd import' a full round-trip for both issues and memories.

This command makes the git-tracked JSONL portable again — after 'git pull'
brings new issues, 'bd import' loads them into the local Dolt database.

EXAMPLES:
  bd import                        # Import from .beads/issues.jsonl
  bd import backup.jsonl           # Import from a specific file
  bd import --dry-run              # Show what would be imported

Usage:
  bd import [file] [flags]

Flags:
      --dry-run   Show what would be imported without importing
  -h, --help      help for import

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


---

## bd index

## `bd`

**Command:** `bd `  
**Slug:** ``

### Help Output

```
Issues chained together like beads. A lightweight issue tracker with first-class dependency support.

Usage:
  bd [flags]
  bd [command]

Working With Issues:
  assign          Assign an issue to someone
  children        List child beads of a parent
  close           Close one or more issues
  comment         Add a comment to an issue
  comments        View or manage comments on an issue
  create          Create a new issue (or batch from markdown/graph JSON)
  create-form     Create a new issue using an interactive form
  delete          Delete one or more issues and clean up references
  edit            Edit an issue field in $EDITOR
  gate            Manage async coordination gates
  label           Manage issue labels
  link            Link two issues with a dependency
  list            List issues
  merge-slot      Manage merge-slot gates for serialized conflict resolution
  note            Append a note to an issue
  priority        Set the priority of an issue
  promote         Promote a wisp to a permanent bead
  q               Quick capture: create issue and output only ID
  query           Query issues using a simple query language
  reopen          Reopen one or more closed issues
  search          Search issues by text query
  set-state       Set operational state (creates event + updates label)
  show            Show issue details
  state           Query the current value of a state dimension
  tag             Add a label to an issue
  todo            Manage TODO items (convenience wrapper for task issues)
  update          Update one or more issues

Views & Reports:
  count           Count issues matching filters
  diff            Show changes between two commits or branches
  find-duplicates Find semantically similar issues using text analysis or AI
  history         Show version history for an issue
  lint            Check issues for missing template sections
  stale           Show stale issues (not updated recently)
  status          Show issue database overview and statistics
  statuses        List valid issue statuses
  types           List valid issue types

Dependencies & Structure:
  dep             Manage dependencies
  duplicate       Mark an issue as a duplicate of another
  duplicates      Find and optionally merge duplicate issues
  epic            Epic management commands
  graph           Display issue dependency graph
  supersede       Mark an issue as superseded by a newer one
  swarm           Swarm management for structured epics

Sync & Data:
  backup          Back up your beads database
  branch          List or create branches
  export          Export issues to JSONL format
  federation      Manage peer-to-peer federation with other workspaces
  import          Import issues from a JSONL file into the database
  restore         Restore full history of a compacted issue from Dolt history
  vc              Version control operations

Setup & Configuration:
  bootstrap       Non-destructive database setup for fresh clones and recovery
  config          Manage configuration settings
  context         Show effective backend identity and repository context
  dolt            Configure Dolt database settings
  forget          Remove a persistent memory
  hooks           Manage git hooks for beads integration
  human           Show essential commands for human users
  info            Show database information
  init            Initialize bd in the current directory
  kv              Key-value store commands
  memories        List or search persistent memories
  onboard         Display minimal snippet for agent instructions file
  prime           Output AI-optimized workflow context
  quickstart      Quick start guide for bd
  recall          Retrieve a specific memory
  remember        Store a persistent memory
  setup           Setup integration with AI editors
  where           Show active beads location

Maintenance:
  compact         Squash old Dolt commits to reduce history size
  doctor          Check and fix beads installation health (start here)
  flatten         Squash all Dolt history into a single commit
  gc              Garbage collect: decay old issues, compact Dolt commits, run Dolt GC
  migrate         Database migration commands
  preflight       Show PR readiness checklist
  purge           Delete closed ephemeral beads to reclaim space
  rename-prefix   Rename the issue prefix for all issues in the database
  rules           Audit and compact Claude rules
  sql             Execute raw SQL against the beads database
  upgrade         Check and manage bd version upgrades
  worktree        Manage git worktrees for parallel development

Integrations & Advanced:
  admin           Administrative commands for database maintenance
  jira            Jira integration commands
  linear          Linear integration commands
  repo            Manage multiple repository configuration

Additional Commands:
  ado             Azure DevOps integration commands
  audit           Record and label agent interactions (append-only JSONL)
  blocked         Show blocked issues
  completion      Generate the autocompletion script for the specified shell
  cook            Compile a formula into a proto (ephemeral by default)
  defer           Defer one or more issues for later
  formula         Manage workflow formulas
  github          GitHub integration commands
  gitlab          GitLab integration commands
  help            Help about any command
  mail            Delegate to mail provider (e.g., gt mail)
  mol             Molecule commands (work templates)
  notion          Notion integration commands
  orphans         Identify orphaned issues (referenced in commits but still open)
  ready           Show ready work (open, no active blockers)
  rename          Rename an issue ID
  ship            Publish a capability for cross-project dependencies
  undefer         Undefer one or more issues (restore to open)
  version         Print version information

Flags:
      --actor string              Actor name for audit trail (default: $BEADS_ACTOR, git user.name, $USER)
      --db string                 Database path (default: auto-discover .beads/*.db)
      --dolt-auto-commit string   Dolt auto-commit policy (off|on|batch). 'on': commit after each write. 'batch': defer commits to bd dolt commit; uncommitted changes persist in the working set until then. SIGTERM/SIGHUP flush pending batch commits. Default: off. Override via config key dolt.auto-commit
  -h, --help                      help for bd
      --json                      Output in JSON format
      --profile                   Generate CPU profile for performance analysis
  -q, --quiet                     Suppress non-essential output (errors only)
      --readonly                  Read-only mode: block write operations (for worker sandboxes)
      --sandbox                   Sandbox mode: disables auto-sync
  -v, --verbose                   Enable verbose/debug output
  -V, --version                   Print version information

Use "bd [command] --help" for more information about a command.
```

### Sub-commands

- [`bd  assign`](./-assign.md) — Assign an issue to someone
- [`bd  children`](./-children.md) — List child beads of a parent
- [`bd  close`](./-close.md) — Close one or more issues
- [`bd  comment`](./-comment.md) — Add a comment to an issue
- [`bd  comments`](./-comments.md) — View or manage comments on an issue
- [`bd  create`](./-create.md) — Create a new issue (or batch from markdown/graph JSON)
- [`bd  create-form`](./-create-form.md) — Create a new issue using an interactive form
- [`bd  delete`](./-delete.md) — Delete one or more issues and clean up references
- [`bd  edit`](./-edit.md) — Edit an issue field in $EDITOR
- [`bd  gate`](./-gate.md) — Manage async coordination gates
- [`bd  label`](./-label.md) — Manage issue labels
- [`bd  link`](./-link.md) — Link two issues with a dependency
- [`bd  list`](./-list.md) — List issues
- [`bd  merge-slot`](./-merge-slot.md) — Manage merge-slot gates for serialized conflict resolution
- [`bd  note`](./-note.md) — Append a note to an issue
- [`bd  priority`](./-priority.md) — Set the priority of an issue
- [`bd  promote`](./-promote.md) — Promote a wisp to a permanent bead
- [`bd  q`](./-q.md) — Quick capture: create issue and output only ID
- [`bd  query`](./-query.md) — Query issues using a simple query language
- [`bd  reopen`](./-reopen.md) — Reopen one or more closed issues
- [`bd  search`](./-search.md) — Search issues by text query
- [`bd  set-state`](./-set-state.md) — Set operational state (creates event + updates label)
- [`bd  show`](./-show.md) — Show issue details
- [`bd  state`](./-state.md) — Query the current value of a state dimension
- [`bd  tag`](./-tag.md) — Add a label to an issue
- [`bd  todo`](./-todo.md) — Manage TODO items (convenience wrapper for task issues)
- [`bd  update`](./-update.md) — Update one or more issues
- [`bd  count`](./-count.md) — Count issues matching filters
- [`bd  diff`](./-diff.md) — Show changes between two commits or branches
- [`bd  history`](./-history.md) — Show version history for an issue
- [`bd  lint`](./-lint.md) — Check issues for missing template sections
- [`bd  stale`](./-stale.md) — Show stale issues (not updated recently)
- [`bd  status`](./-status.md) — Show issue database overview and statistics
- [`bd  statuses`](./-statuses.md) — List valid issue statuses
- [`bd  types`](./-types.md) — List valid issue types
- [`bd  dep`](./-dep.md) — Manage dependencies
- [`bd  duplicate`](./-duplicate.md) — Mark an issue as a duplicate of another
- [`bd  duplicates`](./-duplicates.md) — Find and optionally merge duplicate issues
- [`bd  epic`](./-epic.md) — Epic management commands
- [`bd  graph`](./-graph.md) — Display issue dependency graph
- [`bd  supersede`](./-supersede.md) — Mark an issue as superseded by a newer one
- [`bd  swarm`](./-swarm.md) — Swarm management for structured epics
- [`bd  backup`](./-backup.md) — Back up your beads database
- [`bd  branch`](./-branch.md) — List or create branches
- [`bd  export`](./-export.md) — Export issues to JSONL format
- [`bd  federation`](./-federation.md) — Manage peer-to-peer federation with other workspaces
- [`bd  import`](./-import.md) — Import issues from a JSONL file into the database
- [`bd  restore`](./-restore.md) — Restore full history of a compacted issue from Dolt history
- [`bd  vc`](./-vc.md) — Version control operations
- [`bd  bootstrap`](./-bootstrap.md) — Non-destructive database setup for fresh clones and recovery
- [`bd  config`](./-config.md) — Manage configuration settings
- [`bd  context`](./-context.md) — Show effective backend identity and repository context
- [`bd  dolt`](./-dolt.md) — Configure Dolt database settings
- [`bd  forget`](./-forget.md) — Remove a persistent memory
- [`bd  hooks`](./-hooks.md) — Manage git hooks for beads integration
- [`bd  human`](./-human.md) — Show essential commands for human users
- [`bd  info`](./-info.md) — Show database information
- [`bd  init`](./-init.md) — Initialize bd in the current directory
- [`bd  kv`](./-kv.md) — Key-value store commands
- [`bd  memories`](./-memories.md) — List or search persistent memories
- [`bd  onboard`](./-onboard.md) — Display minimal snippet for agent instructions file
- [`bd  prime`](./-prime.md) — Output AI-optimized workflow context
- [`bd  quickstart`](./-quickstart.md) — Quick start guide for bd
- [`bd  recall`](./-recall.md) — Retrieve a specific memory
- [`bd  remember`](./-remember.md) — Store a persistent memory
- [`bd  setup`](./-setup.md) — Setup integration with AI editors
- [`bd  where`](./-where.md) — Show active beads location
- [`bd  compact`](./-compact.md) — Squash old Dolt commits to reduce history size
- [`bd  doctor`](./-doctor.md) — Check and fix beads installation health (start here)
- [`bd  flatten`](./-flatten.md) — Squash all Dolt history into a single commit
- [`bd  gc`](./-gc.md) — Garbage collect: decay old issues, compact Dolt commits, run Dolt GC
- [`bd  migrate`](./-migrate.md) — Database migration commands
- [`bd  preflight`](./-preflight.md) — Show PR readiness checklist
- [`bd  purge`](./-purge.md) — Delete closed ephemeral beads to reclaim space
- [`bd  rename-prefix`](./-rename-prefix.md) — Rename the issue prefix for all issues in the database
- [`bd  rules`](./-rules.md) — Audit and compact Claude rules
- [`bd  sql`](./-sql.md) — Execute raw SQL against the beads database
- [`bd  upgrade`](./-upgrade.md) — Check and manage bd version upgrades
- [`bd  worktree`](./-worktree.md) — Manage git worktrees for parallel development
- [`bd  admin`](./-admin.md) — Administrative commands for database maintenance
- [`bd  jira`](./-jira.md) — Jira integration commands
- [`bd  linear`](./-linear.md) — Linear integration commands
- [`bd  repo`](./-repo.md) — Manage multiple repository configuration
- [`bd  ado`](./-ado.md) — Azure DevOps integration commands
- [`bd  audit`](./-audit.md) — Record and label agent interactions (append-only JSONL)
- [`bd  blocked`](./-blocked.md) — Show blocked issues
- [`bd  cook`](./-cook.md) — Compile a formula into a proto (ephemeral by default)
- [`bd  defer`](./-defer.md) — Defer one or more issues for later
- [`bd  formula`](./-formula.md) — Manage workflow formulas
- [`bd  github`](./-github.md) — GitHub integration commands
- [`bd  gitlab`](./-gitlab.md) — GitLab integration commands
- [`bd  mail`](./-mail.md) — Delegate to mail provider (e.g., gt mail)
- [`bd  mol`](./-mol.md) — Molecule commands (work templates)
- [`bd  notion`](./-notion.md) — Notion integration commands
- [`bd  orphans`](./-orphans.md) — Identify orphaned issues (referenced in commits but still open)
- [`bd  ready`](./-ready.md) — Show ready work (open, no active blockers)
- [`bd  rename`](./-rename.md) — Rename an issue ID
- [`bd  ship`](./-ship.md) — Publish a capability for cross-project dependencies
- [`bd  undefer`](./-undefer.md) — Undefer one or more issues (restore to open)
- [`bd  version`](./-version.md) — Print version information


---

## bd info

## `bd info`

**Command:** `bd info`  
**Slug:** `info`

### Help Output

```
Display information about the current database.

This command helps debug issues where bd is using an unexpected database. It shows:
  - The absolute path to the database file
  - Database statistics (issue count)
  - Schema information (with --schema flag)
  - What's new in recent versions (with --whats-new flag)

Examples:
  bd info
  bd info --json
  bd info --schema --json
  bd info --whats-new
  bd info --whats-new --json
  bd info --thanks

Usage:
  bd info [flags]

Flags:
  -h, --help        help for info
      --json        Output in JSON format
      --schema      Include schema information in output
      --thanks      Show thank you page for contributors
      --whats-new   Show agent-relevant changes from recent versions

Global Flags:
      --actor string              Actor name for audit trail (default: $BEADS_ACTOR, git user.name, $USER)
      --db string                 Database path (default: auto-discover .beads/*.db)
      --dolt-auto-commit string   Dolt auto-commit policy (off|on|batch). 'on': commit after each write. 'batch': defer commits to bd dolt commit; uncommitted changes persist in the working set until then. SIGTERM/SIGHUP flush pending batch commits. Default: off. Override via config key dolt.auto-commit
      --profile                   Generate CPU profile for performance analysis
  -q, --quiet                     Suppress non-essential output (errors only)
      --readonly                  Read-only mode: block write operations (for worker sandboxes)
      --sandbox                   Sandbox mode: disables auto-sync
  -v, --verbose                   Enable verbose/debug output
```


---

## bd init

## `bd init`

**Command:** `bd init`  
**Slug:** `init`

### Help Output

```
Initialize bd in the current directory by creating a .beads/ directory
and Dolt database. Optionally specify a custom issue prefix.

Dolt is the default (and only supported) storage backend. The legacy SQLite
backend has been removed. Use --backend=sqlite to see migration instructions.

Use --database to specify an existing server database name, overriding the
default prefix-based naming. This is useful when an external tool (e.g. an orchestrator)
has already created the database.

With --stealth: configures per-repository git settings for invisible beads usage:
  • .git/info/exclude to prevent beads files from being committed
  Perfect for personal use without affecting repo collaborators.
  To set up a specific AI tool, run: bd setup <claude|cursor|aider|...> --stealth

By default, beads uses an embedded Dolt engine (no external server needed).
Pass --server to use an external dolt sql-server instead. In server mode,
set connection details with --server-host, --server-port, and --server-user.
Password should be set via BEADS_DOLT_PASSWORD environment variable.

Non-interactive mode (--non-interactive or BD_NON_INTERACTIVE=1):
  Skips all interactive prompts, using sensible defaults:
  • Role defaults to "maintainer" (override with --role)
  • Fork exclude auto-configured when fork detected
  • --contributor and --team flags are rejected (wizards require interaction)
  Also auto-detected when stdin is not a terminal or CI=true is set.

Usage:
  bd init [flags]

Flags:
      --agents-file string       Custom filename for agent instructions (default: AGENTS.md)
      --agents-profile string    AGENTS.md profile: 'minimal' (default, pointer to bd prime) or 'full' (complete command reference)
      --agents-template string   Path to custom AGENTS.md template (overrides embedded default)
      --backend string           Storage backend (default: dolt). --backend=sqlite prints deprecation notice.
      --contributor              Run OSS contributor setup wizard
      --database string          Use existing server database name (overrides prefix-based naming)
      --destroy-token string     Explicit confirmation token for destructive re-init in non-interactive mode (format: 'DESTROY-<prefix>')
      --force                    Force re-initialization even if database already has issues (may cause data loss)
      --from-jsonl               Import issues from .beads/issues.jsonl instead of git history
  -h, --help                     help for init
      --non-interactive          Skip all interactive prompts (auto-detected in CI or non-TTY environments)
  -p, --prefix string            Issue prefix (default: current directory name)
  -q, --quiet                    Suppress output (quiet mode)
      --role string              Set beads role without prompting: "maintainer" or "contributor"
      --server                   Use external dolt sql-server instead of embedded engine
      --server-host string       Dolt server host (default: 127.0.0.1)
      --server-port int          Dolt server port (default: 3307)
      --server-user string       Dolt server MySQL user (default: root)
      --setup-exclude            Configure .git/info/exclude to keep beads files local (for forks)
      --shared-server            Enable shared Dolt server mode (all projects share one server at ~/.beads/shared-server/)
      --skip-agents              Skip AGENTS.md and Claude settings generation
      --skip-hooks               Skip git hooks installation
      --stealth                  Enable stealth mode: global gitattributes and gitignore, no local repo tracking
      --team                     Run team workflow setup wizard

Global Flags:
      --actor string              Actor name for audit trail (default: $BEADS_ACTOR, git user.name, $USER)
      --db string                 Database path (default: auto-discover .beads/*.db)
      --dolt-auto-commit string   Dolt auto-commit policy (off|on|batch). 'on': commit after each write. 'batch': defer commits to bd dolt commit; uncommitted changes persist in the working set until then. SIGTERM/SIGHUP flush pending batch commits. Default: off. Override via config key dolt.auto-commit
      --json                      Output in JSON format
      --profile                   Generate CPU profile for performance analysis
      --readonly                  Read-only mode: block write operations (for worker sandboxes)
      --sandbox                   Sandbox mode: disables auto-sync
  -v, --verbose                   Enable verbose/debug output
```


---

## bd jira status

## `bd jira status`

**Command:** `bd jira status`  
**Slug:** `jira-status`

### Help Output

```
Show the current Jira sync status, including:
  - Last sync timestamp
  - Configuration status
  - Number of issues with Jira links
  - Issues pending push (no external_ref)

Usage:
  bd jira status [flags]

Flags:
  -h, --help   help for status

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


---

## bd jira sync

## `bd jira sync`

**Command:** `bd jira sync`  
**Slug:** `jira-sync`

### Help Output

```
Synchronize issues between beads and Jira.

Modes:
  --pull         Import issues from Jira into beads
  --push         Export issues from beads to Jira
  (no flags)     Bidirectional sync: pull then push, with conflict resolution

Conflict Resolution:
  By default, newer timestamp wins. Override with:
  --prefer-local   Always prefer local beads version
  --prefer-jira    Always prefer Jira version

Examples:
  bd jira sync --pull                # Import from Jira
  bd jira sync --push --create-only  # Push new issues only
  bd jira sync --dry-run             # Preview without changes
  bd jira sync --prefer-local        # Bidirectional, local wins

Usage:
  bd jira sync [flags]

Flags:
      --create-only       Only create new issues, don't update existing
      --dry-run           Preview sync without making changes
  -h, --help              help for sync
      --prefer-jira       Prefer Jira version on conflicts
      --prefer-local      Prefer local version on conflicts
      --project strings   Project key(s) to sync (overrides configured project/projects)
      --pull              Pull issues from Jira
      --push              Push issues to Jira
      --state string      Issue state to sync: open, closed, all (default "all")

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


---

## bd jira

## `bd jira`

**Command:** `bd jira`  
**Slug:** `jira`

### Help Output

```
Synchronize issues between beads and Jira.

Configuration:
  bd config set jira.url "https://company.atlassian.net"
  bd config set jira.project "PROJ"
  bd config set jira.projects "PROJ1,PROJ2"   # Multiple projects
  bd config set jira.api_token "YOUR_TOKEN"
  bd config set jira.username "your_email@company.com"  # For Jira Cloud
  bd config set jira.push_prefix "hippo"       # Only push hippo-* issues to Jira
  bd config set jira.push_prefix "proj1,proj2" # Multiple prefixes (comma-separated)

Environment variables (alternative to config):
  JIRA_API_TOKEN  - Jira API token
  JIRA_USERNAME   - Jira username/email
  JIRA_PROJECTS   - Comma-separated project keys

Examples:
  bd jira sync --pull         # Import issues from Jira
  bd jira sync --push         # Export issues to Jira
  bd jira sync                # Bidirectional sync (pull then push)
  bd jira sync --dry-run      # Preview sync without changes
  bd jira status              # Show sync status

Usage:
  bd jira [command]

Available Commands:
  status      Show Jira sync status
  sync        Synchronize issues with Jira

Flags:
  -h, --help   help for jira

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

Use "bd jira [command] --help" for more information about a command.
```

### Sub-commands

- [`bd jira status`](./jira-status.md) — Show Jira sync status
- [`bd jira sync`](./jira-sync.md) — Synchronize issues with Jira


---

## bd kv clear

## `bd kv clear`

**Command:** `bd kv clear`  
**Slug:** `kv-clear`

### Help Output

```
Delete a key from the beads key-value store.

Examples:
  bd kv clear feature_flag
  bd kv clear api_endpoint

Usage:
  bd kv clear <key> [flags]

Flags:
  -h, --help   help for clear

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


---

## bd kv get

## `bd kv get`

**Command:** `bd kv get`  
**Slug:** `kv-get`

### Help Output

```
Get a value from the beads key-value store.

Examples:
  bd kv get feature_flag
  bd kv get api_endpoint

Usage:
  bd kv get <key> [flags]

Flags:
  -h, --help   help for get

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


---

## bd kv list

## `bd kv list`

**Command:** `bd kv list`  
**Slug:** `kv-list`

### Help Output

```
List all key-value pairs in the beads key-value store.

Examples:
  bd kv list
  bd kv list --json

Usage:
  bd kv list [flags]

Flags:
  -h, --help   help for list

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


---

## bd kv set

## `bd kv set`

**Command:** `bd kv set`  
**Slug:** `kv-set`

### Help Output

```
Set a key-value pair in the beads key-value store.

This is useful for storing flags, environment variables, or other
user-defined data that persists across sessions.

Examples:
  bd kv set feature_flag true
  bd kv set api_endpoint https://api.example.com
  bd kv set max_retries 3

Usage:
  bd kv set <key> <value> [flags]

Flags:
  -h, --help   help for set

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


---

## bd kv

## `bd kv`

**Command:** `bd kv`  
**Slug:** `kv`

### Help Output

```
Commands for working with the beads key-value store.

The key-value store is useful for storing flags, environment variables,
or other user-defined data that persists across sessions.

Examples:
  bd kv set mykey myvalue    # Set a value
  bd kv get mykey            # Get a value
  bd kv clear mykey          # Delete a key
  bd kv list                 # List all key-value pairs

Usage:
  bd kv [command]

Available Commands:
  clear       Delete a key-value pair
  get         Get a value by key
  list        List all key-value pairs
  set         Set a key-value pair

Flags:
  -h, --help   help for kv

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

Use "bd kv [command] --help" for more information about a command.
```

### Sub-commands

- [`bd kv clear`](./kv-clear.md) — Delete a key-value pair
- [`bd kv get`](./kv-get.md) — Get a value by key
- [`bd kv list`](./kv-list.md) — List all key-value pairs
- [`bd kv set`](./kv-set.md) — Set a key-value pair


---

## bd label add

## `bd label add`

**Command:** `bd label add`  
**Slug:** `label-add`

### Help Output

```
Add a label to one or more issues

Usage:
  bd label add [issue-id...] [label] [flags]

Flags:
  -h, --help   help for add

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


---

## bd label list all

## `bd label list-all`

**Command:** `bd label list-all`  
**Slug:** `label-list-all`

### Help Output

```
List all unique labels in the database

Usage:
  bd label list-all [flags]

Flags:
  -h, --help   help for list-all

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


---

## bd label list

## `bd label list`

**Command:** `bd label list`  
**Slug:** `label-list`

### Help Output

```
List labels for an issue

Usage:
  bd label list [issue-id] [flags]

Flags:
  -h, --help   help for list

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


---

## bd label propagate

## `bd label propagate`

**Command:** `bd label propagate`  
**Slug:** `label-propagate`

### Help Output

```
Push a label from a parent down to all direct children that don't already have it. Useful for applying branch: labels across an epic's subtasks.

Usage:
  bd label propagate [parent-id] [label] [flags]

Flags:
  -h, --help   help for propagate

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


---

## bd label remove

## `bd label remove`

**Command:** `bd label remove`  
**Slug:** `label-remove`

### Help Output

```
Remove a label from one or more issues

Usage:
  bd label remove [issue-id...] [label] [flags]

Flags:
  -h, --help   help for remove

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


---

## bd label

## `bd label`

**Command:** `bd label`  
**Slug:** `label`

### Help Output

```
Manage issue labels

Usage:
  bd label [command]

Available Commands:
  add         Add a label to one or more issues
  list        List labels for an issue
  list-all    List all unique labels in the database
  propagate   Propagate a label from a parent issue to all its children
  remove      Remove a label from one or more issues

Flags:
  -h, --help   help for label

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

Use "bd label [command] --help" for more information about a command.
```

### Sub-commands

- [`bd label add`](./label-add.md) — Add a label to one or more issues
- [`bd label list`](./label-list.md) — List labels for an issue
- [`bd label list-all`](./label-list-all.md) — List all unique labels in the database
- [`bd label propagate`](./label-propagate.md) — Propagate a label from a parent issue to all its children
- [`bd label remove`](./label-remove.md) — Remove a label from one or more issues


---

## bd linear status

## `bd linear status`

**Command:** `bd linear status`  
**Slug:** `linear-status`

### Help Output

```
Show the current Linear sync status, including:
  - Last sync timestamp
  - Configuration status
  - Number of issues with Linear links
  - Issues pending push (no external_ref)

Usage:
  bd linear status [flags]

Flags:
  -h, --help   help for status

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


---

## bd linear sync

## `bd linear sync`

**Command:** `bd linear sync`  
**Slug:** `linear-sync`

### Help Output

```
Synchronize issues between beads and Linear.

Modes:
  --pull         Import issues from Linear into beads
  --push         Export issues from beads to Linear
  (no flags)     Bidirectional sync: pull then push, with conflict resolution

Team Selection:
  --team ID1,ID2  Override configured team IDs for this sync
  Multiple teams can be configured via linear.team_ids (comma-separated).
  Falls back to linear.team_id for backward compatibility.
  Push requires explicit --team when multiple teams are configured.

Type Filtering (--push only):
  --type task,feature       Only sync issues of these types
  --exclude-type wisp       Exclude issues of these types
  --include-ephemeral       Include ephemeral issues (wisps, etc.); default is to exclude
  --parent TICKET           Only push this ticket and its descendants

Conflict Resolution:
  By default, newer timestamp wins. Override with:
  --prefer-local    Always prefer local beads version
  --prefer-linear   Always prefer Linear version

Examples:
  bd linear sync --pull                         # Import from Linear
  bd linear sync --push --create-only           # Push new issues only
  bd linear sync --push --type=task,feature     # Push only tasks and features
  bd linear sync --push --exclude-type=wisp     # Push all except wisps
  bd linear sync --push --parent=bd-abc123      # Push one ticket tree
  bd linear sync --dry-run                      # Preview without changes
  bd linear sync --prefer-local                 # Bidirectional, local wins

Usage:
  bd linear sync [flags]

Flags:
      --create-only            Only create new issues, don't update existing
      --dry-run                Preview sync without making changes
      --exclude-type strings   Exclude issues of these types (can be repeated)
  -h, --help                   help for sync
      --include-ephemeral      Include ephemeral issues (wisps, etc.) when pushing to Linear
      --parent string          Limit push to this beads ticket and its descendants
      --prefer-linear          Prefer Linear version on conflicts
      --prefer-local           Prefer local version on conflicts
      --pull                   Pull issues from Linear
      --push                   Push issues to Linear
      --state string           Issue state to sync: open, closed, all (default "all")
      --team strings           Team ID(s) to sync (overrides configured team_id/team_ids)
      --type strings           Only sync issues of these types (can be repeated)
      --update-refs            Update external_ref after creating Linear issues (default true)

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


---

## bd linear teams

## `bd linear teams`

**Command:** `bd linear teams`  
**Slug:** `linear-teams`

### Help Output

```
List all teams accessible with your Linear API key.

Use this to find the team ID (UUID) needed for configuration.

Example:
  bd linear teams
  bd config set linear.team_id "12345678-1234-1234-1234-123456789abc"

Usage:
  bd linear teams [flags]

Flags:
  -h, --help   help for teams

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


---

## bd linear

## `bd linear`

**Command:** `bd linear`  
**Slug:** `linear`

### Help Output

```
Synchronize issues between beads and Linear.

Configuration:
  bd config set linear.api_key "YOUR_API_KEY"
  bd config set linear.team_id "TEAM_ID"
  bd config set linear.team_ids "TEAM_ID1,TEAM_ID2"  # Multiple teams (comma-separated)
  bd config set linear.project_id "PROJECT_ID"  # Optional: sync only this project

Environment variables (alternative to config):
  LINEAR_API_KEY  - Linear API key
  LINEAR_TEAM_ID  - Linear team ID (UUID, singular)
  LINEAR_TEAM_IDS - Linear team IDs (comma-separated UUIDs)

Data Mapping (optional, sensible defaults provided):
  Priority mapping (Linear 0-4 to Beads 0-4):
    bd config set linear.priority_map.0 4    # No priority -> Backlog
    bd config set linear.priority_map.1 0    # Urgent -> Critical
    bd config set linear.priority_map.2 1    # High -> High
    bd config set linear.priority_map.3 2    # Medium -> Medium
    bd config set linear.priority_map.4 3    # Low -> Low

  State mapping (Linear state type to Beads status):
    bd config set linear.state_map.backlog open
    bd config set linear.state_map.unstarted open
    bd config set linear.state_map.started in_progress
    bd config set linear.state_map.completed closed
    bd config set linear.state_map.canceled closed
    bd config set linear.state_map.my_custom_state in_progress  # Custom state names

  Label to issue type mapping:
    bd config set linear.label_type_map.bug bug
    bd config set linear.label_type_map.feature feature
    bd config set linear.label_type_map.epic epic

  Relation type mapping (Linear relations to Beads dependencies):
    bd config set linear.relation_map.blocks blocks
    bd config set linear.relation_map.blockedBy blocks
    bd config set linear.relation_map.duplicate duplicates
    bd config set linear.relation_map.related related

  ID generation (optional, hash IDs to match bd/Jira hash mode):
    bd config set linear.id_mode "hash"      # hash (default)
    bd config set linear.hash_length "6"     # hash length 3-8 (default: 6)

Examples:
  bd linear sync --pull         # Import issues from Linear
  bd linear sync --push         # Export issues to Linear
  bd linear sync                # Bidirectional sync (pull then push)
  bd linear sync --dry-run      # Preview sync without changes
  bd linear status              # Show sync status

Usage:
  bd linear [command]

Available Commands:
  status      Show Linear sync status
  sync        Synchronize issues with Linear
  teams       List available Linear teams

Flags:
  -h, --help   help for linear

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

Use "bd linear [command] --help" for more information about a command.
```

### Sub-commands

- [`bd linear status`](./linear-status.md) — Show Linear sync status
- [`bd linear sync`](./linear-sync.md) — Synchronize issues with Linear
- [`bd linear teams`](./linear-teams.md) — List available Linear teams


---

## bd link

## `bd link`

**Command:** `bd link`  
**Slug:** `link`

### Help Output

```
Link two issues with a dependency.

Shorthand for 'bd dep add <id1> <id2>'. By default creates a "blocks"
dependency (id2 blocks id1). Use --type to specify a different relationship.

Examples:
  bd link bd-123 bd-456                    # bd-456 blocks bd-123
  bd link bd-123 bd-456 --type related     # bd-123 related to bd-456
  bd link bd-123 bd-456 --type parent-child

Usage:
  bd link <id1> <id2> [flags]

Flags:
  -h, --help          help for link
  -t, --type string   Dependency type (blocks|tracks|related|parent-child|discovered-from) (default "blocks")

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


---

## bd lint

## `bd lint`

**Command:** `bd lint`  
**Slug:** `lint`

### Help Output

```
Check issues for missing recommended sections based on issue type.

By default, lints all open issues. Specify issue IDs to lint specific issues.

Section requirements by type:
  bug:      Steps to Reproduce, Acceptance Criteria
  task:     Acceptance Criteria
  feature:  Acceptance Criteria
  epic:     Success Criteria
  chore:    (none)

Examples:
  bd lint                    # Lint all open issues
  bd lint bd-abc             # Lint specific issue
  bd lint bd-abc bd-def      # Lint multiple issues
  bd lint --type bug         # Lint only bugs
  bd lint --status all       # Lint all issues (including closed)


Usage:
  bd lint [issue-id...] [flags]

Flags:
  -h, --help            help for lint
  -s, --status string   Filter by status (default: open, use 'all' for all)
  -t, --type string     Filter by issue type (bug, task, feature, epic)

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


---

## bd list

## `bd list`

**Command:** `bd list`  
**Slug:** `list`

### Help Output

```
List issues

Usage:
  bd list [flags]

Flags:
      --all                          Show all issues including closed (overrides default filter)
  -a, --assignee string              Filter by assignee
      --closed-after string          Filter issues closed after date (YYYY-MM-DD or RFC3339)
      --closed-before string         Filter issues closed before date (YYYY-MM-DD or RFC3339)
      --created-after string         Filter issues created after date (YYYY-MM-DD or RFC3339)
      --created-before string        Filter issues created before date (YYYY-MM-DD or RFC3339)
      --defer-after string           Filter issues deferred after date (supports relative: +6h, tomorrow)
      --defer-before string          Filter issues deferred before date (supports relative: +6h, tomorrow)
      --deferred                     Show only issues with defer_until set
      --desc-contains string         Filter by description substring (case-insensitive)
      --due-after string             Filter issues due after date (supports relative: +6h, tomorrow)
      --due-before string            Filter issues due before date (supports relative: +6h, tomorrow)
      --empty-description            Filter issues with empty or missing description
      --exclude-type strings         Exclude issue types from results (comma-separated or repeatable, e.g., --exclude-type=convoy,epic)
      --flat                         Disable tree format and use legacy flat list output
      --format string                Output format: 'digraph' (for golang.org/x/tools/cmd/digraph), 'dot' (Graphviz), or Go template
      --has-metadata-key string      Filter issues that have this metadata key set
  -h, --help                         help for list
      --id string                    Filter by specific issue IDs (comma-separated, e.g., bd-1,bd-5,bd-10)
      --include-gates                Include gate issues in output (normally hidden)
      --include-infra                Include infrastructure beads (agent/rig/role/message) in output
      --include-templates            Include template molecules in output
  -l, --label strings                Filter by labels (AND: must have ALL). Can combine with --label-any
      --label-any strings            Filter by labels (OR: must have AT LEAST ONE). Can combine with --label
      --label-pattern string         Filter by label glob pattern (e.g., 'tech-*' matches tech-debt, tech-legacy)
      --label-regex string           Filter by label regex pattern (e.g., 'tech-(debt|legacy)')
  -n, --limit int                    Limit results (default 50, use 0 for unlimited) (default 50)
      --long                         Show detailed multi-line output for each issue
      --metadata-field stringArray   Filter by metadata field (key=value, repeatable)
      --mol-type string              Filter by molecule type: swarm, patrol, or work
      --no-assignee                  Filter issues with no assignee
      --no-labels                    Filter issues with no labels
      --no-pager                     Disable pager output
      --no-parent                    Exclude child issues (show only top-level issues)
      --no-pinned                    Exclude pinned issues
      --notes-contains string        Filter by notes substring (case-insensitive)
      --overdue                      Show only issues with due_at in the past (not closed)
      --parent string                Filter by parent issue ID (shows children of specified issue)
      --pinned                       Show only pinned issues
      --pretty                       Display issues in a tree format with status/priority symbols
  -p, --priority string              Priority (0-4 or P0-P4, 0=highest)
      --priority-max string          Filter by maximum priority (inclusive, 0-4 or P0-P4)
      --priority-min string          Filter by minimum priority (inclusive, 0-4 or P0-P4)
      --ready                        Show only ready issues (status=open, excludes hooked/in_progress/blocked/deferred)
  -r, --reverse                      Reverse sort order
      --sort string                  Sort by field: priority, created, updated, closed, status, id, title, type, assignee
      --spec string                  Filter by spec_id prefix
  -s, --status string                Filter by stored status (open, in_progress, blocked, deferred, closed). Comma-separated for multiple: --status open,in_progress
      --title string                 Filter by title text (case-insensitive substring match)
      --title-contains string        Filter by title substring (case-insensitive)
      --tree                         Hierarchical tree format (default: true; use --flat to disable) (default true)
  -t, --type string                  Filter by type (bug, feature, task, epic, chore, decision, merge-request, molecule, gate, convoy). Aliases: mr→merge-request, feat→feature, mol→molecule, dec/adr→decision
      --updated-after string         Filter issues updated after date (YYYY-MM-DD or RFC3339)
      --updated-before string        Filter issues updated before date (YYYY-MM-DD or RFC3339)
  -w, --watch                        Watch for changes and auto-update display (implies --pretty)
      --wisp-type string             Filter by wisp type: heartbeat, ping, patrol, gc_report, recovery, error, escalation

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


---

## bd memories

## `bd memories`

**Command:** `bd memories`  
**Slug:** `memories`

### Help Output

```
List all memories, or search by keyword.

Examples:
  bd memories              # list all memories
  bd memories dolt         # search for memories about dolt
  bd memories "race flag"  # search for a phrase

Usage:
  bd memories [search] [flags]

Flags:
  -h, --help   help for memories

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


---

## bd merge slot acquire

## `bd merge-slot acquire`

**Command:** `bd merge-slot acquire`  
**Slug:** `merge-slot-acquire`

### Help Output

```
Attempt to acquire the merge slot for exclusive access.

If the slot is available (status=open), it will be acquired:
  - status set to in_progress
  - holder set to the requester

If the slot is held (status=in_progress), the command fails unless
--wait is passed, which adds the requester to the waiters queue.

Use --holder to specify who is acquiring (default: BEADS_ACTOR env var).

Usage:
  bd merge-slot acquire [flags]

Flags:
  -h, --help            help for acquire
      --holder string   Who is acquiring the slot (default: BEADS_ACTOR)
      --wait            Add to waiters list if slot is held

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


---

## bd merge slot check

## `bd merge-slot check`

**Command:** `bd merge-slot check`  
**Slug:** `merge-slot-check`

### Help Output

```
Check if the merge slot is available or held.

Returns:
  - available: slot can be acquired
  - held by <holder>: slot is currently held
  - not found: no merge slot exists for this rig

Usage:
  bd merge-slot check [flags]

Flags:
  -h, --help   help for check

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


---

## bd merge slot create

## `bd merge-slot create`

**Command:** `bd merge-slot create`  
**Slug:** `merge-slot-create`

### Help Output

```
Create a merge slot bead for serialized conflict resolution.

The slot ID is automatically generated based on the beads prefix (e.g., gt-merge-slot).
The slot is created with status=open (available).

Usage:
  bd merge-slot create [flags]

Flags:
  -h, --help   help for create

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


---

## bd merge slot release

## `bd merge-slot release`

**Command:** `bd merge-slot release`  
**Slug:** `merge-slot-release`

### Help Output

```
Release the merge slot after conflict resolution is complete.

Sets status back to open and clears the holder field.
If there are waiters, the highest-priority waiter should then acquire.

Usage:
  bd merge-slot release [flags]

Flags:
  -h, --help            help for release
      --holder string   Who is releasing the slot (for verification)

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


---

## bd merge slot

## `bd merge-slot`

**Command:** `bd merge-slot`  
**Slug:** `merge-slot`

### Help Output

```
Merge-slot gates serialize conflict resolution in the merge queue.

A merge slot is an exclusive access primitive: only one agent can hold it at a time.
This prevents "monkey knife fights" where multiple polecats race to resolve conflicts
and create cascading conflicts.

Each rig has one merge slot bead: <prefix>-merge-slot (labeled gt:slot).
The slot uses:
  - status=open: slot is available
  - status=in_progress: slot is held
  - metadata.holder: who currently holds the slot
  - metadata.waiters: priority-ordered queue of waiters

Examples:
  bd merge-slot create              # Create merge slot for current rig
  bd merge-slot check               # Check if slot is available
  bd merge-slot acquire             # Try to acquire the slot
  bd merge-slot release             # Release the slot

Usage:
  bd merge-slot [command]

Available Commands:
  acquire     Acquire the merge slot
  check       Check merge slot availability
  create      Create a merge slot bead for the current rig
  release     Release the merge slot

Flags:
  -h, --help   help for merge-slot

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

Use "bd merge-slot [command] --help" for more information about a command.
```

### Sub-commands

- [`bd merge-slot acquire`](./merge-slot-acquire.md) — Acquire the merge slot
- [`bd merge-slot check`](./merge-slot-check.md) — Check merge slot availability
- [`bd merge-slot create`](./merge-slot-create.md) — Create a merge slot bead for the current rig
- [`bd merge-slot release`](./merge-slot-release.md) — Release the merge slot


---

## bd migrate hooks

## `bd migrate hooks`

**Command:** `bd migrate hooks`  
**Slug:** `migrate-hooks`

### Help Output

```
Analyze git hook files and sidecar artifacts for migration to marker-managed format.

Modes:
  --dry-run  Preview migration operations without changing files
  --apply    Apply migration operations

Examples:
  bd migrate hooks --dry-run
  bd migrate hooks --apply
  bd migrate hooks --apply --yes
  bd migrate hooks --dry-run --json

Usage:
  bd migrate hooks [path] [flags]

Flags:
      --apply     Apply planned hook migration changes
      --dry-run   Show what would be done without making changes
  -h, --help      help for hooks
      --json      Output in JSON format
      --yes       Skip confirmation prompt for --apply

Global Flags:
      --actor string              Actor name for audit trail (default: $BEADS_ACTOR, git user.name, $USER)
      --db string                 Database path (default: auto-discover .beads/*.db)
      --dolt-auto-commit string   Dolt auto-commit policy (off|on|batch). 'on': commit after each write. 'batch': defer commits to bd dolt commit; uncommitted changes persist in the working set until then. SIGTERM/SIGHUP flush pending batch commits. Default: off. Override via config key dolt.auto-commit
      --profile                   Generate CPU profile for performance analysis
  -q, --quiet                     Suppress non-essential output (errors only)
      --readonly                  Read-only mode: block write operations (for worker sandboxes)
      --sandbox                   Sandbox mode: disables auto-sync
  -v, --verbose                   Enable verbose/debug output
```


---

## bd migrate issues

## `bd migrate issues`

**Command:** `bd migrate issues`  
**Slug:** `migrate-issues`

### Help Output

```
Move issues from one source repository to another with filtering and dependency preservation.

This command updates the source_repo field for selected issues, allowing you to:
- Move contributor planning issues to upstream repository
- Reorganize issues across multi-phase repositories
- Consolidate issues from multiple repos

Examples:
  # Preview migration from planning repo to current repo
  bd migrate-issues --from ~/.beads-planning --to . --dry-run

  # Move all open P1 bugs
  bd migrate-issues --from ~/repo1 --to ~/repo2 --priority 1 --type bug --status open

  # Move specific issues with their dependencies
  bd migrate-issues --from . --to ~/archive --id bd-abc --id bd-xyz --include closure

  # Move issues with label filter
  bd migrate-issues --from . --to ~/feature-work --label frontend --label urgent

Usage:
  bd migrate issues [flags]

Flags:
      --dry-run            Show plan without making changes
      --from string        Source repository (required)
  -h, --help               help for issues
      --id strings         Specific issue IDs to migrate (can specify multiple)
      --ids-file string    File containing issue IDs (one per line)
      --include string     Include dependencies: none/upstream/downstream/closure (default "none")
      --label strings      Filter by labels (can specify multiple)
      --priority int       Filter by priority (0-4) (default -1)
      --status string      Filter by status (open/closed/all)
      --strict             Fail on orphaned dependencies or missing repos
      --to string          Destination repository (required)
      --type string        Filter by issue type (bug/feature/task/epic/chore/decision)
      --within-from-only   Only include dependencies from source repo (default true)
      --yes                Skip confirmation prompt

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


---

## bd migrate sync

## `bd migrate sync`

**Command:** `bd migrate sync`  
**Slug:** `migrate-sync`

### Help Output

```
Configure separate branch workflow for multi-clone setups.

This sets the sync.branch config value so that issue data is committed
to a dedicated branch, keeping your main branch clean.

Example:
  bd migrate sync beads-sync

Usage:
  bd migrate sync <branch> [flags]

Flags:
      --dry-run   Show what would be done without making changes
  -h, --help      help for sync
      --json      Output in JSON format

Global Flags:
      --actor string              Actor name for audit trail (default: $BEADS_ACTOR, git user.name, $USER)
      --db string                 Database path (default: auto-discover .beads/*.db)
      --dolt-auto-commit string   Dolt auto-commit policy (off|on|batch). 'on': commit after each write. 'batch': defer commits to bd dolt commit; uncommitted changes persist in the working set until then. SIGTERM/SIGHUP flush pending batch commits. Default: off. Override via config key dolt.auto-commit
      --profile                   Generate CPU profile for performance analysis
  -q, --quiet                     Suppress non-essential output (errors only)
      --readonly                  Read-only mode: block write operations (for worker sandboxes)
      --sandbox                   Sandbox mode: disables auto-sync
  -v, --verbose                   Enable verbose/debug output
```


---

## bd migrate

## `bd migrate`

**Command:** `bd migrate`  
**Slug:** `migrate`

### Help Output

```
Database migration and data transformation commands.

Without subcommand, checks and updates database metadata to current version.

Subcommands:
  hooks       Plan git hook migration to marker-managed format
  issues      Move issues between repositories
  sync        Set up sync.branch workflow for multi-clone setups


Usage:
  bd migrate [flags]
  bd migrate [command]

Available Commands:
  hooks       Plan or apply git hook migration to marker-managed format
  issues      Move issues between repositories
  sync        Set up sync.branch workflow for multi-clone setups

Flags:
      --dry-run          Show what would be done without making changes
  -h, --help             help for migrate
      --inspect          Show migration plan and database state for AI agent analysis
      --json             Output migration statistics in JSON format
      --update-repo-id   Update repository ID (use after changing git remote)
      --yes              Auto-confirm prompts

Global Flags:
      --actor string              Actor name for audit trail (default: $BEADS_ACTOR, git user.name, $USER)
      --db string                 Database path (default: auto-discover .beads/*.db)
      --dolt-auto-commit string   Dolt auto-commit policy (off|on|batch). 'on': commit after each write. 'batch': defer commits to bd dolt commit; uncommitted changes persist in the working set until then. SIGTERM/SIGHUP flush pending batch commits. Default: off. Override via config key dolt.auto-commit
      --profile                   Generate CPU profile for performance analysis
  -q, --quiet                     Suppress non-essential output (errors only)
      --readonly                  Read-only mode: block write operations (for worker sandboxes)
      --sandbox                   Sandbox mode: disables auto-sync
  -v, --verbose                   Enable verbose/debug output

Use "bd migrate [command] --help" for more information about a command.
```

### Sub-commands

- [`bd migrate hooks`](./migrate-hooks.md) — Plan or apply git hook migration to marker-managed format
- [`bd migrate issues`](./migrate-issues.md) — Move issues between repositories
- [`bd migrate sync`](./migrate-sync.md) — Set up sync.branch workflow for multi-clone setups


---

## bd mol bond

## `bd mol bond`

**Command:** `bd mol bond`  
**Slug:** `mol-bond`

### Help Output

```
Bond two protos or molecules to create a compound.

The bond command is polymorphic - it handles different operand types:

  formula + formula → cook both, compound proto
  formula + proto   → cook formula, compound proto
  formula + mol     → cook formula, spawn and attach
  proto + proto     → compound proto (reusable template)
  proto + mol       → spawn proto, attach to molecule
  mol + proto       → spawn proto, attach to molecule
  mol + mol         → join into compound molecule

Formula names (e.g., mol-polecat-arm) are cooked inline as ephemeral protos.
This avoids needing pre-cooked proto beads in the database.

Bond types:
  sequential (default) - B runs after A completes
  parallel            - B runs alongside A
  conditional         - B runs only if A fails

Phase control:
  By default, spawned protos follow the target's phase:
  - Attaching to mol (Ephemeral=false) → spawns as persistent (Ephemeral=false)
  - Attaching to ephemeral issue (Ephemeral=true) → spawns as ephemeral (Ephemeral=true)

  Override with:
  --pour  Force spawn as liquid (persistent, Ephemeral=false)
  --ephemeral  Force spawn as vapor (ephemeral, Ephemeral=true, excluded from Dolt sync via dolt_ignore)

Dynamic bonding (Christmas Ornament pattern):
  Use --ref to specify a custom child reference with variable substitution.
  This creates IDs like "parent.child-ref" instead of random hashes.

  Example:
    bd mol bond mol-worker-arm bd-patrol --ref arm-{{worker_name}} --var worker_name=ace
    # Creates: bd-patrol.arm-ace (and children like bd-patrol.arm-ace.capture)

Use cases:
  - Found important bug during patrol? Use --pour to persist it
  - Need ephemeral diagnostic on persistent feature? Use --ephemeral
  - Spawning per-worker arms on a patrol? Use --ref for readable IDs

Examples:
  bd mol bond mol-feature mol-deploy                    # Compound proto
  bd mol bond mol-feature mol-deploy --type parallel    # Run in parallel
  bd mol bond mol-feature bd-abc123                     # Attach proto to molecule
  bd mol bond bd-abc123 bd-def456                       # Join two molecules
  bd mol bond mol-critical-bug wisp-patrol --pour       # Persist found bug
  bd mol bond mol-temp-check bd-feature --ephemeral          # Ephemeral diagnostic
  bd mol bond mol-arm bd-patrol --ref arm-{{name}} --var name=ace  # Dynamic child ID

Usage:
  bd mol bond <A> <B> [flags]

Aliases:
  bond, fart

Flags:
      --as string         Custom title for compound proto (proto+proto only)
      --dry-run           Preview what would be created
      --ephemeral         Force spawn as vapor (ephemeral, Ephemeral=true)
  -h, --help              help for bond
      --pour              Force spawn as liquid (persistent, Ephemeral=false)
      --ref string        Custom child reference with {{var}} substitution (e.g., arm-{{polecat_name}})
      --type string       Bond type: sequential, parallel, or conditional (default "sequential")
      --var stringArray   Variable substitution for spawned protos (key=value)

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


---

## bd mol burn

## `bd mol burn`

**Command:** `bd mol burn`  
**Slug:** `mol-burn`

### Help Output

```
Burn a molecule, deleting it without creating a digest.

Unlike squash (which creates a permanent digest before deletion), burn
completely removes the molecule with no trace. Use this for:
  - Abandoned patrol cycles
  - Crashed or failed workflows
  - Test/debug molecules you don't want to preserve

The burn operation differs based on molecule phase:
  - Wisp (ephemeral): Direct delete
  - Mol (persistent): Cascade delete (syncs to remotes)

CAUTION: This is a destructive operation. The molecule's data will be
permanently lost. If you want to preserve a summary, use 'bd mol squash'.

Example:
  bd mol burn bd-abc123              # Delete molecule with no trace
  bd mol burn bd-abc123 --dry-run    # Preview what would be deleted
  bd mol burn bd-abc123 --force      # Skip confirmation
  bd mol burn bd-a1 bd-b2 bd-c3      # Batch delete multiple wisps

Usage:
  bd mol burn <molecule-id> [molecule-id...] [flags]

Flags:
      --dry-run   Preview what would be deleted
      --force     Skip confirmation prompt
  -h, --help      help for burn

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


---

## bd mol current

## `bd mol current`

**Command:** `bd mol current`  
**Slug:** `mol-current`

### Help Output

```
Show where you are in a molecule workflow.

If molecule-id is given, show status for that molecule.
If not given, infer from in_progress issues assigned to current agent.

The output shows all steps with status indicators:
  [done]     - Step is complete (closed)
  [current]  - Step is in_progress (you are here)
  [ready]    - Step is ready to start (unblocked)
  [blocked]  - Step is blocked by dependencies
  [pending]  - Step is waiting

For large molecules (>100 steps), a summary is shown instead.
Use --limit or --range to view specific steps:
  bd mol current <id> --limit 50       # Show first 50 steps
  bd mol current <id> --range 100-150  # Show steps 100-150

Usage:
  bd mol current [molecule-id] [flags]

Flags:
      --for string     Show molecules for a specific agent/assignee
  -h, --help           help for current
      --limit int      Maximum number of steps to display (0 = auto, use 'all' threshold)
      --range string   Display specific step range (e.g., '1-50', '100-150')

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


---

## bd mol distill

## `bd mol distill`

**Command:** `bd mol distill`  
**Slug:** `mol-distill`

### Help Output

```
Distill a molecule by extracting a reusable formula from an existing epic.

This is the reverse of pour: instead of formula → molecule, it's molecule → formula.

The distill command:
  1. Loads the existing epic and all its children
  2. Converts the structure to a .formula.json file
  3. Replaces concrete values with {{variable}} placeholders (via --var flags)

Use cases:
  - Team develops good workflow organically, wants to reuse it
  - Capture tribal knowledge as executable templates
  - Create starting point for similar future work

Variable syntax (both work - we detect which side is the concrete value):
  --var branch=feature-auth    Spawn-style: variable=value (recommended)
  --var feature-auth=branch    Substitution-style: value=variable

Output locations (first writable wins):
  1. .beads/formulas/       (project-level, default)
  2. ~/.beads/formulas/     (user-level, if project not writable)

Examples:
  bd mol distill bd-o5xe my-workflow
  bd mol distill bd-abc release-workflow --var feature_name=auth-refactor

Usage:
  bd mol distill <epic-id> [formula-name] [flags]

Flags:
      --dry-run           Preview what would be created
  -h, --help              help for distill
      --output string     Output directory for formula file
      --var stringArray   Replace value with {{variable}} placeholder (variable=value)

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


---

## bd mol pour

## `bd mol pour`

**Command:** `bd mol pour`  
**Slug:** `mol-pour`

### Help Output

```
Pour a proto into a persistent mol - like pouring molten metal into a mold.

This is the chemistry-inspired command for creating PERSISTENT work from templates.
The resulting mol lives in .beads/ (permanent storage) and is synced with git.

Phase transition: Proto (solid) -> pour -> Mol (liquid)

WHEN TO USE POUR vs WISP:
  pour (liquid): Persistent work that needs audit trail
    - Feature implementations spanning multiple sessions
    - Work you may need to reference later
    - Anything worth preserving in git history

  wisp (vapor): Ephemeral work that auto-cleans up
    - Release workflows (one-time execution)
    - Operational loops and recurring cycles
    - Health checks and diagnostics
    - Any operational workflow without audit value

TIP: Formulas can specify phase:"vapor" to recommend wisp usage.
     If you pour a vapor-phase formula, you'll get a warning.

Examples:
  bd mol pour mol-feature --var name=auth    # Persistent feature work
  bd mol pour mol-review --var pr=123        # Persistent code review

Usage:
  bd mol pour <proto-id> [flags]

Flags:
      --assignee string      Assign the root issue to this agent/user
      --attach strings       Proto to attach after spawning (repeatable)
      --attach-type string   Bond type for attachments: sequential, parallel, or conditional (default "sequential")
      --dry-run              Preview what would be created
  -h, --help                 help for pour
      --var stringArray      Variable substitution (key=value)

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


---

## bd mol progress

## `bd mol progress`

**Command:** `bd mol progress`  
**Slug:** `mol-progress`

### Help Output

```
Show efficient progress summary for a molecule.

This command uses indexed queries to count progress without loading all steps,
making it suitable for very large molecules (millions of steps).

If no molecule-id is given, shows progress for any molecule you're working on.

Output includes:
  - Progress: completed / total (percentage)
  - Current step: the in-progress step (if any)
  - Rate: steps/hour based on closure times
  - ETA: estimated time to completion

Example:
  bd mol progress bd-hanoi-xyz

Usage:
  bd mol progress [molecule-id] [flags]

Flags:
  -h, --help   help for progress

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


---

## bd mol seed

## `bd mol seed`

**Command:** `bd mol seed`  
**Slug:** `mol-seed`

### Help Output

```
Verify that a formula is accessible and can be cooked.

The seed command checks formula search paths to ensure a formula exists
and can be loaded. This is useful for verifying system health before
attempting to spawn work from a formula.

Formula search paths (checked in order):
  1. .beads/formulas/ (project level)
  2. ~/.beads/formulas/ (user level)
  3. $GT_ROOT/.beads/formulas/ (orchestrator level, if GT_ROOT set)

Examples:
  bd mol seed mol-feature                 # Verify specific formula
  bd mol seed mol-review --var name=test  # Verify with variable substitution

Usage:
  bd mol seed <formula-name> [flags]

Flags:
  -h, --help              help for seed
      --var stringArray   Variable substitution for condition filtering (key=value)

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


---

## bd mol show

## `bd mol show`

**Command:** `bd mol show`  
**Slug:** `mol-show`

### Help Output

```
Show molecule structure and details.

The --parallel flag highlights parallelizable steps:
  - Steps with no blocking dependencies can run in parallel
  - Shows which steps are ready to start now
  - Identifies parallel groups (steps that can run concurrently)

Example:
  bd mol show bd-patrol --parallel

Usage:
  bd mol show <molecule-id> [flags]

Flags:
  -h, --help       help for show
  -p, --parallel   Show parallel step analysis

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


---

## bd mol squash

## `bd mol squash`

**Command:** `bd mol squash`  
**Slug:** `mol-squash`

### Help Output

```
Squash a molecule's ephemeral children into a single digest issue.

This command collects all ephemeral child issues of a molecule (Ephemeral=true),
generates a summary digest, and promotes the wisps to persistent by
clearing their Wisp flag (or optionally deletes them).

The squash operation:
  1. Loads the molecule and all its children
  2. Filters to only wisps (ephemeral issues with Ephemeral=true)
  3. Generates a digest (summary of work done)
  4. Creates a permanent digest issue (Ephemeral=false)
  5. Clears Wisp flag on children (promotes to persistent)
     OR keeps them with --keep-children (default: delete)

AGENT INTEGRATION:
Use --summary to provide an AI-generated summary. This keeps bd as a pure
tool - the calling agent (orchestrator worker, Claude Code, etc.) is responsible
for generating intelligent summaries. Without --summary, a basic concatenation
of child issue content is used.

This is part of the wisp workflow: spawn creates wisps,
execution happens, squash compresses the trace into an outcome (digest).

Example:
  bd mol squash bd-abc123                    # Squash and promote children
  bd mol squash bd-abc123 --dry-run          # Preview what would be squashed
  bd mol squash bd-abc123 --keep-children    # Keep wisps after digest
  bd mol squash bd-abc123 --summary "Agent-generated summary of work done"

Usage:
  bd mol squash <molecule-id> [flags]

Flags:
      --dry-run          Preview what would be squashed
  -h, --help             help for squash
      --keep-children    Don't delete ephemeral children after squash
      --summary string   Agent-provided summary (bypasses auto-generation)

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


---

## bd mol stale

## `bd mol stale`

**Command:** `bd mol stale`  
**Slug:** `mol-stale`

### Help Output

```
Detect molecules (epics with children) that are complete but still open.

A molecule is considered stale if:
  1. All children are closed (Completed == Total)
  2. Root issue is still open
  3. Not assigned to anyone (optional, use --unassigned)
  4. Is blocking other work (optional, use --blocking)

By default, shows all complete-but-unclosed molecules.

Examples:
  bd mol stale              # List all stale molecules
  bd mol stale --json       # Machine-readable output
  bd mol stale --blocking   # Only show those blocking other work
  bd mol stale --unassigned # Only show unassigned molecules
  bd mol stale --all        # Include molecules with 0 children

Usage:
  bd mol stale [flags]

Flags:
      --all          Include molecules with 0 children
      --blocking     Only show molecules blocking other work
  -h, --help         help for stale
      --unassigned   Only show unassigned molecules

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


---

## bd mol wisp create

## `bd mol wisp create`

**Command:** `bd mol wisp create`  
**Slug:** `mol-wisp-create`

### Help Output

```
Create a wisp from a proto - sublimation from solid to vapor.

This is the chemistry-inspired command for creating ephemeral work from templates.
The resulting wisp is stored in the main database with Ephemeral=true and NOT synced via git.

Phase transition: Proto (solid) -> Wisp (vapor)

Use wisp for:
  - Operational loops and recurring cycles
  - Health checks and monitoring
  - One-shot orchestration runs
  - Routine operations with no audit value

The wisp will:
  - Be stored in main database with Ephemeral=true flag
  - NOT be synced via git
  - Either evaporate (burn) or condense to digest (squash)

Examples:
  bd mol wisp create mol-patrol                    # Ephemeral patrol cycle
  bd mol wisp create mol-health-check              # One-time health check
  bd mol wisp create mol-diagnostics --var target=db  # Diagnostic run

Usage:
  bd mol wisp create <proto-id> [flags]

Flags:
      --dry-run           Preview what would be created
  -h, --help              help for create
      --root-only         Create only the root issue (no child step issues)
      --var stringArray   Variable substitution (key=value)

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


---

## bd mol wisp gc

## `bd mol wisp gc`

**Command:** `bd mol wisp gc`  
**Slug:** `mol-wisp-gc`

### Help Output

```
Garbage collect old or abandoned wisps from the database.

A wisp is considered abandoned if:
  - It hasn't been updated in --age duration and is not closed

Abandoned wisps are deleted without creating a digest. Use 'bd mol squash'
if you want to preserve a summary before garbage collection.

Use --closed to purge ALL closed wisps (regardless of age). This is the
fastest way to reclaim space from accumulated wisp bloat. Safe by default:
requires --force to actually delete.

Note: This uses time-based cleanup, appropriate for ephemeral wisps.
For graph-pressure staleness detection (blocking other work), see 'bd mol stale'.

Examples:
  bd mol wisp gc                                    # Clean abandoned wisps (default: 1h threshold)
  bd mol wisp gc --dry-run                          # Preview what would be cleaned
  bd mol wisp gc --age 24h                          # Custom age threshold
  bd mol wisp gc --all                              # Also clean closed wisps older than threshold
  bd mol wisp gc --closed                           # Preview closed wisp deletion
  bd mol wisp gc --closed --force                   # Delete all closed wisps
  bd mol wisp gc --closed --dry-run                 # Explicit dry-run (same as no --force)
  bd mol wisp gc --exclude-type agent,rig           # Protect agent and rig wisps from GC
  bd mol wisp gc --closed --force --exclude-type mol # Delete closed wisps except mol type

Usage:
  bd mol wisp gc [flags]

Flags:
      --age string             Age threshold for abandoned wisp detection (default "1h")
      --all                    Also clean closed wisps older than threshold
      --closed                 Delete all closed wisps (ignores --age threshold)
      --dry-run                Preview what would be cleaned
      --exclude-type strings   Exclude wisps of these types from GC (comma-separated, e.g., agent,rig)
  -f, --force                  Actually delete (default: preview only)
  -h, --help                   help for gc

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


---

## bd mol wisp list

## `bd mol wisp list`

**Command:** `bd mol wisp list`  
**Slug:** `mol-wisp-list`

### Help Output

```
List all wisps (ephemeral molecules) in the current context.

Wisps are issues with Ephemeral=true in the main database. They are stored
locally but not synced via git.

The list shows:
  - ID: Issue ID of the wisp
  - Title: Wisp title
  - Status: Current status (open, in_progress, closed)
  - Started: When the wisp was created
  - Updated: Last modification time

Old wisp detection:
  - Old wisps haven't been updated in 24+ hours
  - Use 'bd mol wisp gc' to clean up old/abandoned wisps

Examples:
  bd mol wisp list              # List all wisps
  bd mol wisp list --json       # JSON output for programmatic use
  bd mol wisp list --all        # Include closed wisps

Usage:
  bd mol wisp list [flags]

Flags:
      --all           Include closed wisps
  -h, --help          help for list
      --type string   Filter by issue type (e.g., agent, task, patrol)

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


---

## bd mol wisp

## `bd mol wisp`

**Command:** `bd mol wisp`  
**Slug:** `mol-wisp`

### Help Output

```
Create or manage wisps - EPHEMERAL molecules for operational workflows.

When called with a proto-id argument, creates a wisp from that proto.
When called with a subcommand (list, gc), manages existing wisps.

Wisps are issues with Ephemeral=true in the main database. They're stored
locally but NOT synced via git.

WHEN TO USE WISP vs POUR:
  wisp (vapor): Ephemeral work that auto-cleans up
    - Release workflows (one-time execution)
    - Operational loops and recurring cycles
    - Health checks and diagnostics
    - Any operational workflow without audit value

  pour (liquid): Persistent work that needs audit trail
    - Feature implementations spanning multiple sessions
    - Work you may need to reference later
    - Anything worth preserving in git history

TIP: Formulas can specify phase:"vapor" to recommend wisp usage.
     If you use pour on a vapor-phase formula, you'll get a warning.

The wisp lifecycle:
  1. Create: bd mol wisp <proto> or bd create --ephemeral
  2. Execute: Normal bd operations work on wisp issues
  3. Squash: bd mol squash <id> (clears Ephemeral flag, promotes to persistent)
  4. Or burn: bd mol burn <id> (deletes without creating digest)

Examples:
  bd mol wisp beads-release --var version=1.0  # Release workflow
  bd mol wisp mol-my-workflow                  # Ephemeral operational cycle
  bd mol wisp list                             # List all wisps
  bd mol wisp gc                               # Garbage collect old wisps

Subcommands:
  list  List all wisps in current context
  gc    Garbage collect orphaned wisps

Usage:
  bd mol wisp [proto-id] [flags]
  bd mol wisp [command]

Available Commands:
  create      Instantiate a proto as a wisp (solid -> vapor)
  gc          Garbage collect old/abandoned wisps
  list        List all wisps in current context

Flags:
      --dry-run           Preview what would be created
  -h, --help              help for wisp
      --root-only         Create only the root issue (no child step issues)
      --var stringArray   Variable substitution (key=value)

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

Use "bd mol wisp [command] --help" for more information about a command.
```

### Sub-commands

- [`bd mol wisp create`](./mol-wisp-create.md) — Instantiate a proto as a wisp (solid -> vapor)
- [`bd mol wisp gc`](./mol-wisp-gc.md) — Garbage collect old/abandoned wisps
- [`bd mol wisp list`](./mol-wisp-list.md) — List all wisps in current context


---

## bd mol

## `bd mol`

**Command:** `bd mol`  
**Slug:** `mol`

### Help Output

```
Manage molecules - work templates for agent workflows.

Protos are template epics with the "template" label. They define a DAG of work
that can be spawned to create real issues (molecules).

The molecule metaphor:
  - A proto is an uninstantiated template (reusable work pattern)
  - Spawning creates a molecule (real issues) from the proto
  - Variables ({{key}}) are substituted during spawning
  - Bonding combines protos or molecules into compounds
  - Distilling extracts a proto from an ad-hoc epic

Commands:
  show       Show proto/molecule structure and variables
  pour       Instantiate proto as persistent mol (liquid phase)
  wisp       Instantiate proto as ephemeral wisp (vapor phase)
  bond       Polymorphic combine: proto+proto, proto+mol, mol+mol
  squash     Condense molecule to digest
  burn       Discard wisp
  distill    Extract proto from ad-hoc epic

Use "bd formula list" to list available formulas.

Usage:
  bd mol [command]

Aliases:
  mol, protomolecule

Available Commands:
  bond          Bond two protos or molecules together
  burn          Delete a molecule without creating a digest
  current       Show current position in molecule workflow
  distill       Extract a formula from an existing epic
  last-activity Show last activity timestamp for a molecule
  pour          Instantiate a proto as a persistent mol (solid -> liquid)
  progress      Show molecule progress summary
  ready         Find molecules ready for gate-resume dispatch
  seed          Verify formula accessibility
  show          Show molecule details
  squash        Compress molecule execution into a digest
  stale         Detect complete-but-unclosed molecules
  wisp          Create or manage wisps (ephemeral molecules)

Flags:
  -h, --help   help for mol

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

Use "bd mol [command] --help" for more information about a command.
```

### Sub-commands

- [`bd mol bond`](./mol-bond.md) — Bond two protos or molecules together
- [`bd mol burn`](./mol-burn.md) — Delete a molecule without creating a digest
- [`bd mol current`](./mol-current.md) — Show current position in molecule workflow
- [`bd mol distill`](./mol-distill.md) — Extract a formula from an existing epic
- [`bd mol pour`](./mol-pour.md) — Instantiate a proto as a persistent mol (solid -> liquid)
- [`bd mol progress`](./mol-progress.md) — Show molecule progress summary
- [`bd mol ready`](./mol-ready.md) — Find molecules ready for gate-resume dispatch
- [`bd mol seed`](./mol-seed.md) — Verify formula accessibility
- [`bd mol show`](./mol-show.md) — Show molecule details
- [`bd mol squash`](./mol-squash.md) — Compress molecule execution into a digest
- [`bd mol stale`](./mol-stale.md) — Detect complete-but-unclosed molecules
- [`bd mol wisp`](./mol-wisp.md) — Create or manage wisps (ephemeral molecules)


---

## bd note

## `bd note`

**Command:** `bd note`  
**Slug:** `note`

### Help Output

```
Append a note to an issue's notes field.

Shorthand for 'bd update <id> --append-notes "text"'.

Examples:
  bd note gt-abc "Fixed the flaky test"
  bd note gt-abc Fixed the flaky test
  echo "note from pipe" | bd note gt-abc --stdin
  bd note gt-abc --file notes.txt

Usage:
  bd note <id> [text...] [flags]

Flags:
      --file string   Read note text from file
  -h, --help          help for note
      --stdin         Read note text from stdin

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


---

## bd notion connect

## `bd notion connect`

**Command:** `bd notion connect`  
**Slug:** `notion-connect`

### Help Output

```
Connect bd to an existing Notion database or data source

Usage:
  bd notion connect [flags]

Flags:
  -h, --help         help for connect
      --url string   Existing Notion database or data source URL

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


---

## bd notion init

## `bd notion init`

**Command:** `bd notion init`  
**Slug:** `notion-init`

### Help Output

```
Create a dedicated Beads database in Notion

Usage:
  bd notion init [flags]

Flags:
  -h, --help            help for init
      --parent string   Parent page ID
      --title string    Database title (default "Beads Issues")

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


---

## bd notion status

## `bd notion status`

**Command:** `bd notion status`  
**Slug:** `notion-status`

### Help Output

```
Show Notion sync status

Usage:
  bd notion status [flags]

Flags:
  -h, --help   help for status

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


---

## bd notion sync

## `bd notion sync`

**Command:** `bd notion sync`  
**Slug:** `notion-sync`

### Help Output

```
Synchronize issues between beads and Notion.

By default this performs bidirectional sync. Use --pull or --push to limit direction.

Usage:
  bd notion sync [flags]

Flags:
      --create-only     Only create missing remote pages, do not update existing ones
      --dry-run         Preview changes without making mutations
  -h, --help            help for sync
      --prefer-local    On conflict, keep the local beads version
      --prefer-notion   On conflict, use the Notion version
      --pull            Only pull issues from Notion
      --push            Only push issues to Notion
      --state string    Issue state to sync: open, closed, or all (default "all")

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


---

## bd notion

## `bd notion`

**Command:** `bd notion`  
**Slug:** `notion`

### Help Output

```
Commands for syncing issues between beads and Notion.

Usage:
  bd notion [command]

Available Commands:
  connect     Connect bd to an existing Notion database or data source
  init        Create a dedicated Beads database in Notion
  status      Show Notion sync status
  sync        Sync issues with Notion

Flags:
  -h, --help   help for notion

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

Use "bd notion [command] --help" for more information about a command.
```

### Sub-commands

- [`bd notion connect`](./notion-connect.md) — Connect bd to an existing Notion database or data source
- [`bd notion init`](./notion-init.md) — Create a dedicated Beads database in Notion
- [`bd notion status`](./notion-status.md) — Show Notion sync status
- [`bd notion sync`](./notion-sync.md) — Sync issues with Notion


---

## bd onboard

## `bd onboard`

**Command:** `bd onboard`  
**Slug:** `onboard`

### Help Output

```
Display a minimal snippet to add to your agent instructions file for bd integration.

By default, the agent instructions file is AGENTS.md. Use 'bd init --agents-file'
to configure a different filename (e.g. BEADS.md).

This outputs a small (~10 line) snippet that points to 'bd prime' for full
workflow context. This is the same minimal profile that 'bd init' generates
by default. This approach:

  • Keeps your agent file lean (doesn't bloat with instructions)
  • bd prime provides dynamic, always-current workflow details
  • Hooks auto-inject bd prime at session start

For agents that don't support hooks (Codex, Factory, etc.), use
'bd init --agents-profile=full' to embed the complete command reference.

Usage:
  bd onboard [flags]

Flags:
  -h, --help   help for onboard

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


---

## bd orphans

## `bd orphans`

**Command:** `bd orphans`  
**Slug:** `orphans`

### Help Output

```
Identify orphaned issues - issues that are referenced in commit messages but remain open or in_progress in the database.

This helps identify work that has been implemented but not formally closed.

Examples:
  bd orphans              # Show orphaned issues
  bd orphans --json       # Machine-readable output
  bd orphans --details    # Show full commit information
  bd orphans --fix        # Close orphaned issues with confirmation

Usage:
  bd orphans [flags]

Flags:
      --details   Show full commit information
  -f, --fix       Close orphaned issues with confirmation
  -h, --help      help for orphans

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


---

## bd preflight

## `bd preflight`

**Command:** `bd preflight`  
**Slug:** `preflight`

### Help Output

```
Display a checklist of common pre-PR checks for contributors.

This command helps catch common issues before pushing to CI:
- Tests not run locally
- Lint errors
- Unformatted Go files
- .beads/issues.jsonl pollution
- Stale nix vendorHash
- Version mismatches

Examples:
  bd preflight              # Show checklist
  bd preflight --check      # Run checks automatically
  bd preflight --check --json  # JSON output for programmatic use
  bd preflight --check --skip-lint  # Explicitly skip lint check


Usage:
  bd preflight [flags]

Flags:
      --check       Run checks automatically
      --fix         Auto-fix issues where possible (not yet implemented)
  -h, --help        help for preflight
      --json        Output results as JSON
      --skip-lint   Skip lint check explicitly

Global Flags:
      --actor string              Actor name for audit trail (default: $BEADS_ACTOR, git user.name, $USER)
      --db string                 Database path (default: auto-discover .beads/*.db)
      --dolt-auto-commit string   Dolt auto-commit policy (off|on|batch). 'on': commit after each write. 'batch': defer commits to bd dolt commit; uncommitted changes persist in the working set until then. SIGTERM/SIGHUP flush pending batch commits. Default: off. Override via config key dolt.auto-commit
      --profile                   Generate CPU profile for performance analysis
  -q, --quiet                     Suppress non-essential output (errors only)
      --readonly                  Read-only mode: block write operations (for worker sandboxes)
      --sandbox                   Sandbox mode: disables auto-sync
  -v, --verbose                   Enable verbose/debug output
```


---

## bd prime

## `bd prime`

**Command:** `bd prime`  
**Slug:** `prime`

### Help Output

```
Output essential Beads workflow context in AI-optimized markdown format.

Automatically detects if MCP server is active and adapts output:
- MCP mode: Brief workflow reminders (~50 tokens)
- CLI mode: Full command reference (~1-2k tokens)

Designed for Claude Code hooks (SessionStart, PreCompact) to prevent
agents from forgetting bd workflow after context compaction.

Config options:
- no-git-ops: When true, outputs stealth mode (no git commands in session close protocol).
  Set via: bd config set no-git-ops true
  Useful when you want to control when commits happen manually.

Workflow customization:
- Place a .beads/PRIME.md file to override the default output entirely.
- Use --export to dump the default content for customization.

Usage:
  bd prime [flags]

Flags:
      --export    Output default content (ignores PRIME.md override)
      --full      Force full CLI output (ignore MCP detection)
  -h, --help      help for prime
      --mcp       Force MCP mode (minimal output)
      --stealth   Stealth mode (no git operations, flush only)

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


---

## bd priority

## `bd priority`

**Command:** `bd priority`  
**Slug:** `priority`

### Help Output

```
Set the priority of an issue.

Shorthand for 'bd update <id> --priority <n>'.

Priority levels:
  0 - Critical (security, data loss, broken builds)
  1 - High (major features, important bugs)
  2 - Medium (default)
  3 - Low (polish, optimization)
  4 - Backlog (future ideas)

Examples:
  bd priority bd-123 0    # Critical
  bd priority bd-123 2    # Medium

Usage:
  bd priority <id> <n> [flags]

Flags:
  -h, --help   help for priority

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


---

## bd promote

## `bd promote`

**Command:** `bd promote`  
**Slug:** `promote`

### Help Output

```
Promote a wisp (ephemeral issue) to a permanent bead.

This copies the issue from the wisps table (dolt_ignored) to the permanent
issues table (Dolt-versioned), preserving labels, dependencies, events, and
comments. The original ID is preserved so all links keep working.

A comment is added recording the promotion and optional reason.

Examples:
  bd promote bd-wisp-abc123
  bd promote bd-wisp-abc123 --reason "Worth tracking long-term"

Usage:
  bd promote <wisp-id> [flags]

Flags:
  -h, --help            help for promote
  -r, --reason string   Reason for promotion

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


---

## bd purge

## `bd purge`

**Command:** `bd purge`  
**Slug:** `purge`

### Help Output

```
Permanently delete closed ephemeral beads and their associated data.

Closed ephemeral beads (wisps, transient molecules) accumulate rapidly and
have no value once closed. This command removes them to reclaim storage.

Deletes: issues, dependencies, labels, events, and comments for matching beads.
Skips: pinned beads (protected).

EXAMPLES:
  bd purge                           # Preview what would be purged
  bd purge --force                   # Delete all closed ephemeral beads
  bd purge --older-than 7d --force   # Only purge items closed 7+ days ago
  bd purge --pattern "*-wisp-*"      # Only purge matching ID pattern
  bd purge --dry-run                 # Detailed preview with stats

Usage:
  bd purge [flags]

Flags:
      --dry-run             Preview what would be purged with stats
  -f, --force               Actually purge (without this, shows preview)
  -h, --help                help for purge
      --older-than string   Only purge beads closed more than N ago (e.g., 7d, 2w, 30)
      --pattern string      Only purge beads matching ID glob pattern (e.g., *-wisp-*)

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


---

## bd q

## `bd q`

**Command:** `bd q`  
**Slug:** `q`

### Help Output

```
Quick capture creates an issue and outputs only the issue ID.
Designed for scripting and AI agent integration.

Example:
  bd q "Fix login bug"           # Outputs: bd-a1b2
  ISSUE=$(bd q "New feature")    # Capture ID in variable
  bd q "Task" | xargs bd show    # Pipe to other commands

Usage:
  bd q [title] [flags]

Flags:
  -h, --help              help for q
  -l, --labels strings    Labels
  -p, --priority string   Priority (0-4 or P0-P4) (default "2")
  -t, --type string       Issue type (default "task")

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


---

## bd query

## `bd query`

**Command:** `bd query`  
**Slug:** `query`

### Help Output

```
Query issues using a simple query language that supports compound filters,
boolean operators, and date-relative expressions.

The query language enables complex filtering that would otherwise require
multiple flags or piping through jq.

Syntax:
  field=value       Equality comparison
  field!=value      Inequality comparison
  field>value       Greater than
  field>=value      Greater than or equal
  field<value       Less than
  field<=value      Less than or equal

Boolean operators (case-insensitive):
  expr AND expr     Both conditions must match
  expr OR expr      Either condition can match
  NOT expr          Negates the condition
  (expr)            Grouping with parentheses

Supported fields:
  status            Stored status (open, in_progress, blocked, deferred, closed). Note: dependency-blocked issues stay "open"; use 'bd blocked' to find them
  priority          Priority level (0-4)
  type              Issue type (bug, feature, task, epic, chore, decision)
  assignee          Assigned user (use "none" for unassigned)
  owner             Issue owner
  label             Issue label (use "none" for unlabeled)
  title             Search in title (contains)
  description       Search in description (contains, "none" for empty)
  notes             Search in notes (contains)
  created           Creation date/time
  updated           Last update date/time
  closed            Close date/time
  id                Issue ID (supports wildcards: bd-*)
  spec              Spec ID (supports wildcards)
  pinned            Boolean (true/false)
  ephemeral         Boolean (true/false)
  template          Boolean (true/false)
  parent            Parent issue ID
  mol_type          Molecule type (swarm, patrol, work)

Date values:
  Relative durations: 7d (7 days ago), 24h (24 hours ago), 2w (2 weeks ago)
  Absolute dates: 2025-01-15, 2025-01-15T10:00:00Z
  Natural language: tomorrow, "next monday", "in 3 days"

Examples:
  bd query "status=open AND priority>1"
  bd query "status=open AND priority<=2 AND updated>7d"
  bd query "(status=open OR status=blocked) AND priority<2"
  bd query "type=bug AND label=urgent"
  bd query "NOT status=closed"
  bd query "assignee=none AND type=task"
  bd query "created>30d AND status!=closed"
  bd query "label=frontend OR label=backend"
  bd query "title=authentication AND priority=0"

Usage:
  bd query [expression] [flags]

Flags:
  -a, --all           Include closed issues (default: exclude closed)
  -h, --help          help for query
  -n, --limit int     Limit results (default: 50, 0 = unlimited) (default 50)
      --long          Show detailed multi-line output for each issue
      --parse-only    Only parse the query and show the AST (for debugging)
  -r, --reverse       Reverse sort order
      --sort string   Sort by field: priority, created, updated, closed, status, id, title, type, assignee

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


---

## bd quickstart

## `bd quickstart`

**Command:** `bd quickstart`  
**Slug:** `quickstart`

### Help Output

```
Display a quick start guide showing common bd workflows and patterns.

Usage:
  bd quickstart [flags]

Flags:
  -h, --help   help for quickstart

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


---

## bd ready

## `bd ready`

**Command:** `bd ready`  
**Slug:** `ready`

### Help Output

```
Show ready work (open issues with no active blockers).

Excludes in_progress, blocked, deferred, and hooked issues. This uses the
GetReadyWork API which applies blocker-aware semantics to find truly claimable work.

Note: 'bd list --ready' is NOT equivalent - it only filters by status=open.

Use --mol to filter to a specific molecule's steps:
  bd ready --mol bd-patrol   # Show ready steps within molecule

Use --gated to find molecules ready for gate-resume dispatch:
  bd ready --gated           # Find molecules where a gate closed

This is useful for agents executing molecules to see which steps can run next.

Usage:
  bd ready [flags]

Flags:
  -a, --assignee string              Filter by assignee
      --exclude-type strings         Exclude issue types from results (comma-separated or repeatable, e.g., --exclude-type=convoy,epic)
      --explain                      Show dependency-aware reasoning for why issues are ready or blocked
      --gated                        Find molecules ready for gate-resume dispatch
      --has-metadata-key string      Filter issues that have this metadata key set
  -h, --help                         help for ready
      --include-deferred             Include issues with future defer_until timestamps
      --include-ephemeral            Include ephemeral issues (wisps) in results
  -l, --label strings                Filter by labels (AND: must have ALL). Can combine with --label-any
      --label-any strings            Filter by labels (OR: must have AT LEAST ONE). Can combine with --label
  -n, --limit int                    Maximum issues to show (default 10)
      --metadata-field stringArray   Filter by metadata field (key=value, repeatable)
      --mol string                   Filter to steps within a specific molecule
      --mol-type string              Filter by molecule type: swarm, patrol, or work
      --parent string                Filter to descendants of this bead/epic
      --plain                        Display issues as a plain numbered list
      --pretty                       Display issues in a tree format with status/priority symbols (default true)
  -p, --priority int                 Filter by priority
  -s, --sort string                  Sort policy: priority (default), hybrid, oldest (default "priority")
  -t, --type string                  Filter by issue type (task, bug, feature, epic, decision, merge-request). Aliases: mr→merge-request, feat→feature, mol→molecule, dec/adr→decision
  -u, --unassigned                   Show only unassigned issues

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


---

## bd recall

## `bd recall`

**Command:** `bd recall`  
**Slug:** `recall`

### Help Output

```
Retrieve the full content of a memory by its key.

Examples:
  bd recall dolt-phantoms
  bd recall auth-jwt

Usage:
  bd recall <key> [flags]

Flags:
  -h, --help   help for recall

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


---

## bd rename prefix

## `bd rename-prefix`

**Command:** `bd rename-prefix`  
**Slug:** `rename-prefix`

### Help Output

```
Rename the issue prefix for all issues in the database.
This will update all issue IDs and all text references across all fields.

USE CASES:
- Shortening long prefixes (e.g., 'knowledge-work-' → 'kw-')
- Rebranding project naming conventions
- Consolidating multiple prefixes after database corruption
- Migrating to team naming standards

Prefix validation rules:
- Max length: 8 characters
- Allowed characters: lowercase letters, numbers, hyphens
- Must start with a letter
- Must end with a hyphen (e.g., 'kw-', 'work-')
- Cannot be empty or just a hyphen

Multiple prefix detection and repair:
If issues have multiple prefixes (corrupted database), use --repair to consolidate them.
The --repair flag will rename all issues with incorrect prefixes to the new prefix,
preserving issues that already have the correct prefix.

EXAMPLES:
  bd rename-prefix kw-                # Rename from 'knowledge-work-' to 'kw-'
  bd rename-prefix mtg- --repair      # Consolidate multiple prefixes into 'mtg-'
  bd rename-prefix team- --dry-run    # Preview changes without applying

NOTE: This is a rare operation. Most users never need this command.

Usage:
  bd rename-prefix <new-prefix> [flags]

Flags:
      --dry-run   Preview changes without applying them
  -h, --help      help for rename-prefix
      --repair    Repair database with multiple prefixes by consolidating them

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


---

## bd rename

## `bd rename`

**Command:** `bd rename`  
**Slug:** `rename`

### Help Output

```
Rename an issue from one ID to another.

This updates:
- The issue's primary ID
- All references in other issues (descriptions, titles, notes, etc.)
- Dependencies pointing to/from this issue
- Labels, comments, and events

Examples:
  bd rename bd-w382l bd-dolt     # Rename to memorable ID
  bd rename gt-abc123 gt-auth    # Use descriptive ID

Note: The new ID must use a valid prefix for this database.

Usage:
  bd rename <old-id> <new-id> [flags]

Flags:
  -h, --help   help for rename

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


---

## bd reopen

## `bd reopen`

**Command:** `bd reopen`  
**Slug:** `reopen`

### Help Output

```
Reopen closed issues by setting status to 'open' and clearing the closed_at timestamp.
This is more explicit than 'bd update --status open' and emits a Reopened event.

Usage:
  bd reopen [id...] [flags]

Flags:
  -h, --help            help for reopen
  -r, --reason string   Reason for reopening

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


---

## bd repo add

## `bd repo add`

**Command:** `bd repo add`  
**Slug:** `repo-add`

### Help Output

```
Add a repository path to the repos.additional list in config.yaml.

The path should point to a directory containing a .beads folder.
Paths can be absolute or relative (they are stored as-is).

This modifies .beads/config.yaml, which is version-controlled and
shared across all clones of this repository.

Usage:
  bd repo add <path> [flags]

Flags:
  -h, --help   help for add
      --json   Output JSON

Global Flags:
      --actor string              Actor name for audit trail (default: $BEADS_ACTOR, git user.name, $USER)
      --db string                 Database path (default: auto-discover .beads/*.db)
      --dolt-auto-commit string   Dolt auto-commit policy (off|on|batch). 'on': commit after each write. 'batch': defer commits to bd dolt commit; uncommitted changes persist in the working set until then. SIGTERM/SIGHUP flush pending batch commits. Default: off. Override via config key dolt.auto-commit
      --profile                   Generate CPU profile for performance analysis
  -q, --quiet                     Suppress non-essential output (errors only)
      --readonly                  Read-only mode: block write operations (for worker sandboxes)
      --sandbox                   Sandbox mode: disables auto-sync
  -v, --verbose                   Enable verbose/debug output
```


---

## bd repo list

## `bd repo list`

**Command:** `bd repo list`  
**Slug:** `repo-list`

### Help Output

```
List all repositories configured in .beads/config.yaml.

Shows the primary repository (always ".") and any additional
repositories configured for hydration.

Usage:
  bd repo list [flags]

Flags:
  -h, --help   help for list
      --json   Output JSON

Global Flags:
      --actor string              Actor name for audit trail (default: $BEADS_ACTOR, git user.name, $USER)
      --db string                 Database path (default: auto-discover .beads/*.db)
      --dolt-auto-commit string   Dolt auto-commit policy (off|on|batch). 'on': commit after each write. 'batch': defer commits to bd dolt commit; uncommitted changes persist in the working set until then. SIGTERM/SIGHUP flush pending batch commits. Default: off. Override via config key dolt.auto-commit
      --profile                   Generate CPU profile for performance analysis
  -q, --quiet                     Suppress non-essential output (errors only)
      --readonly                  Read-only mode: block write operations (for worker sandboxes)
      --sandbox                   Sandbox mode: disables auto-sync
  -v, --verbose                   Enable verbose/debug output
```


---

## bd repo remove

## `bd repo remove`

**Command:** `bd repo remove`  
**Slug:** `repo-remove`

### Help Output

```
Remove a repository path from the repos.additional list in config.yaml.

The path must exactly match what was added (e.g., if you added "~/foo",
you must remove "~/foo", not "/home/user/foo").

This command also removes any previously-hydrated issues from the database
that came from the removed repository.

Usage:
  bd repo remove <path> [flags]

Flags:
  -h, --help   help for remove
      --json   Output JSON

Global Flags:
      --actor string              Actor name for audit trail (default: $BEADS_ACTOR, git user.name, $USER)
      --db string                 Database path (default: auto-discover .beads/*.db)
      --dolt-auto-commit string   Dolt auto-commit policy (off|on|batch). 'on': commit after each write. 'batch': defer commits to bd dolt commit; uncommitted changes persist in the working set until then. SIGTERM/SIGHUP flush pending batch commits. Default: off. Override via config key dolt.auto-commit
      --profile                   Generate CPU profile for performance analysis
  -q, --quiet                     Suppress non-essential output (errors only)
      --readonly                  Read-only mode: block write operations (for worker sandboxes)
      --sandbox                   Sandbox mode: disables auto-sync
  -v, --verbose                   Enable verbose/debug output
```


---

## bd repo sync

## `bd repo sync`

**Command:** `bd repo sync`  
**Slug:** `repo-sync`

### Help Output

```
Synchronize issues from all configured additional repositories.

Reads issues.jsonl from each additional repository and imports them into
the primary database with their original prefixes and source_repo set.
Uses mtime caching to skip repos whose JSONL hasn't changed.

Also triggers Dolt push/pull if a remote is configured.

Usage:
  bd repo sync [flags]

Flags:
  -h, --help      help for sync
      --json      Output JSON
      --verbose   Show detailed sync progress

Global Flags:
      --actor string              Actor name for audit trail (default: $BEADS_ACTOR, git user.name, $USER)
      --db string                 Database path (default: auto-discover .beads/*.db)
      --dolt-auto-commit string   Dolt auto-commit policy (off|on|batch). 'on': commit after each write. 'batch': defer commits to bd dolt commit; uncommitted changes persist in the working set until then. SIGTERM/SIGHUP flush pending batch commits. Default: off. Override via config key dolt.auto-commit
      --profile                   Generate CPU profile for performance analysis
  -q, --quiet                     Suppress non-essential output (errors only)
      --readonly                  Read-only mode: block write operations (for worker sandboxes)
      --sandbox                   Sandbox mode: disables auto-sync
```


---

## bd repo

## `bd repo`

**Command:** `bd repo`  
**Slug:** `repo`

### Help Output

```
Configure and manage multiple repository support for multi-repo hydration.

Multi-repo support allows hydrating issues from multiple beads repositories
into a single database for unified cross-repo issue tracking.

Configuration is stored in .beads/config.yaml under the 'repos' section:

  repos:
    primary: "."
    additional:
      - ~/beads-planning
      - ~/work-repo

Examples:
  bd repo add ~/beads-planning       # Add planning repo
  bd repo add ../other-repo          # Add relative path repo
  bd repo list                       # Show all configured repos
  bd repo remove ~/beads-planning    # Remove by path
  bd repo sync                       # Sync from all configured repos

Usage:
  bd repo [command]

Available Commands:
  add         Add an additional repository to sync
  list        List all configured repositories
  remove      Remove a repository from sync configuration
  sync        Manually trigger multi-repo sync

Flags:
  -h, --help   help for repo

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

Use "bd repo [command] --help" for more information about a command.
```

### Sub-commands

- [`bd repo add`](./repo-add.md) — Add an additional repository to sync
- [`bd repo list`](./repo-list.md) — List all configured repositories
- [`bd repo remove`](./repo-remove.md) — Remove a repository from sync configuration
- [`bd repo sync`](./repo-sync.md) — Manually trigger multi-repo sync


---

## bd restore

## `bd restore`

**Command:** `bd restore`  
**Slug:** `restore`

### Help Output

```
Restore full history of a compacted issue from Dolt version history.

When an issue is compacted, its description and notes are truncated.
This command queries Dolt's history tables to find the pre-compaction
version and displays the full issue content.

This is read-only and does not modify the database.

Usage:
  bd restore <issue-id> [flags]

Flags:
  -h, --help   help for restore
      --json   Output restore results in JSON format

Global Flags:
      --actor string              Actor name for audit trail (default: $BEADS_ACTOR, git user.name, $USER)
      --db string                 Database path (default: auto-discover .beads/*.db)
      --dolt-auto-commit string   Dolt auto-commit policy (off|on|batch). 'on': commit after each write. 'batch': defer commits to bd dolt commit; uncommitted changes persist in the working set until then. SIGTERM/SIGHUP flush pending batch commits. Default: off. Override via config key dolt.auto-commit
      --profile                   Generate CPU profile for performance analysis
  -q, --quiet                     Suppress non-essential output (errors only)
      --readonly                  Read-only mode: block write operations (for worker sandboxes)
      --sandbox                   Sandbox mode: disables auto-sync
  -v, --verbose                   Enable verbose/debug output
```


---

## bd rules audit

## `bd rules audit`

**Command:** `bd rules audit`  
**Slug:** `rules-audit`

### Help Output

```
Scan rules for contradictions and merge opportunities

Usage:
  bd rules audit [flags]

Flags:
  -h, --help              help for audit
      --path string       Path to rules directory (default ".claude/rules/")
      --threshold float   Jaccard similarity threshold (default 0.6)

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


---

## bd rules compact

## `bd rules compact`

**Command:** `bd rules compact`  
**Slug:** `rules-compact`

### Help Output

```
Merge related rules into composites

Usage:
  bd rules compact [flags]

Flags:
      --auto            Apply audit suggestions
      --dry-run         Preview without applying
      --group strings   Rule names to merge
  -h, --help            help for compact
      --path string     Path to rules directory (default ".claude/rules/")

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


---

## bd rules

## `bd rules`

**Command:** `bd rules`  
**Slug:** `rules`

### Help Output

```
Audit and compact Claude rules

Usage:
  bd rules [command]

Available Commands:
  audit       Scan rules for contradictions and merge opportunities
  compact     Merge related rules into composites

Flags:
  -h, --help   help for rules

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

Use "bd rules [command] --help" for more information about a command.
```

### Sub-commands

- [`bd rules audit`](./rules-audit.md) — Scan rules for contradictions and merge opportunities
- [`bd rules compact`](./rules-compact.md) — Merge related rules into composites


---

## bd search

## `bd search`

**Command:** `bd search`  
**Slug:** `search`

### Help Output

```
Search issues across title and ID (excludes closed issues by default).

ID-like queries (e.g., "bd-123", "hq-319") use fast exact/prefix matching.
Text queries search titles. Use --desc-contains for description search.
Use --status all to include closed issues.

Examples:
  bd search "authentication bug"
  bd search "login" --status open
  bd search "database" --label backend --limit 10
  bd search --query "performance" --assignee alice
  bd search "bd-5q" # Search by partial ID (fast prefix match)
  bd search "security" --priority-min 0 --priority-max 2
  bd search "bug" --created-after 2025-01-01
  bd search "refactor" --status all  # Include closed issues
  bd search "bug" --sort priority
  bd search "task" --sort created --reverse
  bd search "api" --desc-contains "endpoint"
  bd search "cleanup" --no-assignee --no-labels

Usage:
  bd search [query] [flags]

Flags:
  -a, --assignee string              Filter by assignee
      --closed-after string          Filter issues closed after date (YYYY-MM-DD or RFC3339)
      --closed-before string         Filter issues closed before date (YYYY-MM-DD or RFC3339)
      --created-after string         Filter issues created after date (YYYY-MM-DD or RFC3339)
      --created-before string        Filter issues created before date (YYYY-MM-DD or RFC3339)
      --desc-contains string         Filter by description substring (case-insensitive)
      --empty-description            Filter issues with empty or missing description
      --external-contains string     Filter by external ref substring (case-insensitive)
      --has-metadata-key string      Filter issues that have this metadata key set
  -h, --help                         help for search
  -l, --label strings                Filter by labels (AND: must have ALL)
      --label-any strings            Filter by labels (OR: must have AT LEAST ONE)
  -n, --limit int                    Limit results (default: 50) (default 50)
      --long                         Show detailed multi-line output for each issue
      --metadata-field stringArray   Filter by metadata field (key=value, repeatable)
      --no-assignee                  Filter issues with no assignee
      --no-labels                    Filter issues with no labels
      --notes-contains string        Filter by notes substring (case-insensitive)
      --priority-max string          Filter by maximum priority (inclusive, 0-4 or P0-P4)
      --priority-min string          Filter by minimum priority (inclusive, 0-4 or P0-P4)
      --query string                 Search query (alternative to positional argument)
  -r, --reverse                      Reverse sort order
      --sort string                  Sort by field: priority, created, updated, closed, status, id, title, type, assignee
  -s, --status string                Filter by stored status (open, in_progress, blocked, deferred, closed, all). Default excludes closed; use 'all' to include closed. Note: dependency-blocked issues use 'bd blocked'
  -t, --type string                  Filter by type (bug, feature, task, epic, chore, decision, merge-request, molecule, gate)
      --updated-after string         Filter issues updated after date (YYYY-MM-DD or RFC3339)
      --updated-before string        Filter issues updated before date (YYYY-MM-DD or RFC3339)

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


---

## bd set state

## `bd set-state`

**Command:** `bd set-state`  
**Slug:** `set-state`

### Help Output

```
Atomically set operational state on an issue.

This command:
1. Creates an event bead recording the state change (source of truth)
2. Removes any existing label for the dimension
3. Adds the new dimension:value label (fast lookup cache)

State labels follow the convention <dimension>:<value>, for example:
  patrol:active, patrol:muted
  mode:normal, mode:degraded
  health:healthy, health:failing

Examples:
  bd set-state agent-abc patrol=muted --reason "Investigating stuck worker"
  bd set-state agent-abc mode=degraded --reason "High error rate detected"
  bd set-state agent-abc health=healthy

The --reason flag provides context for the event bead (recommended).

Usage:
  bd set-state <issue-id> <dimension>=<value> [flags]

Flags:
  -h, --help            help for set-state
      --reason string   Reason for the state change (recorded in event)

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


---

## bd setup

## `bd setup`

**Command:** `bd setup`  
**Slug:** `setup`

### Help Output

```
Setup integration files for AI editors and coding assistants.

Recipes define where beads workflow instructions are written. Built-in recipes
include cursor, claude, gemini, aider, factory, codex, mux, opencode, junie, windsurf, cody, and kilocode.

Examples:
  bd setup cursor          # Install Cursor IDE integration
  bd setup mux --project   # Install Mux workspace layer (.mux/AGENTS.md)
  bd setup mux --global    # Install Mux global layer (~/.mux/AGENTS.md)
  bd setup mux --project --global  # Install both Mux layers
  bd setup --list          # Show all available recipes
  bd setup --print         # Print the template to stdout
  bd setup -o rules.md     # Write template to custom path
  bd setup --add myeditor .myeditor/rules.md  # Add custom recipe

Use 'bd setup <recipe> --check' to verify installation status.
Use 'bd setup <recipe> --remove' to uninstall.

Usage:
  bd setup [recipe] [flags]

Flags:
      --add string      Add a custom recipe with given name
      --check           Check if integration is installed
      --global          Install globally (claude/mux; writes to ~/.claude/settings.json or ~/.mux/AGENTS.md)
  -h, --help            help for setup
      --list            List all available recipes
  -o, --output string   Write template to custom path
      --print           Print the template to stdout
      --project         Install for this project only (gemini/mux)
      --remove          Remove the integration
      --stealth         Use stealth mode (claude/gemini)

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


---

## bd ship

## `bd ship`

**Command:** `bd ship`  
**Slug:** `ship`

### Help Output

```
Ship a capability to satisfy cross-project dependencies.

This command:
  1. Finds issue with export:<capability> label
  2. Validates issue is closed (or --force to override)
  3. Adds provides:<capability> label

External projects can depend on this capability using:
  bd dep add <issue> external:<project>:<capability>

The capability is resolved when the external project has a closed issue
with the provides:<capability> label.

Examples:
  bd ship mol-run-assignee              # Ship the mol-run-assignee capability
  bd ship mol-run-assignee --force      # Ship even if issue is not closed
  bd ship mol-run-assignee --dry-run    # Preview without making changes

Usage:
  bd ship <capability> [flags]

Flags:
      --dry-run   Preview without making changes
      --force     Ship even if issue is not closed
  -h, --help      help for ship

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


---

## bd show

## `bd show`

**Command:** `bd show`  
**Slug:** `show`

### Help Output

```
Show issue details

Usage:
  bd show [id...] [--id=<id>...] [--current] [flags]

Aliases:
  show, view

Flags:
      --as-of string     Show issue as it existed at a specific commit hash or branch (requires Dolt)
      --children         Show only the children of this issue
      --current          Show the currently active issue (in-progress, hooked, or last touched)
  -h, --help             help for show
      --id stringArray   Issue ID (use for IDs that look like flags, e.g., --id=gt--xyz)
      --local-time       Show timestamps in local time instead of UTC
      --long             Show all available fields (extended metadata, agent identity, gate fields, etc.)
      --refs             Show issues that reference this issue (reverse lookup)
      --short            Show compact one-line output per issue
      --thread           Show full conversation thread (for messages)
  -w, --watch            Watch for changes and auto-refresh display

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


---

## bd sql

## `bd sql`

**Command:** `bd sql`  
**Slug:** `sql`

### Help Output

```
Execute a raw SQL query against the underlying database (SQLite or Dolt).

Useful for debugging, maintenance, and working around bugs in higher-level commands.

Examples:
  bd sql 'SELECT COUNT(*) FROM issues'
  bd sql 'SELECT id, title FROM issues WHERE status = "open" LIMIT 5'
  bd sql 'DELETE FROM dirty_issues WHERE issue_id = "bd-abc123"'
  bd sql --csv 'SELECT id, title, status FROM issues'

The query is passed directly to the database. SELECT queries return results as a
table (or JSON/CSV with --json/--csv). Non-SELECT queries (INSERT, UPDATE, DELETE)
report the number of rows affected.

WARNING: Direct database access bypasses the storage layer. Use with caution.

Usage:
  bd sql <query> [flags]

Flags:
      --csv    Output results in CSV format
  -h, --help   help for sql

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


---

## bd stale

## `bd stale`

**Command:** `bd stale`  
**Slug:** `stale`

### Help Output

```
Show issues that haven't been updated recently and may need attention.
This helps identify:
- In-progress issues with no recent activity (may be abandoned)
- Open issues that have been forgotten
- Issues that might be outdated or no longer relevant

Usage:
  bd stale [flags]

Flags:
  -d, --days int        Issues not updated in this many days (default 30)
  -h, --help            help for stale
  -n, --limit int       Maximum issues to show (default 50)
  -s, --status string   Filter by status (open|in_progress|blocked|deferred)

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


---

## bd state list

## `bd state list`

**Command:** `bd state list`  
**Slug:** `state-list`

### Help Output

```
List all state labels (dimension:value format) on an issue.

This filters labels to only show those following the state convention.

Example:
  bd state list witness-abc
  # Output:
  #   patrol: active
  #   mode: normal
  #   health: healthy

Usage:
  bd state list <issue-id> [flags]

Flags:
  -h, --help   help for list

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


---

## bd state

## `bd state`

**Command:** `bd state`  
**Slug:** `state`

### Help Output

```
Query the current value of a state dimension from an issue's labels.

State labels follow the convention <dimension>:<value>, for example:
  patrol:active
  mode:degraded
  health:healthy

This command extracts the value for a given dimension.

Examples:
  bd state witness-abc patrol     # Output: active
  bd state witness-abc mode       # Output: normal
  bd state witness-abc health     # Output: healthy

Usage:
  bd state <issue-id> <dimension> [flags]
  bd state [command]

Available Commands:
  list        List all state dimensions on an issue

Flags:
  -h, --help   help for state

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

Use "bd state [command] --help" for more information about a command.
```

### Sub-commands

- [`bd state list`](./state-list.md) — List all state dimensions on an issue


---

## bd status

## `bd status`

**Command:** `bd status`  
**Slug:** `status`

### Help Output

```
Show a quick snapshot of the issue database state and statistics.

This command provides a summary of issue counts by state (open, in_progress,
blocked, closed), ready work, extended statistics (pinned issues,
average lead time), and recent activity over the last 24 hours from git history.

Similar to how 'git status' shows working tree state, 'bd status' gives you
a quick overview of your issue database without needing multiple queries.

Use cases:
  - Quick project health check
  - Onboarding for new contributors
  - Integration with shell prompts or CI/CD
  - Daily standup reference

Examples:
  bd status                    # Show summary with activity
  bd status --no-activity      # Skip git activity (faster)
  bd status --json             # JSON format output
  bd status --assigned         # Show issues assigned to current user
  bd stats                     # Alias for bd status

Usage:
  bd status [flags]

Aliases:
  status, stats

Flags:
      --all           Show all issues (default behavior)
      --assigned      Show issues assigned to current user
  -h, --help          help for status
      --no-activity   Skip git activity tracking (faster)

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


---

## bd statuses

## `bd statuses`

**Command:** `bd statuses`  
**Slug:** `statuses`

### Help Output

```
List all valid issue statuses and their categories.

Built-in statuses (open, in_progress, blocked, etc.) are always valid.
Additional statuses can be configured via status.custom:

  bd config set status.custom "in_review:active,qa_testing:wip,on_hold:frozen"

Categories control behavior:
  active  — appears in 'bd ready' and default 'bd list'
  wip     — excluded from 'bd ready', visible in default 'bd list'
  done    — excluded from 'bd ready' and default 'bd list'
  frozen  — excluded from 'bd ready' and default 'bd list'

Statuses without a category (legacy format) are valid but excluded from 'bd ready'.

Examples:
  bd statuses            # List all statuses with icons and categories
  bd statuses --json     # Output as JSON


Usage:
  bd statuses [flags]

Flags:
  -h, --help   help for statuses

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


---

## bd swarm create

## `bd swarm create`

**Command:** `bd swarm create`  
**Slug:** `swarm-create`

### Help Output

```
Create a swarm molecule to orchestrate parallel work on an epic.

The swarm molecule:
- Links to the epic it orchestrates
- Has mol_type=swarm for discovery
- Specifies a coordinator (optional)
- Can be picked up by any coordinator agent

If given a single issue (not an epic), it will be auto-wrapped:
- Creates an epic with that issue as its only child
- Then creates the swarm molecule for that epic

Examples:
  bd swarm create bd-epic-123                          # Create swarm for epic
  bd swarm create bd-epic-123 --coordinator=observer/   # With specific coordinator
  bd swarm create bd-task-456                          # Auto-wrap single issue

Usage:
  bd swarm create [epic-id] [flags]

Flags:
      --coordinator string   Coordinator address (e.g., my-project/witness)
      --force                Create new swarm even if one already exists
  -h, --help                 help for create

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


---

## bd swarm list

## `bd swarm list`

**Command:** `bd swarm list`  
**Slug:** `swarm-list`

### Help Output

```
List all swarm molecules with their status.

Shows each swarm molecule with:
- Progress (completed/total issues)
- Active workers
- Epic ID and title

Examples:
  bd swarm list         # List all swarms
  bd swarm list --json  # Machine-readable output

Usage:
  bd swarm list [flags]

Flags:
  -h, --help   help for list

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


---

## bd swarm status

## `bd swarm status`

**Command:** `bd swarm status`  
**Slug:** `swarm-status`

### Help Output

```
Show the current status of a swarm, computed from beads.

Accepts either:
- An epic ID (shows status for that epic's children)
- A swarm molecule ID (follows the link to find the epic)

Displays issues grouped by state:
- Completed: Closed issues
- Active: Issues currently in_progress (with assignee)
- Ready: Open issues with all dependencies satisfied
- Blocked: Open issues waiting on dependencies

The status is COMPUTED from beads, not stored separately.
If beads changes, status changes.

Examples:
  bd swarm status gt-epic-123       # Show swarm status by epic
  bd swarm status gt-swarm-456      # Show status via swarm molecule
  bd swarm status gt-epic-123 --json  # Machine-readable output

Usage:
  bd swarm status [epic-or-swarm-id] [flags]

Flags:
  -h, --help   help for status

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


---

## bd swarm validate

## `bd swarm validate`

**Command:** `bd swarm validate`  
**Slug:** `swarm-validate`

### Help Output

```
Validate an epic's structure to ensure it's ready for swarm execution.

Checks for:
- Correct dependency direction (requirement-based, not temporal)
- Orphaned issues (roots with no dependents)
- Missing dependencies (leaves that should depend on something)
- Cycles (impossible to resolve)
- Disconnected subgraphs

Reports:
- Ready fronts (waves of parallel work)
- Estimated worker-sessions
- Maximum parallelism
- Warnings for potential issues

Examples:
  bd swarm validate gt-epic-123           # Validate epic structure
  bd swarm validate gt-epic-123 --verbose # Include detailed issue graph

Usage:
  bd swarm validate [epic-id] [flags]

Flags:
  -h, --help      help for validate
      --verbose   Include detailed issue graph in output

Global Flags:
      --actor string              Actor name for audit trail (default: $BEADS_ACTOR, git user.name, $USER)
      --db string                 Database path (default: auto-discover .beads/*.db)
      --dolt-auto-commit string   Dolt auto-commit policy (off|on|batch). 'on': commit after each write. 'batch': defer commits to bd dolt commit; uncommitted changes persist in the working set until then. SIGTERM/SIGHUP flush pending batch commits. Default: off. Override via config key dolt.auto-commit
      --json                      Output in JSON format
      --profile                   Generate CPU profile for performance analysis
  -q, --quiet                     Suppress non-essential output (errors only)
      --readonly                  Read-only mode: block write operations (for worker sandboxes)
      --sandbox                   Sandbox mode: disables auto-sync
```


---

## bd swarm

## `bd swarm`

**Command:** `bd swarm`  
**Slug:** `swarm`

### Help Output

```
Swarm management commands for coordinating parallel work on epics.

A swarm is a structured body of work defined by an epic and its children,
with dependencies forming a DAG (directed acyclic graph) of work.

Usage:
  bd swarm [command]

Available Commands:
  create      Create a swarm molecule from an epic
  list        List all swarm molecules
  status      Show current swarm status
  validate    Validate epic structure for swarming

Flags:
  -h, --help   help for swarm

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

Use "bd swarm [command] --help" for more information about a command.
```

### Sub-commands

- [`bd swarm create`](./swarm-create.md) — Create a swarm molecule from an epic
- [`bd swarm list`](./swarm-list.md) — List all swarm molecules
- [`bd swarm status`](./swarm-status.md) — Show current swarm status
- [`bd swarm validate`](./swarm-validate.md) — Validate epic structure for swarming


---

## bd tag

## `bd tag`

**Command:** `bd tag`  
**Slug:** `tag`

### Help Output

```
Add a label to an issue.

Shorthand for 'bd update <id> --add-label <label>'.

Examples:
  bd tag bd-123 bug
  bd tag bd-123 needs-review

Usage:
  bd tag <id> <label> [flags]

Flags:
  -h, --help   help for tag

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


---

## bd todo add

## `bd todo add`

**Command:** `bd todo add`  
**Slug:** `todo-add`

### Help Output

```
Add a new TODO item

Usage:
  bd todo add <title> [flags]

Flags:
  -d, --description string   Description
  -h, --help                 help for add
  -p, --priority int         Priority (0-4, default 2) (default 2)

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


---

## bd todo done

## `bd todo done`

**Command:** `bd todo done`  
**Slug:** `todo-done`

### Help Output

```
Mark TODO(s) as done

Usage:
  bd todo done <id> [<id>...] [flags]

Flags:
  -h, --help            help for done
      --reason string   Reason for closing (default: Completed)

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


---

## bd todo list

## `bd todo list`

**Command:** `bd todo list`  
**Slug:** `todo-list`

### Help Output

```
List TODO items

Usage:
  bd todo list [flags]

Flags:
      --all    Show all TODOs including completed
  -h, --help   help for list

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


---

## bd todo

## `bd todo`

**Command:** `bd todo`  
**Slug:** `todo`

### Help Output

```
Manage TODO items as lightweight task issues.

TODOs are regular task-type issues with convenient shortcuts:
  bd todo add "Title"    -> bd create "Title" -t task -p 2
  bd todo                -> bd list --type task --status open
  bd todo done <id>      -> bd close <id>

TODOs can be promoted to full issues by changing type or priority:
  bd update todo-123 --type bug --priority 0

Usage:
  bd todo [flags]
  bd todo [command]

Available Commands:
  add         Add a new TODO item
  done        Mark TODO(s) as done
  list        List TODO items

Flags:
  -h, --help   help for todo

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

Use "bd todo [command] --help" for more information about a command.
```

### Sub-commands

- [`bd todo add`](./todo-add.md) — Add a new TODO item
- [`bd todo done`](./todo-done.md) — Mark TODO(s) as done
- [`bd todo list`](./todo-list.md) — List TODO items


---

## bd types

## `bd types`

**Command:** `bd types`  
**Slug:** `types`

### Help Output

```
List all valid issue types that can be used with bd create --type.

Core work types (bug, task, feature, chore, epic, decision) are always valid.
Additional types require configuration via types.custom in .beads/config.yaml.

Examples:
  bd types              # List all types with descriptions
  bd types --json       # Output as JSON


Usage:
  bd types [flags]

Flags:
  -h, --help   help for types

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


---

## bd undefer

## `bd undefer`

**Command:** `bd undefer`  
**Slug:** `undefer`

### Help Output

```
Undefer issues to restore them to open status.

This brings issues back from the icebox so they can be worked on again.
Issues will appear in 'bd ready' if they have no blockers.

Examples:
  bd undefer bd-abc        # Undefer a single issue
  bd undefer bd-abc bd-def # Undefer multiple issues

Usage:
  bd undefer [id...] [flags]

Flags:
  -h, --help   help for undefer

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


---

## bd update

## `bd update`

**Command:** `bd update`  
**Slug:** `update`

### Help Output

```
Update one or more issues.

If no issue ID is provided, updates the last touched issue (from most recent
create, update, show, or close operation).

Usage:
  bd update [id...] [flags]

Flags:
      --acceptance string            Acceptance criteria
      --add-label strings            Add labels (repeatable)
      --allow-empty-description      Allow empty description replacement when reading from stdin or file
      --append-notes string          Append to existing notes (with newline separator)
  -a, --assignee string              Assignee
      --await-id string              Set gate await_id (e.g., GitHub run ID for gh:run gates)
      --body-file string             Read description from file (use - for stdin)
      --claim                        Atomically claim the issue (sets assignee to you, status to in_progress; idempotent if already claimed by you)
      --defer string                 Defer until date (empty to clear). Issue hidden from bd ready until then
  -d, --description string           Issue description
      --design string                Design notes
      --design-file string           Read design from file (use - for stdin)
      --due string                   Due date/time (empty to clear). Formats: +6h, +1d, +2w, tomorrow, next monday, 2025-01-15
      --ephemeral                    Mark issue as ephemeral (wisp) - not exported to JSONL
  -e, --estimate int                 Time estimate in minutes (e.g., 60 for 1 hour)
      --external-ref string          External reference (e.g., 'gh-9', 'jira-ABC')
  -h, --help                         help for update
      --history                      Clear no-history flag (re-enable Dolt commit history)
      --metadata string              Set custom metadata (JSON string or @file.json to read from file)
      --no-history                   Mark issue as no-history (skip Dolt commits, not GC-eligible)
      --notes string                 Additional notes
      --parent string                New parent issue ID (reparents the issue, use empty string to remove parent)
      --persistent                   Mark issue as persistent (promote wisp to regular issue)
  -p, --priority string              Priority (0-4 or P0-P4, 0=highest)
      --remove-label strings         Remove labels (repeatable)
      --session string               Claude Code session ID for status=closed (or set CLAUDE_SESSION_ID env var)
      --set-labels strings           Set labels, replacing all existing (repeatable)
      --set-metadata stringArray     Set metadata key=value (repeatable, e.g., --set-metadata team=platform)
      --spec-id string               Link to specification document
  -s, --status string                New status
      --stdin                        Read description from stdin (alias for --body-file -)
      --title string                 New title
  -t, --type string                  New type (bug|feature|task|epic|chore|decision); custom types require types.custom config
      --unset-metadata stringArray   Remove metadata key (repeatable, e.g., --unset-metadata team)

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


---

## bd upgrade ack

## `bd upgrade ack`

**Command:** `bd upgrade ack`  
**Slug:** `upgrade-ack`

### Help Output

```
Mark the current bd version as acknowledged.

This updates metadata.json to record that you've seen the current
version. Mainly useful after reviewing upgrade changes to suppress
future upgrade notifications.

Note: Version tracking happens automatically, so you don't need to
run this command unless you want to explicitly mark acknowledgement.

Examples:
  bd upgrade ack
  bd upgrade ack --json

Usage:
  bd upgrade ack [flags]

Flags:
  -h, --help   help for ack

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


---

## bd upgrade review

## `bd upgrade review`

**Command:** `bd upgrade review`  
**Slug:** `upgrade-review`

### Help Output

```
Show what's new in bd since the last version you used.

Unlike 'bd info --whats-new' which shows the last 3 versions,
this command shows ALL changes since your specific last version.

If you're upgrading from an old version, you'll see the complete
changelog of everything that changed since then.

Examples:
  bd upgrade review
  bd upgrade review --json

Usage:
  bd upgrade review [flags]

Flags:
  -h, --help   help for review

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


---

## bd upgrade status

## `bd upgrade status`

**Command:** `bd upgrade status`  
**Slug:** `upgrade-status`

### Help Output

```
Check if bd has been upgraded since you last used it.

This command uses the version tracking that happens automatically
at startup to detect if bd was upgraded.

Examples:
  bd upgrade status
  bd upgrade status --json

Usage:
  bd upgrade status [flags]

Flags:
  -h, --help   help for status

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


---

## bd upgrade

## `bd upgrade`

**Command:** `bd upgrade`  
**Slug:** `upgrade`

### Help Output

```
Commands for checking bd version upgrades and reviewing changes.

The upgrade command helps you stay aware of bd version changes:
  - bd upgrade status: Check if bd version changed since last use
  - bd upgrade review: Show what's new since your last version
  - bd upgrade ack: Acknowledge the current version

Version tracking is automatic - bd updates metadata.json on every run.

Usage:
  bd upgrade [command]

Available Commands:
  ack         Acknowledge the current bd version
  review      Review changes since last bd version
  status      Check if bd version has changed

Flags:
  -h, --help   help for upgrade

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

Use "bd upgrade [command] --help" for more information about a command.
```

### Sub-commands

- [`bd upgrade ack`](./upgrade-ack.md) — Acknowledge the current bd version
- [`bd upgrade review`](./upgrade-review.md) — Review changes since last bd version
- [`bd upgrade status`](./upgrade-status.md) — Check if bd version has changed


---

## bd vc commit

## `bd vc commit`

**Command:** `bd vc commit`  
**Slug:** `vc-commit`

### Help Output

```
Create a new Dolt commit with all current changes.

Examples:
  bd vc commit -m "Added new feature issues"
  bd vc commit --message "Fixed priority on several issues"
  echo "Multi-line message" | bd vc commit --stdin

Usage:
  bd vc commit [flags]

Flags:
  -h, --help             help for commit
  -m, --message string   Commit message
      --stdin            Read commit message from stdin

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


---

## bd vc merge

## `bd vc merge`

**Command:** `bd vc merge`  
**Slug:** `vc-merge`

### Help Output

```
Merge the specified branch into the current branch.

If there are merge conflicts, they will be reported. You can resolve
conflicts with --strategy.

Examples:
  bd vc merge feature-xyz                    # Merge feature-xyz into current branch
  bd vc merge feature-xyz --strategy ours    # Merge, preferring our changes on conflict
  bd vc merge feature-xyz --strategy theirs  # Merge, preferring their changes on conflict

Usage:
  bd vc merge <branch> [flags]

Flags:
  -h, --help              help for merge
      --strategy string   Conflict resolution strategy: 'ours' or 'theirs'

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


---

## bd vc status

## `bd vc status`

**Command:** `bd vc status`  
**Slug:** `vc-status`

### Help Output

```
Show the current branch, commit hash, and any uncommitted changes.

Examples:
  bd vc status

Usage:
  bd vc status [flags]

Flags:
  -h, --help   help for status

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


---

## bd vc

## `bd vc`

**Command:** `bd vc`  
**Slug:** `vc`

### Help Output

```
Version control operations for the beads database.

These commands provide git-like version control for your issue data, including branching, merging, and
viewing history.

Note: 'bd history', 'bd diff', and 'bd branch' also work for quick access.
This subcommand provides additional operations like merge and commit.

Usage:
  bd vc [command]

Available Commands:
  commit      Create a commit with all staged changes
  merge       Merge a branch into the current branch
  status      Show current branch and uncommitted changes

Flags:
  -h, --help   help for vc

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

Use "bd vc [command] --help" for more information about a command.
```

### Sub-commands

- [`bd vc commit`](./vc-commit.md) — Create a commit with all staged changes
- [`bd vc merge`](./vc-merge.md) — Merge a branch into the current branch
- [`bd vc status`](./vc-status.md) — Show current branch and uncommitted changes


---

## bd version

## `bd version`

**Command:** `bd version`  
**Slug:** `version`

### Help Output

```
Print version information

Usage:
  bd version [flags]

Flags:
  -h, --help   help for version

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


---

## bd where

## `bd where`

**Command:** `bd where`  
**Slug:** `where`

### Help Output

```
Show the active beads database location, including redirect information.

This command is useful for debugging when using redirects, to understand
which .beads directory is actually being used.

Examples:
  bd where           # Show active beads location
  bd where --json    # Output in JSON format


Usage:
  bd where [flags]

Flags:
  -h, --help   help for where

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


---

## bd worktree create

## `bd worktree create`

**Command:** `bd worktree create`  
**Slug:** `worktree-create`

### Help Output

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


---

## bd worktree info

## `bd worktree info`

**Command:** `bd worktree info`  
**Slug:** `worktree-info`

### Help Output

```
Show information about the current worktree.

If the current directory is in a git worktree, shows:
- Worktree path and name
- Branch
- Beads configuration (redirect or main)
- Main repository location

Examples:
  bd worktree info          # Show current worktree info
  bd worktree info --json   # JSON output

Usage:
  bd worktree info [flags]

Flags:
  -h, --help   help for info

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


---

## bd worktree list

## `bd worktree list`

**Command:** `bd worktree list`  
**Slug:** `worktree-list`

### Help Output

```
List all git worktrees and their beads configuration state.

Shows each worktree with:
- Name (directory name)
- Path (full path)
- Branch
- Beads state: "redirect" (uses shared db), "shared" (is main), "none" (no beads)

Examples:
  bd worktree list          # List all worktrees
  bd worktree list --json   # JSON output

Usage:
  bd worktree list [flags]

Flags:
  -h, --help   help for list

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


---

## bd worktree remove

## `bd worktree remove`

**Command:** `bd worktree remove`  
**Slug:** `worktree-remove`

### Help Output

```
Remove a git worktree with safety checks.

Before removing, this command checks for:
- Uncommitted changes
- Unpushed commits
- Stashes

Use --force to skip safety checks (not recommended).

Examples:
  bd worktree remove feature-auth         # Remove with safety checks
  bd worktree remove feature-auth --force # Skip safety checks

Usage:
  bd worktree remove <name> [flags]

Flags:
      --force   Skip safety checks
  -h, --help    help for remove

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


---

## bd worktree

## `bd worktree`

**Command:** `bd worktree`  
**Slug:** `worktree`

### Help Output

```
Manage git worktrees with proper beads configuration.

Worktrees allow multiple working directories sharing the same git repository,
enabling parallel development (e.g., multiple agents or features).

When creating a worktree, beads automatically sets up a redirect file so all
worktrees share the same .beads database. This ensures consistent issue state
across all worktrees.

Examples:
  bd worktree create feature-auth           # Create worktree with beads redirect
  bd worktree create bugfix --branch fix-1  # Create with specific branch name
  bd worktree list                          # List all worktrees
  bd worktree remove feature-auth           # Remove worktree (with safety checks)
  bd worktree info                          # Show info about current worktree

Usage:
  bd worktree [command]

Available Commands:
  create      Create a worktree with beads redirect
  info        Show worktree info for current directory
  list        List all git worktrees
  remove      Remove a worktree with safety checks

Flags:
  -h, --help   help for worktree

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

Use "bd worktree [command] --help" for more information about a command.
```

### Sub-commands

- [`bd worktree create`](./worktree-create.md) — Create a worktree with beads redirect
- [`bd worktree info`](./worktree-info.md) — Show worktree info for current directory
- [`bd worktree list`](./worktree-list.md) — List all git worktrees
- [`bd worktree remove`](./worktree-remove.md) — Remove a worktree with safety checks

