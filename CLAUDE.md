# Teya — Remote & bulk configuration prototype

Interactive HTML prototype comparing **two solutions** for configuring several Teya card
machines at once. Published via GitHub Pages: https://igorabertolino.github.io/teya-bulk-config/

Owner: Igor Bertolino (Product Designer). Respond in Brazilian Portuguese; all product
copy inside the prototype is **British English**.

## Source of truth

- PRD: Confluence — "(Upsells + Remote/Bulk Config) — PRD & User Stories"
  (space SALTPOS, page 9140568236). Key stories: B1 (see all machines, active + pending
  delivery), B2 (configure many at once), B3 (pre-configure before delivery), B4
  (zero-touch first boot), B5 (edit and re-apply), B6 (Security PIN — open decision),
  B7 (reusable profile, bridge to V2 auto-inherit on upsell).
- Figma refs (file `I3m2FDRARh7uBS2CxfgAc6`): side menu `7001-1090`,
  card machine list `7001-10817`, card machine details `7001-10900`.

## Decisions — do not revisit without asking Igor

- **Variant C ("mirror a machine") was DISCARDED. Never reintroduce it.**
- Two variants remain:
  - **A — Multi-select**: act on the machines. Select rows → one settings form →
    apply → per-device status (Applied / Waiting · offline / Ready on arrival).
  - **B — Setup profiles**: act on the configuration. Named profile ("Front of house"),
    machines follow it; editing re-applies to the fleet; "Apply to new machines" toggle
    is the bridge to PRD B7 / V2 auto-inherit.
- Both variants group the machine list into **Arriving soon** / **Active**. A pending
  machine on a profile shows the tag **Ready on arrival** (PRD B3).
- Mobile form factor: 393×852 iPhone frame, content scrolls inside the phone.

## Architecture

```
index.html          ← generated, fully self-contained (~1 MB). Do not hand-edit.
build_shell.py      ← rebuilds index.html: base64-embeds each variant into an
                      iframe-per-blob shell with evaluation notes sidebar.
sections/
  variant-a.html    ← editable source, self-contained (Tailwind inlined)
  variant-b.html    ← editable source, self-contained (Tailwind inlined)
assets/tailwind.js  ← Tailwind CSS v4 browser build (vendored, inlined at build time)
manifest.json       ← section metadata
```

Workflow: edit a section → `python3 build_shell.py` → open `index.html` to check →
commit + push to `main` → GitHub Pages redeploys (~1 min).

## Design system — Lemonade (essentials)

- Font: Figtree (400/500/600). Page bg `#f6f5f3`, cards `bg-white rounded-3xl`.
- Brand: yellow-lime `#e1e51a` (primary button bg, text `#29320c`, `rounded-[32px]`,
  `min-h-14`). Selected chips: bg `#46520f`, text `#e1e51a`.
- Text: primary `#090806ec`, secondary `#16140e8c`, tertiary `#211c1266`.
  Dividers/borders `#756b571a`.
- Tags (h-5, `rounded-[6px]`, 12px semibold): positive `#7ccf001a`/`#497d00`,
  caution `#fe9a001a`/`#bb4d00`, info `#2b7fff1a`/`#1447e6`, neutral `#5f4f300d`/`#0b0b0a`.
- List items: `p-3 rounded-[20px]`, 40px SymbolContainer leading, inset dividers.
- Motion: transitions 200–300ms `cubic-bezier(0.2,0,0,1)`; `active:scale-[0.96]`;
  enter = fadeInUp 400ms with 100ms stagger.

## Copy rules (Teya style)

British English, sentence case everywhere. "Card machine" (never terminal/POS),
"Security PIN" (never Manager PIN in UI), "tap" not "click", "Wi-Fi", no ampersands,
no exclamation marks, dates as "7 August", £ with no space. Plausible merchant data
only — no lorem ipsum (business: CoffeeBrain; machines: Front till, Bar, Garden till).

## Backlog candidates (ask before building)

- Zero-touch first boot simulation (PRD B4: switch on → downloading → ready).
- Security PIN decision support: A/B toggle showing remote-PIN vs on-device-PIN boot.
- Desktop/portal version for the multi-site operator lens.
- Merchant-testing script for the two variants (Traditional Owner-Operator and
  Multi-Site Operator lenses, per PRD).
