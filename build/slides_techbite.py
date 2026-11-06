# Slide content for the TED Youth Startup Fund by KX-TECHBITE application (PDF pitch deck).
# Section order follows TECHBITE_Pitchdeck.pptx: 7 main topics, then Backup slides and Reference.
# Figures come from Milestone2_Report_Group3.pdf; the funding ask and its 5-year model were
# recomputed for a 150,000-baht grant (see FIN / SCEN below and the notes on each slide).
# Build: python build/build_deck.py techbite  ->  techbite-pitch.html
import re

import slides_khonnai as m2

OUT_NAME = 'techbite-pitch.html'
TITLE = 'Khonnai · TED Youth Startup Fund · KX-TECHBITE'
BRAND = 'TED Youth Startup Fund · KX-TECHBITE'
NSEC = 8
PHOTO_PREFIX = 'tb-team-'  # build/assets/tb-team-1..N.(jpg|png|webp), in TEAM order
ASSETS = {'{MVP}': ('mvp-screens-v2.png', 'image/png'),  # MVP screens (audit-fixes-v1): home, stock, bill, booking
          '{QRK}': ('qr-khonnai.svg', 'image/svg+xml')}


def reuse(i, sec, name):
    """A Milestone 2 slide moved into this deck's section numbering."""
    s = m2.SLIDES[i]
    s = re.sub(r'data-sec="\d+"', f'data-sec="{sec}"', s, count=1)
    return re.sub(r'data-secname="[^"]*"', f'data-secname="{name}"', s, count=1)


SLIDES = []

# ---------------------------------------------------------------- 00 Project Title & Applicant
SLIDES.append('''
<section class="s-cover" data-chrome="none" data-silk="cover" data-cubes="cover" data-sec="00" data-secname="Khonnai">
  <div class="gridbg" style="opacity:.55"></div>
  <div class="abs" style="left:150px;top:250px">
    <div class="kick in" style="--i:1">ted_youth_startup_fund --kx-techbite</div>
    <div class="h1 wm in" style="--i:2;margin-top:50px;font-size:172px"><img class="uh-logo" src="{LOGO}" alt="Khonnai" style="display:block;height:150px;width:auto"></div>
    <div class="h3 in" style="--i:3;margin-top:48px;font-weight:400;color:var(--ink-2);white-space:nowrap">คนใน · ระบบบริหารสต็อก การจองสินค้า<br>และการออกบิลบนมือถือ</div>
    <div class="lede in" style="--i:5;margin-top:36px;color:var(--ink)">สำหรับร้านค้าส่งชุดชั้นในและเสื้อผ้าขนาดเล็ก</div>
  </div>
  <div class="abs in soft" style="left:150px;bottom:92px;--i:6;display:grid;grid-template-columns:auto auto;gap:14px 28px;align-items:center">
    <span class="pill solid">ผู้เสนอโครงการ</span><span class="h4" style="font-size:32px">{APPLICANT}</span>
    <span class="pill">ทีม</span><span class="h4" style="font-size:32px">{TEAM_LINE}</span>
  </div>
  <div class="abs cv-clock in soft" style="right:150px;bottom:104px;--i:8"><i></i>Bangkok&nbsp; <b>--:--:--</b></div>
  <aside class="notes">
PROJECT TITLE &amp; APPLICANT: Khonnai (คนใน) ระบบบริหารสต็อก การจองสินค้า และการออกบิลบนมือถือ สำหรับร้านค้าส่งชุดชั้นในและเสื้อผ้าขนาดเล็ก
ระยะธุรกิจ: Pre-Seed (Ideation → MVP) มี MVP2 ทดสอบกับร้านนำร่องแล้ว ขอทุนเพื่อพัฒนา MMP และทดสอบตลาด
  </aside>
</section>''')

# ---------------------------------------------------------------- 01 Problem / Pain Point (ch.1.3, table 4.1)
# Validation strip replaces the C1 note: interview -> owner tested MVP2 herself (ch.3, ch.12, appendix A)
problem = reuse(1, '01', 'Problem').replace(
    'ปัญหาหลัก 4 ข้อ<br><span class="g">ของร้านค้าส่ง</span>', 'ปัญหาจริง 4 ข้อ<br><span class="g">ที่ validate แล้ว.</span>')
problem = re.sub(r'  <div class="abs in" style="left:150px;top:900px;--i:8">.*?</div></div>\n', '''  <div class="abs row" style="left:150px;right:150px;top:850px;gap:24px">
    <div class="vl-note in" style="position:static;flex:1;font-size:22px;--i:8"><i data-i="mic"></i><span><b>สัมภาษณ์</b> เจ้าของร้านค้าส่งชุดชั้นใน ร้านครอบครัวบนตึก 3 ชั้น ข้อมูลอยู่ในความจำ สมุด และ LINE</span></div>
    <div class="vl-note in" style="position:static;flex:1;font-size:22px;--i:9"><i data-i="check"></i><span><b>ทดสอบ MVP2</b> เจ้าของลงมือใช้เอง 30 นาที (28 ต.ค. 2569) ยืนยันปัญหา และได้ 7 ข้อปรับปรุง</span></div>
    <div class="vl-note in" style="position:static;flex:1;font-size:22px;--i:10"><i data-i="alert"></i><span><b>ข้อจำกัด</b> ผู้ใช้อายุ 40+ ไม่คุ้นเทคโนโลยี ระบบต้องไม่ทำให้งานเดิมยุ่งขึ้น</span></div>
  </div>
''', problem, count=1, flags=re.S)
problem = problem.replace('  <div class="flow">', '''  <div class="abs" style="left:1070px;top:186px;width:700px">
    <div class="small in" style="--i:2;font-size:22px;color:var(--ink-2)">โอกาสที่มองเห็น: ธุรกิจเล็กสำคัญ แต่ยังใช้ดิจิทัลน้อย</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:14px">
      <div class="in" style="--i:3"><div class="num g" style="font-size:88px">35.2%</div><div class="small" style="margin-top:12px;font-size:21px">ของ GDP ไทยมาจาก MSME<br>(สสว. ปี 2566)</div></div>
      <div class="in" style="--i:4"><div class="num g" style="font-size:88px">8%</div><div class="small" style="margin-top:12px;font-size:21px">ของ SME ใช้ดิจิทัลปรับปรุงการผลิต เช่น ERP (สสว. 2568, 2,704 ราย)</div></div>
    </div>
  </div>
  <div class="flow">''', 1)
assert 'ทดสอบ MVP2' in problem and '35.2%' in problem
SLIDES.append(problem)

# ---------------------------------------------------------------- 02 Business Overview (ch.2, 9, 12) — what the business is + impact
SNAP = [('users', 'ลูกค้า', 'ร้านค้าส่งชุดชั้นใน/เสื้อผ้าขนาดเล็ก เจ้าของวัย 40+ ดูแลร้านเอง'),
        ('cube', 'ผลิตภัณฑ์', 'แอปบนมือถือ รวมสต็อก ใบจอง และบิลเงินสดในข้อมูลชุดเดียว'),
        ('tag', 'รายได้', 'ค่าสมาชิกรายเดือน Free / 299 / 699 บาท'),
        ('check', 'ระยะธุรกิจ', 'Pre-Seed · MVP2 ทดสอบกับร้านนำร่องแล้ว')]
IMPACT = [('เดินขึ้นตึก 3 ชั้นทุกครั้งที่ลูกค้าถาม', 'เช็กยอดเหลือขายจากมือถือได้ทันที'),
          ('หน้าร้านกับ LINE ใช้สต็อกคนละชุด', 'ใบจองกันสต็อกชุดเดียวกัน ไม่ขายซ้ำ'),
          ('บิลเขียนมือ คำนวณเอง ถ่ายรูปส่ง', 'บิลเงินสดคำนวณให้ ตัดสต็อกเมื่อยืนยัน'),
          ('ความรู้สต็อกอยู่ในหัวเจ้าของคนเดียว', 'ข้อมูลที่ผู้ช่วยหรือคนรุ่นถัดไปทำต่อได้')]
snap_cards = ''.join(
    f'<div class="card glow in" style="--i:{3 + k};padding:26px 28px"><div class="row" style="align-items:center;gap:16px"><i class="ic sm" data-i="{ic}"></i><div class="ct" style="font-size:28px">{t}</div></div>'
    f'<div class="cb" style="font-size:21px;margin-top:14px">{d}</div></div>' for k, (ic, t, d) in enumerate(SNAP))
impact_cards = ''.join(
    f'<div class="card in" style="--i:{8 + k};padding:24px 28px"><div class="small" style="font-size:20px;text-decoration:line-through;text-decoration-color:rgba(255,128,50,.7)">{a}</div>'
    f'<div style="margin:10px 0 8px;font:600 26px/1 Poppins;color:var(--web3)">↓</div><div style="font:500 26px/1.3 Poppins;color:#fff">{b}</div></div>' for k, (a, b) in enumerate(IMPACT))
