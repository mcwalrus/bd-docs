# bd config

**Purpose** — Manage bd configuration settings that control issue tracker behavior, display options, and integration preferences.

## When to use it

• **Initial setup** — Configure bd after installation to set your preferred editor, display format, or default labels
• **Team onboarding** — Set consistent configuration across team members for uniform workflows
• **Workflow customization** — Adjust settings like default issue templates, priority schemes, or integration endpoints
• **Troubleshooting** — Check current configuration values when debugging unexpected behavior
• **Environment changes** — Update settings when switching between projects or development environments
• **Integration setup** — Configure external tool connections (editors, notification systems, etc.)

## Key sub-commands

| Command | Purpose |
|---------|---------|
| `get` | Retrieve the current value of a specific configuration setting |
| `set` | Update a single configuration value |
| `set-many` | Batch update multiple configuration values in one operation |
| `list` | Display all current configuration settings and their values |
| `unset` | Remove a configuration setting, reverting to default behavior |
| `validate` | Check that sync-related configuration is properly formatted and functional |

## Example workflows

**Check current editor setting:**
```bash
bd config get editor
# Shows which editor bd will open for issue editing
```

**Set up initial preferences:**
```bash
bd config set-many \
  editor=vim \
  display.format=compact \
  default.priority=normal
# Configure multiple settings at once during setup
```

**Clean up old configuration:**
```bash
bd config list | grep deprecated
bd config unset old.setting.name
# Remove obsolete settings after bd updates
```

## Tips & gotchas

• **Scope awareness** — Configuration can be project-specific or global; check which level you're modifying
• **Validation timing** — Use `validate` before committing configuration changes to avoid breaking sync functionality
• **Batch operations** — Prefer `set-many` over multiple `set` calls for related configuration changes to maintain consistency
• **Default fallbacks** — Unsetting a value reverts to bd's built-in defaults, not empty/null values

## Related commands

• `bd init` — Often followed by configuration setup for new repositories
• `bd status` — May be affected by display-related configuration settings
• `bd sync` — Relies on configuration values validated by `config validate`
• `bd edit` — Uses the editor specified in configuration settings