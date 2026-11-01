"""Landing page mock-up v2: the full page, following the section order and styling of feedspring.com.

Usage: python -I design/build_landing_v2.py [menus]   (after build_landing_navbar.py)
"menus" rebuilds only the nav dropdown frames ("Landing v2 — Features / Services / Language menu").
Adds (or rebuilds) the frame "Landing v2 — Desktop" in design/khonnai-landing.figcraft, beside the
section frames, and exports design/preview/landing/Landing v2 — Desktop.png.

feedspring.com (reverse-engineered 2026-11-01) → khonnai:
  floating pill nav + blue gradient hero + card mosaic   → same, mosaic shows real app screens and the pilot test
  "Platform Overview" 2×2 bento                          → ภาพรวมระบบ: สต็อก / ออกบิล / ใบจอง / ไม่ขายเกิน
  "Made For No-Code" tab list + illustration panel       → ออกแบบให้ใช้ง่าย: 5 points + home screen
  dark photo CTA banner                                  → pricing: Free / Basic 299 / Pro 699 with limit bars
  FAQ accordion (620 wide, 16 radius, #F5F5F5)            → คำถามที่พบบ่อย
  blue gradient closing CTA with product screenshot      → same, with three phones
  footer columns + Discord card                          → footer columns + demo card
Backgrounds run brand blue → orange; white text only sits on the blue part (≥ 4.5:1).
Content comes from khonnai-pitch-final.pdf and the hero brief; no customer quotes or user counts are invented.
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from build_landing_hero import ARROW, SCREENS, phone  # noqa: E402
from build_landing_navbar import (BLUE, BLUE_50, BORDER, CHEVRON_DOWN, CHEVRON_UP, F_TH, HOVER, ICON, INK, LOGO, MENU, MUTED,  # noqa: E402
                                  PREVIEW, WHITE, box, col, export_frame, icon, one, row, run, txt)

NAME = "Landing v2 — Desktop"
X = 1600   # beside the section frames
NAVY = "#0F172A"
ORANGE = "#FF8032"
ORANGE_700 = "#9A4A0C"
ORANGE_50 = "#FFF3E8"
SURFACE = "#F8FAFC"
FAQ_BG = "#F5F5F5"
CHEVRON_RIGHT = "M6 4l4 4-4 4"   # 16 grid
GLOBE = ("M12 22a10 10 0 1 0 0-20 10 10 0 0 0 0 20z M2 12h20 M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10"
         " 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z")   # Lucide globe, 24 grid
# blue → orange; the first half stays dark enough for white text
BRAND_GRADIENT = ["#1650D7", "#1A53D8", "#2459DB", "#3F68DF", "#9C86D0", "#FF9F5E", "#FFE3CC"]
HEADLINE_ACCENT = "#FFD2B0"   # 64px on the blue part, above 3:1
CHECK = "M4 10.5l4 4 8-9"   # 20 grid
SHADOW = [{"type": "dropShadow", "color": "#0F172A1A", "offset": [0, 12], "radius": 32, "spread": -8}]
CARD_SHADOW = [{"type": "dropShadow", "color": "#0713131A", "offset": [0, 1], "radius": 1, "spread": 0}]


def stroke(nid, color=BORDER):
    one("node.set", {"id": nid, "stroke": color, "strokeWeight": 1, "strokeAlign": "inside"})


def th(parent, text, size, style="Regular", color=INK, **props):
    return txt(parent, text, size, style, color, F_TH, **props)


def center(parent, text, size, style="Regular", color=INK, **props):
    return th(parent, text, size, style, color, textAlign="center", **props)


def pill(parent, label, kind, size=48, arrow=False):
    fill, color = {"primary": (BLUE, WHITE), "white": (WHITE, BLUE), "outline-light": (None, WHITE),
                   "dark": (NAVY, WHITE), "outline": (WHITE, INK)}[kind]
    b = row(parent, "Button / " + label, gap=8, padding=[0, 24, 0, 24], cornerRadius=999, height=size,
            sizingV="fixed", fill=fill)
    if kind == "outline":
        stroke(b, "#CBD5E1")
    if kind == "outline-light":   # on the blue: white text sits on the blue itself, not on a glass tint
        one("node.set", {"id": b, "stroke": WHITE, "strokeWeight": 1.5, "strokeAlign": "inside"})
    family = F_TH if any("฀" <= ch <= "๿" for ch in label) else None
    if family:
        th(b, label, 16, "Bold", color)
    else:
        txt(b, label, 16, "Medium", color)
    if arrow:
        icon(b, ARROW, 18, color)
    return b


def section(parent, name, gap=48, pad=(96, 80, 96, 80), fill=WHITE, **props):
    return box(parent, name, 1440, 100, layout="vertical", gap=gap, padding=list(pad), crossAlign="center",
               sizingH="fixed", sizingV="hug", fill=fill, **props)


def heading(parent, title, body=None, align="center", size=48):
    h = col(parent, "Heading", gap=16, crossAlign="center" if align == "center" else "min")
    write = center if align == "center" else th
    write(h, title, size, "Bold", INK, lineHeight="130%")
    if body:
        write(h, body, 18, "Regular", MUTED, lineHeight="170%")
    return h


def screen_img(parent, name, w, h, radius=16):
    img = one("image.place", {"path": os.path.join(SCREENS, name), "parent": parent, "width": w, "height": h,
                              "mode": "fill"})["id"]
    one("node.set", {"id": img, "name": "Screen", "cornerRadius": radius})
    return img


def glow(parent, x, y, w, h, color, opacity=0.6, blur=140):
    """A blurred colour blob behind a section's content."""
    g = one("node.create", {"type": "ellipse", "parent": parent, "x": x, "y": y, "width": w, "height": h,
                            "name": "Glow", "props": {"fill": color, "opacity": opacity,
                                                      "effects": [{"type": "layerBlur", "radius": blur}]}})["id"]
    one("node.set", {"id": g, "absolute": True, "x": x, "y": y})
    one("node.reorder", {"id": g, "index": 0})


