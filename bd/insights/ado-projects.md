# bd ado projects

**Purpose** — Lists all projects in an Azure DevOps organization to help you find the correct project for importing work items.

## When to use it

• Before running `bd ado import` to verify the target project exists
• When exploring an ADO organization to understand its structure  
• To find the exact project name/ID needed for other ADO commands
• During initial setup of bd in a repository connected to Azure DevOps
• When troubleshooting ADO integration issues
• To confirm your authentication and organization access is working

## Key flags / options

Based on the command structure, this appears to be a simple listing command without complex options. The authentication and organization details would likely be configured separately or inherited from ADO CLI configuration.

## Example workflows

**Explore available projects:**
```bash
bd ado projects
```
Lists all projects in your configured ADO organization, showing names and IDs you can reference in import commands.

**Verify project before import:**
```bash
# First check what projects are available
bd ado projects
# Then import from the specific project
bd ado import --project "MyProject" --query "assigned-to-me"
```

**Pipeline integration:**
```bash
# In CI/CD, verify project exists before automated imports
if bd ado projects | grep -q "MyProject"; then
    bd ado import --project "MyProject"
fi
```

## Tips & gotchas

• Make sure you're authenticated with Azure DevOps CLI (`az devops login`) before running this command
• The command respects your default ADO organization setting — verify with `az devops configure --list`
• Project names are case-sensitive in subsequent import commands, so note the exact spelling
• Some projects may be visible but not accessible depending on your permissions
• Large organizations may have many projects — consider using `grep` to filter output

## Related commands

• `bd ado import` — Import work items from ADO projects into bd issues
• `bd ado auth` — Configure authentication for Azure DevOps integration  
• `bd list` — View imported issues after running ADO imports
• `bd ado sync` — Synchronize changes between bd and ADO work items