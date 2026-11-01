"""Landing page mock-up v2, mobile (375): the desktop page re-composed for a phone, not scaled.

Usage: python -I design/build_landing_mobile.py   (after build_landing_v2.py)
Adds (or rebuilds) "Landing v2 — Mobile" and "Landing v2 — Mobile menu" in design/khonnai-landing.figcraft
and exports their PNGs to design/preview/landing/.

Same sections and order as the desktop frame. What changes on a phone:
  nav            → pill with logo, TH switcher and a 44px menu button; the menu is a full-screen sheet
  hero           → copy first, full-width stacked CTAs, one phone with two toasts, pilot card below
  bento / plans  → single column; the three bill steps run vertically
  type           → nothing under 14px, body 16px; Thai lines are broken by hand so phrases stay whole
Audit fixes (shared with desktop): outlined secondary hero button instead of glass (contrast), 44px footer
link rows, no section eyebrows, Thai CTAs inside the page (the nav keeps its English labels).
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from build_landing_hero import phone  # noqa: E402
from build_landing_navbar import (BLUE, BLUE_50, BORDER, HOVER, ICON, INK, LOGO, MUTED, PREVIEW, WHITE,  # noqa: E402
                                  box, col, export_frame, icon, one, row, run, txt)
from build_landing_v2 import (BAR, BAR_ON_BLUE, BRAND_GRADIENT, CHECK, CHEVRON_DOWN, CHEVRON_RIGHT, FAQ_BG,  # noqa: E402
                              HEADLINE_ACCENT, INCLUDED, MENU_ICONS, ORANGE, ORANGE_50, ORANGE_700, PLANS,
                              POINT_PATHS, SHADOW, SURFACE, X, center, glow, hero_chip, lang_switch, pill, sellable,
                              stock_matrix, stroke, th)

NAME = "Landing v2 — Mobile"
MENU_NAME = "Landing v2 — Mobile menu"
MX = X + 1540 + 1540   # right of the dropdown frames
W = 375
PAD = 20
INNER = W - 2 * PAD
MENU_ICON = "M4 6h16 M4 12h16 M4 18h16"
CLOSE_ICON = "M18 6L6 18 M6 6l12 12"


def section(parent, name, gap=32, pad=(64, PAD, 64, PAD), **props):
    return box(parent, name, W, 100, **{"layout": "vertical", "gap": gap, "padding": list(pad),
                                        "crossAlign": "center", "sizingH": "fixed", "sizingV": "hug",
                                        "fill": WHITE, **props})


def wide(nid):
    one("node.set", {"id": nid, "sizingH": "fill", "mainAlign": "center"})
    return nid


def heading(parent, title, body=None, align="center"):
    h = col(parent, "Heading", gap=12, crossAlign="center" if align == "center" else "min", sizingH="fill")
    write = center if align == "center" else th
    write(h, title, 28, "Bold", INK, lineHeight="135%")
    if body:
        write(h, body, 16, "Regular", MUTED, lineHeight="165%")


# ---------------------------------------------------------------- nav
def nav(parent):
    n = box(parent, "Navbar / mobile", W - 32, 60, layout="horizontal", mainAlign="spaceBetween",
            crossAlign="center", padding=[0, 8, 0, 18], cornerRadius=999, fill=WHITE, effects=SHADOW,
            sizingH="fixed", sizingV="fixed")
    logo = one("image.place", {"path": LOGO, "parent": n, "width": 110, "height": 24, "mode": "fit"})["id"]
    one("node.set", {"id": logo, "name": "Logo / khonnai"})
    right = row(n, "Actions", gap=6)
    lang_switch(right)
    menu = box(right, "Menu button", 44, 44, layout="horizontal", mainAlign="center", crossAlign="center",
               cornerRadius=999, fill=BLUE)
    icon(menu, MENU_ICON, 24, WHITE)
    return n


# ---------------------------------------------------------------- hero
def pilot(parent):
    c = col(parent, "Card / ร้านนำร่อง", gap=14, padding=20, cornerRadius=24, fill=WHITE, effects=SHADOW,
            width=INNER, sizingH="fixed")
    top = row(c, "Head", gap=8)
    icon(top, CHECK, 20, BLUE)
    th(top, "ทดสอบกับร้านนำร่อง · 28 ต.ค. 2569", 14, "Bold", BLUE)
    stats = row(c, "Stats", gap=8, sizingH="fill")
    for big, small in (("1 ร้าน", "ร้านนำร่อง\nทดสอบจริง"), ("30 นาที", "เพิ่มสต็อก\nออกบิลครบ"),
                       ("7 ข้อ", "ข้อค้นพบ\nไปปรับ UX")):
        s = col(stats, "Stat", gap=4, padding=12, cornerRadius=16, fill=SURFACE, sizingH="fill")
        th(s, big, 20, "Bold", INK)
        th(s, small, 14, "Regular", MUTED, lineHeight="145%")


def hero(parent):
    h = box(parent, "Hero", W, 100, layout="vertical", gap=0, padding=[12, PAD, 48, PAD], crossAlign="center",
            sizingH="fixed", sizingV="hug", clip=True, fills=[{"type": "linearGradient", "stops": BRAND_GRADIENT}])
    nav(h)
    copy = col(h, "Copy", gap=20, crossAlign="center", paddingTop=44, paddingBottom=12, sizingH="fill")
    head = col(copy, "Headline", gap=0, crossAlign="center")
    center(head, "สต็อก การจอง และบิล", 34, "Bold", WHITE, lineHeight="130%")
    center(head, "จบในข้อมูลชุดเดียว", 34, "Bold", HEADLINE_ACCENT, lineHeight="130%")
    center(copy, "จัดการสินค้าแยกตามรุ่น สี และไซซ์\nตรวจของพร้อมขาย บันทึกการจอง\nและออกบิลจากข้อมูลชุดเดียวกัน",
           17, "Regular", WHITE, lineHeight="160%")
    ctas = col(copy, "CTAs", gap=12, sizingH="fill", paddingTop=4)
    wide(pill(ctas, "เริ่มใช้ฟรี", "white", 52, arrow=True))
    wide(pill(ctas, "นัดดูเดโม", "outline-light", 52))
    center(copy, "ฟรี 20 รหัสสินค้า · 50 บิล/เดือน", 15, "Regular", WHITE)
    shot = box(h, "Product shot", INNER, 460, clip=False)   # let the glows bleed past the box
    glow(shot, -80, 200, 300, 300, ORANGE, 0.55, 90)
    glow(shot, 160, -40, 260, 220, "#7FA8FF", 0.6, 90)
    phone(shot, "home", 430, 70, 16, "หน้าโฮม")
    hero_chip(shot, -8, 96, "ออกบิลแล้ว", "ตัดสต็อก 5 แพ็ก", "#16A34A")
    hero_chip(shot, 160, 330, "รับของแล้ว", "+ ฿1,160", ORANGE)
    pilot(h)


def proof(parent):
    s = section(parent, "Proof line", pad=(24, PAD, 8, PAD))
    r = row(s, "Line", gap=10, crossAlign="min")
    icon(r, CHECK, 20, BLUE)
    th(r, "ออกแบบจากการทดสอบ\nกับร้านค้าส่งนำร่องจริง", 16, "Bold", INK, lineHeight="150%")


# ---------------------------------------------------------------- overview
def card(parent, title, body, visual_h):
    c = col(parent, "Card / " + title, gap=0, cornerRadius=24, fill=SURFACE, width=INNER, sizingH="fixed",
            clip=True)
    stroke(c)
    v = box(c, "Visual", INNER, visual_h, layout="horizontal", mainAlign="center", crossAlign="center",
            sizingH="fill", sizingV="fixed")
    t = col(c, "Text", gap=8, padding=[4, 24, 24, 24], sizingH="fill")
    th(t, title, 20, "Bold", INK)
    th(t, body, 16, "Regular", MUTED, lineHeight="160%")
    return v


def steps(parent):
    s = col(parent, "Steps", gap=8, crossAlign="center")
    for i, label in enumerate(("เลือกสินค้า", "ยืนยันออเดอร์", "ได้บิลเงินสด")):
        st = row(s, "Step " + str(i + 1), gap=10, padding=[10, 18, 10, 10], cornerRadius=999, width=220,
                 sizingH="fixed", fill=BLUE if i == 2 else WHITE)
        if i < 2:
            stroke(st)
        n = box(st, "Number", 32, 32, layout="horizontal", mainAlign="center", crossAlign="center",
                cornerRadius=999, fill=WHITE if i == 2 else BLUE_50)
        txt(n, str(i + 1), 15, "Bold", BLUE)
        th(st, label, 16, "Bold", WHITE if i == 2 else INK)
        if i < 2:
            arrow = icon(s, "M12 5v14 M6 13l6 6 6-6", 18, MUTED)
            one("node.set", {"id": arrow, "name": "Arrow"})


def overview(parent):
    s = section(parent, "Overview", gap=24)
    heading(s, "ข้อมูลชุดเดียว\nใช้ได้ทั้งสต็อก จอง และบิล",
            "ไม่ต้องจดหลายเล่ม ไม่ต้องเช็กของซ้ำ\nขั้นตอนสั้น อ่านง่ายบนมือถือ")
    stock_matrix(card(s, "สต็อกแยกรุ่น สี และไซซ์", "เห็นทันทีว่าไซซ์ไหน สีไหน\nเหลือกี่แพ็ก ตัวไหนต้องเติม", 230))
    steps(card(s, "ออกบิลใน 3 ขั้น", "ได้บิลตามแบบฟอร์มของร้าน\nสต็อกถูกตัดทันทีที่ยืนยัน", 250))
    v = card(s, "ใบจองที่กันสต็อกไว้ให้", "จองจากหน้าร้านหรือ LINE\nกดรับของแล้วจึงออกบิล ไม่ตัดซ้ำ", 250)
    p, _ = phone(v, "reserve", 226, 0, 0, "การจอง")
    one("node.set", {"id": p, "absolute": True, "x": round((INNER - 110) / 2), "y": 24})
    sellable(card(s, "ไม่ขายเกินของที่มี", "ยืนยันบิลได้เมื่อของพร้อมขายพอ\nกันขายชิ้นสุดท้ายซ้ำ", 200))


# ---------------------------------------------------------------- easy to use
POINTS = [("หน้าโฮมสรุปร้านในจอเดียว", "รายได้วันนี้ ของรอรับ และของที่ต้องเติม\nพร้อมปุ่มลัดออกบิล ดูสต็อก และจอง", "home"),
          ("ตัวอักษรใหญ่ อ่านง่ายวัย 40+", None, "type"), ("เพิ่มรุ่นใหม่ได้ในหน้าเดียว", None, "package"),
          ("ใช้ผ่านเว็บ ไม่ต้องติดตั้ง", None, "smartphone"), ("บันทึกบิลเป็น PDF", None, "file")]


def easy(parent):
    s = section(parent, "Easy to use", gap=24, pad=(32, PAD, 64, PAD))
    heading(s, "ขั้นตอนสั้น ตัวใหญ่\nเจ้าของร้านใช้เองได้ทุกวัน", align="left")
    lst = col(s, "Points", gap=4, sizingH="fill")
    for title, desc, key in POINTS:
        p = row(lst, "Point / " + title, gap=12, padding=[14, 14, 14, 14], cornerRadius=16, sizingH="fill",
                crossAlign="min", fill=HOVER if desc else None, minHeight=52)
        ic = box(p, "Icon", 36, 36, layout="horizontal", mainAlign="center", crossAlign="center", cornerRadius=10,
                 fill=BLUE_50 if desc else None)
        icon(ic, POINT_PATHS[key], 24, BLUE if desc else MUTED)
        t = col(p, "Text", gap=6, paddingTop=6)
        th(t, title, 16, "Bold", INK if desc else MUTED)
        if desc:
            th(t, desc, 15, "Regular", MUTED, lineHeight="160%")
    panel = box(s, "Panel", INNER, 380, cornerRadius=24, clip=True,
                fills=[{"type": "linearGradient", "stops": [BLUE_50, "#F4ECFA", ORANGE_50], "from": [0, 0], "to": [1, 1]}])
    one("node.create", {"type": "ellipse", "parent": panel, "x": 38, "y": 40, "width": 260, "height": 260,
                        "name": "Backdrop", "props": {"fill": "#FFFFFF99"}})
    phone(panel, "home", 400, 92, 36, "หน้าโฮม")
    for (label, value, color), (x, y) in zip((("รอรับของ", "3 ออเดอร์", BLUE), ("ต้องเติม", "25 แพ็ก", ORANGE)),
                                             ((12, 96), (196, 250))):
        c = col(panel, "Chip / " + label, gap=2, padding=[10, 14, 10, 14], cornerRadius=16, fill=WHITE,
                effects=SHADOW)
        one("node.set", {"id": c, "x": x, "y": y})
        th(c, label, 14, "Regular", MUTED)
        v = row(c, "Value", gap=6)
        box(v, "Dot", 8, 8, cornerRadius=999, fill=color)
        th(v, value, 17, "Bold", INK)
    wide(pill(s, "ดูฟีเจอร์ทั้งหมด", "primary", 52, arrow=True))


# ---------------------------------------------------------------- pricing
def meter(parent, label, value, max_value, dark, width):
    m = col(parent, "Meter / " + label, gap=8, sizingH="fill")
    top = row(m, "Label", gap=8, mainAlign="spaceBetween", sizingH="fill")
    th(top, label, 14, "Regular", "#FFFFFFCC" if dark else MUTED)
    txt(top, f"{value:,}", 15, "Bold", WHITE if dark else INK)
    track = box(m, "Track", width, 8, cornerRadius=999, fill="#FFFFFF33" if dark else "#E2E8F0")
    box(track, "Bar", max(12, round(width * value / max_value)), 8, cornerRadius=999,
        fills=BAR_ON_BLUE if dark else BAR)


def plan(parent, p, featured):
    name, price, audience, skus, bills, cta, kind = p
    fg, sub = (WHITE, "#FFFFFFCC") if featured else (INK, MUTED)
    look = ({"fills": [{"type": "linearGradient", "stops": ["#1650D7", "#1D3FA6"], "from": [0, 0], "to": [1, 1]}]}
            if featured else {"fill": WHITE})
    c = col(parent, "Plan / " + name, gap=20, padding=24, cornerRadius=24, width=INNER, sizingH="fixed",
            clip=True, effects=SHADOW, **look)
    if featured:
        glow(c, 180, -110, 220, 200, ORANGE, 0.7, 80)
    else:
        stroke(c)
    head = row(c, "Head", gap=10, mainAlign="spaceBetween", sizingH="fill")
    t = col(head, "Name", gap=2)
    txt(t, name, 20, "Bold", fg)
    th(t, audience, 15, "Regular", sub)
    if featured:
        tag = row(head, "Recommended", padding=[4, 12, 4, 12], cornerRadius=999, fill=ORANGE)
        th(tag, "แนะนำ", 14, "Bold", INK)
    pr = row(c, "Price", gap=8, crossAlign="baseline")
    txt(pr, price, 44, "Bold", fg)
    th(pr, "บาท / เดือน", 16, "Regular", sub)
    ms = col(c, "Limits", gap=14, sizingH="fill")
    meter(ms, "รหัสสินค้า", skus, 1000, featured, INNER - 48)
    meter(ms, "บิลต่อเดือน", bills, 2000, featured, INNER - 48)
    inc = col(c, "Included", gap=8)
    for item in INCLUDED:
        r = row(inc, "Item", gap=10)
        icon(r, CHECK, 20, "#FFD2B0" if featured else BLUE)
        th(r, item, 15, "Regular", fg)
    wide(pill(c, cta, kind, 52))


def pricing(parent):
    s = section(parent, "Pricing", gap=24, clip=True,
                fills=[{"type": "linearGradient", "stops": [WHITE, "#F1F5FE", "#FFF4EA"]}])
    glow(s, -140, 500, 300, 300, "#BFD0F7", 0.7, 100)
    glow(s, 220, 1300, 300, 300, "#FFD2B0", 0.8, 100)
    heading(s, "เลือกแพ็กเกจที่เหมาะกับร้าน", "เริ่มฟรี แล้วค่อยอัปเกรดเมื่อร้านโตขึ้น\nทุกแพ็กเกจใช้ฟีเจอร์หลักได้ครบ")
    toggle = row(s, "Billing toggle", gap=4, padding=4, cornerRadius=999, fill=WHITE)
    stroke(toggle)
    on = row(toggle, "Monthly", padding=[0, 20, 0, 20], cornerRadius=999, height=44, sizingV="fixed", fill=INK)
    th(on, "รายเดือน", 15, "Bold", WHITE)
    off = row(toggle, "Yearly", gap=8, padding=[0, 14, 0, 20], cornerRadius=999, height=44, sizingV="fixed")
    th(off, "รายปี", 15, "Bold", MUTED)
    save = row(off, "Save", padding=[2, 8, 2, 8], cornerRadius=999, fill=ORANGE_50)
    th(save, "ลด 10%", 14, "Bold", ORANGE_700)
    cards = col(s, "Plans", gap=16, clip=False)
    for i, p in enumerate(PLANS):
        plan(cards, p, i == 1)
    center(s, "* ราคาอยู่ระหว่างทดสอบกับร้านนำร่อง", 14, "Regular", MUTED)


# ---------------------------------------------------------------- FAQ
FAQ = [("khonnai คืออะไร?", "เว็บแอปบนมือถือสำหรับร้านค้าส่ง\nชุดชั้นในและเสื้อผ้าขนาดเล็ก จัดการสินค้า\n"
                            "แยกรุ่น สี ไซซ์ บันทึกการจอง และออกบิล\nจากข้อมูลชุดเดียวกัน"),
       ("ต่างจากจดสมุดหรือ Excel อย่างไร?", None), ("ต้องติดตั้งแอปไหม?", None), ("มีให้ทดลองใช้ฟรีไหม?", None),
       ("ค่าสมาชิกรายเดือนเท่าไร?", None)]


def faq(parent):
    s = section(parent, "FAQ", gap=24)
    heading(s, "คำถามที่พบบ่อย")
    lst = col(s, "Accordion", gap=10, sizingH="fill")
    for q, a in FAQ:
        item = col(lst, "Item / " + q, gap=10, padding=[16, 18, 16, 18], cornerRadius=16, fill=FAQ_BG,
                   sizingH="fill", minHeight=56)
        head = row(item, "Question", gap=12, mainAlign="spaceBetween", sizingH="fill")
        th(head, q, 16, "Bold", INK)
        icon(head, CHEVRON_DOWN if a else CHEVRON_RIGHT, 16, INK)
        if a:
            th(item, a, 15, "Regular", MUTED, lineHeight="165%")
    wide(pill(s, "ติดต่อทีม khonnai", "primary", 52, arrow=True))


# ---------------------------------------------------------------- closing + footer
def closing(parent):
    s = section(parent, "Closing CTA", pad=(0, PAD, 64, PAD))
    b = box(s, "Panel", INNER, 560, layout="vertical", gap=20, crossAlign="center", padding=[48, 24, 0, 24],
            cornerRadius=28, sizingH="fixed", sizingV="fixed", clip=True,
            fills=[{"type": "linearGradient", "stops": ["#1650D7", "#2459DB", "#6A6FD8", "#E98E86", "#FF9F5E"]}])
    glow(b, -100, 300, 260, 260, ORANGE, 0.6, 80)
    center(b, "ให้คนในจำสต็อก\nแทนเจ้าของร้าน", 32, "Bold", WHITE, lineHeight="130%")
    wide(pill(b, "เริ่มใช้ฟรี", "white", 52, arrow=True))
    shots = box(b, "Phones", INNER, 300)
    phone(shots, "home", 360, round((INNER - 170) / 2), 20, "หน้าโฮม")


FOOTER = [("PRODUCT", ["Features", "Pricing", "Services"]), ("COMPANY", ["ทีม Khonnai", "Contact Us"]),
          ("RESOURCES", ["คำถามที่พบบ่อย", "ความเป็นส่วนตัว"])]


def footer(parent):
    s = section(parent, "Footer", gap=28, pad=(48, PAD, 32, PAD))
    one("node.set", {"id": s, "stroke": BORDER, "strokeTopWeight": 1, "strokeRightWeight": 0,
                     "strokeBottomWeight": 0, "strokeLeftWeight": 0, "strokeAlign": "inside"})
    brand = col(s, "Brand", gap=12, sizingH="fill")
    logo = one("image.place", {"path": LOGO, "parent": brand, "width": 120, "height": 26, "mode": "fit"})["id"]
    one("node.set", {"id": logo, "name": "Logo / khonnai"})
    th(brand, "คนใน · ระบบบริหารสต็อก การจองสินค้า\nและการออกบิลบนมือถือ", 15, "Regular", MUTED, lineHeight="165%")
    grid = row(s, "Links", gap=16, crossAlign="min", sizingH="fill")
    for head, links in FOOTER:
        c = col(grid, head, gap=0, sizingH="fill")
        txt(c, head, 14, "Bold", INK, letterSpacing="4%")
        for link in links:
            r = row(c, "Link / " + link, minHeight=44, sizingH="fill")
            (th if any("฀" <= ch <= "๿" for ch in link) else txt)(r, link, 15, "Regular", MUTED)
    demo = col(s, "Demo card", gap=12, padding=20, cornerRadius=20, fill=SURFACE, sizingH="fill")
    stroke(demo)
    th(demo, "นัดดูเดโมกับทีม", 18, "Bold", INK)
    th(demo, "ให้ทีมพาดูการทำงานจริงบนมือถือของคุณ", 15, "Regular", MUTED)
    wide(pill(demo, "นัดดูเดโม", "dark", 48))
    bottom = col(s, "Bottom", gap=16, sizingH="fill", paddingTop=20)
    one("node.set", {"id": bottom, "stroke": BORDER, "strokeTopWeight": 1, "strokeRightWeight": 0,
                     "strokeBottomWeight": 0, "strokeLeftWeight": 0, "strokeAlign": "inside"})
    r = row(bottom, "Meta", gap=12, mainAlign="spaceBetween", sizingH="fill")
    txt(r, "Terms · Privacy", 14, "Regular", MUTED)
    lang_switch(r, outline=True)
    th(bottom, "© 2569 Khonnai · TED Youth Startup Fund", 14, "Regular", MUTED)


# ---------------------------------------------------------------- menu sheet
FEATURES = [("package", "สต็อกสินค้า"), ("receipt", "ออกบิล"), ("bookmark", "การจอง"), ("home", "หน้าโฮมสรุปร้าน")]


def menu_sheet():
    old = run([{"command": "select.byName", "params": {"query": MENU_NAME}}])[0]["selection"]
    if old:
        run([{"command": "edit.delete", "params": {"ids": old}}])
    f = box(None, MENU_NAME, W, 812, layout="vertical", gap=0, padding=[12, 16, 24, 16], sizingH="fixed",
            sizingV="fixed", fill=WHITE)
    one("node.set", {"id": f, "x": MX + W + 80, "y": 0})
    top = box(f, "Top", W - 32, 60, layout="horizontal", mainAlign="spaceBetween", crossAlign="center",
              padding=[0, 8, 0, 18], sizingH="fixed", sizingV="fixed")
    logo = one("image.place", {"path": LOGO, "parent": top, "width": 110, "height": 24, "mode": "fit"})["id"]
    one("node.set", {"id": logo, "name": "Logo / khonnai"})
    close = box(top, "Close", 44, 44, layout="horizontal", mainAlign="center", crossAlign="center",
                cornerRadius=999, fill=HOVER)
    icon(close, CLOSE_ICON, 24, INK)
    body = col(f, "Menu", gap=4, paddingTop=16, sizingH="fill", sizingV="fill")
    feat = col(body, "Features", gap=4, padding=[4, 4, 12, 4], cornerRadius=20, fill=SURFACE, sizingH="fill")
    head = row(feat, "Head", mainAlign="spaceBetween", padding=[10, 12, 10, 14], minHeight=52, sizingH="fill")
    txt(head, "Features", 18, "Medium", BLUE)
    icon(head, "M4 10l4-4 4 4", 16, BLUE)
    for key, label in FEATURES:
        it = row(feat, "Module / " + label, gap=12, padding=[8, 12, 8, 14], minHeight=48, sizingH="fill")
        tile = box(it, "Icon", 32, 32, layout="horizontal", mainAlign="center", crossAlign="center",
                   cornerRadius=10, fill=WHITE)
        icon(tile, MENU_ICONS.get(key) or ICON[key], 24, BLUE)
        th(it, label, 16, "Regular", INK)
    for label in ("Pricing", "Services", "Contact Us"):
        it = row(body, "Item / " + label, mainAlign="spaceBetween", padding=[10, 16, 10, 18], minHeight=56,
                 sizingH="fill")
        txt(it, label, 18, "Medium", INK)
        icon(it, CHEVRON_DOWN if label == "Services" else CHEVRON_RIGHT, 16, MUTED)
    lang = row(body, "Language", gap=4, padding=4, cornerRadius=999, fill=HOVER, sizingH="fill")
    for i, (code, label) in enumerate((("TH", "ภาษาไทย"), ("EN", "English"))):
        seg = row(lang, "Lang / " + code, gap=8, mainAlign="center", cornerRadius=999, height=44, sizingV="fixed",
                  sizingH="fill", fill=WHITE if i == 0 else None)
        (th if code == "TH" else txt)(seg, label, 15, "Bold" if i == 0 else "Regular", INK if i == 0 else MUTED)
    actions = col(f, "Actions", gap=10, sizingH="fill")
    wide(pill(actions, "Schedule a Demo", "primary", 52, arrow=True))
    wide(pill(actions, "Sign up", "outline", 52))
    return f


def export(name):
    export_frame(name, os.path.join(PREVIEW, name + ".png"))


def main():
    old = run([{"command": "select.byName", "params": {"query": NAME}}])[0]["selection"]
    old = [i for i in old if one("node.get", {"id": i}).get("name") == NAME]
    if old:
        run([{"command": "edit.delete", "params": {"ids": old}}])
    page = box(None, NAME, W, 100, layout="vertical", gap=0, sizingH="fixed", sizingV="hug", fill=WHITE)
    one("node.set", {"id": page, "x": MX, "y": 0})
    for build in (hero, proof, overview, easy, pricing, faq, closing, footer):
        build(page)
        print("built", build.__name__, flush=True)
    menu_sheet()
    export(NAME)
    export(MENU_NAME)


if __name__ == "__main__":
    main()