def lang_switch(parent, outline=False):
    s = row(parent, "Language", gap=6, padding=[0, 12, 0, 12], cornerRadius=999, height=44, sizingV="fixed",
            fill=WHITE if outline else HOVER)
    if outline:
        stroke(s, "#CBD5E1")
    icon(s, GLOBE, 20, INK, weight=1.75)
    txt(s, "TH", 15, "Medium", INK)
    icon(s, CHEVRON_DOWN, 16, MUTED)
    return s


# ---------------------------------------------------------------- hero
def floating_nav(parent, active=None):
    """The pill nav; returns {label: item id} so a dropdown can line up under its item."""
    nav = box(parent, "Navbar / floating", 1200, 64, layout="horizontal", mainAlign="spaceBetween",
              crossAlign="center", padding=[0, 10, 0, 24], cornerRadius=999, fill=WHITE, effects=SHADOW,
              sizingH="fixed", sizingV="fixed")
    left = row(nav, "Left", gap=32)
    logo = one("image.place", {"path": LOGO, "parent": left, "width": 128, "height": 28, "mode": "fit"})["id"]
    one("node.set", {"id": logo, "name": "Logo / khonnai"})
    menu = row(left, "Menu", gap=4)
    items = {}
    for label, dropdown in MENU:
        on = label == active
        item = row(menu, "Menu / " + label, gap=4, padding=[10, 12, 10, 12], cornerRadius=999, minHeight=44,
                   fill=HOVER if on else None)
        txt(item, label, 15, "Medium", BLUE if on else INK)
        if dropdown:
            icon(item, CHEVRON_UP if on else CHEVRON_DOWN, 16, BLUE if on else MUTED)
        items[label] = item
    right = row(nav, "Actions", gap=8)
    items["lang"] = lang_switch(right)
    pill(right, "Sign up", "outline", 44)
    pill(right, "Schedule a Demo", "primary", 44, arrow=True)
    return items


def mosaic_card(parent, title, img, caption, w, h_img):
    c = col(parent, "Card / " + title, gap=12, padding=12, cornerRadius=24, fill=WHITE, effects=SHADOW,
            width=w, sizingH="fixed")
    head = row(c, "Head", gap=8, padding=[4, 4, 0, 4])
    th(head, title, 14, "Bold", INK)
    screen_img(c, img, w - 24, h_img)
    th(c, caption, 14, "Regular", MUTED, lineHeight="160%")
    return c


def pilot_card(parent):
    c = col(parent, "Card / ร้านนำร่อง", gap=16, padding=24, cornerRadius=24, fill=WHITE, effects=SHADOW,
            width=400, sizingH="fixed")
    top = row(c, "Head", gap=8)
    icon(top, CHECK, 20, BLUE)
    th(top, "ทดสอบกับร้านค้าส่งนำร่อง · 28 ต.ค. 2569", 14, "Bold", BLUE)
    stats = row(c, "Stats", gap=12)
    for big, small in (("1 ร้าน", "ร้านนำร่อง\nที่ทดสอบจริง"), ("30 นาที", "เพิ่มสต็อก ทำบิล\nออกบิลครบ"),
                       ("7 ข้อ", "ข้อค้นพบที่นำ\nไปปรับ UX")):
        s = col(stats, "Stat", gap=4, padding=12, cornerRadius=16, fill=SURFACE, width=109, sizingH="fixed")
        th(s, big, 22, "Bold", INK)
        th(s, small, 14, "Regular", MUTED, lineHeight="150%")
    th(c, "เจ้าของร้านลองใช้งานหลักด้วยตัวเอง แล้วเราปรับ\nหน้าจอให้อ่านง่ายขึ้นจากผลทดสอบ", 15, "Regular",
       MUTED, lineHeight="165%")
    return c


