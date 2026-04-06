# bd create-form

**Purpose** — Generates pre-populated forms or templates for creating new issues with standardized fields and structure.

## When to use it

- Setting up issue templates for different types of work (bugs, features, documentation)
- Ensuring team members include required information when creating issues
- Streamlining issue creation in CI/CD pipelines or automation scripts
- Creating consistent issue formats across multiple projects
- Generating forms that capture specific metadata or custom fields
- Preparing templates for different stakeholder groups (developers, QA, product)

## Key flags / options

Based on typical form generation patterns, this command likely supports:

| Flag | Description |
|------|-------------|
| `--type` | Specify template type (bug, feature, task, etc.) |
| `--fields` | Define custom fields to include in the form |
| `--output` | Set output format or destination for the generated form |
| `--template` | Use a predefined template as a starting point |

## Example workflows

**Create a bug report template:**
```bash
bd create-form --type=bug --fields="steps,expected,actual"
```
Generates a structured form for bug reports with steps to reproduce, expected behavior, and actual behavior fields.

**Generate feature request form:**
```bash
bd create-form --type=feature --output=.bd/templates/feature.md
```
Creates a feature request template saved to the project's template directory for reuse.

**Custom form with specific fields:**
```bash
bd create-form --fields="priority,component,assignee" --template=custom
```
Builds a form with custom metadata fields for more detailed issue tracking.

## Tips & gotchas

- Generated forms are typically saved as Markdown templates that can be edited before use
- Custom fields may need to match your project's metadata schema
- Forms don't automatically validate input—they're templates for manual completion
- Consider version controlling your templates in `.bd/templates/` for team consistency
- Some form fields might be automatically populated from git context (branch, author, etc.)

## Related commands

- **`bd create`** — Actually create issues using the generated forms
- **`bd list`** — View existing issues to understand what templates might be needed
- **`bd config`** — Set up project-level defaults for form generation
- **`bd template`** — Manage and edit existing issue templates