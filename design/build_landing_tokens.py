"""Landing page mock-up: tokens, interaction states and file hygiene (run last).

Usage: python -I design/build_landing_tokens.py   (after build_landing_v2.py, build_landing_v2.py menus and
build_landing_mobile.py)
- creates the "khonnai" colour variables and binds them to every matching solid colour in the landing frames
- rebuilds "Landing v2 — Tokens & States": colour swatches, the type scale (saved as text styles) and
  default / hover / pressed / focus / disabled for each interactive element
- moves the superseded section frames (old navbar and Hero 41) to an "Archive" page
Exports design/preview/landing/Landing v2 — Tokens & States.png.
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from build_landing_navbar import (BLUE, BLUE_50, F, F_TH, HOVER, INK, MUTED, PREVIEW, WHITE, box, col,  # noqa: E402
                                  export_frame, icon, one, row, run, txt)
from build_landing_v2 import ARROW, CHEVRON_DOWN, CHEVRON_RIGHT, CHEVRON_UP, FAQ_BG, X, stroke, th  # noqa: E402

NAME = "Landing v2 — Tokens & States"
LANDING = ["Landing v2 — Desktop", "Landing v2 — Features menu", "Landing v2 — Services menu",
           "Landing v2 — Language menu", "Landing v2 — Mobile", "Landing v2 — Mobile menu",
           "Landing v2 — Mobile sticky", NAME]
ARCHIVE = ["Navbar — Default", "Navbar — Features open", "Hero — Default"]
COLLECTION = "khonnai"
# one brand blue for the landing (#1650D7, as in the pitch deck); the app screens' #1F56D6 is the app's own token
TOKENS = [
    ("color/brand/blue", "#1650D7"), ("color/brand/blue-dark", "#1D3FA6"), ("color/brand/blue-tint", "#EEF3FD"),
    ("color/brand/orange", "#FF8032"), ("color/brand/orange-tint", "#FFF3E8"), ("color/brand/orange-text", "#9A4A0C"),
    ("color/accent/headline", "#FFD2B0"), ("color/text/ink", "#0F172A"), ("color/text/muted", "#475569"),
    ("color/surface/page", "#FFFFFF"), ("color/surface/subtle", "#F8FAFC"), ("color/surface/hover", "#F1F5F9"),
    ("color/surface/faq", "#F5F5F5"), ("color/border/default", "#E2E8F0"), ("color/border/strong", "#CBD5E1"),
]
TYPE_SCALE = [  # name, size, style, line height, sample
    ("Display", 64, "Bold", "125%", "สต็อก การจอง และบิล"), ("H2", 48, "Bold", "130%", "เลือกแพ็กเกจที่เหมาะกับร้าน"),
    ("H2 / Mobile", 28, "Bold", "135%", "คำถามที่พบบ่อย"), ("H3", 24, "Bold", "140%", "ออกบิลใน 3 ขั้น"),
    ("Body L", 20, "Regular", "165%", "จัดการสินค้าแยกตามรุ่น สี และไซซ์"),
    ("Body", 16, "Regular", "165%", "เลือกสินค้า ยืนยันออเดอร์ แล้วได้บิลเงินสด"),
    ("Label", 16, "Bold", "150%", "เริ่มใช้ฟรี"), ("Caption", 14, "Regular", "150%", "ราคาอยู่ระหว่างทดสอบกับร้านนำร่อง"),
]
BLUE_HOVER, BLUE_PRESSED = "#1243B8", "#0F3A9E"
DISABLED_BG, DISABLED_FG = "#E2E8F0", "#94A3B8"
STATES = ["Default", "Hover", "Pressed", "Focus", "Disabled"]


def hexof(paint):
    """'#RRGGBB' for an opaque solid paint from selection.colors, else None."""
    if not isinstance(paint, dict) or paint.get("type", "solid") != "solid" or paint.get("opacity", 1) < 1:
        return None
    c = paint.get("color")
    if isinstance(c, str):
        c = c.upper()
        return c[:7] if len(c) == 7 or c.endswith("FF") else None
    if isinstance(c, dict) and c.get("a", 1) >= 1:
        return "#%02X%02X%02X" % tuple(round(c[k] * 255) for k in "rgb")
    return None


def frame_id(name):
    for i in run([{"command": "select.byName", "params": {"query": name}}])[0]["selection"]:
        if one("node.get", {"id": i}).get("name") == name:
            return i
    return None


# ---------------------------------------------------------------- variables
def variables():
    listed = one("variable.list", {})
    have = {v["name"] for v in listed["variables"]}
    if COLLECTION not in {c["name"] for c in listed["collections"]}:
        one("variable.createCollection", {"name": COLLECTION})
    run([{"command": "variable.create", "params": {"collection": COLLECTION, "name": n, "type": "color", "value": v}}
         for n, v in TOKENS if n not in have] or [{"command": "variable.list", "params": {}}])


def bind():
    by_hex = {v: n for n, v in reversed(TOKENS)}
    bound = 0
    for name in LANDING:
        fid = frame_id(name)
        if fid is None:
            continue
        cmds = []
        for entry in one("selection.colors", {"ids": [fid]})["colors"]:
            token = by_hex.get(hexof(entry["paint"]) or "")
            if token:
                cmds.append({"command": "selection.bindColorVariable",
                             "params": {"targets": entry["targets"], "variable": token}})
        if cmds:
            run(cmds)
            bound += len(cmds)
    print("bound colour groups:", bound)


# ---------------------------------------------------------------- states frame
def ring(color=BLUE, gap=WHITE):
    """Focus ring: 2px gap in the surface colour, then 2px ring."""
    return [{"type": "dropShadow", "color": color, "offset": [0, 0], "radius": 0, "spread": 4},
            {"type": "dropShadow", "color": gap, "offset": [0, 0], "radius": 0, "spread": 2}]


def button(parent, label, fill, fg, border=None, effects=None, arrow=False):
    b = row(parent, "Button", gap=8, padding=[0, 24, 0, 24], cornerRadius=999, height=48, sizingV="fixed",
            fill=fill, effects=effects or [])
    if border:
        stroke(b, border)
    th(b, label, 16, "Bold", fg)
    if arrow:
        icon(b, ARROW, 18, fg)


def state_row(parent, title, note, cells, dark=False):
    r = col(parent, "Row / " + title, gap=12, sizingH="fill", clip=False)
    head = row(r, "Head", gap=12)
    txt(head, title, 18, "Bold", INK)
    th(head, note, 14, "Regular", MUTED)
    strip = row(r, "States", gap=24, padding=24, cornerRadius=20, sizingH="fill", crossAlign="min",
                fill=BLUE if dark else "#F8FAFC", clip=False)   # clipping would cut the focus rings
    for state, build in zip(STATES, cells):
        c = col(strip, "State / " + state, gap=12, width=230, sizingH="fixed", clip=False)
        txt(c, state, 14, "Medium", "#FFFFFFCC" if dark else MUTED)
        if build:
            build(c)
        else:
            th(c, "—", 16, "Regular", "#FFFFFFCC" if dark else MUTED)


def nav_item(parent, fill=None, color=INK, chevron=CHEVRON_DOWN, effects=None):
    it = row(parent, "Menu item", gap=4, padding=[10, 12, 10, 12], cornerRadius=999, minHeight=44, fill=fill,
             effects=effects or [])
    th(it, "ฟีเจอร์", 16, "Regular", color)
    icon(it, chevron, 16, color if color != INK else MUTED)


def faq_item(parent, fill=FAQ_BG, open_=False, effects=None):
    it = col(parent, "FAQ item", gap=8, padding=[16, 18, 16, 18], cornerRadius=16, fill=fill, width=230,
             sizingH="fixed", effects=effects or [])
    h = row(it, "Question", gap=8, mainAlign="spaceBetween", sizingH="fill")
    th(h, "ต้องติดตั้งแอปไหม?", 15, "Bold", INK)
    icon(h, CHEVRON_DOWN if open_ else CHEVRON_RIGHT, 16, INK)
    if open_:
        th(it, "ไม่ต้อง ใช้ผ่านเว็บ\nบนมือถือได้ทันที", 14, "Regular", MUTED, lineHeight="160%")


def link(parent, color=MUTED, underline=False, effects=None, fill=None):
    r = row(parent, "Link", padding=[6, 4, 6, 4], cornerRadius=6, minHeight=44, fill=fill, effects=effects or [])
    t = th(r, "ราคา", 15, "Regular", color)
    if underline:
        one("node.set", {"id": t, "textDecoration": "underline"})


def states(parent):
    s = col(parent, "Interaction states", gap=32, sizingH="fill")
    txt(s, "Interaction states", 32, "Bold", INK)
    th(s, "Hover ใช้เฉพาะอุปกรณ์ที่มีเมาส์ · Pressed แทน hover บนจอสัมผัส · Focus ring ห่าง 2px หนา 2px "
          "(ขาวเมื่ออยู่บนพื้นน้ำเงิน) · เปลี่ยนสถานะ 150–200ms ease-out", 15, "Regular", MUTED)
    state_row(s, "Primary button", "พื้นน้ำเงิน", [
        lambda c: button(c, "เริ่มใช้ฟรี", BLUE, WHITE, arrow=True),
        lambda c: button(c, "เริ่มใช้ฟรี", BLUE_HOVER, WHITE, arrow=True),
        lambda c: button(c, "เริ่มใช้ฟรี", BLUE_PRESSED, WHITE, arrow=True),
        lambda c: button(c, "เริ่มใช้ฟรี", BLUE, WHITE, effects=ring(), arrow=True),
        lambda c: button(c, "เริ่มใช้ฟรี", DISABLED_BG, DISABLED_FG, arrow=True)])
    state_row(s, "Outline button", "บนพื้นสว่าง", [
        lambda c: button(c, "คุยทาง LINE", WHITE, INK, "#CBD5E1"),
        lambda c: button(c, "คุยทาง LINE", HOVER, INK, "#CBD5E1"),
        lambda c: button(c, "คุยทาง LINE", "#E2E8F0", INK, "#94A3B8"),
        lambda c: button(c, "คุยทาง LINE", WHITE, INK, "#CBD5E1", effects=ring()),
        lambda c: button(c, "คุยทาง LINE", WHITE, DISABLED_FG, DISABLED_BG)])
    state_row(s, "Buttons on blue", "Hero และ CTA ปิดท้าย", [
        lambda c: (button(c, "เริ่มใช้ฟรี", WHITE, BLUE, arrow=True), button(c, "คุยทาง LINE", None, WHITE, WHITE)),
        lambda c: (button(c, "เริ่มใช้ฟรี", BLUE_50, BLUE, arrow=True), button(c, "คุยทาง LINE", "#FFFFFF1F", WHITE, WHITE)),
        lambda c: (button(c, "เริ่มใช้ฟรี", "#D9E4FA", BLUE_PRESSED, arrow=True),
                   button(c, "คุยทาง LINE", "#FFFFFF33", WHITE, WHITE)),
        lambda c: (button(c, "เริ่มใช้ฟรี", WHITE, BLUE, effects=ring(WHITE, BLUE), arrow=True),
                   button(c, "คุยทาง LINE", BLUE, WHITE, WHITE, effects=ring(WHITE, BLUE))),
        None], dark=True)
    state_row(s, "Nav item", "เมนูบนแถบ (Open = dropdown เปิด)", [
        lambda c: nav_item(c),
        lambda c: nav_item(c, fill=HOVER),
        lambda c: nav_item(c, fill=HOVER, color=BLUE, chevron=CHEVRON_UP),
        lambda c: nav_item(c, fill=WHITE, effects=ring()),   # a ring needs a filled shape to follow
        None])
    state_row(s, "FAQ item", "Pressed = เปิดคำตอบ", [
        lambda c: faq_item(c),
        lambda c: faq_item(c, fill="#EDEDED"),
        lambda c: faq_item(c, open_=True),
        lambda c: faq_item(c, effects=ring()),
        None])
    state_row(s, "Text link", "footer และลิงก์ในเนื้อหา", [
        lambda c: link(c),
        lambda c: link(c, INK, True),
        lambda c: link(c, BLUE, True),
        lambda c: link(c, effects=ring(), fill="#F8FAFC"),
        None])


def swatches(parent):
    s = col(parent, "Colour tokens", gap=16, sizingH="fill")
    txt(s, "Colour tokens", 32, "Bold", INK)
    grid = row(s, "Swatches", gap=16, wrap=True, sizingH="fill", crossGap=16)
    for name, value in TOKENS:
        c = col(grid, name, gap=8, width=176, sizingH="fixed")
        chip = box(c, "Swatch", 176, 72, cornerRadius=14, fill=value)
        stroke(chip)
        txt(c, name.replace("color/", ""), 14, "Bold", INK)
        txt(c, value, 14, "Regular", MUTED)


def type_scale(parent):
    s = col(parent, "Type scale", gap=16, sizingH="fill")
    txt(s, "Type scale", 32, "Bold", INK)
    th(s, f"Thai: {F_TH} (web font) · Latin: {F}", 15, "Regular", MUTED)
    specimens = []
    for name, size, style, lh, sample in TYPE_SCALE:
        r = row(s, "Type / " + name, gap=24, crossAlign="center", sizingH="fill")
        lab = col(r, "Label", gap=2, width=200, sizingH="fixed")
        txt(lab, name, 15, "Bold", INK)
        txt(lab, f"{size}px · {style} · {lh}", 14, "Regular", MUTED)
        specimens.append((name, th(r, sample, size, style, INK, lineHeight=lh)))
    return specimens


def text_styles(specimens):
    listed = one("style.list", {})
    have = {st.get("name") for st in (listed if isinstance(listed, list) else listed.get("styles", []))}
    run([{"command": "style.create", "params": {"type": "text", "name": "Landing/" + name, "from": nid}}
         for name, nid in specimens if "Landing/" + name not in have] or [{"command": "style.list", "params": {}}])


def tokens_frame():
    old = frame_id(NAME)
    if old:
        run([{"command": "edit.delete", "params": {"ids": [old]}}])
    f = box(None, NAME, 1440, 100, layout="vertical", gap=64, padding=[80, 80, 80, 80], sizingH="fixed",
            sizingV="hug", fill=WHITE)
    one("node.set", {"id": f, "x": X, "y": 6600})
    swatches(f)
    specimens = type_scale(f)
    states(f)
    text_styles(specimens)


# ---------------------------------------------------------------- archive
def archive():
    ids = [i for i in (frame_id(n) for n in ARCHIVE) if i]
    if not ids:
        return
    page = one("page.add", {"name": "Archive — superseded sections"})["id"]
    one("node.reparent", {"ids": ids, "parent": page})
    one("page.select", {"index": 0})   # page.add makes the new page current, and the file remembers it
    print("archived", ids)


def main():
    variables()
    tokens_frame()
    bind()
    archive()
    export_frame(NAME, os.path.join(PREVIEW, NAME + ".png"))


if __name__ == "__main__":
    main()