def hero(parent):
    h = box(parent, "Hero", 1440, 1120, layout="vertical", gap=0, padding=[24, 120, 0, 120], crossAlign="center",
            sizingH="fixed", sizingV="fixed", clip=True,
            fills=[{"type": "linearGradient", "stops": BRAND_GRADIENT}])
    floating_nav(h)
    copy = col(h, "Copy", gap=24, crossAlign="center", paddingTop=72, paddingBottom=56)
    head = col(copy, "Headline", gap=0, crossAlign="center")
    center(head, "สต็อก การจอง และบิล", 64, "Bold", WHITE, lineHeight="125%")
    center(head, "จบในข้อมูลชุดเดียว", 64, "Bold", HEADLINE_ACCENT, lineHeight="125%")
    center(copy, "จัดการสินค้าแยกตามรุ่น สี และไซซ์ ตรวจจำนวนที่พร้อมขาย บันทึกการจอง\n"
                 "และออกบิลจากข้อมูลชุดเดียวกัน สำหรับร้านค้าส่งชุดชั้นในและเสื้อผ้าขนาดเล็ก",
           20, "Regular", WHITE, lineHeight="165%")
    ctas = row(copy, "CTAs", gap=12, paddingTop=8)
    pill(ctas, "เริ่มใช้ฟรี", "white", arrow=True)
    pill(ctas, "นัดดูเดโม", "outline-light")
    grid = row(h, "Mosaic", gap=24, crossAlign="min")
    mosaic_card(grid, "สต็อกสินค้า", "tile-stock.png", "เห็นจำนวนพร้อมขายแยกไซซ์และสี\nทุกรุ่นในจอเดียว", 300, 322)
    mid = col(grid, "Middle", gap=24)
    pilot_card(mid)
    tiles = row(mid, "Tiles", gap=24)
    for img, label in (("tile-reserve.png", "ใบจองที่กันสต็อก"), ("tile-history.png", "ประวัติการขาย")):
        t = col(tiles, "Tile / " + label, gap=10, padding=10, cornerRadius=24, fill=WHITE, effects=SHADOW,
                width=188, sizingH="fixed")
        screen_img(t, img, 168, 160, 14)
        th(t, label, 14, "Bold", INK)
    mosaic_card(grid, "บิลเงินสด", "tile-bill.png", "ออกบิลตามแบบฟอร์มของร้าน\nตัดสต็อกให้ทันที", 300, 322)
    fade = one("node.create", {"type": "rectangle", "parent": h, "x": 0, "y": 1070, "width": 1440, "height": 50,
                               "name": "Fade", "props": {"fills": [{"type": "linearGradient",
                                                                     "stops": ["#FFFFFF00", "#FFFFFF"]}]}})["id"]
    one("node.set", {"id": fade, "absolute": True, "x": 0, "y": 1070})
    hero_chip(h, 92, 720, "ออกบิลแล้ว", "ตัดสต็อก 5 แพ็ก", "#16A34A")
    hero_chip(h, 1132, 900, "รับของแล้ว", "+ ฿1,160", ORANGE)
    glow(h, 980, -160, 640, 420, "#7FA8FF", 0.55)
    glow(h, -160, 700, 620, 520, ORANGE, 0.55)
    glow(h, 1040, 760, 520, 420, "#FFB27A", 0.6)


def hero_chip(parent, x, y, label, value, color):
    """A small toast that floats over the mosaic edge."""
    c = row(parent, "Toast / " + label, gap=10, padding=[10, 16, 10, 12], cornerRadius=16, fill=WHITE,
            effects=SHADOW)
    one("node.set", {"id": c, "absolute": True, "x": x, "y": y})
    dot = box(c, "Status", 32, 32, layout="horizontal", mainAlign="center", crossAlign="center", cornerRadius=999,
              fill=color + "26")
    icon(dot, CHECK, 20, color)
    t = col(c, "Text", gap=0)
    th(t, label, 14, "Regular", MUTED)
    th(t, value, 16, "Bold", INK)


def proof_line(parent):
    s = section(parent, "Proof line", pad=(0, 80, 24, 80))
    p = row(s, "Line", gap=10)
    icon(p, CHECK, 20, BLUE)
    th(p, "ออกแบบจากการทดสอบกับร้านค้าส่งนำร่อง ไม่ใช่จากโต๊ะประชุม", 18, "Bold", INK)


# ---------------------------------------------------------------- overview bento
def bento_card(parent, w, title, body):
    c = col(parent, "Card / " + title, gap=0, cornerRadius=24, fill=SURFACE, width=w, height=440,
            sizingH="fixed", sizingV="fixed", clip=True, effects=CARD_SHADOW)
    stroke(c)
    visual = box(c, "Visual", w, 300, layout="horizontal", mainAlign="center", crossAlign="center",
                 sizingH="fill", sizingV="fixed")
    text = col(c, "Text", gap=8, padding=[0, 28, 28, 28])
    th(text, title, 24, "Bold", INK)
    th(text, body, 16, "Regular", MUTED, lineHeight="165%")
    return visual


def stock_matrix(parent):
    m = col(parent, "Size × colour", gap=8, padding=20, cornerRadius=20, fill=WHITE, effects=SHADOW)
    rows = [("", ["32", "34", "36"]), ("ดำ", ["12", "8", "0"]), ("ขาว", ["3", "6", "—"]), ("เนื้อ", ["—", "2", "9"])]
    for i, (colour, cells) in enumerate(rows):
        r = row(m, "Row " + (colour or "head"), gap=8)
        lab = box(r, "Colour", 56, 36, layout="horizontal", crossAlign="center")
        th(lab, colour, 15, "Bold", INK)
        for v in cells:
            cell = box(r, "Cell", 64, 36, layout="horizontal", mainAlign="center", crossAlign="center",
                       cornerRadius=10, fill=None if i == 0 else (ORANGE_50 if v == "0" else BLUE_50 if v != "—" else SURFACE))
            th(cell, v, 15, "Bold", MUTED if i == 0 or v == "—" else ORANGE_700 if v == "0" else BLUE)


def bill_steps(parent):
    s = row(parent, "Steps", gap=12)
    for i, label in enumerate(("เลือกสินค้า", "ยืนยันออเดอร์", "ได้บิลเงินสด")):
        st = row(s, "Step " + str(i + 1), gap=10, padding=[12, 18, 12, 12], cornerRadius=999,
                 fill=BLUE if i == 2 else WHITE)
        if i < 2:
            stroke(st)
        n = box(st, "Number", 32, 32, layout="horizontal", mainAlign="center", crossAlign="center",
                cornerRadius=999, fill=WHITE if i == 2 else BLUE_50)
        txt(n, str(i + 1), 15, "Bold", BLUE)
        th(st, label, 16, "Bold", WHITE if i == 2 else INK)
        if i < 2:
            icon(s, ARROW, 18, MUTED)


