# bd config get

**Purpose:** Retrieves the current value of a specific configuration setting from your bd project.

## When to use it

• Check current configuration values before making changes
• Troubleshoot unexpected bd behavior by inspecting settings
• Verify configuration after initial project setup
• Audit configuration in scripts or automation workflows
• Debug issues with custom templates, formats, or identifiers
• Confirm inherited or default values for unset options

## Key flags / options

| Flag | Description |
|------|-------------|
| `--global` | Retrieve configuration from global bd settings instead of project-specific |
| `--local` | Explicitly target project-specific configuration (default behavior) |
| `--format` | Output format: `json`, `yaml`, or `plain` (default: plain) |

## Example workflows

**Check issue ID format settings:**
```bash
bd config get issue.id_format
# Output: {type}-{number:04d}
```
This helps verify how new issues will be numbered and formatted in your project.

**Inspect template configuration:**
```bash
bd config get templates.bug --format json
```
Useful when debugging custom issue templates or understanding why certain fields appear in new issues.

**Audit global vs project settings:**
```bash
bd config get user.name --global
bd config get user.name --local
```
Compare global and project-specific author settings to ensure issues are attributed correctly.

## Tips & gotchas

• Configuration keys use dot notation (e.g., `issue.id_format`, `templates.feature`)
• If a key doesn't exist locally, bd may fall back to global or default values
• The `--format json` option is particularly useful when parsing config values in scripts
• Some configuration values are computed or have complex inheritance—use this command to see the effective value bd actually uses

## Related commands

• **`bd config set`** — Modify configuration values
• **`bd config list`** — View all configuration settings at once  
• **`bd init`** — Initial project setup that creates default configuration
• **`bd status`** — May reveal configuration-dependent behavior in action