SLIDES.append('''
<section data-silk="center" data-cubes="none" data-sec="02" data-secname="Business Overview">
  <div class="abs" style="left:150px;top:180px">
    <div class="kick in" style="--i:1">business_overview</div>
    <div class="h2 sm in" style="--i:2;margin-top:24px">ระบบหลังร้าน<br><span class="g">ของร้านค้าส่ง.</span></div>
  </div>
  <div class="abs body in" style="left:1000px;top:226px;width:770px;font-size:28px;--i:2">Khonnai ทำให้ร้านค้าส่งขนาดเล็กรู้ยอดของที่ขายได้จริง รับจอง และออกบิลจากมือถือเครื่องเดียว <span class="b">โดยไม่ต้องเปลี่ยนวิธีขายเดิม</span></div>
  <div class="abs" style="left:150px;right:150px;top:440px;display:grid;grid-template-columns:repeat(4,1fr);gap:24px">''' + snap_cards + '''</div>
  <div class="abs in" style="left:150px;top:672px;--i:7"><span class="pill w3"><span class="dot"></span>ผลกระทบ (Impact) ต่อการทำงานของร้าน</span></div>
  <div class="abs" style="left:150px;right:150px;top:738px;display:grid;grid-template-columns:repeat(4,1fr);gap:24px">''' + impact_cards + '''</div>
  <aside class="notes">
BUSINESS OVERVIEW (บทที่ 2 Vision, บทที่ 9 Lean Canvas, บทที่ 12 Traction)
ภาพรวม: ลูกค้า · ผลิตภัณฑ์ · รายได้ · ระยะธุรกิจ (Pre-Seed: มี MVP2 ที่ทดสอบกับเจ้าของร้านจริงเมื่อ 28 ต.ค. 2569 ยังไม่มีลูกค้าจ่ายเงิน)
Impact ก่อน → หลัง จากปัญหา P1–P4 ที่ validate กับร้านนำร่อง ระยะยาวคือเปลี่ยนความจำของเจ้าของร้านเป็นข้อมูลที่ส่งต่อได้ (บทที่ 2.3)
  </aside>
</section>''')

# ---------------------------------------------------------------- 02b Market Opportunity: TAM · SAM · SOM (ch.6.4)
SLIDES.append('''
<section data-silk="center" data-cubes="none" data-sec="02" data-secname="Business Overview">
  <div class="abs" style="left:150px;top:180px">
    <div class="kick in" style="--i:1">market_opportunity</div>
    <div class="h2 sm in" style="--i:2;margin-top:24px">ขนาดตลาด<br><span class="g">TAM · SAM · SOM.</span></div>
  </div>
  <div class="pod ai" style="left:150px;bottom:150px">
    <div class="amt in" style="left:0;top:180px;--i:5">5,696<small>กิจการ</small></div><div class="bar" style="left:0;height:290px;animation-delay:.5s"><div class="pl">SAM</div><div class="itm"><span>กทม. + ชลบุรี</span><br>20.44 ล้าน/ปี</div></div>
    <div class="amt in" style="left:245px;top:90px;--i:4">8,770<small>กิจการ</small></div><div class="bar" style="left:245px;height:380px;animation-delay:.3s"><div class="pl">TAM</div><div class="itm"><span>ทั่วไทย</span><br>31.47 ล้าน/ปี</div></div>
    <div class="amt in" style="left:490px;top:260px;--i:6">15<small>ร้าน</small></div><div class="bar" style="left:490px;height:210px;animation-delay:.7s"><div class="pl">SOM</div><div class="itm"><span>สิ้นปีแรก</span><br>68,220/ปี</div></div>
  </div>
  <div class="ubl" style="left:1070px;top:200px;width:700px;gap:30px">
    <div class="ubl-i in" style="--i:7"><i data-i="globe"></i><div><b style="font-size:32px">TAM · 8,770 กิจการ</b><span style="font-size:22px">ค้าส่งเสื้อผ้าขนาด Micro + Small ทั่วไทย ≈ 31.47 ล้านบาท/ปี</span></div></div>
    <div class="ubl-i in" style="--i:8"><i data-i="pin"></i><div><b style="font-size:32px">SAM · 5,696 กิจการ</b><span style="font-size:22px">กรุงเทพฯ + ชลบุรี พื้นที่ที่ทีมลงพื้นที่ได้จริง ≈ 20.44 ล้านบาท/ปี</span></div></div>
    <div class="ubl-i in" style="--i:9"><i data-i="users"></i><div><b style="font-size:32px">SOM · 15 → 124 ร้าน</b><span style="font-size:22px">ร้านที่จ่ายเงินอยู่ สิ้นปีแรก 15 ร้าน → สิ้นปีที่ 5 124 ร้าน (2.2% ของ SAM) หลังหักร้านที่ยกเลิกแล้ว</span></div></div>
  </div>
  <div class="vl-note in" style="left:1070px;top:700px;width:700px;font-size:21px;--i:10"><i data-i="alert"></i><span>ฐาน สสว. เป็นค้าส่งเสื้อผ้าโดยรวม ยังไม่แยกชุดชั้นใน และยังไม่ได้ยืนยันว่าทุกร้านใช้สมุดหรือ LINE · ขั้นถัดไปคือสำรวจร้านภายนอก 3–5 ร้าน</span></div>
  <div class="abs small in" style="left:150px;top:942px;--i:11;font-size:18px">ที่มา: สสว. ปี 2567 · TSIC 46414 · มูลค่า TAM/SAM = จำนวนกิจการ × 299 บาท (Basic) × 12 เดือน · SOM = ร้านจ่ายเงินจากโมเดลกรณี Base × 379 บาท × 12 เดือน</div>
  <aside class="notes">
MARKET OPPORTUNITY (บทที่ 6.4) TAM 8,770 กิจการ ≈ 31.47 ล้านบาท/ปี · SAM 5,696 กิจการ (กทม. + ชลบุรี) ≈ 20.44 ล้านบาท/ปี · SOM สิ้นปีแรก 15 ร้าน × 379 × 12 = 68,220 บาท/ปี
SOM ใช้ตัวเลขเดียวกับประมาณการ 5 ปี (Backup): ร้านจ่ายเงินสิ้นปี 15 / 48 / 85 / 110 / 124 หลังหัก churn 5%/เดือน · 124 / 5,696 ≈ 2.2% ของ SAM
ข้อจำกัด: ยังไม่ได้ validate ว่ากิจการทั้งหมดใช้สมุด/LINE จึงไม่เขียนเป็นข้อเท็จจริงบนสไลด์
  </aside>
</section>''')

# ---------------------------------------------------------------- 03 Technology Solution / Innovative Feature (current MVP2 screens)
SLIDES.append('''
<section data-silk="right" data-cubes="none" data-sec="03" data-secname="Technology">
  <div class="abs" style="left:150px;top:180px">
    <div class="kick in" style="--i:1">technology --innovative_features</div>
    <div class="h2 sm in" style="--i:2;margin-top:24px">"คนใน" ที่จำสต็อก<br><span class="g">แทนเจ้าของร้าน.</span></div>
  </div>
  <div class="abs in grow" style="left:130px;top:450px;--i:3"><img src="{MVP}" alt="หน้าจอ Khonnai MVP: หน้าโฮม สต็อก บิลเงินสด และรายการจอง" style="display:block;width:880px;height:auto;filter:drop-shadow(0 24px 50px rgba(0,0,0,.45))"></div>
  <div class="ubl" style="left:1060px;top:190px;width:710px;gap:26px">
    <div class="ubl-i in" style="--i:4"><i data-i="list"></i><div><b style="font-size:30px">หน้าโฮมสรุปร้านในจอเดียว</b><span style="font-size:21px">รายได้วันนี้ ออเดอร์รอรับของ และของที่ต้องเติม พร้อมปุ่มลัด ออกบิล · ดูสต็อก · เพิ่มรุ่น · จอง</span></div></div>
    <div class="ubl-i in" style="--i:5"><i data-i="doc"></i><div><b style="font-size:30px">ออกบิล 3 ขั้น</b><span style="font-size:21px">เลือกสินค้า → ยืนยันออเดอร์ → ได้บิลเงินสดตามแบบฟอร์มของร้าน ตัดสต็อกให้ทันที</span></div></div>
    <div class="ubl-i in" style="--i:6"><i data-i="cal"></i><div><b style="font-size:30px">ใบจองที่กันสต็อก</b><span style="font-size:21px">จองจากหน้าร้านหรือ LINE ใช้สต็อกชุดเดียว กด "ลูกค้ารับของแล้ว" จึงตัดจริง</span></div></div>
    <div class="ubl-i in" style="--i:7"><i data-i="lock"></i><div><b style="font-size:30px">ตัดสต็อกแบบ transaction</b><span style="font-size:21px">ยืนยันบิลได้เมื่อ on_hand − reserved ≥ n เท่านั้น ไม่พอยกเลิกทั้งบิล กันขายชิ้นสุดท้ายซ้ำ</span></div></div>
    <div class="ubl-i in" style="--i:8"><i data-i="heart"></i><div><b style="font-size:30px">ออกแบบสำหรับวัย 40+</b><span style="font-size:21px">ตัวเลขใหญ่ เพิ่มรุ่นใหม่ได้ในหน้าเดียว พิมพ์ชื่อสีแล้วสีขึ้นเอง บอกช่องที่ยังกรอกไม่ครบ</span></div></div>
  </div>
  <div class="vl-note in" style="left:1060px;top:880px;width:710px;font-size:21px;--i:10"><i data-i="spark"></i><span><b>MVP</b> ออกแบบใหม่จากผลทดสอบกับเจ้าของร้านนำร่อง 28 ต.ค. 2569</span></div>
  <aside class="notes">
TECHNOLOGY SOLUTION / INNOVATIVE FEATURE: หน้าจอจาก MVP2 เวอร์ชันล่าสุด (หลังทดสอบกับร้านนำร่อง) — สต็อกของรุ่น · ออกบิล · ใบจอง
ตัดสต็อก (บทที่ 14.5): UPDATE variants SET on_hand = on_hand - n WHERE id = ? AND on_hand - reserved >= n ภายใน transaction เดียวกับการสร้างบิล ถ้าไม่สำเร็จ rollback ทั้งบิล และบันทึก stock_movements ทุกครั้ง
  </aside>
</section>''')

