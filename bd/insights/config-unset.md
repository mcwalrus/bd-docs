# bd config unset

**Purpose:** Removes configuration options from bd's local or global settings.

## When to use it

- Reset configuration options back to default values
- Remove accidentally set incorrect configuration values
- Clean up obsolete or experimental settings
- Remove sensitive data from configuration (tokens, URLs)
- Prepare a clean configuration state for team sharing
- Troubleshoot configuration-related issues

## Key flags / options

| Flag | Description |
|------|-------------|
| `--global` | Remove setting from global configuration instead of local |
| `--local` | Remove setting from local project configuration (default) |
| `--all` | Remove all configuration entries matching the key pattern |

## Example workflows

**Remove a local project setting:**
```bash
bd config unset issue.default_assignee
```
This clears the default assignee for issues in the current project, reverting to bd's built-in behavior.

**Clean up global authentication:**
```bash
bd config unset --global auth.token
bd config unset --global remote.url
```
Removes stored authentication credentials and remote URLs from your global bd configuration, useful when switching accounts or servers.

**Reset all editor preferences:**
```bash
bd config unset --all editor.*
```
Removes all editor-related configuration options, letting bd fall back to system defaults for text editing.

## Tips & gotchas

- **No confirmation prompt** — The command immediately removes settings without asking for confirmation, so double-check your key names.
- **Cascading defaults** — Removing a local setting may reveal a global setting with the same key; use `bd config list` to verify the final state.
- **Pattern matching** — When using `--all`, be careful with wildcards as they can remove more settings than intended.
- **Case sensitivity** — Configuration keys are case-sensitive, so `issue.Template` and `issue.template` are different settings.

## Related commands

- **`bd config set`** — Set configuration values (opposite operation)
- **`bd config list`** — View current configuration to identify what to unset
- **`bd config get`** — Check specific configuration values before removing them
- **`bd init`** — May set initial configuration that you later want to unset