"""Landing page mock-up, section 2: the hero (based on shadcn studio "Hero Section 41").

Usage: python -I design/build_landing_hero.py   (after build_landing_navbar.py)
Adds (or rebuilds) the frame "Hero — Default" in design/khonnai-landing.figcraft and exports its PNG.
Layout of hero-41 on a 5-column, 1280 container: copy (3 cols) + product shot (2 cols) on top; thumbnail
strip (3 cols) + one line of the comments carousel (2 cols) below. The plates become phones showing real
screens from design/revisions/audit-fixes-v1/khonnai-home-v1.figcraft (design/preview/landing/screens/*-screen.png).
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
import build_design_system as ds  # noqa: E402
from build_landing_navbar import (BLUE, BLUE_50, BORDER, F_TH, INK, MUTED, OUT, PREVIEW, WHITE, box, col, icon,  # noqa: E402
                                  navbar, one, row, run, txt)

NAME = "Hero — Default"
SCREENS = os.path.join(PREVIEW, "screens")
K_LOGO = os.path.join(os.path.dirname(ROOT), "build", "assets", "khonnai-k.png")
BEZEL = "#111827"
ARROW = "M3.75 9h10.5 M9 3.75l5.25 5.25L9 14.25"   # 18 grid
# hero-41 thumbnail frame (161×92)
THUMB_SHAPE = ("M0.682517 80.6118L0.501193 39.6946C0.480127 34.9409 3.80852 30.8294 8.46241 29.8603L148.426 0.713985"
               "C154.636 -0.579105 160.465 4.16121 160.465 10.504V80.7397C160.465 86.2674 155.98 90.7465 150.453 90.7397"
               "L10.6701 90.5674C5.16936 90.5607 0.706893 86.1125 0.682517 80.6118Z")
THUMBS = [("home", "หน้าโฮม"), ("stock", "สต็อก"), ("bill", "ออกบิล"), ("reserve", "การจอง"), ("history", "ประวัติขาย")]

HEADLINE = "สต็อก การจอง และบิล\nจบในข้อมูลชุดเดียว"
BODY = ("เว็บแอปบนมือถือสำหรับร้านค้าส่งชุดชั้นในและเสื้อผ้าขนาดเล็ก\n"
        "จัดการสินค้าแยกตามรุ่น สี และไซซ์ ตรวจจำนวนที่พร้อมขาย\n"
        "บันทึกการจอง และออกบิลจากข้อมูลชุดเดียวกัน\n"
        "ไม่ต้องเช็กของซ้ำ สต็อกกับบิลก็ไม่คลาดกัน")
# first slide of the comments carousel; all slides are kept in the frame's pluginData
NOTE = "ต้นแบบเปิดให้ร้านนำร่องทดลองงานหลักแล้ว\nค่าสมาชิกที่กำลังทดลอง: Free · Basic 299 · Pro 699 บาท/เดือน"
NOTE_SLIDES = [NOTE, "ขั้นตอนสั้น ตัวใหญ่ อ่านง่ายบนมือถือ\nออกแบบมาให้เจ้าของร้านใช้เองได้ทุกวัน",
               "กำลังพัฒนาฟีเจอร์เพิ่มจากผลทดสอบกับร้านจริง\nเช่น ให้ลูกค้าสั่งเองผ่านลิงก์ร้าน"]


def phone(parent, screen, h, x, y, name):
    """A device bezel around a real screen, placed absolutely; h is the outer height."""
    b = max(3, round(h * 0.022))
    sh = h - 2 * b
    sw = round(sh * 393 / 852)
    radius = round(sh * 0.065)
    p = box(parent, "Phone / " + name, sw + 2 * b, h, fill=BEZEL, cornerRadius=radius + b, clip=True)
    one("node.set", {"id": p, "x": x, "y": y})
    img = one("image.place", {"path": os.path.join(SCREENS, screen + "-screen.png"), "parent": p,
                              "x": b, "y": b, "width": sw, "height": sh, "mode": "fill"})["id"]
    one("node.set", {"id": img, "name": "Screen", "cornerRadius": radius})
    return p, sw + 2 * b


def pill(parent, label, primary):
    b = row(parent, "Button / " + label, gap=8, padding=[0, 24, 0, 24], cornerRadius=999, height=48,
            sizingV="fixed", fill=BLUE if primary else "#1650D71A")
    txt(b, label, 16, "Medium", WHITE if primary else BLUE)
    if primary:
        icon(b, ARROW, 18, WHITE)


def copy(parent):
    c = col(parent, "Copy", gap=20, width=758, height=400, sizingH="fixed", sizingV="fixed", mainAlign="center")
    txt(c, HEADLINE, 48, "Bold", INK, F_TH, lineHeight="135%")
    txt(c, BODY, 20, "Regular", MUTED, F_TH, lineHeight="165%")
    ctas = row(c, "CTAs", gap=16, paddingTop=8)
    pill(ctas, "Start for free", True)
    pill(ctas, "Schedule a Demo", False)


def product_shot(parent):
    s = box(parent, "Product shot", 498, 400)
    one("node.create", {"type": "ellipse", "parent": s, "x": 69, "y": 20, "width": 360, "height": 360,
                        "name": "Backdrop", "props": {"fill": BLUE_50}})
    phone(s, "stock", 340, 262, 40, "สต็อก")
    phone(s, "home", 400, 112, 0, "หน้าโฮม")


def thumb(parent, screen, label, selected):
    t = box(parent, "Thumb / " + label, 182, 132)
    shape = one("vector.create", {"path": THUMB_SHAPE, "x": 10, "y": 40, "parent": t,
                                  "props": {"fill": WHITE if not selected else "#1650D70D",
                                            "stroke": BLUE if selected else BORDER, "strokeWeight": 1}})["id"]
    one("node.set", {"id": shape, "name": "Frame"})
    phone(t, screen, 100, 34, 16, label)
    txt_id = txt(t, label, 14, "Bold" if selected else "Regular", BLUE if selected else MUTED, F_TH)
    one("node.set", {"id": txt_id, "x": 92, "y": 92})
    return t


def fade(parent, x, to_right):
    stops = ["#FFFFFF", "#FFFFFF00"] if to_right else ["#FFFFFF00", "#FFFFFF"]
    one("node.create", {"type": "rectangle", "parent": parent, "x": x, "y": 0, "width": 100, "height": 132,
                        "name": "Fade", "props": {"fills": [{"type": "linearGradient", "stops": stops,
                                                               "from": [0, 0.5], "to": [1, 0.5]}]}})


def strip(parent):
    s = box(parent, "Thumbnail carousel", 730, 132, clip=True)
    for i, (screen, label) in enumerate(THUMBS):
        one("node.set", {"id": thumb(s, screen, label, i == 0), "x": i * 182, "y": 0})
    fade(s, 0, True)
    fade(s, 630, False)


def note(parent):
    n = row(parent, "Comments carousel", gap=16, width=550, sizingH="fixed", height=132, sizingV="fixed",
            padding=[0, 24, 0, 24])
    av = box(n, "Avatar", 48, 48, cornerRadius=999, fill=WHITE, clip=True)
    one("node.set", {"id": av, "stroke": WHITE, "strokeWeight": 4, "strokeAlign": "inside", "effects": [
        {"type": "dropShadow", "color": "#0F172A26", "offset": [0, 6], "radius": 12, "spread": 0}]})
    one("image.place", {"path": K_LOGO, "parent": av, "x": 0, "y": 0, "width": 48, "height": 48, "mode": "fill"})
    box(n, "Separator", 2, 24, fill=BLUE, cornerRadius=999)
    txt(n, NOTE, 16, "Regular", INK, F_TH, lineHeight="160%")


def main():
    old = run([{"command": "select.byName", "params": {"query": NAME}}])[0]["selection"]
    if old:
        run([{"command": "edit.delete", "params": {"ids": old}}])

    frame = box(None, NAME, 1440, 870, layout="vertical", sizingH="fixed", sizingV="fixed", fill=WHITE)
    one("node.set", {"id": frame, "x": 0, "y": 900,
                     "pluginData": {"commentsCarouselSlides": "\n\n".join(NOTE_SLIDES)}})
    navbar(frame)
    hero = box(frame, "Hero", 1440, 790, layout="vertical", gap=64, padding=[96, 80, 96, 80],
               sizingH="fixed", sizingV="fill", fill=WHITE)
    top = row(hero, "Hero header", gap=24)
    copy(top)
    product_shot(top)
    bottom = row(hero, "Hero footer", gap=0, mainAlign="spaceBetween", width=1280, sizingH="fixed")
    strip(bottom)
    note(bottom)

    os.makedirs(PREVIEW, exist_ok=True)
    proc = subprocess.run([ds.CLI, "export", OUT, "-o", os.path.join(PREVIEW, NAME + ".png"), "--node", NAME,
                           "--format", "png", "--scale", "1"], capture_output=True, text=True, encoding="utf-8")
    print(proc.stdout + proc.stderr)


if __name__ == "__main__":
    main()
