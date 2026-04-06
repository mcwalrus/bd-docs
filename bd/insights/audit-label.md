# bd audit label

**Purpose:** Validates and reports inconsistencies in bead labels across your issue tracker to ensure data integrity and consistency.

## When to use it

- Before major releases to verify all beads are properly labeled
- After bulk editing or importing beads from external sources
- When debugging search/filtering issues that might be label-related
- As part of CI/CD pipelines to catch labeling errors early
- When onboarding new team members who may have inconsistent labeling practices
- After merging branches that contain bead changes

## Key flags / options

| Flag | Description |
|------|-------------|
| `--fix` | Automatically fix common label inconsistencies where possible |
| `--verbose` | Show detailed information about each label issue found |
| `--format` | Output format (text, json, csv) for integration with other tools |
| `--label-type` | Audit only specific label types (e.g., priority, component, status) |

## Example workflows

**Basic audit check:**
```bash
bd audit label
```
Quick scan to identify any label problems in your bead database. Returns a summary of issues found with recommendations for fixes.

**Automated cleanup:**
```bash
bd audit label --fix --verbose
```
Automatically corrects common issues like case inconsistencies, duplicate labels, and invalid label formats while providing detailed output of all changes made.

**CI integration:**
```bash
bd audit label --format json | jq '.errors | length'
```
Returns the number of label errors in JSON format, perfect for failing CI builds when label inconsistencies are detected.

## Tips & gotchas

- The audit doesn't modify beads unless `--fix` is explicitly used
- Some label inconsistencies may require manual intervention even with `--fix`
- Running this command frequently helps catch problems before they spread across many beads
- Custom label schemas may require additional configuration to validate properly
- Large repositories may take several seconds to audit completely

## Related commands

- `bd label` — Create and manage labels on individual beads
- `bd list` — Filter and search beads by labels to verify audit results  
- `bd status` — Check overall repository health including label statistics
- `bd migrate` — Update bead formats which may affect label structures