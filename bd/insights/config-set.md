# bd config set

**Purpose**: Updates configuration values in the beads repository settings.

## When to use it

- Set your identity (name/email) when first setting up bd in a project
- Configure default priority levels or status values for new issues
- Adjust display preferences like date formats or color schemes
- Set up integrations with external tools or services
- Override global bd settings for a specific repository
- Customize workflow automation triggers

## Key options

| Flag | Description |
|------|-------------|
| `--global` | Apply setting to global bd configuration instead of repository |
| `--unset` | Remove a configuration key entirely |
| `--type <type>` | Force value to be interpreted as specific type (string, int, bool) |

## Example workflows

**Set your identity for issue tracking:**
```bash
bd config set user.name "Jane Developer"
bd config set user.email "jane@company.com"
```
This establishes your identity for any issues you create or modify in this repository.

**Configure default issue settings:**
```bash
bd config set defaults.priority "medium"
bd config set defaults.status "open"
```
New issues will automatically inherit these default values, streamlining issue creation.

**Set global preferences:**
```bash
bd config set --global display.date-format "2006-01-02"
bd config set --global editor.command "code --wait"
```
These settings apply across all bd repositories on your system.

## Tips & gotchas

- Configuration follows a hierarchy: repository settings override global ones
- Use `bd config get` to verify your changes took effect
- Some settings require specific formats (like date patterns) - check documentation
- Boolean values accept `true`/`false`, `1`/`0`, or `on`/`off`
- Removing a key with `--unset` falls back to the next level in the hierarchy
- Changes take effect immediately but may require restarting long-running processes

## Related commands

- `bd config get` - View current configuration values
- `bd config list` - Display all configuration settings
- `bd init` - Initialize repository (often sets initial config)
- `bd status` - Check repository state (may be affected by display settings)