# ---------------------------------------------------------------- 03b Technology stack + research used (ch.14, references)
STACK = [('users', 'ผู้ใช้', 'เจ้าของร้าน + ผู้ช่วย<br>ผ่านเบราว์เซอร์บนมือถือ'),
         ('code', 'Web App (PWA)', 'React · TypeScript<br>Tailwind CSS · Vercel'),
         ('shield', 'Supabase', 'Auth · PostgreSQL<br>RPC แบบ transaction<br>Row-Level Security')]
stack_boxes = ''.join(
    (f'<div class="in" style="--i:{4 + k};display:grid;place-items:center;font:600 40px/1 Poppins;color:var(--web3)">→</div>' if k else '')
    + f'<div class="card glow{" w3" if k == 2 else ""} in" style="--i:{4 + k};padding:28px 26px"><i class="ic sm" data-i="{ic}"></i><div class="ct" style="font-size:28px;margin-top:18px">{t}</div><div class="cb" style="font-size:21px;margin-top:10px">{d}</div></div>'
    for k, (ic, t, d) in enumerate(STACK))
RESEARCH = [('Usability for Older Adults', 'Nielsen Norman Group (Kane, 2019)', 'ตัวอักษรและปุ่มใหญ่ ลดขั้นตอน ภาษาตรงไปตรงมา'),
            ('Usability Testing 101', 'Nielsen Norman Group (Moran, 2019)', 'ให้เจ้าของร้านลงมือใช้เอง แล้วเก็บข้อค้นพบ'),
            ('Test Card · Learning Card', 'Strategyzer (Osterwalder, Amarsy)', 'ตั้งสมมติฐาน วัดผล และสรุปบทเรียนทุกรอบ'),
            ('C4 Model · MoSCoW', 'Brown · Agile Business Consortium', 'ออกแบบสถาปัตยกรรม MMP และจัดลำดับฟีเจอร์')]
research_items = ''.join(
    f'<div class="in" style="--i:{8 + k}"><div style="font:600 26px/1.2 Poppins;color:#fff">{t}</div><div class="mono" style="margin-top:6px;font-size:17px;color:var(--web3)">{src}</div><div class="small" style="margin-top:6px;font-size:20px">→ {use}</div></div>'
    for k, (t, src, use) in enumerate(RESEARCH))
SLIDES.append('''
<section data-silk="right" data-cubes="none" data-sec="03" data-secname="Technology">
  <div class="abs" style="left:150px;top:180px">
    <div class="kick in" style="--i:1">tech_stack --research</div>
    <div class="h2 sm in" style="--i:2;margin-top:24px">เทคโนโลยี<br><span class="g">และงานวิจัยที่ใช้.</span></div>
  </div>
  <div class="abs in" style="left:150px;top:440px;--i:3"><span class="pill ai"><span class="dot"></span>สถาปัตยกรรม MMP (C4 · Container)</span></div>
  <div class="abs" style="left:150px;top:506px;width:1000px;display:grid;grid-template-columns:1fr 50px 1fr 50px 1fr;align-items:stretch">''' + stack_boxes + '''</div>
  <div class="vl-note in" style="left:150px;top:868px;width:1000px;font-size:20px;--i:7"><i data-i="send"></i><span><b>เชื่อมต่อ</b> LINE (ร้านแชร์บิล PDF) · Stripe (เก็บค่าสมาชิก) · Storage เก็บรูปและไฟล์บิล · สำรองรายวัน + pg_dump รายสัปดาห์ (RPO ≤ 24 ชม.)</span></div>
  <div class="abs in" style="left:1250px;top:200px;--i:7"><span class="pill w3"><span class="dot"></span>งานวิจัย / แนวคิดที่นำมาต่อยอด</span></div>
  <div class="abs" style="left:1250px;top:276px;width:520px;display:grid;gap:26px">''' + research_items + '''</div>
  <aside class="notes">
TECHNOLOGY STACK (บทที่ 14) MVP2 ปัจจุบัน: HTML, CSS, JavaScript เก็บข้อมูลในเบราว์เซอร์ ทดสอบด้วย smoke test (Node.js + Playwright)
MMP ที่ขอทุน: React + TypeScript + Tailwind CSS (PWA) บน Vercel · Supabase Auth, PostgreSQL (RPC: confirm_bill, create_reservation, receive_goods, cancel_bill, update_price ทำงานใน transaction เดียว), Storage · RLS ตาม shop_id · บทบาท owner/assistant · สำรองข้อมูลรายวัน 7 วัน + pg_dump รายสัปดาห์
เหตุผล (14.3): TypeScript สร้าง type จาก schema ลดข้อผิดพลาดการคำนวณสต็อก · Tailwind คุมขนาดปุ่ม/ตัวอักษรให้สม่ำเสมอสำหรับผู้ใช้สูงอายุ · PostgreSQL เป็นมาตรฐานเปิด ลดการผูกขาดผู้ให้บริการ
งานวิจัยที่ใช้: NN/g Usability for Older Adults, Usability Testing 101, Strategyzer Test/Learning Card, C4 Model, MoSCoW (เอกสารอ้างอิงในรีพอร์ต)
  </aside>
</section>''')

# ---------------------------------------------------------------- 04 Product Positioning (ch.10.2–10.4)
# Positions are the team's assessment from ch.10.3, not a measured survey.
MAP = [  # (label, x %, y %, highlight) — x: ease for 40+ owners, y: stock-reservation-bill fit for wholesale
    ('Khonnai', 74, 14, True), ('ZORT', 30, 30, False), ('Page365', 38, 62, False),
    ('FlowAccount', 22, 74, False), ('LINE MyShop', 62, 66, False), ('สมุด + LINE', 74, 88, False)]
dots = ''.join(
    f'<div class="in" style="position:absolute;left:{x}%;top:{y}%;transform:translate(-50%,-50%);--i:{4 + k};display:flex;align-items:center;gap:12px;white-space:nowrap">'
    + (f'<img src="{{KICON}}" alt="" style="width:54px;height:54px;border-radius:50%;box-shadow:0 0 30px rgba(255,128,50,.6)"><b style="font:600 32px/1 Poppins;color:#fff">{t}</b>'
       if hi else f'<i style="width:20px;height:20px;border-radius:50%;background:rgba(130,165,255,.85);display:block"></i><span style="font:500 24px/1 Poppins;color:var(--ink-2)">{t}</span>')
    + '</div>' for k, (t, x, y, hi) in enumerate(MAP))