def sellable(parent):
    f = col(parent, "Formula", gap=12, crossAlign="center", padding=24, cornerRadius=20, fill=WHITE, effects=SHADOW)
    r = row(f, "Numbers", gap=14)
    for v, lab, color in (("45", "คงเหลือ", INK), ("–", " ", MUTED), ("5", "จองไว้", ORANGE_700), ("=", " ", MUTED),
                          ("40", "พร้อมขาย", BLUE)):
        c = col(r, "Term", gap=2, crossAlign="center")
        txt(c, v, 40, "Bold", color)
        th(c, lab, 14, "Regular", MUTED)
    th(f, "ระบบไม่ยอมออกบิลถ้าของพร้อมขายไม่พอ", 14, "Bold", INK)


def overview(parent):
    s = section(parent, "Overview", gap=56)
    heading(s, "ข้อมูลชุดเดียว\nใช้ได้ทั้งสต็อก การจอง และบิล",
            "ไม่ต้องจดสมุดหลายเล่ม ไม่ต้องเช็กของซ้ำ ระบบทำงานผ่านขั้นตอนสั้น ๆ และอ่านง่ายบนมือถือ")
    g = col(s, "Bento", gap=24)
    r1 = row(g, "Row 1", gap=24)
    stock_matrix(bento_card(r1, 500, "สต็อกแยกรุ่น สี และไซซ์",
                            "เห็นทันทีว่าไซซ์ไหน สีไหน เหลือกี่แพ็ก\nและตัวไหนหมดต้องเติม"))
    bill_steps(bento_card(r1, 756, "ออกบิลใน 3 ขั้น",
                          "เลือกสินค้า ยืนยันออเดอร์ แล้วได้บิลเงินสดตามแบบฟอร์มของร้าน\nสต็อกถูกตัดให้ทันทีที่ยืนยัน"))
    r2 = row(g, "Row 2", gap=24)
    v = bento_card(r2, 756, "ใบจองที่กันสต็อกไว้ให้",
                   "จองจากหน้าร้านหรือ LINE ใช้สต็อกชุดเดียวกัน\nกด \"ลูกค้ารับของแล้ว\" จึงออกบิลโดยไม่ตัดซ้ำ")
    p, _ = phone(v, "reserve", 250, 0, 0, "การจอง")
    one("node.set", {"id": p, "absolute": True, "x": 320, "y": 28})
    sellable(bento_card(r2, 500, "ไม่ขายเกินของที่มี",
                        "ยืนยันบิลได้เมื่อคงเหลือหักของที่จองไว้แล้วยังพอ\nกันขายชิ้นสุดท้ายซ้ำ"))


# ---------------------------------------------------------------- easy to use
POINTS = [
    ("หน้าโฮมสรุปร้านในจอเดียว", "รายได้วันนี้ ออเดอร์รอรับของ และของที่ต้องเติม พร้อมปุ่มลัดออกบิล ดูสต็อก เพิ่มรุ่น และจอง"),
    ("ตัวอักษรใหญ่ อ่านง่ายสำหรับวัย 40+", None),
    ("เพิ่มรุ่นใหม่ได้ในหน้าเดียว", None),
    ("ใช้ผ่านเว็บบนมือถือ ไม่ต้องติดตั้ง", None),
    ("บันทึกบิลเป็น PDF เพื่อพิมพ์หรือส่งต่อ", None),
]
POINT_ICONS = ["home", "type", "package", "smartphone", "file"]
POINT_PATHS = {  # Lucide
    "home": "M3 10l9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z M9 22V12h6v10",
    "type": "M4 7V4h16v3 M9 20h6 M12 4v16",
    "smartphone": "M7 2h10a2 2 0 0 1 2 2v16a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2z M12 18h.01",
    "file": "M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z M14 2v6h6 M16 13H8 M16 17H8 M10 9H8",
    "package": ICON["package"],
}


def float_chip(parent, x, y, label, value, color):
    c = col(parent, "Chip / " + label, gap=2, padding=[12, 16, 12, 16], cornerRadius=16, fill=WHITE, effects=SHADOW)
    one("node.set", {"id": c, "x": x, "y": y})
    th(c, label, 14, "Regular", MUTED)
    v = row(c, "Value", gap=6)
    box(v, "Dot", 8, 8, cornerRadius=999, fill=color)
    th(v, value, 18, "Bold", INK)


def easy(parent):
    s = section(parent, "Easy to use", gap=48, pad=(48, 80, 96, 80))
    head = box(s, "Head", 1280, 100, layout="horizontal", mainAlign="spaceBetween", crossAlign="max",
               sizingH="fixed", sizingV="hug")
    heading(head, "ขั้นตอนสั้น ตัวใหญ่\nเจ้าของร้านใช้เองได้ทุกวัน", align="left")
    pill(head, "ดูฟีเจอร์ทั้งหมด", "primary", arrow=True)
    body = row(s, "Body", gap=40, crossAlign="min")
    lst = col(body, "Points", gap=6, width=500, sizingH="fixed")
    for i, (title, desc) in enumerate(POINTS):
        p = row(lst, "Point / " + title, gap=14, padding=[16, 18, 16, 18], cornerRadius=16, sizingH="fill",
                crossAlign="min", fill=HOVER if desc else None)
        ic = box(p, "Icon", 36, 36, layout="horizontal", mainAlign="center", crossAlign="center", cornerRadius=10,
                 fill=BLUE_50 if desc else None)
        icon(ic, POINT_PATHS[POINT_ICONS[i]], 24, BLUE if desc else MUTED)
        t = col(p, "Text", gap=6, paddingTop=6)
        th(t, title, 17, "Bold", INK if desc else MUTED)
        if desc:
            txt_id = th(t, desc, 15, "Regular", MUTED, lineHeight="165%")
            one("node.set", {"id": txt_id, "width": 380, "textAutoResize": "height"})
    panel = box(body, "Panel", 740, 480, cornerRadius=24, clip=True,
                fills=[{"type": "linearGradient", "stops": [BLUE_50, "#F4ECFA", ORANGE_50], "from": [0, 0], "to": [1, 1]}])
    one("node.create", {"type": "ellipse", "parent": panel, "x": 190, "y": 60, "width": 360, "height": 360,
                        "name": "Backdrop", "props": {"fill": "#FFFFFF99"}})
    phone(panel, "home", 520, 251, 40, "หน้าโฮม")
    float_chip(panel, 40, 120, "รอรับของ", "3 ออเดอร์", BLUE)
    float_chip(panel, 540, 300, "ของที่ต้องเติม", "25 แพ็ก", ORANGE)


