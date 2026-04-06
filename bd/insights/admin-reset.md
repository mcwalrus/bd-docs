# bd admin reset

**Purpose:** Forcefully resets the bd issue tracker to a clean state, removing all issues, comments, and tracking data.

## When to use it

• Starting fresh after experimenting with bd in a project
• Clearing out test issues before going into production
• Recovering from corrupted bd state or metadata
• Migrating from another issue tracker and want a clean slate
• Demonstrating bd to a team without historical clutter
• Fixing issues when bd commands start behaving unexpectedly

## Key flags / options

This is a destructive administrative command that typically runs without additional flags, though some implementations may offer:

| Flag | Description |
|------|-------------|
| `--confirm` | Skip interactive confirmation prompt |
| `--keep-config` | Preserve bd configuration while clearing issues |

## Example workflows

**Clean slate for new project:**
```bash
# Remove all existing bd data and start fresh
bd admin reset
# Confirm when prompted
bd init  # Re-initialize if needed
```

**Quick reset during development:**
```bash
# Reset without confirmation prompt (if supported)
bd admin reset --confirm
bd add "First real issue" --priority high
```

**Preserve settings while clearing issues:**
```bash
# Keep bd configuration but remove all issues
bd admin reset --keep-config
bd status  # Should show empty issue list
```

## Tips & gotchas

• **This is irreversible** — all issues, comments, and dependency relationships are permanently deleted
• Always run `bd export` or commit your current state before resetting if you might need to recover data
• The command may require confirmation in interactive mode to prevent accidental data loss
• Git history containing bd commits remains intact, but the current working state is cleared
• Some bd configurations (like templates or aliases) might be preserved depending on implementation
• After reset, you may need to re-run `bd init` to re-establish the tracker in your repository

## Related commands

• **`bd init`** — Initialize bd in a repository (often used after reset)
• **`bd export`** — Export issues before resetting (backup strategy)  
• **`bd import`** — Import issues back after a reset
• **`bd status`** — Verify the reset was successful (should show empty state)