SLIDES.append('''
<section data-silk="center" data-cubes="none" data-sec="04" data-secname="Positioning">
  <div class="abs" style="left:150px;top:180px">
    <div class="kick in" style="--i:1">product_positioning</div>
    <div class="h2 sm in" style="--i:2;margin-top:24px">ออกแบบให้ง่าย<br><span class="g">เฉพาะทางค้าส่ง.</span></div>
  </div>
  <div class="abs in" style="left:150px;top:470px;width:820px;height:420px;border-left:2px solid var(--line-2);border-bottom:2px solid var(--line-2);--i:3">
    <div style="position:absolute;left:50%;top:0;bottom:0;border-left:1px dashed var(--line-2)"></div>
    <div style="position:absolute;top:50%;left:0;right:0;border-top:1px dashed var(--line-2)"></div>
''' + dots + '''
    <div class="small" style="position:absolute;right:0;bottom:-40px;font-size:20px">ความง่ายสำหรับวัย 40+ (ทีมประเมิน) →</div>
    <div class="small" style="position:absolute;left:-14px;top:-40px;font-size:20px">↑ เชื่อมสต็อก · การจอง · บิล แบบค้าส่ง</div>
  </div>
  <div class="ubl" style="left:1080px;top:300px;width:690px;gap:26px">
    <div class="ubl-i in" style="--i:10"><i data-i="heart"></i><div><b>ออกแบบให้ใช้ง่าย</b><span>ระบบทั่วไปฟีเจอร์กว้าง หน้าจอเป็นตาราง · Khonnai ทำทีละขั้น ภาษาไทยตรงไปตรงมา (ยังไม่ได้ทดสอบเทียบกับคู่แข่ง)</span></div></div>
    <div class="ubl-i in" style="--i:11"><i data-i="cube"></i><div><b>เฉพาะทางค้าส่ง</b><span>สต็อกแพ็ก/โหลตามรุ่น ไซซ์ สี และการจองที่หักสต็อกร่วมกับบิล</span></div></div>
    <div class="ubl-i in" style="--i:12"><i data-i="tag"></i><div><b>ราคาเข้าถึงได้</b><span>Khonnai Basic 299 · ZORT Starter 600 · Page365 Solo 799 · FlowAccount Pro 299 บาท/เดือน (ราคารายเดือน)</span></div></div>
    <div class="ubl-i in" style="--i:13"><i data-i="key"></i><div><b>Unfair advantage</b><span>เข้าถึงร้านค้าส่งจริงผ่านธุรกิจครอบครัว เรียนรู้จากผู้ใช้จริงได้เร็ว</span></div></div>
  </div>
  <div class="abs small in" style="left:150px;top:950px;width:1620px;--i:14;font-size:17px">ตำแหน่งบนแผนภาพเป็นการประเมินของทีมจากเอกสารผู้ให้บริการ (บทที่ 10.3) ไม่ใช่ผลทดสอบให้ผู้ใช้กลุ่มเดียวกันใช้ทุกระบบ · ราคาจากเว็บไซต์ทางการ ตรวจ 28 ต.ค. 2569 ฟีเจอร์แต่ละแพ็กเกจต่างกัน</div>
  <aside class="notes">
PRODUCT POSITIONING (บทที่ 10.2–10.4)
แกนนอน: ความง่ายสำหรับเจ้าของร้านวัย 40+ · แกนตั้ง: ความเหมาะกับขั้นตอนค้าส่ง (สต็อกแพ็กตามรุ่น/ไซซ์/สี + การจอง + บิล ในข้อมูลชุดเดียว)
ไม่กล่าวอ้างว่าคู่แข่งทำไม่ได้: ZORT รองรับสี/ไซซ์ FlowAccount Pro ราคา 299 เท่ากัน จุดต่างคือความง่ายและความเฉพาะทาง
  </aside>
</section>''')

# ---------------------------------------------------------------- 05 Business Model / Revenue Model (ch.9, 13, table 14.1)
SLIDES.append('''
<section data-silk="right" data-cubes="none" data-sec="05" data-secname="Business Model">
  <div class="abs" style="left:150px;top:180px">
    <div class="kick in" style="--i:1">business_model --subscription</div>
    <div class="h2 sm in" style="--i:2;margin-top:24px">รายได้ค่าสมาชิก<br><span class="g">รายเดือน.</span></div>
  </div>
  <div class="abs in" style="right:150px;top:206px;text-align:right;--i:3"><div class="h4" style="font-size:34px">ราคาเฉลี่ย 379 บาท/ร้าน/เดือน</div><div class="small" style="margin-top:6px">สมมติ Basic 80% : Pro 20% · รายปีลด 10% · ยังต้องทดสอบความเต็มใจจ่าย</div></div>
  <div class="abs" style="left:150px;right:150px;top:440px;display:grid;grid-template-columns:repeat(3,1fr);gap:28px">
    <div class="card glow in" style="--i:4;padding:34px 38px"><div class="ct" style="font-size:38px">Free · 0 บาท</div><div class="cb" style="font-size:24px">20 รหัสสินค้า · 50 บิล/เดือน<br>ให้ร้านลองใช้ก่อนจ่าย</div></div>
    <div class="card glow in" style="--i:5;padding:34px 38px"><div class="ct" style="font-size:38px">Basic · 299 บาท</div><div class="cb" style="font-size:24px">200 รหัสสินค้า · 500 บิล/เดือน<br>ร้านค้าส่งทั่วไป</div></div>
    <div class="card glow w3 in" style="--i:6;padding:34px 38px"><div class="ct" style="font-size:38px">Pro · 699 บาท</div><div class="cb" style="font-size:24px">1,000 รหัสสินค้า · 2,000 บิล/เดือน<br>ร้านที่มียอดขายสูง</div></div>
  </div>
  <div class="abs" style="left:150px;right:150px;top:720px;display:grid;grid-template-columns:repeat(3,1fr);gap:28px">
    <div class="ubl-i in" style="--i:7;align-items:flex-start"><i data-i="users"></i><div><b style="font-size:30px">ลูกค้าเป้าหมาย</b><span style="font-size:22px">เจ้าของร้านค้าส่งชุดชั้นใน/เสื้อผ้าขนาดเล็ก วัย 40+ ใน กทม. และชลบุรี</span></div></div>
    <div class="ubl-i in" style="--i:8;align-items:flex-start"><i data-i="send"></i><div><b style="font-size:30px">ช่องทาง</b><span style="font-size:22px">ร้านแนะนำต่อในเครือข่าย · ลงพื้นที่หน้าร้าน · LINE OA และกลุ่มผู้ค้าส่ง</span></div></div>
    <div class="ubl-i in" style="--i:9;align-items:flex-start"><i data-i="trophy"></i><div><b style="font-size:30px">ส่วนแบ่งตลาด</b><span style="font-size:22px">สิ้นปีที่ 5 ราว 124 ร้านจ่ายเงิน (2.2% ของ SAM) · คุ้มค่าเซิร์ฟเวอร์ที่ 7 ร้าน</span></div></div>
  </div>
  <div class="vl-note in" style="left:150px;right:150px;top:885px;font-size:22px;--i:10"><i data-i="hand"></i><span><b>Early adopter</b> เจ้าของตัดสินใจเอง · สินค้าหลายไซซ์หลายสี · ยินดีร่วมทดลอง เริ่มจากร้านครอบครัวในทีม แล้วขอให้แนะนำร้านใกล้เคียง</span></div>
  <aside class="notes">
BUSINESS MODEL / REVENUE MODEL (Lean Canvas บทที่ 9, ตารางที่ 14.1, บทที่ 13)
แพ็กเกจ Free / Basic 299 / Pro 699 บาทต่อเดือน รายปีลด 10% · ราคาเฉลี่ยถ่วงน้ำหนัก = 299 × 0.8 + 699 × 0.2 = 379 บาท
Go-to-Market 4 ช่วง: หาร้านทดลอง → ใช้ Free พร้อมทีมช่วยตั้งค่า → เปลี่ยนเป็น Basic/Pro → ขยายผล
ส่วนแบ่งตลาด: กรณี Base สิ้นปีที่ 5 มี 124 ร้านจ่ายเงิน = 124 / 5,696 ≈ 2.2% ของ SAM · คุ้มค่าโครงสร้างพื้นฐาน 1,575 บาท/เดือนที่ 7 ร้าน (Basic รายปี)
  </aside>
</section>''')

# ---------------------------------------------------------------- 05b Funding request: 150,000 baht for a 6-month plan (M1–M3)
# Use of funds (baht) for months 1–6; what is left funds months 7+ until revenue covers costs
FUNDS = [('54,000', 'พัฒนา MMP 6 เดือน (2 คน)', '#ff8032', 36.0),
         ('26,000', 'ทดสอบตลาด + ลงพื้นที่ 6 เดือน', '#ffb27f', 17.3),
         ('11,250', 'ระบบคลาวด์ + LINE OA 6 เดือน', '#82a6ff', 7.5),
         ('12,000', 'ตั้งค่าและสอนใช้งานร้าน', '#3d6ef5', 8.0),
         ('18,000', 'ชุดเดโม + จดทะเบียน/PDPA', '#a9c1ff', 12.0),
         ('28,750', 'เงินหมุนเวียนหลังเดือนที่ 6', '#5b7bd6', 19.2)]
