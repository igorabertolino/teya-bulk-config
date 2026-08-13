#!/usr/bin/env python3
import base64, pathlib

root = pathlib.Path(__file__).parent
section = (root / 'sections/variant-b.html').read_text(encoding='utf-8')
b64 = base64.b64encode(section.encode('utf-8')).decode('ascii')

shell = """<!DOCTYPE html>
<html lang="en" class="antialiased">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Bulk configuration — setup profiles · Teya prototype</title>
__TW_INLINE__
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  html, body { font-family: "Figtree", sans-serif; -webkit-font-smoothing: antialiased; }
  iframe { border: 0; }
</style>
</head>
<body class="bg-[#e8e6e1] min-h-screen">
<div class="max-w-6xl mx-auto px-6 py-8">
  <header class="mb-6">
    <p class="text-[12px] leading-[16px] font-semibold uppercase tracking-[1.5px] text-[#16140e8c]">Teya · Card machines · Remote and bulk configuration</p>
    <h1 class="text-[32px] leading-[40px] font-semibold text-[#090806ec] mt-1">Setup profiles</h1>
    <p class="text-[16px] leading-[24px] text-[#16140e8c] mt-1 max-w-2xl">Set up several card machines at once — including ones that haven't arrived yet. Machines follow a named profile; edit it once and the whole fleet updates. Tap through the phone.</p>
  </header>

  <div class="grid grid-cols-1 lg:grid-cols-[1fr_320px] gap-6 items-start">
    <div class="rounded-3xl overflow-hidden bg-[#e8e6e1]">
      <iframe id="frame" title="Prototype" class="w-full" style="height: 960px;"></iframe>
    </div>
    <aside class="bg-white rounded-3xl p-5 border border-[#756b571a] sticky top-6">
      <p class="text-[12px] leading-[16px] font-semibold uppercase tracking-[1.5px] text-[#16140e8c]">Setup profiles</p>
      <h2 class="text-[18px] leading-[26px] font-semibold text-[#090806ec] mt-1">Act on the configuration</h2>
      <p class="text-[14px] leading-[20px] text-[#16140e8c] mt-2">Settings live as a named profile that machines follow. Edit the profile once and the whole fleet updates; new machines can inherit it automatically.</p>
      <ul class="text-[14px] leading-[20px] text-[#090806ec] mt-3 space-y-2 list-disc pl-4">
        <li>Try: Setup profiles tab → Front of house → flip a toggle</li>
        <li>Add machines to the profile; note "Apply to new machines"</li>
        <li>Tap "+ Add" — model, quantity, store, review and pay; machines arrive with the profile ready (upsell, PRD B7)</li>
      </ul>
      <p class="text-[13px] leading-[18px] text-[#16140e8c] mt-4"><strong class="text-[#090806ec]">Why this model:</strong> the profile is the bridge to auto-inherit on upsell (PRD B7 / V2) — a machine ordered in-app arrives already set up (B3, B4).</p>
    </aside>
  </div>
</div>

<script>
const DOC = "__B64_B__";
const html = new TextDecoder().decode(Uint8Array.from(atob(DOC), c => c.charCodeAt(0)));
document.getElementById('frame').src = URL.createObjectURL(new Blob([html], { type: 'text/html' }));
</script>
</body>
</html>
"""

tw = (root / 'assets/tailwind.js').read_text(encoding='utf-8')
shell = shell.replace('__TW_INLINE__', '<script>' + tw + '\n</' + 'script>')
shell = shell.replace('__B64_B__', b64)
out = root / 'index.html'
out.write_text(shell, encoding='utf-8')
print(f"Wrote {out} ({out.stat().st_size/1024:.0f} KB)")
