# Screen an ingestion batch

## Identity
- **Name:** Screen an ingestion batch
- **Definition:** Perform a bounded technical and safety review of a proposed ingestion manifest without granting authority to ingest it.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Establish whether an exact candidate batch is technically coherent and free of identified excluded material before readiness or owner approval.
- **Meaningful outcome:** A pass, fail, or blocked technical-screen result identifies checked scope, evidence, defects, and unresolved risks.
- **Boundaries — includes:** manifest scope, checksums, timestamps, sensitivity screening, planned identifiers, event mapping, exclusions, duplicate risk, and evidence receipt.
- **Boundaries — excludes:** checklist closure, owner authorization, upload, retention decisions, connector activation, and source decommissioning.
- **Terms and concepts:** A `technical screen` is evidence about a batch; it is not permission to act.

## Interaction Contract MLEs
### Produce technical-screen result
- **Actor:** An authorized peer reviewer, operator, or screening agent.
- **Command / intent:** Verify the exact candidate ingestion batch against its technical and safety checks.
- **Current state:** A bounded manifest and required review evidence exist.
- **Policies / invariants:** The reviewed manifest is immutable or version-identified; checks are reproducible; missing evidence produces blocked/fail rather than assumed pass; the result grants no upload authority.
- **Transition:** Evaluate the candidate set and record findings, evidence, and screen status.
- **Result:** A durable pass, fail, or blocked technical-screen record.
- **Events / effects:** A passing screen may make checklist readiness assessment eligible.
- **Unknowns:** Universal screening checklist contents are not established.

## Rules and defaults
### Rules / invariants
- Technical success must not be interpreted as owner approval.
- Any changed manifest requires a new or explicitly updated screen.
### Recommended defaults
- Include hashes, item counts, exclusions, sensitivity findings, and planned event/object identities.

## Unknown / unresolved
- Independent-review requirements vary by risk and source class.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| The peer technical screen verifies evidence but cannot authorize ingestion. | rule/invariant | sourced | [C11](../evidence/statement-provenance.md). |