# ---------------------------------------------------------------- pricing
# slide 8 of the pitch: prices still being tested with pilot shops; yearly assumed 10% off
PLANS = [("Free", "0", "ให้ร้านลองใช้ก่อนจ่าย", 20, 50, "เริ่มใช้ฟรี", "outline"),
         ("Basic", "299", "ร้านค้าส่งทั่วไป", 200, 500, "เลือก Basic", "white"),
         ("Pro", "699", "ร้านที่มียอดขายสูง", 1000, 2000, "เลือก Pro", "dark")]
INCLUDED = ["สต็อกแยกรุ่น สี และไซซ์", "ใบจองที่กันสต็อก", "ออกบิลเงินสดและบันทึก PDF"]
BAR = [{"type": "linearGradient", "stops": [BLUE, ORANGE], "from": [0, 0.5], "to": [1, 0.5]}]
BAR_ON_BLUE = [{"type": "linearGradient", "stops": ["#FFD2B0", ORANGE], "from": [0, 0.5], "to": [1, 0.5]}]


def meter(parent, label, value, max_value, dark):
    m = col(parent, "Meter / " + label, gap=8, sizingH="fill")
    top = row(m, "Label", gap=8, mainAlign="spaceBetween", sizingH="fill")
    th(top, label, 14, "Regular", "#FFFFFFCC" if dark else MUTED)
    txt(top, f"{value:,}", 15, "Bold", WHITE if dark else INK)
    track = box(m, "Track", 316, 8, cornerRadius=999, fill="#FFFFFF33" if dark else "#E2E8F0")
    box(track, "Bar", max(12, round(316 * value / max_value)), 8, cornerRadius=999,
        fills=BAR_ON_BLUE if dark else BAR)


def plan_card(parent, plan, featured):
    name, price, audience, skus, bills, cta, kind = plan
    fg, sub = (WHITE, "#FFFFFFCC") if featured else (INK, MUTED)
    look = ({"fills": [{"type": "linearGradient", "stops": ["#1650D7", "#1D3FA6"], "from": [0, 0], "to": [1, 1]}]}
            if featured else {"fill": WHITE})
    c = col(parent, "Plan / " + name, gap=24, padding=[36 if featured else 32, 32, 32, 32], cornerRadius=28,
            width=380, sizingH="fixed", clip=True, effects=SHADOW, **look)
    if featured:
        glow(c, 220, -120, 260, 220, ORANGE, 0.7, 90)
    else:
        stroke(c)
    head = row(c, "Head", gap=10, mainAlign="spaceBetween", sizingH="fill")
    txt(head, name, 22, "Bold", fg)
    if featured:
        tag = row(head, "Recommended", padding=[4, 12, 4, 12], cornerRadius=999, fill=ORANGE)
        th(tag, "แนะนำ", 14, "Bold", INK)
    th(c, audience, 15, "Regular", sub)
    pr = row(c, "Price", gap=8, crossAlign="baseline")
    txt(pr, price, 56, "Bold", fg)
    th(pr, "บาท / เดือน", 16, "Regular", sub)
    meters = col(c, "Limits", gap=16, sizingH="fill")
    meter(meters, "รหัสสินค้า", skus, 1000, featured)
    meter(meters, "บิลต่อเดือน", bills, 2000, featured)
    inc = col(c, "Included", gap=10)
    for item in INCLUDED:
        r = row(inc, "Item", gap=10)
        icon(r, CHECK, 20, "#FFD2B0" if featured else BLUE)
        th(r, item, 15, "Regular", fg)
    b = pill(c, cta, kind)
    one("node.set", {"id": b, "sizingH": "fill", "mainAlign": "center"})


def pricing(parent):
    s = section(parent, "Pricing", gap=40, pad=(96, 80, 96, 80), clip=True,
                fills=[{"type": "linearGradient", "stops": [WHITE, "#F1F5FE", "#FFF4EA"]}])
    glow(s, -200, 360, 520, 520, "#BFD0F7", 0.7, 160)
    glow(s, 1140, 420, 520, 520, "#FFD2B0", 0.8, 160)
    heading(s, "เลือกแพ็กเกจที่เหมาะกับร้าน",
            "เริ่มฟรี แล้วค่อยอัปเกรดเมื่อร้านโตขึ้น ทุกแพ็กเกจใช้ฟีเจอร์หลักได้ครบ")
    toggle = row(s, "Billing toggle", gap=4, padding=4, cornerRadius=999, fill=WHITE)
    stroke(toggle)
    on = row(toggle, "Monthly", padding=[0, 20, 0, 20], cornerRadius=999, height=44, sizingV="fixed", fill=INK)
    th(on, "รายเดือน", 15, "Bold", WHITE)
    off = row(toggle, "Yearly", gap=8, padding=[0, 12, 0, 20], cornerRadius=999, height=44, sizingV="fixed")
    th(off, "รายปี", 15, "Bold", MUTED)
    save = row(off, "Save", padding=[2, 8, 2, 8], cornerRadius=999, fill=ORANGE_50)
    th(save, "ลด 10%", 14, "Bold", ORANGE_700)
    cards = row(s, "Plans", gap=24, crossAlign="center", clip=False)   # clipping lightens the shadows
    for i, plan in enumerate(PLANS):
        plan_card(cards, plan, i == 1)
    center(s, "* ราคาอยู่ระหว่างทดสอบความเต็มใจจ่ายกับร้านนำร่อง", 14, "Regular", MUTED)