left, fbar = 0.0, []
for k, (_, _, c, w) in enumerate(FUNDS):
    fbar.append(f'<i style="left:calc({left:.3f}% + {0 if k == 0 else 3}px);width:calc({w:.3f}% - 3px);background:{c};animation-delay:{3.1 + .15 * k:.2f}s"></i>')
    left += w
flegend = ''.join(f'<div class="in" style="--i:{6 + k}"><div class="h4" style="font-size:36px;color:#fff"><i style="display:inline-block;width:14px;height:14px;border-radius:4px;background:{c};margin-right:12px;vertical-align:middle;box-shadow:0 0 12px {c}"></i>{v}</div><div class="small" style="margin-top:8px;font-size:20px;color:rgba(255,255,255,.75)">{t}</div></div>'
                  for k, (v, t, c, _) in enumerate(FUNDS))
SLIDES.append('''
<section class="s-pp" data-silk="center" data-cubes="none" data-sec="05" data-secname="Business Model" data-pp-a="147328" data-pp-b="150000">
  <div class="burst"></div>
  <div class="abs c" style="left:0;right:0;top:230px">
    <div class="kick in" style="--i:1"><span class="pp-ks"><span class="pp-k0">peak_cash_need --stress</span><span class="pp-k1">funding_request --6_months</span></span></div>
    <div class="pp-stage in grow" style="--i:2;margin-top:60px">
      <div class="pp-num pp-old"><span class="pp-strike"><span data-count="147328" data-dur="2" data-delay=".3" style="display:inline-block;line-height:.9">147,328</span></span><small>บาท</small><div class="pp-was">เงินที่ต้องใช้สูงสุด กรณี MMP ล่าช้า 6 เดือน</div></div>
      <div class="pp-num pp-new"><span class="pp-n" style="display:inline-block;line-height:.9">150,000</span><small>บาท</small></div>
    </div>
  </div>
  <div class="pp-after">
  <div class="pbar in soft" style="left:150px;right:150px;top:690px;--i:4">''' + ''.join(fbar) + '''</div>
  <div class="abs" style="left:150px;right:150px;top:752px;display:grid;grid-template-columns:repeat(6,1fr);gap:22px">''' + flegend + '''</div>
  <div class="abs row in" style="left:0;right:0;top:920px;justify-content:center;align-items:center;gap:20px;--i:13"><i class="ic sm" data-i="shield"></i><span class="h4" style="font-size:30px">งบ 6 เดือน (M1–M3) · ครอบคลุมกรณี Base, Downside และ Stress · เงินสดต่ำสุด 2,672 บาท</span></div>
  </div>
  <span class="fragment step"></span>
  <aside class="notes">
FUNDING REQUEST 150,000 บาท (ทุน TED Youth Startup ปีงบ 2569) งบสำหรับ 6 เดือน = แผนพัฒนา M1–M3
การใช้เงิน: พัฒนา MMP 2 คน × 4,500 × 6 เดือน = 54,000 · ทดสอบตลาดและลงพื้นที่ 3,500 × 6 + ของตอบแทนร้าน 5,000 = 26,000 · ระบบคลาวด์ 1,575 + โดเมน/LINE OA 300 = 1,875 × 6 = 11,250 · ตั้งค่าและสอนใช้งานร้าน 3,000 × 4 = 12,000 · ชุดเดโม 10,000 + จดทะเบียน/PDPA 8,000 = 18,000 · เงินหมุนเวียนหลังเดือนที่ 6 = 28,750
หลังเดือนที่ 6 ไม่มีค่าพัฒนา ค่าการตลาดคิดตามร้านใหม่ (CAC 1,500 บาท/ร้าน) และใช้รายได้ค่าสมาชิกกับเงินหมุนเวียน
เงินที่ต้องใช้สูงสุด: Base 131,578 (เดือน 12) · Downside 138,280 (เดือน 19) · Stress 147,328 (เดือน 18) → 150,000 ครอบคลุมทุกกรณี
  </aside>
</section>''')

# ---------------------------------------------------------------- 06 Team Member
SLIDES.append('''
<section data-silk="center" data-cubes="none" data-sec="06" data-secname="Team">
  <div class="abs" style="left:150px;top:180px">
    <div class="kick in" style="--i:1">team_members</div>
    <div class="h2 sm in" style="--i:2;margin-top:24px">ทีม <span class="g">Khonnai.</span></div>
  </div>
  <style>.jgrid.three .jcard .nm { font-size: 26px; white-space: nowrap; } .tb-role { display: block; margin-bottom: 6px; font: 600 19px/1.3 Poppins; color: var(--web3); white-space: nowrap; }</style>
  <div class="jgrid {TEAM_GRID}">
{TEAM}
  </div>
  <aside class="notes">
TEAM MEMBER: รูป ชื่อ ตำแหน่ง และหน้าที่ของสมาชิกทีม และที่ปรึกษาโครงการ (ถ้ามี)
  </aside>
</section>''')

# ---------------------------------------------------------------- 07 Backup slides divider
SLIDES.append('''
<section data-silk="hot" data-cubes="corners" data-sec="07" data-secname="Backup">
  <div class="abs c" style="left:0;right:0;top:380px">
    <div class="kick in" style="--i:1">appendix</div>
    <div class="statement in" style="--i:2;margin-top:40px;font-size:130px"><span class="g">BACKUP SLIDES</span></div>
    <div class="lede in" style="--i:4;margin-top:50px">ผลทดสอบ · แผนอนาคต MMP · แผนเข้าสู่ตลาด · ประมาณการ 5 ปี · Unit Economics</div>
  </div>
</section>''')

SLIDES.append(reuse(6, '07', 'Backup'))   # Traction

# ---------------------------------------------------------------- Backup: MMP scope (MoSCoW)
SCOPE = [('Must · ฟีเจอร์เดิม', '', ['ตารางสต็อกที่อ่านง่าย', 'ร่างบิล → บิลเงินสด ตัดสต็อก ส่ง PDF ทาง LINE', 'พิมพ์ด่วน + รุ่นขายบ่อย/ล่าสุด',
                                    'การจอง หน้าร้านและ LINE ใช้สต็อกชุดเดียว', 'รับสินค้าเข้าหลายรุ่น + ประวัติเข้า–ออก', 'เพิ่มรุ่นใหม่ทีละคำถาม',
                                    'คลาวด์ ล็อกอิน ซิงก์หลายอุปกรณ์', 'แยกข้อมูลร้าน สิทธิ์ผู้ใช้ สำรองข้อมูล']),
         ('Must · ฟีเจอร์ใหม่', ' w3', ['แคตตาล็อก + ลิงก์สั่งซื้อ เข้าเป็นการจองทันที', 'ราคาส่งแยกตามลูกค้า / ลิงก์เฉพาะลูกค้า', 'QR พร้อมเพย์บนบิล + ปุ่ม "รับเงินแล้ว"',
                                       'รูปสินค้าบนคลาวด์ (เลื่อนจาก Could)', 'นำเข้าสินค้าจาก Excel', 'เก็บค่าสมาชิก Free / 299 / 699 + จำกัดสิทธิ์ตามแพ็กเกจ']),
         ('Should', '', ['Stripe ยืนยันการจ่ายอัตโนมัติ (จุดขาย Pro)', 'พักบิลหลายใบพร้อมกัน', 'วางข้อความจาก LINE แล้วแยกเป็นรายการ',
                         'บิลจัดส่ง + สมุดที่อยู่ลูกค้า', 'แก้ไข/ยกเลิก บิล การจอง การรับสินค้า']),
         ("Won't (รอบนี้)", '', ['ระบบเจ้าหนี้/ใบสั่งซื้อ (Vendor/PO)', 'ลูกหนี้ค้างชำระ (ร้านขายเงินสด)', 'e-Tax · หลายคลัง · Shopee/Lazada · บัญชีเต็มรูปแบบ',
                                 'แจ้งเตือนสินค้าใกล้หมด (ผลทดสอบว่าไม่ต้องการ)'])]
scope_cols = ''.join(
    f'<div class="card glow{cls} in" style="--i:{3 + k};padding:28px 26px"><div class="ct" style="font-size:28px">{t}</div>'
    + ''.join(f'<div style="display:flex;gap:10px;margin-top:12px;font:400 19px/1.4 Poppins;color:var(--ink-2)"><span style="color:var(--web3)">•</span><span>{it}</span></div>' for it in items)
    + '</div>' for k, (t, cls, items) in enumerate(SCOPE))
