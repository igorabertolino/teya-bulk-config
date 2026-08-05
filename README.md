# Teya — Remote & bulk configuration prototype

Interactive prototype comparing two solutions for configuring several card machines at once, grounded in the Lemonade design system.

- **Variant A — Multi-select:** act on the machines (Gmail-style selection).
- **Variant B — Setup profiles:** act on the configuration (profiles the fleet follows).

**Live:** https://igorabertolino.github.io/teya-bulk-config/

`index.html` is fully self-contained (Tailwind inlined, variants embedded). `sections/` holds the editable variant sources; `build_shell.py` rebuilds `index.html` from them.

Source PRD: Confluence — (Upsells + Remote/Bulk Config) — PRD & User Stories.
