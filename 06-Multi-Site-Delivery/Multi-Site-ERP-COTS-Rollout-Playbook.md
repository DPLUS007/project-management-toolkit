# Multi-Site ERP/COTS Rollout Playbook

**Reusable delivery guide · Illustrative examples · By Adedayo Ajayi**

Use this guide to coordinate a packaged software rollout across business units or locations. Adapt the gates, owners and acceptance thresholds to the project's approved scope and business risks.

## 1. Choose the rollout approach

| Approach | Suitable conditions | Main tradeoff |
|---|---|---|
| Pilot, then waves | Sites share a core process but have different readiness levels | Pilot lessons improve later waves; temporary interfaces and dual operations need control |
| Phased by module | Modules can operate independently with manageable dependencies | Smaller releases; end-to-end benefits may arrive later |
| Single coordinated launch | Sites must transition together and rehearsals demonstrate readiness | Shorter transition; greater concentration of operational risk |

Record the decision, alternatives, dependencies and approval. Do not select waves solely by geography: consider data quality, process complexity, staffing, integrations and business calendars.

## 2. Define central and local accountability

| Role | Accountability |
|---|---|
| Sponsor / steering committee | Business priorities, funding and escalated decisions |
| Project manager | Integrated plan, dependencies, readiness reporting and escalation |
| Process owner | Common process design and business acceptance |
| Site lead | Local readiness, user availability, communications and site sign-off recommendation |
| Vendor delivery lead | Contracted deliverables, configuration evidence and defect resolution |
| Data / integration leads | Migration, reconciliation and interface validation |
| Service owner | Support readiness, incident routing and operational acceptance |

Name an individual for each role. Establish who can authorize launch, defer a site, accept residual risks and activate contingency.

## 3. Build a site readiness register

Illustrative entries below show how to expose blockers rather than average them away.

| Site | Data | UAT | Training | Support | Overall | Blocking action | Owner |
|---|---|---|---|---|---|---|---|
| Pilot A | Green | Amber | Green | Green | Amber | Retest supplier approval defect | Business test lead |
| Wave 1 B | Red | Amber | Amber | Green | Red | Resolve duplicate supplier records | Local data owner |
| Wave 1 C | Green | Green | Green | Green | Green | Attach acceptance evidence | Site lead |

- **Green:** criteria met with linked evidence.
- **Amber:** recoverable gap with an owner and date; launch impact assessed.
- **Red:** unmet mandatory criterion or blocker without an acceptable recovery plan.

A critical blocker keeps the site red even when other areas are ready. Link each status to evidence, a last-reviewed date and an accountable owner.

## 4. Apply evidence-based gates

| Gate | Required evidence | Decision |
|---|---|---|
| Scope baseline | Site inventory, process scope, agreed exclusions, RACI and delivery dependencies | Approve baseline |
| Pilot readiness | Tested critical workflows, reconciled migration rehearsal, trained users and staffed support | Launch or defer pilot |
| Pilot exit | Business transactions validated, significant defects assessed, support workload understood and lessons assigned | Authorize next wave |
| Wave readiness | Site-specific acceptance, access, data reconciliation, integration tests and cutover rehearsal | Launch, reduce scope or defer |
| Operational handover | Service acceptance, known issues, ownership, monitoring and escalation paths | Close hypercare or extend |

Approvals should capture evidence, residual risks, conditions and decision-maker names. Define mandatory criteria and the permitted exception authority before the launch meeting.

## 5. Coordinate data, testing and change

1. Agree a common process baseline and record justified local variations in the [fit-gap register](../02-Requirements-and-ERP-COTS/ERP-COTS-Fit-Gap-Register.md).
2. Assign local data owners; profile, cleanse and reconcile data in rehearsals before the final load.
3. Trace each critical business requirement to a test and acceptance result using the [requirements traceability matrix](../02-Requirements-and-ERP-COTS/Requirements-Traceability-Matrix.md).
4. Test both standard and local workflows, including business-unit permissions and cross-site dependencies.
5. Schedule training by user role; confirm users can complete their actual tasks.
6. Publish site-specific launch communications, support contacts and escalation arrangements.

For an illustrative procurement workflow, validate requisition creation, approval limits, purchase order creation, goods receipt, invoice matching and downstream financial posting. Include rejected approvals, duplicate invoices and interface failures.

## 6. Manage the launch window

Use the [cutover plan](../04-Testing-and-Deployment/Cutover-Plan.md) to record task sequence, prerequisites, planned duration, owner, validation and contingency.

Before the window, confirm:
- Change freeze, backup and recovery responsibilities.
- Data extraction, final reconciliation and business sign-off.
- Interface scheduling and treatment of queued transactions.
- Site access, staffing and operational workarounds.
- Latest safe decision time and contingency triggers.

Example contingency triggers: financial reconciliation exceeds an approved tolerance; a critical workflow fails; or remaining tasks cannot finish within the approved window. The relevant technical and business owners must establish whether rollback is feasible and how transactions created after launch will be treated.

## 7. Run hypercare and release the next wave

Hold a short daily triage with site, business, vendor and support leads. Track severity, business impact, workaround, owner and next update. Escalate critical incidents immediately through the agreed incident process.

Monitor:
- Successful completion of critical business transactions.
- Open defects by severity and age.
- Integration failures and reconciliation exceptions.
- Support volume, response performance and recurring user issues.
- Adoption of the approved process.

Set handover thresholds before go-live. Transfer open issues with named owners, documentation and service acceptance. Feed pilot lessons into the next wave's plan and readiness criteria.

## Weekly executive update

| Item | Report |
|---|---|
| Delivery health | Overall status with reasons |
| Site readiness | Sites ready, conditional and blocked |
| Next milestone | Date, owner and confidence |
| Top dependency | Consequence if late and recovery action |
| Decision required | Options, recommendation, approver and deadline |
| Business impact | Operational disruption, workaround or adoption concern |

## Related tools

- [UAT plan](../04-Testing-and-Deployment/UAT-Plan.md)
- [Go-live readiness checklist](../04-Testing-and-Deployment/Go-Live-Readiness-Checklist.md)
- [RAID register](../03-Governance-and-Control/RAID-Register.md)
- [ERP/COTS simulated case study](https://github.com/DPLUS007/erp-cots-implementation-case-study)

This is an original illustrative delivery guide, not a record of a completed employer project.