SLIDES.append('''
<section data-silk="right" data-cubes="none" data-sec="07" data-secname="Backup">
  <div class="abs" style="left:150px;top:180px">
    <div class="kick in" style="--i:1">future --mmp_scope</div>
    <div class="h2 sm in" style="--i:2;margin-top:24px">แผนอนาคต <span class="g">MMP.</span></div>
  </div>
  <div class="abs body in" style="left:1000px;top:226px;width:770px;font-size:26px;--i:2">ฟีเจอร์ที่จะพัฒนาหลังได้ทุน: MMP ต้องเป็นสินค้าที่ร้าน<span class="b">ยอมจ่ายเงินและใช้ทุกวัน</span> ต่อยอดจากระบบสต็อกของ MVP</div>
  <div class="abs" style="left:150px;right:150px;top:390px;display:grid;grid-template-columns:repeat(4,1fr);gap:22px;align-items:start">''' + scope_cols + '''</div>
  <aside class="notes">
MMP SCOPE (MoSCoW) ข้อมูลดิบจากทีม: Must เดิม 8 ข้อ · Must ใหม่ 6 ข้อ · Should 5 ข้อ · Won't 4 กลุ่ม
Stripe (Should): ยืนยันการจ่ายอัตโนมัติทั้ง PromptPay และบัตร ค่าธรรมเนียม 1.65% ร้านเป็นผู้จ่าย เสนอเป็นจุดขายแพ็กเกจ Pro · ใช้ระบบเดียวกันทั้งรับเงินจากลูกค้าของร้านและเก็บค่าสมาชิกจากร้าน
  </aside>
</section>''')

# ---------------------------------------------------------------- Backup (future): order flow through a catalog link
FLOW = [('send', 'แชร์ลิงก์', 'ร้านกดแชร์แคตตาล็อก ส่งลิงก์ใน LINE'),
        ('list', 'ลูกค้าเลือกเอง', 'รุ่น ไซซ์ สี จำนวนแพ็ก เห็นเฉพาะของที่มี'),
        ('lock', 'กันสต็อกทันที', 'ระบบสร้างการจอง ตรวจสต็อกซ้ำตอนกดส่ง'),
        ('doc', 'ยืนยันเป็นบิล', 'ร้านกดครั้งเดียว ได้บิล + QR พร้อมเพย์ ส่ง PDF'),
        ('check', 'รับเงินแล้ว', 'ลูกค้าโอน ร้านกดยืนยัน (Pro: Stripe ยืนยันให้อัตโนมัติ)')]
flow_cards = ''.join(
    (f'<div class="in" style="--i:{3 + k};display:grid;place-items:center;font:600 36px/1 Poppins;color:var(--web3)">→</div>' if k else '')
    + f'<div class="card glow{" w3" if k == 3 else ""} in" style="--i:{3 + k};padding:28px 24px"><div class="row" style="align-items:center;gap:14px"><i class="ic sm" data-i="{ic}"></i><span class="mono" style="font-size:22px;color:var(--web3)">0{k + 1}</span></div>'
    f'<div class="ct" style="font-size:28px;margin-top:20px">{t}</div><div class="cb" style="font-size:20px;margin-top:10px">{d}</div></div>'
    for k, (ic, t, d) in enumerate(FLOW))
SLIDES.append('''
<section data-silk="center" data-cubes="none" data-sec="07" data-secname="Backup">
  <div class="abs" style="left:150px;top:180px">
    <div class="kick in" style="--i:1">future --mmp_order_flow</div>
    <div class="h2 sm in" style="--i:2;margin-top:24px">ลูกค้าสั่งเอง<br><span class="g">ร้านกดยืนยันครั้งเดียว.</span></div>
  </div>
  <div class="abs in" style="left:1010px;top:180px;width:760px;--i:2"><span class="pill w3"><span class="dot"></span>แผนอนาคต MMP · ยังไม่ได้พัฒนา</span><div class="small" style="font-size:22px;margin-top:18px">เทียบกับโฟลว์ปัจจุบัน</div><div style="margin-top:8px;font:400 24px/1.45 Poppins;color:var(--ink-3);text-decoration:line-through;text-decoration-color:rgba(255,128,50,.7)">ส่งรูป → ลูกค้าแคปรูปส่งกลับ → ร้านพิมพ์รายการเอง → เขียนบิล → ตรวจสลิป</div></div>
  <div class="abs" style="left:150px;right:150px;top:470px;display:grid;grid-template-columns:1fr 36px 1fr 36px 1fr 36px 1fr 36px 1fr;align-items:stretch">''' + flow_cards + '''</div>
  <div class="abs row" style="left:150px;right:150px;top:820px;gap:24px">
    <div class="vl-note in" style="position:static;flex:1;font-size:21px;--i:9"><i data-i="alert"></i><span><b>ของหมดระหว่างเลือก</b> ตรวจสต็อกซ้ำตอนกดส่ง (transaction)</span></div>
    <div class="vl-note in" style="position:static;flex:1;font-size:21px;--i:10"><i data-i="refresh"></i><span><b>จองแล้วไม่จ่าย</b> ร้านยกเลิก สต็อกคืนอัตโนมัติ</span></div>
    <div class="vl-note in" style="position:static;flex:1;font-size:21px;--i:11"><i data-i="mic"></i><span><b>ที่มา</b> เจ้าของร้านชี้ว่าเว็บซัพพลายเออร์ดูได้แค่แคตตาล็อก สั่งไม่ได้ และช้า</span></div>
  </div>
  <aside class="notes">
แผนอนาคต (MMP ระยะ M2) ยังไม่ได้พัฒนา · ORDER FLOW ผ่านแคตตาล็อก 5 ขั้น: แชร์ลิงก์ → ลูกค้าเลือกรุ่น/ไซซ์/สี/จำนวนแพ็ก (เห็นเฉพาะของที่มี) → ระบบสร้างการจองและกันสต็อก → ร้านยืนยันเป็นบิลพร้อม QR พร้อมเพย์ ส่ง PDF ทาง LINE → ลูกค้าโอน ร้านกดรับเงินแล้ว (ถ้ามี Stripe ระบบยืนยันให้อัตโนมัติ)
โฟลว์เดิม: ส่งรูป → ลูกค้าแคปรูปส่งกลับ → ร้านพิมพ์รายการเอง → เขียนบิล → ตรวจสลิป
กรณีขอบ: ของหมดระหว่างเลือก ตรวจซ้ำตอนกดส่ง · จองแล้วไม่จ่าย ร้านยกเลิก สต็อกคืนอัตโนมัติ
  </aside>
</section>''')

# ---------------------------------------------------------------- Backup: MMP roadmap + KPIs
ROAD = [('M1', 'เดือน 1–2', 'Must เดิม + คลาวด์ ล็อกอิน แยกร้าน + นำเข้า Excel', 'ร้านนำร่องใช้จริงทุกวัน 4 สัปดาห์'),
        ('M2', 'เดือน 3–4', 'แคตตาล็อก + ลิงก์สั่ง + ราคาตามลูกค้า + รูปบนคลาวด์ + QR พร้อมเพย์', 'ร้านภายนอก 3–5 ร้าน · ออร์เดอร์ผ่านลิงก์ ≥ 30% ของออร์เดอร์ LINE'),
        ('M3', 'เดือน 5–6', 'เก็บค่าสมาชิก + Stripe (Should)', 'เริ่มมีร้านจ่ายเงิน · ถึง 7 ร้าน (คุ้มค่าเซิร์ฟเวอร์) ภายในเดือนที่ 9')]
road_cards = ''.join(
    f'<div class="card glow{" w3" if k == 2 else ""} in" style="--i:{3 + k};padding:32px 34px"><div class="row" style="align-items:baseline;gap:16px"><span class="num g" style="font-size:64px">{m}</span><span class="mono" style="font-size:22px;color:var(--ink-3)">{when}</span></div>'
    f'<div class="cb" style="font-size:23px;margin-top:18px">{what}</div><div style="margin-top:22px;padding-top:18px;border-top:1px solid var(--line-2)"><div class="small" style="font-size:18px">ตัวชี้วัด</div><div style="margin-top:6px;font:500 24px/1.35 Poppins;color:#fff">{kpi}</div></div></div>'
    for k, (m, when, what, kpi) in enumerate(ROAD))
SLIDES.append('''
<section data-silk="center" data-cubes="none" data-sec="07" data-secname="Backup">
  <div class="abs" style="left:150px;top:180px">
    <div class="kick in" style="--i:1">future --mmp_roadmap</div>
    <div class="h2 sm in" style="--i:2;margin-top:24px">แผนพัฒนา<br><span class="g">และตัวชี้วัด.</span></div>
  </div>
  <div class="abs" style="left:150px;right:150px;top:450px;display:grid;grid-template-columns:repeat(3,1fr);gap:28px;align-items:stretch">''' + road_cards + '''</div>
  <div class="vl-note in" style="left:150px;right:150px;top:880px;font-size:21px;--i:7"><i data-i="shield"></i><span><b>Should อยู่ระยะท้าย</b> ถ้าเวลาไม่พอ M1–M2 ก็ยังเป็นสินค้าที่ขายได้ · งบ 150,000 บาทครอบคลุม 6 เดือนนี้ · กรณี MMP ล่าช้า 6 เดือนยังพอ (เงินสดต่ำสุด 2,672 บาท)</span></div>
  <aside class="notes">
ROADMAP: M1 (เดือน 1–2) ร้านนำร่องใช้จริงทุกวัน 4 สัปดาห์ · M2 (เดือน 3–4) ร้านภายนอก 3–5 ร้าน และออร์เดอร์ผ่านลิงก์ ≥ 30% ของออร์เดอร์ LINE (เป้าที่ตั้งเอง รอทีมยืนยัน) · M3 (เดือน 5–6) เริ่มเก็บเงิน ถึง 7 ร้าน (จุดคุ้มค่าเซิร์ฟเวอร์) ภายในเดือนที่ 9 ตามโมเดลกรณี Base
  </aside>
</section>''')

