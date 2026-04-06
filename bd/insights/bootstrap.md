# `bd bootstrap`

**Purpose:** Initialize a new bd issue tracker repository with the necessary Git hooks and configuration files.

## When to use it

• Starting a new project that needs issue tracking
• Setting up bd in an existing Git repository for the first time
• Reinitializing bd after accidentally removing configuration files
• Creating a clean bd environment after repository corruption
• Adding issue tracking to a project that previously used external tools

## Key flags / options

| Flag | Description |
|------|-------------|
| `--force` | Overwrite existing bd configuration and hooks |
| `--no-hooks` | Skip Git hook installation during initialization |
| `--template` | Initialize with a specific issue template or configuration |

## Example workflows

**New project setup:**
```bash
git init my-project
cd my-project
bd bootstrap
```
Sets up a fresh repository with bd tracking from the start. Creates the `.bd/` directory structure and installs Git hooks for automatic issue validation.

**Existing project integration:**
```bash
cd existing-project
bd bootstrap --force
git add .bd/
git commit -m "Add bd issue tracking"
```
Integrates bd into an established codebase. The `--force` flag overwrites any conflicting files, ensuring a clean setup.

**Lightweight setup for scripts:**
```bash
bd bootstrap --no-hooks
```
Creates the bd structure without Git hooks, useful for automated environments or when you want manual control over when bd validation occurs.

## Tips & gotchas

**Git hooks consideration:** Bootstrap installs Git hooks that validate issues on commit. If your project already has custom hooks, they may be overwritten unless you use `--no-hooks` and manually integrate bd validation.

**Permissions on hooks:** The installed Git hooks need execute permissions. Bootstrap handles this automatically, but if you copy `.bd/` directories between systems, you may need to fix permissions manually.

**Nested repositories:** Bootstrap detects the Git repository root automatically. Running it in a subdirectory will still initialize bd at the repository level, not the current working directory.

## Related commands

• **`bd new`** — Create your first issue after bootstrapping
• **`bd status`** — Verify the bootstrap worked correctly and check repository health
• **`bd config`** — Customize bd behavior after initial setup
• **`bd validate`** — Manually run the validation that Git hooks perform automatically