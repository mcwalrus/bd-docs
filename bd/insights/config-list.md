# bd config list

**Purpose:** Lists all current bd configuration settings with their values and sources.

## When to use it

• **Debugging configuration issues** — check which settings are active and where they're defined
• **Auditing project setup** — verify configuration before sharing repositories or onboarding team members
• **Learning available options** — discover what configuration keys bd supports
• **Troubleshooting unexpected behavior** — confirm settings match your expectations
• **Setting up new environments** — understand existing configuration patterns to replicate

## Key flags / options

| Flag | Description |
|------|-------------|
| *No flags shown in help output* | Command appears to use default list behavior |

## Example workflows

**Check all current settings:**
```bash
bd config list
```
Shows every configuration key-value pair that bd recognizes, helping you understand your current setup.

**Audit before repository handoff:**
```bash
bd config list > config-snapshot.txt
git add config-snapshot.txt
```
Captures current configuration state for documentation or troubleshooting, ensuring team members can replicate your environment.

**Debug unexpected behavior:**
```bash
bd config list | grep -i template
bd config list | grep -i format
```
Filter output to check specific configuration categories when bd isn't behaving as expected.

## Tips & gotchas

• Configuration values may come from multiple sources (global, repository-local, environment variables) — the output should indicate which source takes precedence
• Some settings might show default values even if you haven't explicitly set them
• Empty or unset values may still appear in the list, which is helpful for understanding the complete configuration schema
• The output format is likely designed for both human reading and script parsing

## Related commands

• **`bd config set`** — modify configuration values discovered through listing
• **`bd config get`** — retrieve specific configuration values identified from the list
• **`bd config unset`** — remove unwanted configuration entries found during listing
• **`bd init`** — often used after config listing to set up repositories with desired settings