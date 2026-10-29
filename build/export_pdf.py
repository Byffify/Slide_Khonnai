"""Capture every slide of khonnai-pitch.html in its final state and save khonnai-pitch.pdf.

Uses the installed Google Chrome through Playwright (no browser download):
    python build/export_pdf.py
Each slide is shown with all its click-steps revealed and given time for its
animations to finish; the presenter timer and reveal.js controls are hidden.
"""
import io
from pathlib import Path

import img2pdf
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
DECK = ROOT / 'khonnai-pitch.html'
OUT = ROOT / 'khonnai-pitch.pdf'
SETTLE_MS = 6000  # longest entrance animation (The Ask count-up and bar) finishes in ~5 s


def main():
    pages = []
    with sync_playwright() as p:
        browser = p.chromium.launch(channel='chrome', args=['--enable-unsafe-swiftshader', '--use-angle=swiftshader'])
        page = browser.new_page(viewport={'width': 1920, 'height': 1080}, device_scale_factor=1.5)
        page.goto(DECK.as_uri())
        page.wait_for_function('window.Reveal && Reveal.isReady()')
        page.add_style_tag(content='#ptimer, .reveal .controls { display: none !important; }')
        page.evaluate('document.fonts.ready')
        total = page.evaluate('Reveal.getTotalSlides()')
        for i in range(total):
            steps = page.evaluate(f'Reveal.getSlides()[{i}].querySelectorAll(".fragment").length')
            page.evaluate(f'Reveal.slide({i}, 0, {steps - 1 if steps else -1})')
            page.wait_for_timeout(SETTLE_MS)
            png = page.screenshot(type='png')
            jpg = io.BytesIO()
            Image.open(io.BytesIO(png)).convert('RGB').save(jpg, 'JPEG', quality=92)
            pages.append(jpg.getvalue())
            print(f'slide {i + 1}/{total} ({steps} steps)')
        browser.close()
    layout = img2pdf.get_layout_fun((img2pdf.mm_to_pt(338.67), img2pdf.mm_to_pt(190.5)))  # 16:9, PowerPoint widescreen size
    OUT.write_bytes(img2pdf.convert(pages, layout_fun=layout))
    print(f'wrote {OUT} ({OUT.stat().st_size / 1e6:.1f} MB, {len(pages)} pages)')


if __name__ == '__main__':
    main()
