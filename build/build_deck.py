"""Build khonnai-pitch.html from the cloned U-Hackathon deck (build/source-index.html).

The original layout, CSS, animations and scripts are kept; only slide content,
brand chrome and a few data hooks are swapped. Run from anywhere:
    python build/build_deck.py
"""
import base64
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from slides_khonnai import SLIDES, TEAM  # noqa: E402

SRC = HERE / 'source-index.html'  # the cloned U-Hackathon deck, kept untouched
OUT = ROOT / 'khonnai-pitch.html'
ASSETS = HERE / 'assets'


def data_uri(name, mime):
    return f'data:{mime};base64,' + base64.b64encode((ASSETS / name).read_bytes()).decode()


def photo_uri(i):
    for ext, mime in (('jpg', 'image/jpeg'), ('png', 'image/png'), ('webp', 'image/webp')):
        p = ASSETS / f'team-{i + 1}.{ext}'
        if p.exists():
            return data_uri(p.name, mime)
    return None


def team_cards():
    cards = []
    for i, (name, role) in enumerate(TEAM):
        uri = photo_uri(i)
        ph = (f'<div class="ph has-photo" style="--photo:url({uri});background-size:cover;background-position:center top"></div>'
              if uri else '<div class="ph" data-label="รูปสมาชิก"></div>')
        cards.append(f'    <div class="card glow jcard in" style="--i:{3 + i}">{ph}<div class="nm">{name}</div><div class="rl">{role}</div></div>')
    return '\n'.join(cards)


# Khonnai brand: blue #1650D7 and orange #FF8032 (sampled from the logo sheet).
# Old violet/purple values of the U-Hackathon theme -> blue, its magenta accent -> orange.
THEME_SWAPS = [
    (r'rgba\(\s*118,\s*96,\s*255', 'rgba(61,110,245'),
    (r'rgba\(\s*196,\s*110,\s*255', 'rgba(255,128,50'),
    (r'rgba\(\s*155,\s*140,\s*255', 'rgba(130,165,255'),
    (r'rgba\(\s*150,\s*140,\s*255', 'rgba(125,160,255'),
    (r'rgba\(\s*150,\s*130,\s*255', 'rgba(120,155,255'),
    (r'rgba\(\s*140,\s*110,\s*255', 'rgba(110,145,255'),
    (r'rgba\(\s*120,\s*104,\s*255', 'rgba(90,130,255'),
    (r'rgba\(\s*180,\s*165,\s*255', 'rgba(160,190,255'),
    (r'rgba\(\s*220,\s*210,\s*255', 'rgba(210,225,255'),
    (r'rgba\(\s*80,\s*60,\s*220', 'rgba(30,80,215'),
    (r'rgba\(\s*145,\s*54,\s*224', 'rgba(230,110,40'),
    (r'rgba\(\s*40,\s*38,\s*92', 'rgba(24,40,96'),
    (r'--tc: 196, 110, 255', '--tc: 255, 128, 50'),
    (r'#7660ff', '#3d6ef5'), (r'#6b45eb', '#2457e6'), (r'#5b3fe6', '#1650d7'),
    (r'#8d7bff', '#6f97ff'), (r'#9b8cff', '#82a6ff'), (r'#b3a8ff', '#a9c1ff'),
    (r'#cfc8ff', '#d4e2ff'), (r'#9f8fff', '#7fa6ff'), (r'#c46eff', '#ff8032'),
    (r'#e2b0ff', '#ffc59c'), (r'#0b0d2a', '#07112e'),
    # icon circles, orange (w3) icons, avatars, bars and glows that still carried violet
    (r'#9d8dff', '#7fa6ff'), (r'#5a3fe0', '#1650d7'), (r'#9136e0', '#e0601a'),
    (r'#a24fe8', '#ff8a3d'), (r'#3a2a9e', '#c2410c'), (r'#4a33c8', '#1f4fd0'),
    (r'#5d43e8', '#2f5ae8'), (r'#c7bdff', '#bfd2ff'), (r'#c9bcff', '#bfd2ff'), (r'#8f7dff', '#6f97ff'),
    (r'#221940', '#14203f'), (r'#3a3192', '#1d3a92'), (r'#16153f', '#0f1a3f'),
    # silk background: body stays brand blue (blue mixed with orange turns muddy purple),
    # the bright ridges become orange; glass cube palette blue -> orange
    (r'violet=vec3\(\.42,\.27,\.92\), cyan=vec3\(\.43,\.84,1\.\)', 'violet=vec3(.09,.31,.84), cyan=vec3(1.,.5,.2)'),
    (r'c2=vec3\(\.47,\.36,1\.\),c3=vec3\(\.86,\.38,1\.\),c4=vec3\(1\.,\.5,\.78\)',
     'c2=vec3(.24,.42,1.),c3=vec3(1.,.5,.2),c4=vec3(1.,.68,.38)'),
    (r'vec3\(\.3,\.22,\.8\)\*\.05\+vec3\(\.5,\.4,1\.\)', 'vec3(.16,.3,.85)*.05+vec3(.4,.55,1.)'),
    (r'vec3\(\.42,\.3,1\.\)\*\.11', 'vec3(.24,.42,1.)*.11'),
]

