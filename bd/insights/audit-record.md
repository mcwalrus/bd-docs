# `bd audit-record`

**Purpose** — Records an audit entry documenting actions taken on issues, creating a permanent log for compliance and tracking purposes.

## When to use it

• After resolving critical bugs that require documented remediation steps
• When implementing security fixes that need compliance trails
• During code reviews where significant changes affect multiple issues
• For post-incident documentation linking issues to resolution actions
• When external auditors request proof of issue handling procedures
• Before major releases to document all addressed issues

## Key flags / options

| Flag | Description |
|------|-------------|
| `--issue` | Specify which issue(s) this audit record relates to |
| `--type` | Set audit type (security, compliance, review, incident, etc.) |
| `--message` | Provide detailed audit message describing actions taken |
| `--reference` | Link to external documentation, tickets, or commit hashes |
| `--severity` | Mark audit importance level for filtering and reporting |

## Example workflows

**Document security fix resolution:**
```bash
bd audit-record --issue SEC-001 --type security \
  --message "Applied CVE-2024-1234 patch, updated dependencies" \
  --reference "commit:abc123f"
```
Creates a permanent record linking the security issue to specific remediation actions and code changes.

**Log compliance review:**
```bash
bd audit-record --type compliance --severity high \
  --message "GDPR data handling review completed for user registration flow" \
  --reference "https://internal-docs.company.com/gdpr-review-2024"
```
Documents regulatory compliance activities with external reference links for auditor access.

**Post-incident documentation:**
```bash
bd audit-record --issue BUG-456 --issue BUG-789 --type incident \
  --message "Database timeout issues resolved via connection pool tuning"
```
Links multiple related issues to a single remediation effort for comprehensive incident tracking.

## Tips & gotchas

• Audit records are immutable once created — double-check your message content before submitting
• Use consistent `--type` values across your team to enable effective filtering and reporting
• Reference external documents that might change; consider archiving critical compliance documentation locally
• Audit trails integrate with git history but exist independently, so they persist even if issues are deleted

## Related commands

• `bd list --audit` — Filter and view existing audit records
• `bd show` — Display issue details including associated audit entries
• `bd report` — Generate compliance reports including audit trail summaries
• `bd export` — Extract audit data for external compliance systems