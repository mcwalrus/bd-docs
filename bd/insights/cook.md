# bd cook

**Purpose** — Generate and execute code to resolve an active beads issue using AI assistance.

## When to use it

• Working on a beads issue and need AI help to generate implementation code
• Stuck on a complex problem that could benefit from automated code generation
• Want to prototype a solution quickly before manual refinement
• Need to auto-generate boilerplate code based on issue requirements
• Testing AI-assisted development workflows within your project
• Exploring solutions when you have a clear issue description but unclear implementation path

## Key flags / options

| Flag | Description |
|------|-------------|
| `--model` | Specify which AI model to use for code generation |
| `--dry-run` | Preview generated code without executing or applying changes |
| `--interactive` | Enable step-by-step confirmation before applying changes |
| `--context` | Include additional files or directories for AI context |

## Example workflows

**Basic AI-assisted coding:**
```bash
bd work 42
bd cook
```
Start working on issue #42, then let AI generate and apply code to resolve it based on the issue description and current codebase context.

**Preview before applying:**
```bash
bd cook --dry-run --model gpt-4
```
Generate code using GPT-4 but only show the proposed changes without modifying files, useful for reviewing AI suggestions before committing.

**Interactive development:**
```bash
bd cook --interactive --context src/utils/
```
Generate code with step-by-step confirmations and include the `src/utils/` directory for additional context, allowing manual approval of each change.

## Tips & gotchas

• The `cook` command works best with well-defined issue descriptions — vague issues lead to vague code generation
• AI-generated code should be reviewed and tested before considering the issue resolved
• The command respects your project's existing code style and patterns when generating solutions
• Works most effectively when you have an active issue context (use `bd work` first)
• Generated code may need manual refinement to handle edge cases or integrate properly with complex codebases

## Related commands

• **`bd work`** — Start working on an issue (typically used before cooking)
• **`bd show`** — View issue details to ensure clear requirements before cooking  
• **`bd test`** — Validate that generated code works correctly
• **`bd finish`** — Mark issue as resolved after successful code generation and testing