TIMER_JS = '''  /* ---------- presentation timer: starts only when pressed (T or click), Y reset, ?limit=<minutes> turns it orange near the end ---------- */
  const T_PLAY = '<svg viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z" fill="#fff"/></svg>';
  const T_PAUSE = '<svg viewBox="0 0 24 24"><path d="M7.5 5.5h3v13h-3zM13.5 5.5h3v13h-3z" fill="#fff"/></svg>';
  const T_RESET = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12a8 8 0 1 0 2.4-5.7"/><path d="M4 4.5V10h5.5"/></svg>';
  const timer = document.createElement('div');
  timer.id = 'ptimer';
  timer.title = 'ปุ่มเริ่ม/หยุด หรือกด T · ปุ่มรีเซ็ต หรือกด Y';
  timer.innerHTML = '<i></i><b>00:00</b><button class="tb go" type="button"></button><button class="tb rs" type="button" aria-label="รีเซ็ต" title="รีเซ็ต (Y)">' + T_RESET + '</button>';
  $('.reveal .slides').appendChild(timer);
  const LIMIT = (+new URLSearchParams(location.search).get('limit') || 0) * 60000;
  let tStart = 0, tAcc = 0, tRun = false;
  const tNow = () => tAcc + (tRun ? Date.now() - tStart : 0);
  const tDraw = () => {
    const ms = tNow(), sec = Math.floor(ms / 1000);
    $('b', timer).textContent = String(Math.floor(sec / 60)).padStart(2, '0') + ':' + String(sec % 60).padStart(2, '0');
    timer.classList.toggle('run', tRun);
    const go = $('.go', timer), want = tRun ? 'pause' : 'play';
    if (go.dataset.s !== want) { go.dataset.s = want; go.innerHTML = tRun ? T_PAUSE : T_PLAY; go.setAttribute('aria-label', tRun ? 'หยุด' : 'เริ่ม'); go.title = (tRun ? 'หยุด' : 'เริ่ม') + ' (T)'; }
    timer.classList.toggle('warn', LIMIT > 0 && ms >= LIMIT - 60000 && ms < LIMIT);
    timer.classList.toggle('over', LIMIT > 0 && ms >= LIMIT);
  };
  const tToggle = () => { if (tRun) { tAcc += Date.now() - tStart; tRun = false; } else { tStart = Date.now(); tRun = true; } tDraw(); };
  const tReset = () => { tAcc = 0; tRun = false; tDraw(); }; // back to 00:00 and wait for start
  // buttons only; stopPropagation keeps the click from reaching reveal.js
  $('.go', timer).addEventListener('click', e => { e.stopPropagation(); tToggle(); e.currentTarget.blur(); });
  $('.rs', timer).addEventListener('click', e => { e.stopPropagation(); tReset(); e.currentTarget.blur(); });
  setInterval(tDraw, 250); tDraw();
  Reveal.addKeyBinding({ keyCode: 84, key: 'T', description: 'Timer: start / pause' }, tToggle);
  Reveal.addKeyBinding({ keyCode: 89, key: 'Y', description: 'Timer: reset' }, tReset);
'''

