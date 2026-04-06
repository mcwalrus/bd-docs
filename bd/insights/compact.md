# bd compact

**Purpose:** Optimize the bd repository by cleaning up unnecessary metadata and reclaiming storage space.

## When to use it

• After significant bead deletions or bulk operations to reclaim disk space
• Before creating backups or distributing the repository
• When repository performance seems sluggish due to metadata bloat
• As part of periodic maintenance workflows
• Before migrating or archiving a project
• When preparing for a clean repository state

## Key flags / options

| Flag | Description |
|------|-------------|
| `--dry-run` | Show what would be compacted without making changes |
| `--force` | Skip confirmation prompts and proceed with compaction |
| `--verbose` | Display detailed information about the compaction process |

## Example workflows

**Basic repository cleanup:**
```bash
bd compact
```
Performs standard compaction, removing orphaned metadata and optimizing storage. bd will prompt for confirmation before making changes.

**Safe preview of compaction:**
```bash
bd compact --dry-run --verbose
```
Shows exactly what files and metadata would be cleaned up without modifying anything. Useful for understanding the impact before committing to the operation.

**Automated maintenance:**
```bash
bd compact --force
```
Runs compaction without user prompts, ideal for CI/CD pipelines or automated maintenance scripts where manual confirmation isn't practical.

## Tips & gotchas

• **Always backup before compacting** — while bd compact is designed to be safe, it permanently removes data that's deemed unnecessary
• **Git integration remains intact** — compaction only affects bd's internal metadata, not your git history or working directory
• **Compaction is irreversible** — deleted metadata cannot be recovered, so use `--dry-run` first if you're unsure
• **Performance impact** — compaction can be slow on large repositories with extensive bead histories
• **Concurrent operations** — avoid running other bd commands while compaction is in progress

## Related commands

• **`bd status`** — Check repository health before and after compaction
• **`bd list`** — Verify bead integrity after compaction operations
• **`bd init`** — Often used together when setting up clean repository states
• **`bd sync`** — Commonly run after compaction to ensure remote repositories are updated