# ---------------------------------------------------------------- FAQ
FAQ = [
    ("khonnai คืออะไร?",
     "เว็บแอปบนมือถือสำหรับร้านค้าส่งชุดชั้นในและเสื้อผ้าขนาดเล็ก ช่วยจัดการสินค้าแยกตามรุ่น สี และไซซ์\n"
     "บันทึกการจอง และออกบิลจากข้อมูลชุดเดียวกัน เพื่อลดการเช็กของซ้ำและบิลที่ไม่ตรงกับสต็อก"),
    ("ต่างจากการจดสมุดหรือ Excel อย่างไร?", None),
    ("ต้องติดตั้งแอปไหม?", None),
    ("มีให้ทดลองใช้ฟรีไหม?", None),
    ("ค่าสมาชิกรายเดือนเท่าไร?", None),
]


def faq(parent):
    s = section(parent, "FAQ", gap=48, pad=(32, 80, 96, 80))
    heading(s, "คำถามที่พบบ่อย")
    lst = col(s, "Accordion", gap=12, width=720, sizingH="fixed")
    for q, a in FAQ:
        item = col(lst, "Item / " + q, gap=10, padding=[20, 24, 20, 24], cornerRadius=16, fill=FAQ_BG,
                   sizingH="fill", effects=CARD_SHADOW)
        head = row(item, "Question", gap=12, mainAlign="spaceBetween", sizingH="fill")
        th(head, q, 17, "Bold", INK)
        icon(head, CHEVRON_DOWN if a else CHEVRON_RIGHT, 16, INK)
        if a:
            th(item, a, 15, "Regular", MUTED, lineHeight="170%")
    pill(s, "ติดต่อทีม khonnai", "primary", arrow=True)


# ---------------------------------------------------------------- closing CTA
def closing(parent):
    s = section(parent, "Closing CTA", pad=(0, 80, 96, 80))
    b = box(s, "Panel", 1280, 600, layout="vertical", gap=20, crossAlign="center", padding=[72, 0, 0, 0],
            cornerRadius=32, sizingH="fixed", sizingV="fixed", clip=True,
            fills=[{"type": "linearGradient", "stops": ["#1650D7", "#2459DB", "#6A6FD8", "#E98E86", "#FF9F5E"]}])
    glow(b, -120, 260, 480, 420, ORANGE, 0.6)
    glow(b, 900, -140, 520, 360, "#7FA8FF", 0.6)
    center(b, "ให้คนในจำสต็อก\nแทนเจ้าของร้าน", 56, "Bold", WHITE, lineHeight="125%")
    pill(b, "เริ่มใช้ฟรี", "white", arrow=True)
    phones = box(b, "Phones", 1280, 320)
    phone(phones, "stock", 340, 380, 70, "สต็อก")
    phone(phones, "bill", 340, 740, 70, "บิลเงินสด")
    phone(phones, "home", 420, 552, 20, "หน้าโฮม")


# ---------------------------------------------------------------- footer
FOOTER = [("PRODUCT", ["Features", "Pricing", "Services"]), ("COMPANY", ["ทีม Khonnai", "Contact Us"]),
          ("RESOURCES", ["คำถามที่พบบ่อย", "นโยบายความเป็นส่วนตัว"])]


def footer(parent):
    s = section(parent, "Footer", gap=48, pad=(64, 80, 40, 80))
    one("node.set", {"id": s, "stroke": BORDER, "strokeTopWeight": 1, "strokeRightWeight": 0,
                     "strokeBottomWeight": 0, "strokeLeftWeight": 0, "strokeAlign": "inside"})
    top = box(s, "Top", 1280, 100, layout="horizontal", mainAlign="spaceBetween", crossAlign="min",
              sizingH="fixed", sizingV="hug")
    brand = col(top, "Brand", gap=16, width=300, sizingH="fixed")
    logo = one("image.place", {"path": LOGO, "parent": brand, "width": 128, "height": 28, "mode": "fit"})["id"]
    one("node.set", {"id": logo, "name": "Logo / khonnai"})
    th(brand, "คนใน · ระบบบริหารสต็อก การจองสินค้า\nและการออกบิลบนมือถือ", 15, "Regular", MUTED, lineHeight="165%")
    for head, links in FOOTER:
        c = col(top, head, gap=14, width=170, sizingH="fixed")
        txt(c, head, 14, "Bold", INK, letterSpacing="6%")
        for link in links:
            if any("฀" <= ch <= "๿" for ch in link):
                th(c, link, 15, "Regular", MUTED)
            else:
                txt(c, link, 15, "Regular", MUTED)
    card = col(top, "Demo card", gap=16, padding=24, cornerRadius=20, fill=SURFACE, width=340, sizingH="fixed")
    stroke(card)
    th(card, "นัดดูเดโมกับทีม", 18, "Bold", INK)
    th(card, "ให้ทีมพาดูการทำงานจริง\nบนมือถือของคุณ", 15, "Regular", MUTED, lineHeight="165%")
    btn = pill(card, "นัดดูเดโม", "dark", 44)
    one("node.set", {"id": btn, "sizingH": "fill", "mainAlign": "center"})
    bottom = box(s, "Bottom", 1280, 100, layout="horizontal", mainAlign="spaceBetween", crossAlign="center",
                 sizingH="fixed", sizingV="hug", paddingTop=24)
    one("node.set", {"id": bottom, "stroke": BORDER, "strokeTopWeight": 1, "strokeRightWeight": 0,
                     "strokeBottomWeight": 0, "strokeLeftWeight": 0, "strokeAlign": "inside"})
    th(bottom, "© 2569 Khonnai · TED Youth Startup Fund · KX-TECHBITE", 14, "Regular", MUTED)
    links = row(bottom, "Links", gap=20)
    txt(links, "Terms of Use  ·  Privacy Policy", 14, "Regular", MUTED)
    lang_switch(links, outline=True)


