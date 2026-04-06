# `bd`

**Command:** `bd `  
**Slug:** ``

## Help Output

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

## Sub-commands

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
