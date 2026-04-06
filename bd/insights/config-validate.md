# bd config validate

## Purpose
Validates the current repository's bd configuration files for syntax errors, missing required fields, and invalid values.

## When to use it
• Before committing configuration changes to avoid breaking the tracker
• When setting up bd in a new repository to ensure proper configuration
• After modifying `.bd/config.toml` or other configuration files manually
• When troubleshooting unexpected bd behavior or errors
• As part of CI/CD pipelines to catch configuration issues early
• When onboarding new team members to verify their bd setup

## Key flags / options
| Flag | Description |
|------|-------------|
| `--strict` | Enable strict validation mode with additional checks |
| `--format` | Output format: `text`, `json`, or `compact` |
| `--quiet` | Show only errors, suppress warnings and info messages |
| `--config-path` | Validate specific config file instead of auto-discovery |

## Example workflows

**Basic validation check:**
```bash
bd config validate
```
Run this before committing to ensure your configuration changes are valid and won't break bd for other team members.

**Strict validation in CI:**
```bash
bd config validate --strict --format json --quiet
```
Use in automated workflows to catch configuration issues with machine-readable output and strict validation rules that might be too pedantic for daily development.

**Validate specific config file:**
```bash
bd config validate --config-path ./custom-bd-config.toml
```
Useful when testing configuration templates or validating config files outside the standard `.bd/` directory structure.

## Tips & gotchas
• Validation runs automatically during most bd operations, but explicit validation helps catch issues early
• Strict mode may flag valid but unconventional configurations as warnings
• JSON output format is particularly useful for integrating with other tools or parsing validation results programmatically
• Configuration validation includes checking for valid issue templates, workflow definitions, and dependency relationship rules
• Remember that some configuration errors only surface during actual issue operations, not during validation

## Related commands
• `bd config show` — Display current configuration values
• `bd config init` — Initialize bd configuration in a new repository
• `bd init` — Set up bd tracker with initial configuration
• `bd status` — Check repository health including configuration status