# ---------------------------------------------------------------- nav dropdowns (feedspring Product / Resources)
MENU_ICONS = {  # Lucide, 24 grid
    "home": "M3 10l9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z M9 22V12h6v10",
    "sparkle": "M12 3l1.9 5.8L20 10l-6.1 1.2L12 17l-1.9-5.8L4 10l6.1-1.2z",
    "arrow": "M5 12h14 M13 6l6 6-6 6",
    "shirt": "M20.38 3.46L16 2a4 4 0 0 1-8 0L3.62 3.46a2 2 0 0 0-1.34 2.23l.58 3.47a1 1 0 0 0 .99.84H6v10"
             "c0 1.1.9 2 2 2h8a2 2 0 0 0 2-2V10h2.15a1 1 0 0 0 .99-.84l.58-3.47a2 2 0 0 0-1.34-2.23z",
    "store": "M3 9l1.5-5h15L21 9 M4 9v11h16V9 M9 20v-6h6v6 M3 9h18",
    "message": "M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z",
    "calendar": "M8 2v4 M16 2v4 M3 10h18 M5 4h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z",
    "upload": "M12 3v12 M7 8l5-5 5 5 M5 21h14",
    "teach": "M22 10L12 5 2 10l10 5 10-5z M6 12v5c3 2 9 2 12 0v-5",
    "book": "M4 19.5A2.5 2.5 0 0 1 6.5 17H20 M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z",
    "help": "M12 22a10 10 0 1 0 0-20 10 10 0 0 0 0 20z M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3 M12 17h.01",
    "phone": "M7 2h10a2 2 0 0 1 2 2v16a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2z M12 18h.01",
}
FEATURE_MODULES = [("package", "สต็อกสินค้า"), ("receipt", "ออกบิล"), ("bookmark", "การจอง"), ("home", "หน้าโฮมสรุปร้าน")]
FEATURE_LINKS = [("sparkle", "ดูเดโมการทำงาน"), ("arrow", "ทดลองใช้ฟรี")]
FIT_FOR = [("shirt", "ร้านค้าส่งชุดชั้นใน"), ("shirt", "ร้านเสื้อผ้าขนาดเล็ก"), ("store", "ขายหน้าร้าน"),
           ("message", "รับออเดอร์ทาง LINE")]
# proposed service list for the mock-up; confirm with the team before launch
SERVICES = [("calendar", "นัดดูเดโม", "ทีมพาดูการทำงานจริง"), ("help", "ศูนย์ช่วยเหลือ", "บัญชีและค่าสมาชิก"),
            ("store", "ช่วยตั้งค่าร้าน", "เพิ่มสินค้าชุดแรกให้"), ("sparkle", "อัปเดตระบบ", "ฟีเจอร์ใหม่ล่าสุด"),
            ("upload", "ย้ายข้อมูลเดิม", "จากสมุดหรือ Excel"), ("book", "คู่มือการใช้งาน", "เริ่มต้นใช้งาน"),
            ("teach", "สอนใช้งาน", "ทีละขั้นบนมือถือ"), ("message", "ติดต่อทีม", "LINE และโทรศัพท์")]
PANEL_FILLS = [{"type": "linearGradient", "stops": ["#FFFFFFF2", "#EEF3FDF2"]}]


def menu_icon(parent, key, size=24, color=INK):
    return icon(parent, MENU_ICONS.get(key) or ICON[key], size, color)


def panel(parent, x, w, **props):
    p = box(parent, "Dropdown", w, 100, cornerRadius=20, fills=PANEL_FILLS, effects=SHADOW, sizingH="fixed",
            sizingV="hug", **props)
    stroke(p, "#FFFFFF")
    one("node.set", {"id": p, "absolute": True, "x": x, "y": 104})
    return p