TIMER_CSS = '''/* presentation timer (top-right) */
#ptimer { position: absolute; right: var(--pad); top: 62px; z-index: 100; pointer-events: auto; display: flex; align-items: center; gap: 12px; padding: 10px 18px; border-radius: 100px; background: rgba(255,255,255,.06); border: 1px solid var(--line-2); font: 500 24px/1 "JetBrains Mono"; color: var(--ink-2); letter-spacing: .04em; transition: color .4s, background .4s, border-color .4s; }
#ptimer i { width: 10px; height: 10px; border-radius: 50%; background: var(--ink-4); }
#ptimer.run i { background: var(--yes); box-shadow: 0 0 10px var(--yes); }
#ptimer .tb { width: 40px; height: 40px; padding: 0; display: grid; place-items: center; border-radius: 50%; border: 1px solid var(--line-2); background: rgba(255,255,255,.08); cursor: pointer; transition: background .3s, border-color .3s; }
#ptimer .tb:hover { background: rgba(255,255,255,.16); }
#ptimer .tb svg { width: 20px; height: 20px; display: block; }
#ptimer .tb.go { background: rgba(61,110,245,.45); border-color: rgba(130,165,255,.6); }
#ptimer.run .tb.go { background: rgba(255,128,50,.35); border-color: var(--web3); }
#ptimer.warn { color: var(--web3); border-color: var(--web3); }
#ptimer.over { color: #fff; background: rgba(255,128,50,.35); border-color: var(--web3); animation: tpulse 1s ease-in-out infinite; }
@keyframes tpulse { 50% { opacity: .55; } }
html.reveal-print #ptimer { display: none; }
'''


def retheme(html):
    for pat, new in THEME_SWAPS:
        html, n = re.subn(pat, new, html)
        if n == 0:
            raise SystemExit(f'theme swap found nothing: {pat}')
    # gradient text runs brand blue -> orange (same angle and stops as the original white -> violet)
    html = replace_once(html, '.g { background: linear-gradient(100deg, #d4e2ff 0%, #7fa6ff 45%, #3d6ef5 100%);',
                        '.g { background: linear-gradient(100deg, #4f86ff 0%, #8f9bff 45%, #ff8032 100%);', 'gradient text')
    # the "> " of code labels picks up the orange accent
    html = replace_once(html, '.kick::before { content: "> "; color: var(--violet); }',
                        '.kick::before { content: "> "; color: var(--web3); }', 'kick accent')
    return html


def replace_once(html, old, new, label):
    if html.count(old) != 1:
        raise SystemExit(f'{label}: expected exactly one match, found {html.count(old)}')
    return html.replace(old, new)


