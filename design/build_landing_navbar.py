"""Landing page mock-up, section 1: the navbar (based on React Bits Pro "Navbar 4").

Usage: python -I design/build_landing_navbar.py
Writes design/khonnai-landing.figcraft (page "01 Navbar") and PNG previews under design/preview/landing/.
Two desktop frames (1440): the default bar, and the bar with the Features panel open.
"""
import json
import os
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
import build_design_system as ds  # noqa: E402

OUT = os.environ.get("KHONNAI_LANDING_OUT") or os.path.join(ROOT, "khonnai-landing.figcraft")
PREVIEW = os.path.join(ROOT, "preview", "landing")
LOGO = os.path.join(os.path.dirname(ROOT), "build", "assets", "khonnai-blue.png")
F = ds.FONT_FAMILY
FONT_TH = os.path.join(ROOT, "fonts", "NotoSansThai[wdth,wght].ttf")
F_TH = "Noto Sans Thai"   # Thai web font (Google Fonts); not installed, so export through export_frame()

BLUE = "#1650D7"
BLUE_50 = "#EEF3FD"
INK = "#0F172A"
MUTED = "#475569"
BORDER = "#E2E8F0"
HOVER = "#F1F5F9"
WHITE = "#FFFFFF"

MENU = [("Features", True), ("Pricing", False), ("Services", True), ("Contact Us", False)]
FEATURES = [
    ("Stock tracking", "Live counts for every size and colour", "package"),
    ("Quick billing", "Issue a bill and cut stock in one tap", "receipt"),
    ("Reservations", "Hold items for a customer until pickup", "bookmark"),
    ("Sales history", "Every bill, searchable and printable", "history"),
]
# Lucide icons (24 grid, 2px stroke)
ICON = {
    "package": "M11 21.73a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8"
               "a2 2 0 0 0 1 1.73z M12 22V12 M3.29 7 12 12l8.71-5 M7.5 4.27l9 5.15",
    "receipt": "M4 2v20l2-1 2 1 2-1 2 1 2-1 2 1 2-1 2 1V2l-2 1-2-1-2 1-2-1-2 1-2-1-2 1z M16 8h-6a2 2 0 1 0 0 4h4"
               "a2 2 0 1 1 0 4H8 M12 17.5v-11",
    "bookmark": "M19 21l-7-4-7 4V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16z",
    "history": "M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8 M3 3v5h5 M12 7v5l4 2",
}
CHEVRON_DOWN = "M4 6l4 4 4-4"   # 16 grid
CHEVRON_UP = "M4 10l4-4 4 4"
ARROW = "M3.75 9h10.5 M9 3.75l5.25 5.25L9 14.25"   # 18 grid


def run(cmds, new=False):
    """Run commands in one headless session on OUT and return their results."""
    steps = [{"command": "text.loadFont", "params": {"path": p}} for p in (ds.FONT, FONT_TH)] + cmds
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(steps, f, ensure_ascii=False)
        script = f.name
    args = [ds.CLI, "run", script, "--out", OUT] + ([] if new else ["--in", OUT])
    for attempt in range(6):
        proc = subprocess.run(args, capture_output=True, text=True, encoding="utf-8")
        # os error 1224: another process (indexer / antivirus) briefly maps the file we just wrote
        if "os error 1224" not in proc.stderr + proc.stdout:
            break
        time.sleep(2 + attempt)
    os.unlink(script)
    results = []
    for line in proc.stdout.splitlines():
        if line.startswith("{"):
            r = json.loads(line)
            if not r.get("ok"):
                sys.exit(f"step failed: {r}")
            results.append(r.get("result"))
    if proc.returncode != 0:
        sys.exit(proc.stdout + proc.stderr)
    return results[2:]


def one(command, params):
    return run([{"command": command, "params": params}])[0]


def export_frame(name, path):
    """Export a top-level frame from a session that has the fonts loaded (`figcraft-cli export` does not)."""
    ids = [i for i in run([{"command": "select.byName", "params": {"query": name}}])[0]["selection"]
           if one("node.get", {"id": i}).get("name") == name]
    run([{"command": "file.export", "params": {"ids": ids[:1], "format": "png", "path": os.path.abspath(path)}}])
    print(path)


def box(parent, name, w=None, h=None, **props):
    p = {"type": "frame", "name": name, "props": {"fill": None, **props}}
    if parent:
        p["parent"] = parent
    if w:
        p["width"] = w
    if h:
        p["height"] = h
    return one("node.create", p)["id"]


def row(parent, name, gap=0, **props):
    return box(parent, name, **{"layout": "horizontal", "gap": gap, "crossAlign": "center",
                                "sizingH": "hug", "sizingV": "hug", **props})


def col(parent, name, gap=0, **props):
    return box(parent, name, **{"layout": "vertical", "gap": gap, "sizingH": "hug", "sizingV": "hug", **props})


