# config-set-many

**Purpose** — Batch update multiple beads configuration values in a single command.

## When to use it

• **Initial repository setup** — Configure multiple settings when first setting up bd in a project
• **Environment migration** — Apply consistent configuration across development, staging, and production environments
• **Team onboarding** — Set standard configuration values for new team members
• **Bulk reconfiguration** — Update multiple related settings after workflow changes
• **Scripted deployments** — Apply configuration programmatically in CI/CD pipelines
• **Template application** — Set up projects from predefined configuration templates

## Key flags / options

| Flag | Description |
|------|-------------|
| `--from-file` | Read configuration pairs from a file instead of command line |
| `--dry-run` | Preview changes without actually updating configuration |
| `--force` | Overwrite existing values without confirmation prompts |
| `--backup` | Create a backup of current configuration before changes |

## Example workflows

**Basic batch configuration:**
```bash
bd config set-many user.name "Jane Doe" user.email "jane@company.com" workflow.auto-assign true
```
Set up user identity and enable automatic assignment in one command.

**Configuration from file:**
```bash
echo "user.name=John Smith\nworkflow.labels=bug,feature,docs\nui.color=always" > team-config.txt
bd config set-many --from-file team-config.txt
```
Apply standardized team configuration from a file, useful for maintaining consistency across team members.

**Safe bulk updates:**
```bash
bd config set-many --dry-run --backup integration.github.enabled true integration.slack.webhook "https://hooks.slack.com/..." 
```
Preview integration settings before applying, with automatic backup creation for rollback capability.

## Tips & gotchas

• **Validation happens upfront** — All configuration keys and values are validated before any changes are applied, preventing partial updates
• **File format flexibility** — The `--from-file` option accepts both `key=value` and YAML formats
• **Atomic operations** — Either all configuration changes succeed or none are applied
• **Nested key support** — Use dot notation for nested configuration like `integration.github.token`
• **Quote complex values** — Wrap values containing spaces or special characters in quotes

## Related commands

• **`bd config set`** — Update individual configuration values
• **`bd config list`** — View current configuration settings
• **`bd config get`** — Retrieve specific configuration values
• **`bd config reset`** — Reset configuration to defaults