#!/usr/bin/env python3
import base64, pathlib

root = pathlib.Path(__file__).parent
sections = {
    'a': (root / 'sections/variant-a.html').read_text(encoding='utf-8'),
    'b': (root / 'sections/variant-b.html').read_text(encoding='utf-8'),
}
b64 = {k: base64.b64encode(v.encode('utf-8')).decode('ascii') for k, v in sections.items()}

shell = """<!DOCTYPE html>
<html lang="en" class="antialiased">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Bulk configuration — two solutions to evaluate · Teya prototype</title>
__TW_INLINE__
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  html, body { font-family: "Figtree", sans-serif; -webkit-font-smoothing: antialiased; }
  .tab-active { background: #46520f; color: #e1e51a; }
  .tab-idle { background: #ffffff; color: #090806ec; border: 1px solid #756b571a; }
  iframe { border: 0; }
</style>
</head>
<body class="bg-[#e8e6e1] min-h-screen">
<div class="max-w-6xl mx-auto px-6 py-8">
  <header class="mb-6">
    <p class="text-[12px] leading-[16px] font-semibold uppercase tracking-[1.5px] text-[#16140e8c]">Teya · Card machines · Remote and bulk configuration</p>
    <h1 class="text-[32px] leading-[40px] font-semibold text-[#090806ec] mt-1">Two solutions to evaluate</h1>
    <p class="text-[16px] leading-[24px] text-[#16140e8c] mt-1 max-w-2xl">Same job — set up several card machines at once, including ones that haven't arrived yet — through two different mental models. Tap through each phone.</p>
  </header>

  <div class="flex flex-wrap gap-3 mb-6">
    <button data-v="a" class="tab tab-active rounded-2xl px-5 py-3 text-left transition-colors duration-150 min-w-[220px]">
      <p class="text-[16px] leading-[24px] font-semibold">A — Multi-select</p>
      <p class="text-[13px] leading-[18px] opacity-80">Act on the machines</p>
    </button>
    <button data-v="b" class="tab tab-idle rounded-2xl px-5 py-3 text-left transition-colors duration-150 min-w-[220px]">
      <p class="text-[16px] leading-[24px] font-semibold">B — Setup profiles</p>
      <p class="text-[13px] leading-[18px] opacity-80">Act on the configuration</p>
    </button>
  </div>

  <div class="grid grid-cols-1 lg:grid-cols-[1fr_320px] gap-6 items-start">
    <div class="rounded-3xl overflow-hidden bg-[#e8e6e1]">
      <iframe id="frame" title="Prototype" class="w-full" style="height: 960px;"></iframe>
    </div>
    <aside id="notes" class="bg-white rounded-3xl p-5 border border-[#756b571a] sticky top-6"></aside>
  </div>
</div>

<script>
const DOCS = { a: "__B64_A__", b: "__B64_B__" };
const NOTES = {
  a: `<p class="text-[12px] leading-[16px] font-semibold uppercase tracking-[1.5px] text-[#16140e8c]">Variant A · Multi-select</p>
      <h2 class="text-[18px] leading-[26px] font-semibold text-[#090806ec] mt-1">Act on the machines</h2>
      <p class="text-[14px] leading-[20px] text-[#16140e8c] mt-2">Familiar Photos/Mail pattern: tap Select (or any row), pick machines — including ones still on their way — and configure the group in one form.</p>
      <ul class="text-[14px] leading-[20px] text-[#090806ec] mt-3 space-y-2 list-disc pl-4">
        <li>Try: Select → Select all → Configure → Apply</li>
        <li>Per-device status: Applied / Waiting · offline / Ready on arrival</li>
      </ul>
      <p class="text-[13px] leading-[18px] text-[#16140e8c] mt-4"><strong class="text-[#090806ec]">Trade-off:</strong> quick and familiar, but the setup is one-off — nothing is remembered for the next machine (PRD B1, B2, B3).</p>`,
  b: `<p class="text-[12px] leading-[16px] font-semibold uppercase tracking-[1.5px] text-[#16140e8c]">Variant B · Setup profiles</p>
      <h2 class="text-[18px] leading-[26px] font-semibold text-[#090806ec] mt-1">Act on the configuration</h2>
      <p class="text-[14px] leading-[20px] text-[#16140e8c] mt-2">Settings live as a named profile that machines follow. Edit the profile once and the whole fleet updates; new machines can inherit it automatically.</p>
      <ul class="text-[14px] leading-[20px] text-[#090806ec] mt-3 space-y-2 list-disc pl-4">
        <li>Try: Setup profiles tab → Front of house → flip a toggle</li>
        <li>Add machines to the profile; note "Apply to new machines"</li>
        <li>Order a new card machine from the Machines tab — it arrives with the profile ready (upsell, PRD B7)</li>
      </ul>
      <p class="text-[13px] leading-[18px] text-[#16140e8c] mt-4"><strong class="text-[#090806ec]">Trade-off:</strong> most powerful — it is the bridge to auto-inherit on upsell (PRD B7 / V2) — but introduces a new concept merchants must learn.</p>`
};
const frame = document.getElementById('frame');
const notes = document.getElementById('notes');
const urls = {};
function show(v) {
  if (!urls[v]) {
    const html = new TextDecoder().decode(Uint8Array.from(atob(DOCS[v]), c => c.charCodeAt(0)));
    urls[v] = URL.createObjectURL(new Blob([html], { type: 'text/html' }));
  }
  frame.src = urls[v];
  notes.innerHTML = NOTES[v];
  document.querySelectorAll('.tab').forEach(t => {
    const active = t.dataset.v === v;
    t.classList.toggle('tab-active', active);
    t.classList.toggle('tab-idle', !active);
  });
}
document.querySelectorAll('.tab').forEach(t => t.addEventListener('click', () => show(t.dataset.v)));
show('a');
</script>
</body>
</html>
"""

tw = (root / 'assets/tailwind.js').read_text(encoding='utf-8')
shell = shell.replace('__TW_INLINE__', '<script>' + tw + '\n</' + 'script>')
shell = shell.replace('__B64_A__', b64['a']).replace('__B64_B__', b64['b'])
out = root / 'index.html'
out.write_text(shell, encoding='utf-8')
print(f"Wrote {out} ({out.stat().st_size/1024:.0f} KB)")