def txt(parent, text, size=16, style="Medium", color=INK, family=F, **props):
    return one("text.create", {"text": text, "x": 0, "y": 0, "parent": parent,
                               "props": {"fontFamily": family, "fontStyle": style, "fontSize": size,
                                         "fill": color, "lineHeight": "150%", **props}})["id"]


def icon(parent, path, size, color, weight=2):
    """A stroked icon on a fixed size×size box so auto layout keeps its grid."""
    holder = box(parent, "Icon", w=size, h=size, clip=False)
    one("vector.create", {"path": path, "x": 0, "y": 0, "parent": holder,
                          "props": {"fill": None, "stroke": color, "strokeWeight": weight,
                                    "strokeCap": "round", "strokeJoin": "round"}})
    return holder


def menu_item(parent, label, dropdown, active=False):
    item = row(parent, "Menu / " + label, gap=4, padding=[10, 14, 10, 14], cornerRadius=8,
               minHeight=44, fill=HOVER if active else None)
    txt(item, label, 16, "Medium", BLUE if active else INK)
    if dropdown:
        icon(item, CHEVRON_UP if active else CHEVRON_DOWN, 16, BLUE if active else MUTED)
    return item


def button(parent, label, primary):
    b = row(parent, "Button / " + label, gap=8, padding=[0, 20, 0, 20], cornerRadius=10, height=44,
            sizingV="fixed", fill=BLUE if primary else WHITE)
    if not primary:
        one("node.set", {"id": b, "stroke": "#CBD5E1", "strokeWeight": 1, "strokeAlign": "inside"})
    txt(b, label, 16, "Medium", WHITE if primary else INK)
    if primary:
        icon(b, ARROW, 18, WHITE)
    return b


def navbar(frame, open_menu=None):
    bar = box(frame, "Navbar", 1440, 80, layout="horizontal", mainAlign="spaceBetween", crossAlign="center",
              padding=[0, 80, 0, 80], sizingH="fixed", sizingV="fixed", fill=WHITE)
    one("node.set", {"id": bar, "stroke": BORDER, "strokeAlign": "inside", "strokeTopWeight": 0,
                     "strokeRightWeight": 0, "strokeLeftWeight": 0, "strokeBottomWeight": 1})
    left = row(bar, "Left", gap=40)
    logo = one("image.place", {"path": LOGO, "parent": left, "width": 147, "height": 32, "mode": "fit"})["id"]
    one("node.set", {"id": logo, "name": "Logo / khonnai"})
    menu = row(left, "Menu", gap=4)
    items = {label: menu_item(menu, label, dd, label == open_menu) for label, dd in MENU}
    right = row(bar, "Actions", gap=12)
    button(right, "Sign up", False)
    button(right, "Schedule a Demo", True)
    return bar, items


def features_panel(frame, x, y):
    panel = col(frame, "Dropdown / Features", gap=4, padding=8, cornerRadius=16, fill=WHITE, width=380,
                sizingH="fixed")
    one("node.set", {"id": panel, "x": x, "y": y, "stroke": BORDER, "strokeWeight": 1, "strokeAlign": "inside",
                     "effects": [{"type": "dropShadow", "color": "#0F172A1F", "offset": [0, 16],
                                  "radius": 40, "spread": -8}]})
    for i, (title, desc, ic) in enumerate(FEATURES):
        it = row(panel, "Item / " + title, gap=14, padding=12, cornerRadius=12, sizingH="fill",
                 crossAlign="min", fill=HOVER if i == 0 else None)
        tile = box(it, "Icon tile", 40, 40, layout="horizontal", mainAlign="center", crossAlign="center",
                   cornerRadius=10, fill=BLUE_50)
        icon(tile, ICON[ic], 24, BLUE)
        text = col(it, "Text", gap=2)
        txt(text, title, 16, "Medium", INK)
        txt(text, desc, 14, "Regular", MUTED)
    return panel


def main():
    run([], new=True)
    page_bg = "#F8FAFC"

    a = box(None, "Navbar — Default", 1440, 200, fill=page_bg)
    navbar(a)

    b = box(None, "Navbar — Features open", 1440, 460, fill=page_bg)
    one("node.set", {"id": b, "x": 0, "y": 320, "clip": True})
    bar, items = navbar(b, "Features")
    item = one("node.get", {"id": items["Features"]})["absoluteBounds"]
    features_panel(b, item["x"], 80 + 8)

    os.makedirs(PREVIEW, exist_ok=True)
    proc = subprocess.run([ds.CLI, "export", OUT, "-o", PREVIEW, "--format", "png", "--scale", "1"],
                          capture_output=True, text=True, encoding="utf-8")
    print(proc.stdout + proc.stderr)


if __name__ == "__main__":
    main()
