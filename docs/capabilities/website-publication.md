# Capability Library website publication plan

**Status:** documentation review cleared; website contribution not yet created and no live route exists

## Verified site mechanism

At inspected `peecos/peecos-web` source revision `08fd000`, the PIOS master page:

1. stores the rendered document in `src/content/pios-master.html`;
2. imports it as raw content from `src/pages/PiosMaster.tsx`;
3. registers `/pios/master` in `src/App.tsx`.

The website source therefore requires its own reviewed contribution. A commit to `peecos/pios` does not update the live site.

## Planned capability-library projection

- Proposed route: `/pios/capabilities`.
- Index source of truth: `docs/capabilities/capability-inventory.md` in `peecos/pios`.
- Detail source of truth: each CRD under `docs/capabilities/crds/`.
- Website output: a human-facing inventory plus one HTML detail view per capability and public supporting document.
- Rendering rule: the website is a projection; it must not introduce requirements absent from the canonical Markdown.
- Privacy rule: restricted realization evidence is represented only by the public-safe status already present in the canonical source.

## Publication sequence

1. Obtain review clearance for the initial PIOS capability-library milestone. Completed for PIOS commit `fda4a68c65dfb72f08e8ea459809b4a35eb14783`.
2. Synchronize a clean website branch with current `origin/main` without including unrelated local changes.
3. Add the capability route and static content projection using the site's existing React/Vite conventions.
4. Run lint, tests, build, internal-link checks, and a local rendering check.
5. Submit a separate website review contribution identifying the exact PIOS source revision represented.
6. Merge and deploy through the existing website workflow.
7. Verify the actual public URL, rendered capability count, detail links, and represented source revision.

## Publication report requirements

Report separately:

- PIOS source commit and review/merge state;
- website commit and review/merge state;
- actual route and live URL;
- represented PIOS revision;
- content, link, and rendering verification;
- any review, authentication, synchronization, or deployment blocker.