def features_panel(parent, x):
    p = panel(parent, x, 820, layout="horizontal", gap=0, padding=8, crossAlign="min")
    left = col(p, "Modules", gap=0, width=232, height=316, sizingH="fixed", sizingV="fixed", padding=8,
               mainAlign="spaceBetween")
    mods = col(left, "List", gap=4, sizingH="fill")
    for i, (key, label) in enumerate(FEATURE_MODULES):
        it = row(mods, "Module / " + label, gap=12, padding=[10, 12, 10, 12], cornerRadius=999, sizingH="fill",
                 minHeight=44, fill=WHITE if i == 0 else None, effects=SHADOW if i == 0 else [])
        tile = box(it, "Icon", 28, 28, layout="horizontal", mainAlign="center", crossAlign="center",
                   cornerRadius=999, fill=BLUE_50 if i == 0 else None)
        menu_icon(tile, key, 18, BLUE if i == 0 else MUTED)
        th(it, label, 16, "Bold" if i == 0 else "Regular", INK)
    links = col(left, "Links", gap=2, sizingH="fill")
    for key, label in FEATURE_LINKS:
        it = row(links, "Link / " + label, gap=12, padding=[10, 12, 10, 12], minHeight=44)
        menu_icon(it, key, 18, MUTED)
        th(it, label, 15, "Regular", MUTED)
    right = row(p, "Content", gap=0, cornerRadius=16, fill="#FFFFFFB3", crossAlign="min")
    start = col(right, "Get started", gap=16, padding=[20, 16, 16, 16], width=300, sizingH="fixed")
    th(start, "เริ่มต้นใช้งาน", 14, "Bold", MUTED, letterSpacing="4%")
    card = col(start, "Card", gap=12, padding=[0, 0, 16, 0], cornerRadius=16, fill=WHITE, effects=SHADOW,
               sizingH="fill", clip=True)
    stroke(card)
    screen_img(card, "tile-stock-wide.png", 268, 150, 0)
    t = col(card, "Text", gap=6, padding=[0, 16, 0, 16])
    th(t, "จัดการสต็อกแยกรุ่น สี ไซซ์", 17, "Bold", INK)
    more = row(t, "More", gap=4)
    th(more, "ดูรายละเอียด", 14, "Regular", INK)
    icon(more, CHEVRON_RIGHT, 16, INK)
    fit = col(right, "Fit for", gap=4, padding=[20, 16, 16, 20], width=272, sizingH="fixed")
    th(fit, "เหมาะกับร้าน", 14, "Bold", MUTED, letterSpacing="4%")
    for key, label in FIT_FOR:
        it = row(fit, "Fit / " + label, gap=12, padding=[10, 0, 10, 0], minHeight=44)
        menu_icon(it, key, 20, BLUE)
        th(it, label, 16, "Regular", INK)


def services_panel(parent, x):
    p = panel(parent, x, 620, layout="horizontal", gap=8, padding=[24, 24, 24, 24], crossAlign="min")
    for c in range(2):
        column = col(p, "Column " + str(c + 1), gap=8, width=282, sizingH="fixed")
        for key, title, sub in SERVICES[c::2]:
            it = row(column, "Item / " + title, gap=14, padding=[8, 8, 8, 8], cornerRadius=14, sizingH="fill",
                     fill=WHITE if (c, title) == (0, "นัดดูเดโม") else None)
            circle = box(it, "Icon", 44, 44, layout="horizontal", mainAlign="center", crossAlign="center",
                         cornerRadius=999, fill=WHITE)
            stroke(circle)
            menu_icon(circle, key, 20, INK)
            t = col(it, "Text", gap=0)
            th(t, title, 16, "Bold", INK)
            th(t, sub, 14, "Regular", MUTED)


def menu_frame(name, y, active, build_panel, panel_w):
    old = run([{"command": "select.byName", "params": {"query": name}}])[0]["selection"]
    if old:
        run([{"command": "edit.delete", "params": {"ids": old}}])
    f = box(None, name, 1440, 560, layout="vertical", padding=[24, 120, 0, 120], crossAlign="center",
            sizingH="fixed", sizingV="fixed", clip=True,
            fills=[{"type": "linearGradient", "stops": ["#1650D7", "#2459DB", "#4C6BDC", "#C48AA8", "#FF9F5E"]}])
    one("node.set", {"id": f, "x": X + 1540, "y": y})
    items = floating_nav(f, active)
    item = one("node.get", {"id": items[active]})["absoluteBounds"]
    left = round(item["x"] - (X + 1540))
    x = left - 16 if active != "lang" else left + round(item["width"]) - panel_w
    x = max(40, min(1440 - 40 - panel_w, x))
    build_panel(f, x)
    return f


LANGUAGES = [("TH", "ภาษาไทย"), ("EN", "English")]


def language_panel(parent, x):
    p = panel(parent, x, 220, layout="vertical", gap=4, padding=8)
    for i, (code, label) in enumerate(LANGUAGES):
        it = row(p, "Language / " + code, gap=12, padding=[10, 12, 10, 10], cornerRadius=12, minHeight=44,
                 sizingH="fill", fill=WHITE if i == 0 else None)
        chip = box(it, "Code", 36, 26, layout="horizontal", mainAlign="center", crossAlign="center",
                   cornerRadius=6, fill=BLUE_50 if i == 0 else HOVER)
        txt(chip, code, 14, "Bold", BLUE if i == 0 else MUTED)
        lab = row(it, "Label", sizingH="fill")
        if code == "TH":
            th(lab, label, 15, "Bold", INK)
        else:
            txt(lab, label, 15, "Regular", INK)
        if i == 0:
            icon(it, CHECK, 20, BLUE)


def menus():
    menu_frame("Landing v2 — Features menu", 0, "Features", features_panel, 820)
    menu_frame("Landing v2 — Services menu", 640, "Services", services_panel, 620)
    menu_frame("Landing v2 — Language menu", 1280, "lang", language_panel, 220)
    for name in ("Landing v2 — Features menu", "Landing v2 — Services menu", "Landing v2 — Language menu"):
        export_frame(name, os.path.join(PREVIEW, name + ".png"))


def main():
    if sys.argv[1:] == ["menus"]:
        menus()
        return
    old = run([{"command": "select.byName", "params": {"query": NAME}}])[0]["selection"]
    if old:
        run([{"command": "edit.delete", "params": {"ids": old}}])

    page = box(None, NAME, 1440, 100, layout="vertical", gap=0, sizingH="fixed", sizingV="hug", fill=WHITE)
    one("node.set", {"id": page, "x": X, "y": 0})
    for build in (hero, proof_line, overview, easy, pricing, faq, closing, footer):
        build(page)
        print("built", build.__name__, flush=True)

    os.makedirs(PREVIEW, exist_ok=True)
    export_frame(NAME, os.path.join(PREVIEW, NAME + ".png"))


if __name__ == "__main__":
    main()
