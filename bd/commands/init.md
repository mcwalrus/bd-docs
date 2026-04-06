# `bd init`

**Command:** `bd init`  
**Slug:** `init`

## Help Output

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
