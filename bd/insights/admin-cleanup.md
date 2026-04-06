# bd admin cleanup

**Purpose**: Removes orphaned issue files and performs repository maintenance tasks to keep the beads tracker database clean.

## When to use it

• After deleting git branches that contained issue files
• When you suspect corrupted or orphaned metadata from interrupted operations
• Before archiving or sharing a repository to ensure clean state
• After bulk operations that may have left temporary files behind
• When disk space is a concern and you want to reclaim storage
• As part of regular maintenance workflows in long-running projects

## Key flags / options

The `cleanup` command typically runs with default settings and doesn't require additional flags for basic operation.

## Example workflows

**Basic cleanup after development cycle:**
```bash
# After merging feature branches, clean up any orphaned files
bd admin cleanup
git status  # Verify what was removed
```
This removes any issue files that no longer have corresponding git objects or have become disconnected from the main issue graph.

**Pre-archive maintenance:**
```bash
# Before creating a project archive or backup
bd admin cleanup
bd list --status all  # Verify issue integrity
git add -A && git commit -m "Clean up beads tracker"
```
Ensures the repository contains only valid, connected issue data before long-term storage.

**Automated maintenance script:**
```bash
#!/bin/bash
# Weekly maintenance routine
bd admin cleanup
if [ $? -eq 0 ]; then
    echo "Cleanup completed successfully"
    bd stats  # Show current repository state
fi
```
Integrates cleanup into automated workflows with proper error checking.

## Tips & gotchas

• Always run `git status` after cleanup to review what files were removed before committing changes
• The command is conservative by design — it won't remove files that might be valid issues
• Cleanup operations are not reversible, so ensure your repository is backed up if you're unsure about the current state
• Running cleanup frequently (weekly or monthly) prevents accumulation of orphaned data
• The command may take longer in repositories with extensive branching history

## Related commands

• **`bd init`** — Initialize tracker (sets up clean state initially)
• **`bd list`** — Verify issue integrity after cleanup
• **`bd stats`** — Check repository health and issue count post-cleanup
• **`bd admin validate`** — Verify tracker consistency before or after maintenance