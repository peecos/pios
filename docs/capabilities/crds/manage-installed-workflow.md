# Manage an installed workflow

## Identity
- **Name:** Manage an installed workflow
- **Definition:** Establish and govern an owner's configured instance of a selected workflow-package version.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Let an owner adopt reusable workflow logic while retaining control of version, parameters, triggers, permissions, and lifecycle.
- **Meaningful outcome:** An installed workflow has an owner-scoped configuration, explicit package-version relationship, current enablement state, and auditable changes.
- **Boundaries — includes:** installation, configuration, enable/pause, trigger settings, version pin/update, duplication, removal, and audit events.
- **Boundaries — excludes:** authoring the package, performing a run, granting undeclared permissions, and interpreting produced results.
- **Terms and concepts:** An `installed workflow` is an owner-controlled instance, not merely a package listing or execution run.

## Interaction Contract MLEs
### Maintain installed-workflow lifecycle
- **Actor:** An authorized owner or workflow administrator.
- **Command / intent:** Install or change an owner's configured workflow instance.
- **Current state:** An eligible workflow-package version and required authority are available.
- **Policies / invariants:** Package version and requested permissions are inspectable; triggers are explicitly enabled; update policy is owner-controlled; removal or pause prevents future automatic runs without rewriting prior run history.
- **Transition:** Create or revise owner configuration, trigger state, version binding, and lifecycle status.
- **Result:** A current installed-workflow record ready, paused, disabled, or removed according to owner intent.
- **Events / effects:** Enabled triggers may make a separate workflow-run capability eligible.
- **Unknowns:** Universal update-notification and compatibility policies are not established.

## Rules and defaults
### Rules / invariants
- Installation does not itself authorize undeclared effects.
- Package updates must not silently replace the owner's selected version or settings.
### Recommended defaults
- Default scheduled or event triggers to disabled until reviewed when they can create external or governed effects.

## Unknown / unresolved
- Whether local adaptations remain linked to upstream package updates is realization-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| An installed workflow is an owner-configured instance with explicit lifecycle and version control. | capability purpose | sourced | [B18](../evidence/statement-provenance.md). |