# Go-to-Market with the same paying-shop target as the 5-year model (124 at the end of year 5, after churn)
gtm = reuse(7, '07', 'Backup')
for a, b in [('4 ช่วง สู่<br><span class="g">เป้าหมาย 134 ร้าน.</span>', '4 ช่วง สู่<br><span class="g">124 ร้านจ่ายเงิน.</span>'),
             ('<small>Basic / Pro · คุ้มทุนค่าเซิร์ฟเวอร์ที่ 7 ร้าน</small>', '<small>Basic / Pro ตั้งแต่เดือนที่ 5 · คุ้มค่าเซิร์ฟเวอร์ที่ 7 ร้าน (เดือนที่ 9)</small>'),
             ('<small>ชำระเงิน 134 ร้าน + Free 200 ร้าน ต้องได้ร้านใหม่ 8–10 ร้าน/เดือน</small>', '<small>ร้านใหม่ 5 → 7 ร้าน/เดือน · หลังหักร้านยกเลิก (churn 5%) เหลือ ~124 ร้านจ่ายเงินสิ้นปีที่ 5</small>')]:
    assert a in gtm, a
    gtm = gtm.replace(a, b)
gtm = re.sub(r'<aside class="notes">.*?</aside>', """<aside class="notes">
GO-TO-MARKET (บทที่ 13.1) ใช้เป้าเดียวกับโมเดลการเงินกรณี Base
ช่วงที่ 1 ร้านนำร่อง + ร้านภายนอก 3–5 ร้าน · ช่วงที่ 2 ใช้ Free พร้อมทีมช่วยตั้งค่า · ช่วงที่ 3 เก็บเงิน Basic/Pro ตั้งแต่เดือนที่ 5 ถึง 7 ร้านในเดือนที่ 9
ช่วงที่ 4 ร้านใหม่ปีละ 17 / 50 / 76 / 84 / 84 ร้าน · ร้านที่ยังจ่ายเงินสิ้นปี 15 / 48 / 85 / 110 / 124 (หักร้านยกเลิก 5%/เดือนแล้ว)
เป้า 134 ร้านในรีพอร์ตเป็นกรณีเร่งการเติบโต (ร้านใหม่ 8–10 ร้าน/เดือน) ไม่ใช่กรณี Base จึงไม่ใช้ในเด็คนี้
  </aside>""", gtm, count=1, flags=re.S)
SLIDES.append(gtm)

# ---------------------------------------------------------------- Backup: 5-year financials (recomputed, Base)
# (year, revenue, operating profit, paying shops at year end after churn) — Base case of the 6-month 150,000-baht plan
FIN = [(1, 23569, -113578, '15'), (2, 140717, 33383, '48'), (3, 306065, 148176, '85'),
       (4, 455369, 275045, '110'), (5, 538725, 352576, '124')]
FIN_MAX_H, FIN_COL, FIN_REV_W, FIN_PRO_W = 400, 214, 112, 72
fin_parts = []
for k, (yr, rev, prof, shops) in enumerate(FIN):
    x = k * FIN_COL
    hr = round(rev / FIN[-1][1] * FIN_MAX_H)
    hp = max(round(prof / FIN[-1][1] * FIN_MAX_H), 0)
    d = .3 + .12 * k
    fin_parts.append(
        f'<div class="bar" style="left:{x}px;width:{FIN_REV_W}px;height:{hr}px;animation-delay:{d:.2f}s"></div>'
        f'<div class="bar" style="left:{x + FIN_REV_W + 8}px;width:{FIN_PRO_W}px;height:{hp}px;--tc:255,128,50;animation-delay:{d + .15:.2f}s"></div>'
        f'<div class="fin-v in" style="left:{x - 20}px;width:{FIN_REV_W + 40}px;bottom:{hr + 12}px;--i:{4 + k}">{rev:,}</div>'
        f'<div class="fin-v pro in" style="left:{x + FIN_REV_W - 6}px;width:{FIN_PRO_W + 28}px;bottom:{hp + 12}px;--i:{4 + k}">'
        + (f'({-prof:,})' if prof < 0 else f'{prof:,}') + '</div>'
        f'<div class="fin-y in" style="left:{x}px;width:{FIN_REV_W + FIN_PRO_W + 8}px;--i:{4 + k}"><b>ปีที่ {yr}</b><span>{shops} ร้าน</span></div>')
SLIDES.append('''
<section data-silk="right" data-cubes="none" data-sec="07" data-secname="Backup">
  <div class="abs" style="left:150px;top:180px">
    <div class="kick in" style="--i:1">financials --base --60m</div>
    <div class="h2 sm in" style="--i:2;margin-top:24px">ประมาณการ <span class="g">5 ปี.</span></div>
  </div>
  <div class="abs row in" style="left:150px;top:372px;gap:16px;--i:3"><span class="pill ai"><span class="dot"></span>รายได้ค่าสมาชิก (บาท)</span><span class="pill w3"><span class="dot"></span>กำไรจากการดำเนินงาน (บาท)</span><span class="small" style="align-self:center;font-size:19px">ร้าน = ร้านที่ยังจ่ายเงินสิ้นปี หลังหักร้านยกเลิก</span></div>
  <div class="pod ai" style="left:150px;bottom:190px;width:1060px;height:440px">
''' + ''.join(fin_parts) + '''
  </div>
  <div class="ubl" style="left:1330px;top:372px;width:440px">
    <div class="ubl-i in" style="--i:6"><i data-i="clock"></i><div><b>เดือนที่ 13</b><span>เริ่มมีกำไรรายเดือน (หลังจบงบพัฒนา 6 เดือน)</span></div></div>
    <div class="ubl-i in" style="--i:7"><i data-i="trophy"></i><div><b>เดือนที่ 33</b><span>กำไรสะสมกลับเป็นบวก รวมค่าพัฒนา MMP แล้ว</span></div></div>
    <div class="ubl-i in" style="--i:8"><i data-i="users"></i><div><b>124 ร้าน</b><span>จ่ายเงินสิ้นปีที่ 5 · รายได้ปีละ 538,725 บาท</span></div></div>
  </div>
  <div class="vl-note in" style="left:1330px;top:790px;width:440px;font-size:21px;--i:10"><i data-i="alert"></i><span>หลังปีที่ 3 โตช้าลง: ร้านใหม่ปีละ 84 ร้าน ใกล้เคียงร้านที่ยกเลิก (Churn 5%/เดือน)</span></div>
  <aside class="notes">
FINANCIALS 5 ปี กรณี Base (โมเดลรายเดือนเดียวกับบทที่ 15 ปรับตามงบ 6 เดือน: พัฒนา MMP เดือน 1–6 เริ่มเก็บเงินเดือนที่ 5)
รายได้ปี 1–5: 23,569 / 140,717 / 306,065 / 455,369 / 538,725
กำไรจากการดำเนินงาน: (113,578) / 33,383 / 148,176 / 275,045 / 352,576 · ปีที่ 1 รวมค่าพัฒนา MMP 54,000 และค่าใช้จ่ายช่วงทดสอบที่ใช้เงินทุน
ร้านใหม่ในปี: 17 / 50 / 76 / 84 / 84 · ร้านที่ยังจ่ายเงินสิ้นปี (หัก churn 5%/เดือน): 15 / 48 / 85 / 110 / 124
เงินสดคงเหลือปลายปี (รวมทุน 150,000): 18,422 / 51,805 / 199,981 / 475,026 / 827,602
ไม่รวมภาษีและค่าแรงทีมนอกเหนือจากที่ระบุ ตัวเลขทั้งหมดเป็นประมาณการ
  </aside>
</section>''')

# ---------------------------------------------------------------- Backup: scenarios + unit economics
SCEN = [('Base', '131,578', '18,422', '13', 'เก็บเงินเดือนที่ 5 · ร้านใหม่ 1.5 → 7 ร้าน/เดือน · Churn 5%'),
        ('Downside', '138,280', '11,720', '20', 'ร้านใหม่ 60% ของ Base · Churn 8%'),
        ('Stress', '147,328', '2,672', '19', 'MMP ล่าช้า เริ่มเก็บเงินเดือนที่ 11 แทน 5')]