def main():
    html = SRC.read_text(encoding='utf-8')
    logo = data_uri('khonnai-white.png', 'image/png')
    subs = {
        '{LOGO}': logo,
        '{PHONE}': data_uri('phone-stock.png', 'image/png'),
        '{PRODUCT}': data_uri('product3.png', 'image/png'),
        '{QR}': data_uri('qr.svg', 'image/svg+xml'),
        '{KICON}': data_uri('khonnai-k.png', 'image/png'),
        '{TEAM}': team_cards(),
    }
    body = '\n'.join(SLIDES)
    for k, v in subs.items():
        body = body.replace(k, v)

    # slides block: everything from the first section to the last one
    start = html.index('<div class="slides">') + len('<div class="slides">')
    end = html.rindex('</section>') + len('</section>')
    html = html[:start] + '\n' + body + '\n' + html[end:]

    html = re.sub(r'<title>.*?</title>', '<title>Khonnai · Pitch Deck · Milestone 2</title>', html, count=1, flags=re.S)

    # footer brand (built by the chrome script)
    html, n = re.subn(r'<div class="brand"><img class="uh-logo" src="data:image/webp;base64,[^"]+" alt="U-Hackathon"',
                      f'<div class="brand"><img class="uh-logo" src="{logo}" alt="Khonnai"', html)
    if n != 1:
        raise SystemExit(f'brand logo: found {n}')
    html = replace_once(html, '<span class="ev">Flow Summit</span>', '<span class="ev">Milestone 2 · กลุ่ม 3</span>', 'brand text')
    html = replace_once(html, 'const NSEC = 11;', 'const NSEC = 12;', 'section count')

    # prize-pool scene: read the two amounts from the slide instead of hard-coded prize values
    html = replace_once(html, 'const A = 1000000, B = 2500000,',
                        'const A = +s.dataset.ppA || 1000000, B = +s.dataset.ppB || 2500000,', 'pp amounts')

    # the build-start countdown slide is gone, so T / Y drive the presentation timer instead
    html, n = re.subn(r"  Reveal\.addKeyBinding\(\{ keyCode: 84, key: 'T'.*?\n  Reveal\.addKeyBinding\(\{ keyCode: 89, key: 'Y'.*?\n",
                      lambda m: TIMER_JS, html, count=1, flags=re.S)
    if n != 1:
        raise SystemExit('countdown key bindings not found')
    html = retheme(html)

    # u.bot mascot is u-topia branding: inject nothing
    html, n = re.subn(r'const LAYOUT = \[.*?\];\n', 'const LAYOUT = [];\n', html, count=1, flags=re.S)
    if n != 1:
        raise SystemExit('ubot layout not found')

    extra_css = '''<style>/* Khonnai: Thai glyphs drawn with Prompt inside the deck's Poppins / JetBrains Mono stacks */
@font-face{font-family:Poppins;font-weight:300;font-display:block;src:url(https://fonts.gstatic.com/s/prompt/v12/-W_8XJnvUD7dzB2Cy_gIfWMuQ5Q.woff2) format('woff2');unicode-range:U+0E01-0E5B,U+200C-200D,U+25CC}
@font-face{font-family:Poppins;font-weight:400;font-display:block;src:url(https://fonts.gstatic.com/s/prompt/v12/-W__XJnvUD7dzB2KdNodVkI.woff2) format('woff2');unicode-range:U+0E01-0E5B,U+200C-200D,U+25CC}
@font-face{font-family:Poppins;font-weight:500;font-display:block;src:url(https://fonts.gstatic.com/s/prompt/v12/-W_8XJnvUD7dzB2Ck_kIfWMuQ5Q.woff2) format('woff2');unicode-range:U+0E01-0E5B,U+200C-200D,U+25CC}
@font-face{font-family:Poppins;font-weight:600;font-display:block;src:url(https://fonts.gstatic.com/s/prompt/v12/-W_8XJnvUD7dzB2Cv_4IfWMuQ5Q.woff2) format('woff2');unicode-range:U+0E01-0E5B,U+200C-200D,U+25CC}
@font-face{font-family:Poppins;font-weight:700;font-display:block;src:url(https://fonts.gstatic.com/s/prompt/v12/-W_8XJnvUD7dzB2C2_8IfWMuQ5Q.woff2) format('woff2');unicode-range:U+0E01-0E5B,U+200C-200D,U+25CC}
@font-face{font-family:"JetBrains Mono";font-weight:400;font-display:block;src:url(https://fonts.gstatic.com/s/prompt/v12/-W__XJnvUD7dzB2KdNodVkI.woff2) format('woff2');unicode-range:U+0E01-0E5B,U+200C-200D,U+25CC}
@font-face{font-family:"JetBrains Mono";font-weight:500;font-display:block;src:url(https://fonts.gstatic.com/s/prompt/v12/-W_8XJnvUD7dzB2Ck_kIfWMuQ5Q.woff2) format('woff2');unicode-range:U+0E01-0E5B,U+200C-200D,U+25CC}
/* team grid with five cards */
.jgrid.five { grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 26px; }
.jgrid.five .jcard .nm { font-size: 26px; white-space: nowrap; }
.jgrid.five .jcard .rl { font-size: 20px; }
/* 5-year financials chart built from the podium bars */
.fin-v { position: absolute; text-align: center; font: 600 26px/1 Poppins; letter-spacing: -.01em; white-space: nowrap; }
.fin-v.pro { font: 500 20px/1 "JetBrains Mono"; color: var(--web3); }
.fin-y { position: absolute; top: 456px; text-align: center; }
.fin-y b { display: block; font: 500 26px/1 Poppins; }
.fin-y span { display: block; margin-top: 8px; font: 500 19px/1 "JetBrains Mono"; color: var(--ink-3); }
.pod .fin-base { position: absolute; left: 0; right: 0; bottom: 0; height: 1px; background: var(--line-2); }
''' + TIMER_CSS + '''</style>
</head>'''
    head_end = html.index('</head>')  # the first one; a later copy sits inside a script string
    html = html[:head_end] + extra_css + html[head_end + len('</head>'):]

    OUT.write_text(html, encoding='utf-8')
    print(f'wrote {OUT} ({OUT.stat().st_size / 1e6:.2f} MB, {body.count("<section")} slides)')


if __name__ == '__main__':
    main()