UNIT = [('352.5', 'รายได้สุทธิ/ร้าน/เดือน', '379 − ค่าธรรมเนียมรับเงิน 26.5'),
        ('1,875', 'ต้นทุนได้ร้านใหม่ (บาท/ร้าน)', 'CAC 1,500 + ตั้งค่า 375'),
        ('7,050', 'LTV จากรายได้สุทธิ (บาท/ร้าน)', '352.5 ÷ churn 5%'),
        ('3.8×', 'LTV : ต้นทุนได้ร้านใหม่', '7,050 ÷ 1,875 · เทียบ CAC อย่างเดียว 4.7×'),
        ('5.3', 'Payback (เดือน)', '1,875 ÷ 352.5')]
scen_cards = ''.join(
    f'<div class="card glow{" w3" if k == 2 else ""} in" style="--i:{3 + k};padding:34px 38px"><div class="ct" style="font-size:38px">{n}</div>'
    f'<div class="small" style="margin-top:6px;font-size:20px">{d}</div>'
    f'<div class="row" style="margin-top:26px;gap:30px"><div><div class="h4" style="font-size:40px">{need}</div><div class="small" style="font-size:19px">เงินที่ต้องใช้สูงสุด</div></div>'
    f'<div><div class="h4" style="font-size:40px">{low}</div><div class="small" style="font-size:19px">เงินสดต่ำสุด</div></div>'
    f'<div><div class="h4" style="font-size:40px">{mo}</div><div class="small" style="font-size:19px">เดือนที่กำไร</div></div></div></div>'
    for k, (n, need, low, mo, d) in enumerate(SCEN))
unit_cells = ''.join(f'<div class="in" style="--i:{7 + k}"><div class="h4" style="font-size:46px">{v}</div><div class="small" style="margin-top:6px;font-size:20px;color:var(--ink-2)">{t}</div><div class="mono" style="margin-top:6px;font-size:16px;color:var(--web3)">{f}</div></div>'
                     for k, (v, t, f) in enumerate(UNIT))
SLIDES.append('''
<section data-silk="center" data-cubes="none" data-sec="07" data-secname="Backup">
  <div class="abs" style="left:150px;top:180px">
    <div class="kick in" style="--i:1">scenarios --funding_150k</div>
    <div class="h2 sm in" style="--i:2;margin-top:24px">ทุน 150,000 บาท <span class="g">พอทุกกรณี.</span></div>
  </div>
  <div class="abs" style="left:150px;right:150px;top:400px;display:grid;grid-template-columns:repeat(3,1fr);gap:28px">''' + scen_cards + '''</div>
  <div class="abs in" style="left:150px;top:740px;--i:6"><span class="pill ai"><span class="dot"></span>Unit Economics ต่อร้านที่จ่ายเงิน (Base) · ไม่ปันส่วนค่าเซิร์ฟเวอร์คงที่ 1,575 บาท/เดือน</span></div>
  <div class="abs" style="left:150px;right:150px;top:806px;display:grid;grid-template-columns:repeat(5,1fr);gap:28px">''' + unit_cells + '''</div>
  <aside class="notes">
SCENARIOS (โมเดล 60 เดือน งบ 6 เดือน ทุน 150,000 บาท) เงินที่ต้องใช้สูงสุด = เงินที่ใช้สะสมสูงสุดก่อนรายได้คุ้ม · เงินสดต่ำสุด = 150,000 − เงินที่ต้องใช้สูงสุด
Unit economics: รายได้สุทธิ 352.5 = 379 − ค่าธรรมเนียมรับเงิน (4.35% + 10 บาท) · ไม่มีต้นทุนผันแปรอื่นต่อร้าน เพราะค่าเซิร์ฟเวอร์เป็นต้นทุนคงที่ จึงไม่ได้สมมติ gross margin 80%
LTV 7,050 = 352.5 ÷ 0.05 · LTV/(CAC + ตั้งค่า) = 7,050 ÷ 1,875 = 3.76 ≈ 3.8× · LTV/CAC อย่างเดียว = 7,050 ÷ 1,500 = 4.7× · Payback = 1,875 ÷ 352.5 = 5.3 เดือน · ที่ churn 8%: LTV 4,406 → 2.4×
  </aside>
</section>''')

# ---------------------------------------------------------------- 08 Reference
REFS = [
    'สสว. (2567). จำนวนวิสาหกิจขนาดย่อยและขนาดย่อม TSIC 46414 จำแนกตามจังหวัด',
    'OECD (2026). Financing SMEs and Entrepreneurs 2026: Thailand',
    'ETDA. มูลค่าอีคอมเมิร์ซไทย ปี 2565–2566',
    'ราคา ZORT · Page365 · FlowAccount · LINE OA (เว็บไซต์ทางการ, 28 ต.ค. 2569)',
    'Supabase · Vercel · Stripe Pricing (ดึงข้อมูล 28 ต.ค. 2569)',
    'Kane, L. (2019). Usability for Older Adults. Nielsen Norman Group',
    'Brown, S. The C4 Model for Visualising Software Architecture',
    'Moran, K. (2019). Usability (User) Testing 101 · Strategyzer Test Card / Learning Card · MoSCoW',
    'สสว. รายงานสถานการณ์ MSME ไตรมาส 1/2567 (สัดส่วน GDP ปี 2566)',
    'ผลสำรวจการใช้ดิจิทัลของ SME โดย สสว. (20–28 ก.พ. 2568, 2,704 ราย)',
    'Khonnai Milestone 2 Report: สัมภาษณ์ร้านกรณีศึกษา + ผลทดสอบ MVP2 28 ต.ค. 2569',
]
ref_items = ''.join(f'<div class="in" style="--i:{3 + k};display:flex;gap:18px;font:400 22px/1.4 Poppins;color:var(--ink-2)"><span class="mono" style="color:var(--web3)">{k + 1:02d}</span><span>{r}</span></div>'
                    for k, r in enumerate(REFS))
SLIDES.append('''
<section data-silk="cover" data-cubes="none" data-sec="08" data-secname="Reference">
  <div class="abs" style="left:150px;top:180px">
    <div class="kick in" style="--i:1">reference</div>
    <div class="h2 sm in" style="--i:2;margin-top:24px">แหล่งข้อมูล<br><span class="g">อ้างอิง.</span></div>
  </div>
  <div class="abs" style="left:150px;top:440px;width:1080px;display:grid;gap:12px">''' + ref_items + '''</div>
  <div class="qr in grow" style="left:1360px;top:300px;width:400px;height:400px;--i:9"><img src="{QRK}" alt="QR code: khonnaiofficial.vercel.app"></div>
  <div class="qr-l in" style="left:1300px;top:735px;width:520px;--i:10">ลองใช้ Khonnai MVP<br>khonnaiofficial.vercel.app</div>
  <aside class="notes">
REFERENCE · เว็บ Khonnai MVP https://khonnaiofficial.vercel.app/ · รายละเอียดอ้างอิงครบในรีพอร์ต Milestone 2 หัวข้อเอกสารอ้างอิง
  </aside>
</section>''')

# ---------------------------------------------------------------- team data (placeholders until the new team list arrives)
APPLICANT = 'Borworn Kultumyotin'
# (name, position<br>duty) — photos: build/assets/tb-team-1..N; members without a file show a placeholder
TEAM = [
    ('Borworn Kultumyotin', '<b class="tb-role">Co-Founder &amp; Chief A.I. Officer</b>Product · UX/UI · Design · นำ AI มา integrate ใน Product · ทำ MVP และ MMP'),
    ('Rapeepong Naksan', '<b class="tb-role">Founder &amp; CEO</b>การตลาด · วาง Vision · ดูแลภาพรวมและทิศทางในอนาคต'),
    ('Korawit Rungthampaisan', '<b class="tb-role">President &amp; CTO</b>ดูแลฝั่ง Tech และภาพรวมการทำงานทั้งหมดภายในทีม'),
]
TEAM_LINE = 'ทีม Khonnai · ' + str(len(TEAM)) + ' คน'
TEAM_GRID = {3: 'three" style="left:360px;right:360px;grid-template-columns:repeat(3,minmax(0,1fr));gap:40px', 4: 'four', 5: 'five', 6: 'six'}.get(len(TEAM), 'five')
SLIDES = [s.replace('{APPLICANT}', APPLICANT).replace('{TEAM_LINE}', TEAM_LINE).replace('{TEAM_GRID}', TEAM_GRID)
          for s in SLIDES]
# the deck calls the current prototype just "MVP" (reused Milestone 2 slides say MVP2)
SLIDES = [s.replace('MVP2', 'MVP') for s in SLIDES]
