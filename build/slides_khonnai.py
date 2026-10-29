# Slide content for the Khonnai Milestone 2 pitch deck.
# Every figure and claim comes from Milestone2_Final_v3.docx (chapter noted per slide).
# {LOGO}, {PHONE}, {PRODUCT}, {QR} are replaced with base64 data URIs by build_deck.py.

SLIDES = []

# ---------------------------------------------------------------- cover (report title page)
SLIDES.append('''
<section class="s-cover" data-chrome="none" data-silk="cover" data-cubes="cover" data-sec="00" data-secname="Khonnai">
  <div class="gridbg" style="opacity:.55"></div>
  <div class="abs" style="left:150px;top:290px">
    <div class="kick in" style="--i:1">milestone_2 --pitch</div>
    <div class="h1 wm in" style="--i:2;margin-top:50px;font-size:172px"><img class="uh-logo" src="{LOGO}" alt="Khonnai" style="display:block;height:150px;width:auto"></div>
    <div class="h3 in" style="--i:3;margin-top:48px;font-weight:400;color:var(--ink-2)">คนใน · ระบบบริหารสต็อก การจองสินค้า และการออกบิลบนมือถือ</div>
    <div class="lede in" style="--i:5;margin-top:60px;color:var(--ink)">สำหรับร้านขายส่งชุดชั้นในขนาดเล็ก</div>
  </div>
  <div class="abs row in soft" style="left:150px;bottom:92px;--i:7;align-items:center;gap:24px"><span class="pill solid">กลุ่ม 3</span><span class="h4" style="font-size:30px">My Little Pony</span></div>
  <div class="abs cv-clock in soft" style="right:150px;bottom:104px;--i:8"><i></i>Bangkok&nbsp; <b>--:--:--</b></div>
  <aside class="notes">
หน้าปก: Khonnai (คนใน) ระบบบริหารสต็อก การจองสินค้า และการออกบิลบนอุปกรณ์มือถือ สำหรับร้านขายส่งชุดชั้นในขนาดเล็ก
  </aside>
</section>''')

# ---------------------------------------------------------------- 01 Problem (ch.1.3, table 4.1)
SLIDES.append('''
<section class="s-format" data-silk="top" data-cubes="none" data-sec="01" data-secname="Problem">
  <div class="abs" style="left:150px;top:190px">
    <div class="kick in" style="--i:1">the_problem</div>
    <div class="h2 in" style="--i:2;margin-top:26px">ปัญหาหลัก 4 ข้อ<br><span class="g">ของร้านค้าส่ง</span></div>
  </div>
  <div class="flow">
    <div class="track"></div><div class="fillr"></div>
    <div class="st in" style="left:0;--i:3"><i class="ic" data-i="list"></i><div class="nm" style="font-size:40px">P1 · ไม่มีบันทึก</div><div class="dt">ไม่มีการบันทึกสินค้าเข้า–ออก ต้องตรวจนับหลังปิดร้าน และคาดคะเนการสั่งซื้อ</div></div>
    <div class="st in" style="left:25%;--i:4"><i class="ic" data-i="hall"></i><div class="nm" style="font-size:40px">P2 · อาคาร 3 ชั้น</div><div class="dt">ต้องเดินตรวจสินค้าซ้ำทุกครั้งที่ลูกค้าสอบถาม</div></div>
    <div class="st in" style="left:50%;--i:5"><i class="ic" data-i="refresh"></i><div class="nm" style="font-size:40px">P3 · ข้อมูลแยกกัน</div><div class="dt">หน้าร้านกับ LINE ไม่มีสต็อกร่วมกัน ข้อมูลใน Note ไม่ตรงของจริง เสี่ยงขายซ้ำ</div></div>
    <div class="st in" style="left:75%;--i:6"><i class="ic" data-i="doc"></i><div class="nm" style="font-size:40px">P4 · บิลเขียนมือ</div><div class="dt">ถ่ายรูปส่ง LINE ใช้เวลามาก คำนวณยอดผิดได้ และไม่ตัดสต็อก</div></div>
  </div>
  <div class="abs in" style="left:150px;top:900px;--i:8"><div class="vl-note" style="position:static"><i data-i="alert"></i><span><b>C1</b> ผู้ใช้อายุ 40 ปีขึ้นไป ไม่คุ้นเคยเทคโนโลยี ระบบต้องไม่เพิ่มความยุ่งยากให้การทำงานเดิม</span></div></div>
  <span class="fragment step"></span><span class="fragment step"></span><span class="fragment step"></span><span class="fragment step"></span>
  <aside class="notes">
PROBLEM (บทที่ 1.3 / ตารางที่ 4.1) กดทีละครั้งเพื่อไล่ P1 ถึง P4
ร้านนำร่องมีสินค้าหลายรุ่น หลายไซซ์ หลายสี เก็บบนอาคาร 3 ชั้น ข้อมูลกระจายอยู่ในความจำ สมุด Note บิลเขียนมือ และแชท LINE
  </aside>
</section>''')

# ---------------------------------------------------------------- 02 Solution (ch.4.1, Lean Canvas UVP 9.3)
SLIDES.append('''
<section data-silk="right" data-cubes="none" data-sec="02" data-secname="Solution">
  <div class="abs" style="left:150px;top:180px;width:1000px">
    <div class="kick in" style="--i:1">the_solution</div>
    <div class="h2 in" style="--i:2;margin-top:24px"><img src="{LOGO}" alt="Khonnai" style="display:inline-block;height:96px;width:auto;vertical-align:-14px;margin-right:24px"><span class="g">ของร้าน.</span></div>
    <div class="lede in" style="--i:3;margin-top:34px;max-width:960px">จดจำจำนวนสินค้าทุกรุ่น ทุกไซซ์ ทุกสีแทนเจ้าของร้าน นับเป็นแพ็ก และทุกบิล ทุกการจอง หักจากสต็อกชุดเดียวกัน ทั้งหน้าร้านและ LINE</div>
  </div>
  <div class="ubl" style="left:150px;top:600px;width:1000px">
    <div class="ubl-i in" style="--i:5"><i data-i="cube"></i><div><b>ระบบเดียว</b><span>จัดการสต็อก การจอง และการออกบิลผ่านระบบเดียว</span></div></div>
    <div class="ubl-i in" style="--i:6"><i data-i="heart"></i><div><b>เรียบง่าย เฉพาะทาง</b><span>สอดคล้องกับการทำงานของร้านค้าส่งชุดชั้นในโดยเฉพาะ</span></div></div>
  </div>
  <div class="abs in grow" style="left:1290px;top:150px;--i:4"><img src="{PHONE}" alt="หน้าจอสต็อกของ Khonnai" style="display:block;height:800px;width:auto;border-radius:36px;box-shadow:0 30px 80px rgba(0,0,0,.5),0 0 60px rgba(118,96,255,.25)"></div>
  <aside class="notes">
SOLUTION (บทที่ 4.1 และ Lean Canvas 9.3)
Khonnai ทำหน้าที่เป็น "คนในร้าน" นับสต็อกเป็นแพ็กต่อตัวเลือกสินค้า (รุ่น + ไซซ์ + สี) ทุกบิลและทุกการจองหักจากจำนวนชุดเดียวกัน
ภาพขวา: หน้าสต็อกของรุ่นจากแบบ Figma ของ MMP
  </aside>
</section>''')

# ---------------------------------------------------------------- 03 Market (ch.6.2, 6.4)
SLIDES.append('''
<section data-silk="center" data-cubes="none" data-sec="03" data-secname="Market">
  <div class="abs" style="left:150px;top:180px">
    <div class="kick in" style="--i:1">market_size</div>
    <div class="h2 sm in" style="--i:2;margin-top:24px">TAM · SAM · <span class="g">SOM.</span></div>
  </div>
  <div class="abs in" style="right:150px;top:206px;text-align:right;--i:3"><div class="h4" style="font-size:34px">มูลค่า = จำนวนกิจการ × ราคา × 12 เดือน</div><div class="small" style="margin-top:6px"><b>299</b> = ราคาแพ็กเกจ Basic (บาท/เดือน) · <b>300</b> = ราคาเฉลี่ยปัดกลม (SOM)<br>ฐานจำนวนกิจการ: สสว. ปี 2567 · TSIC 46414 ค้าส่งเสื้อผ้า Micro + Small</div></div>
  <div class="abs in" style="left:0;right:0;top:922px;display:flex;justify-content:center;--i:9"><div class="vl-note" style="position:static;padding:12px 24px;font-size:22px"><i data-i="spark"></i><span>อีคอมเมิร์ซไทยโตจาก <b>5.43</b> เป็น <b>5.96 ล้านล้านบาท</b> (ปี 2565 → ประเมินปี 2566, ETDA)</span></div></div>
  <div class="abs in" style="left:150px;top:400px;--i:4"><span class="pill ai"><span class="dot"></span>จำนวนกิจการ</span></div>
  <div class="abs in" style="left:1070px;top:400px;--i:4"><span class="pill w3"><span class="dot"></span>มูลค่าตลาด (บาท/ปี)</span></div>
  <div class="pod ai" style="left:150px;bottom:170px">
    <div class="amt in" style="left:0;top:180px;--i:6">5,696<small>กิจการ</small></div><div class="bar" style="left:0;height:290px;animation-delay:.5s"><div class="pl">SAM</div><div class="itm"><span>กทม.</span><br>+ ชลบุรี</div></div>
    <div class="amt in" style="left:245px;top:90px;--i:5">8,770<small>กิจการ</small></div><div class="bar" style="left:245px;height:380px;animation-delay:.3s"><div class="pl">TAM</div><div class="itm"><span>ค้าส่งเสื้อผ้า</span><br>ทั่วไทย</div></div>
    <div class="amt in" style="left:490px;top:260px;--i:7">12<small>ร้าน</small></div><div class="bar" style="left:490px;height:210px;animation-delay:.7s"><div class="pl">SOM</div><div class="itm"><span>เป้าหมาย</span><br>ระยะแรก</div></div>
  </div>
  <div class="pod w3" style="left:1070px;bottom:170px">
    <div class="amt in" style="left:0;top:180px;--i:7">20.44<small>ล้าน</small></div><div class="bar" style="left:0;height:290px;animation-delay:.6s"><div class="pl">SAM</div><div class="itm">5,696<br><span>× 299 บาท × 12 เดือน</span></div></div>
    <div class="amt in" style="left:245px;top:90px;--i:6">31.47<small>ล้าน</small></div><div class="bar" style="left:245px;height:380px;animation-delay:.4s"><div class="pl">TAM</div><div class="itm">8,770<br><span>× 299 บาท × 12 เดือน</span></div></div>
    <div class="amt in" style="left:490px;top:260px;--i:8">43,200<small>บาท</small></div><div class="bar" style="left:490px;height:210px;animation-delay:.8s"><div class="pl">SOM</div><div class="itm">12<br><span>× 300 บาท × 12 เดือน</span></div></div>
  </div>
  <aside class="notes">
MARKET (บทที่ 6.4.2) TAM 8,770 กิจการ ≈ 31.47 ล้านบาท/ปี · SAM 5,696 กิจการ ≈ 20.44 ล้านบาท/ปี · SOM 12 ร้าน = 43,200 บาท/ปี
ข้อจำกัด: ฐาน TSIC 46414 เป็นกิจการค้าส่งเสื้อผ้าโดยรวม ไม่ได้แยกเฉพาะชุดชั้นใน และ SOM 12 ร้านเป็นเป้าจำลอง
แนวโน้ม (6.2): อีคอมเมิร์ซไทยปี 2565 = 5.43 ล้านล้านบาท ประเมินปี 2566 = 5.96 ล้านล้านบาท (ETDA)
  </aside>
</section>''')

# ---------------------------------------------------------------- 04 Product (table 4.3 Must have, table 8.3 status)
SLIDES.append('''
<section data-silk="right" data-cubes="none" data-sec="04" data-secname="Product">
  <div class="abs" style="left:150px;top:180px">
    <div class="kick in" style="--i:1">product_mmp</div>
    <div class="h2 sm in" style="--i:2;margin-top:24px">ฟีเจอร์ Must ของ <span class="g">MMP.</span></div>
  </div>
  <div class="ph in has-photo" role="img" aria-label="หน้าจอ Khonnai: สต็อกของรุ่น ออกบิล และออกบิลแล้ว" style="left:150px;top:350px;width:675px;height:628px;--i:3;--photo:url({PRODUCT});background-color:transparent;background-size:contain;background-repeat:no-repeat;background-position:center;box-sizing:border-box"></div>
  <div class="vleg" style="left:910px;top:372px;width:860px">
    <div class="vl-i in" style="--i:4"><i class="ai" data-i="list"></i><div><b>ตารางสต็อก</b><span>เช็กได้ทันที ไม่ต้องเดินขึ้นตึก 3 ชั้น</span></div></div>
    <div class="vl-i in" style="--i:5"><i class="w3" data-i="doc"></i><div><b>ร่างบิล → บิลเงินสด</b><span>ตัดสต็อกอัตโนมัติ ส่ง PDF ทาง LINE</span></div></div>
    <div class="vl-i in" style="--i:6"><i class="" data-i="spark"></i><div><b>พิมพ์ด่วน</b><span>เช่น “215 34 ดำ 3” + รุ่นขายบ่อย</span></div></div>
    <div class="vl-i in" style="--i:7"><i class="" data-i="cal"></i><div><b>การจองสินค้า</b><span>หน้าร้านกับ LINE ใช้สต็อกชุดเดียวกัน</span></div></div>
    <div class="vl-i in" style="--i:8"><i class="" data-i="cube"></i><div><b>รับสินค้าเข้าหลายรุ่น</b><span>พร้อมประวัติสินค้าเข้า–ออก</span></div></div>
    <div class="vl-i in" style="--i:9"><i class="" data-i="tag"></i><div><b>เพิ่มรุ่น 6 ขั้นตอน</b><span>ถามทีละคำถาม ใช้ง่ายสำหรับวัย 40+</span></div></div>
    <div class="vl-i in" style="--i:10"><i class="" data-i="refresh"></i><div><b>ฐานข้อมูลถาวร</b><span>ล็อกอิน + ซิงก์หลายอุปกรณ์</span></div></div>
    <div class="vl-i in" style="--i:11"><i class="" data-i="lock"></i><div><b>แยกข้อมูลร้าน</b><span>สิทธิ์ผู้ใช้ + สำรองข้อมูล</span></div></div>
  </div>
  <div class="vl-note in" style="left:910px;top:893px;--i:12"><i data-i="clock"></i><span>ตอนนี้: <b>MVP2</b> ทดสอบกับร้านนำร่องแล้ว · ระบบหลังบ้าน MMP อยู่ในแผน</span></div>
  <aside class="notes">
PRODUCT (ตารางที่ 4.3 ขอบเขต MMP ระดับ Must และตารางที่ 8.3 สถานะฟีเจอร์)
ภาพซ้าย: สต็อกของรุ่น · ออกบิล · ออกบิลแล้ว (แบบ Figma ของ MMP)
ความต่างจาก MVP2: ข้อมูลถาวรบนคลาวด์ ซิงก์เจ้าของกับผู้ช่วย แยกข้อมูลแต่ละร้าน และตัดสต็อกใน transaction
  </aside>
</section>''')

# ---------------------------------------------------------------- 05 Business Model (table 14.1, table 15.2)
SLIDES.append('''
<section data-silk="right" data-cubes="none" data-sec="05" data-secname="Business Model">
  <div class="abs" style="left:150px;top:180px">
    <div class="kick in" style="--i:1">revenue_model</div>
    <div class="h2 sm in" style="--i:2;margin-top:24px">Subscription<br><span class="g">3 แพ็กเกจ.</span></div>
  </div>
  <div class="abs" style="left:150px;right:150px;top:470px;display:grid;grid-template-columns:repeat(3,1fr);gap:28px">
    <div class="card glow in" style="--i:3;height:350px"><i class="ic lg" data-i="gift"></i><div class="ct" style="margin-top:34px;font-size:40px">Free · 0 บาท</div><div class="cb">20 รหัสสินค้า · 50 บิล/เดือน<br>เริ่มทดลองก่อนชำระเงิน</div></div>
    <div class="card glow in" style="--i:4;height:350px"><i class="ic lg" data-i="tag"></i><div class="ct" style="margin-top:34px;font-size:40px">Basic · 299 บาท/เดือน</div><div class="cb">200 รหัสสินค้า · 500 บิล/เดือน<br>รายปี 3,229.20 บาท (ลด 10%)</div></div>
    <div class="card glow in" style="--i:5;height:350px"><i class="ic lg" data-i="trophy"></i><div class="ct" style="margin-top:34px;font-size:40px">Pro · 699 บาท/เดือน</div><div class="cb">1,000 รหัสสินค้า · 2,000 บิล/เดือน<br>รายปี 7,549.20 บาท (ลด 10%)</div></div>
  </div>
  <div class="abs h4 in" style="left:150px;top:868px;--i:7">สมมติฐาน Basic 80% : Pro 20% → ราคาเฉลี่ย 379 บาท/ร้าน/เดือน</div>
  <aside class="notes">
BUSINESS MODEL (Lean Canvas 9.6, ตารางที่ 14.1 และ 15.2) รายได้จากค่าสมาชิกรายเดือน มีแผนรายปีลด 10%
ราคาเฉลี่ยถ่วงน้ำหนัก = 299 × 0.8 + 699 × 0.2 = 379 บาท/ร้าน/เดือน
ราคาทั้งหมดยังไม่ได้ทดสอบความเต็มใจจ่าย
  </aside>
</section>''')

# ---------------------------------------------------------------- 06 Traction (ch.12, table 5.5)
SLIDES.append('''
<section data-silk="right" data-cubes="tr" data-sec="06" data-secname="Traction">
  <div class="abs" style="left:150px;top:190px">
    <div class="kick in" style="--i:1">traction</div>
    <div class="h2 in" style="--i:2;margin-top:26px">ทดสอบกับ<br><span class="g">ร้านนำร่อง.</span></div>
  </div>
  <div class="abs body in" style="left:1000px;top:250px;width:620px;--i:3;font-size:32px">เจ้าของร้านลงมือใช้เว็บต้นแบบ <span class="b">MVP2</span> เองผ่านการแชร์หน้าจอ เมื่อ <span class="b">28 ต.ค. 2569</span></div>
  <div class="abs row" style="left:150px;right:150px;top:500px;gap:28px">
    <div class="card glow stat in" style="--i:4;min-height:300px"><i class="ic" data-i="hall"></i><div class="sv">1 ร้าน</div><div class="sl">ร้านนำร่องที่ทดสอบจริง</div></div>
    <div class="card glow stat in" style="--i:5;min-height:300px"><i class="ic" data-i="clock"></i><div class="sv">30 นาที</div><div class="sl">เพิ่มสต็อก · ทำบิล · ออกบิลจากการจอง</div></div>
    <div class="card glow stat in" style="--i:6;min-height:300px"><i class="ic" data-i="list"></i><div class="sv">7 ข้อค้นพบ</div><div class="sl">นำไปปรับ UX และตัดฟีเจอร์ที่ไม่ต้องการ</div></div>
  </div>
  <div class="abs h4 in" style="left:150px;top:868px;--i:8">เจ้าของร้านยินดีทดลองระบบอีกครั้งในรอบถัดไป</div>
  <aside class="notes">
TRACTION (บทที่ 12, ตารางที่ 5.5) ร้านนำร่อง 1 ร้าน ทดสอบเมื่อ 28 ต.ค. 2569 ประมาณ 30 นาที
ข้อค้นพบ 7 ประเด็น: หน้าสต็อกอ่านยาก, แป้นพิมพ์บังฟอร์ม, คำอธิบายสี/ไซซ์, ลำดับการกรอก, การค้นรายการออกบิลช้า, ไม่ต้องการแคตตาล็อก, ไม่ต้องการแจ้งเตือนของใกล้หมด
ขั้นถัดไป: ทดสอบซ้ำกับร้านเดิม และขยายไปร้านภายนอก 3–5 ร้าน
  </aside>
</section>''')

# ---------------------------------------------------------------- 07 Go-to-Market (ch.13.1)
SLIDES.append('''
<section class="s-pick" data-silk="low" data-cubes="tr" data-sec="07" data-secname="Market Plan">
  <div class="abs" style="left:150px;top:190px">
    <div class="kick in" style="--i:1">go_to_market</div>
    <div class="h2 in" style="--i:2;margin-top:26px">4 ช่วง สู่<br><span class="g">เป้าหมาย 134 ร้าน.</span></div>
  </div>
  <div class="pick">
    <div class="card glow pc in" style="--i:3"><div class="vis"><i class="ic lg" data-i="users"></i></div><div class="tx"><b>phase_1</b><span>หาร้านทดลอง</span><small>ร้านนำร่อง + ร้านภายนอก 3–5 ร้าน</small></div></div>
    <div class="card glow pc in" style="--i:4"><div class="vis"><i class="ic lg" data-i="key"></i></div><div class="tx"><b>phase_2</b><span>เริ่มใช้งานจริง</span><small>แพ็กเกจ Free + ทีมช่วยตั้งค่าสินค้าล็อตแรก</small></div></div>
    <div class="card glow pc in" style="--i:5"><div class="vis"><i class="ic lg" data-i="tag"></i></div><div class="tx"><b>phase_3</b><span>เปลี่ยนมาชำระเงิน</span><small>Basic / Pro · คุ้มทุนค่าเซิร์ฟเวอร์ที่ 7 ร้าน</small></div></div>
    <div class="card glow pc in" style="--i:6"><div class="vis"><i class="ic lg" data-i="globe"></i></div><div class="tx"><b>phase_4</b><span>ขยายผล</span><small>ชำระเงิน 134 ร้าน + Free 200 ร้าน ต้องได้ร้านใหม่ 8–10 ร้าน/เดือน</small></div></div>
  </div>
  <aside class="notes">
GO-TO-MARKET (บทที่ 13.1)
ช่วงที่ 1 ทดสอบซ้ำกับร้านนำร่อง แล้วขยายไปร้านภายนอกอย่างน้อย 3–5 ร้านใน กทม. และชลบุรี (งบระบบ 0 บาท)
ช่วงที่ 2 เมื่อ MMP เสร็จ ให้ร้านเริ่มใช้แพ็กเกจ Free พร้อมบริการช่วยตั้งค่าสินค้าและสอนใช้งาน
ช่วงที่ 3 เสนออัปเกรด Basic/Pro เมื่อเกินโควตา Free · ค่าโครงสร้างพื้นฐาน 1,575 บาท/เดือน คุ้มทุนค่าเซิร์ฟเวอร์ที่ 7 ร้าน (รวมค่าการตลาด 3,500 บาท/เดือน คุ้มทุนที่ 15 ร้าน) ก่อนถึง SOM 12 ร้าน
ช่วงที่ 4 ขยายสู่ร้านค้าส่งเสื้อผ้า เป้าหมายชำระเงิน 134 ร้าน (Basic 107 + Pro 27) และ Free 200 ร้าน
134 ร้านคือกรณี "เป้าหมาย" (15.5: ร้านใหม่ 8 ร้าน/เดือนในปีที่ 2 และ 10 ร้าน/เดือนในปีที่ 3–5 ทำได้ในปีที่ 3) · กรณี Base ในหน้า Financials ถึง 127 ร้านในปีที่ 5
ช่องทาง (13.3): เครือข่ายร้านนำร่องแนะนำต่อ · ลงพื้นที่หน้าร้าน · LINE OA และกลุ่มผู้ค้าส่งออนไลน์
  </aside>
</section>''')

# ---------------------------------------------------------------- 08 Competition (ch.10.2–10.4, 9.9)
SLIDES.append('''
<section data-silk="center" data-cubes="none" data-sec="08" data-secname="Competition">
  <div class="abs" style="left:150px;top:190px">
    <div class="kick in" style="--i:1">competition</div>
    <div class="h2 in" style="--i:2;margin-top:26px">ทางเลือกเดิม vs <span class="g">Khonnai.</span></div>
  </div>
  <div class="card glow no yn in" style="left:150px;--i:3"><i class="ic no" data-i="cross" data-sw="2.4"></i><div class="lbl">วิธีเดิม &amp; ซอฟต์แวร์ทั่วไป</div><div class="cb" style="font-size:28px">สมุด Note LINE: ข้อมูลกระจาย สต็อกไม่เชื่อมกับบิล<br>ZORT 600 · Page365 799 · FlowAccount 299 บาท/เดือน: ฟีเจอร์กว้าง หน้าจอแบบตาราง ต้องเรียนรู้เยอะ</div></div>
  <div class="card glow yes yn fragment rise" style="left:990px"><i class="ic yes" style="background:none;box-shadow:0 0 34px rgba(94,230,160,.45)"><img src="{KICON}" alt="Khonnai" style="width:78px;height:78px;display:block"></i><div class="lbl">Khonnai</div><div class="cb" style="font-size:28px">ใช้ง่ายสำหรับเจ้าของร้านวัย 40+: ตัวเลขใหญ่ ปุ่มใหญ่ ภาษาไทยตรงไปตรงมา ทำทีละขั้น<br>เฉพาะทางค้าส่ง: สต็อกตามรุ่น/ไซซ์/สี/แพ็ก</div></div>
  <div class="abs in" style="left:0;right:0;top:905px;display:flex;justify-content:center;--i:6"><div class="vl-note" style="position:static;padding:12px 24px;font-size:22px"><i data-i="key"></i><span><b>Unfair advantage</b> เข้าถึงร้านค้าส่งจริงผ่านธุรกิจครอบครัว + เรียนรู้จากผู้ใช้จริงได้เร็ว</span></div></div>
  <aside class="notes">
COMPETITION (บทที่ 10.2–10.4 และ 9.9) กดหนึ่งครั้งเพื่อแสดงฝั่ง Khonnai
คู่แข่ง 4 กลุ่ม: วิธีเดิม (สมุด บิลมือ Note LINE Excel), LINE MyShop/OA, ZORT (Starter 600 บาท/เดือน), Page365 (Solo 799 บาท/เดือน), FlowAccount (Pro 299 บาท/เดือน)
จุดต่างหลักคือความง่าย: ระบบทั่วไปฟีเจอร์กว้างและหน้าจอแบบตาราง ส่วน Khonnai ออกแบบให้เจ้าของร้านที่ไม่คุ้นเทคโนโลยีใช้ได้ (10.4 ข้อ 5, 4.2) · FlowAccount Pro ราคา 299 เท่ากัน ราคาจึงไม่ใช่จุดต่าง
Unfair advantage: Founder-Market Fit, ความรู้หน้างานเรื่องสต็อกแพ็ก/โหล และวงจรเรียนรู้จากผู้ใช้จริงที่รวดเร็ว
  </aside>
</section>''')

# ---------------------------------------------------------------- 09 Team (cover, table 11.1)
SLIDES.append('''
<section data-silk="center" data-cubes="none" data-sec="09" data-secname="Team">
  <div class="abs" style="left:150px;top:180px">
    <div class="kick in" style="--i:1">the_team</div>
    <div class="h2 sm in" style="--i:2;margin-top:24px">ทีม <span class="g">Khonnai.</span></div>
  </div>
  <div class="abs small in" style="right:150px;top:262px;--i:2;text-align:right">My Little Pony · กลุ่ม 3</div>
  <div class="jgrid five">
{TEAM}
  </div>
  <aside class="notes">
TEAM (ตารางที่ 11.1) สมาชิก 5 คน แบ่งงานตามสายงาน
  </aside>
</section>''')

# ---------------------------------------------------------------- 10 Vision (ch.2.3)
SLIDES.append('''
<section data-silk="hot" data-cubes="corners" data-sec="10" data-secname="Vision">
  <div class="abs c" style="left:0;right:0;top:300px">
    <div class="kick in" style="--i:1">long_term_vision</div>
    <div class="statement in" style="--i:2;margin-top:40px;font-size:96px">ระบบสต็อกและออกบิลเฉพาะทาง</div>
    <div class="statement in" style="--i:4;margin-top:20px;font-size:96px"><span class="g">ของร้านค้าส่งเสื้อผ้าทั่วไทย.</span></div>
    <div class="lede in" style="--i:6;margin-top:60px">จาก SAM กทม. + ชลบุรี <b>5,696</b> กิจการ สู่ TAM ทั่วประเทศ <b>8,770</b> กิจการ</div>
  </div>
  <aside class="notes">
VISION (บทที่ 2.3 ทิศทางระยะยาว)
เป็นระบบบริหารสต็อกและออกบิลบนมือถือเฉพาะทางสำหรับร้านค้าส่งชุดชั้นในและเสื้อผ้าขนาดเล็กทั่วไทย ที่มีรุ่น ไซซ์ สี และหน่วยขายแบบแพ็กหรือโหล
เปลี่ยนความรู้ในความทรงจำของเจ้าของร้านให้เป็นข้อมูลที่ตรวจย้อนหลังได้ ช่วยตัดสินใจสั่งซื้อภายใต้เงินทุนจำกัด และให้ผู้ช่วยหรือผู้รับช่วงกิจการทำงานต่อได้
  </aside>
</section>''')

# ---------------------------------------------------------------- 11 Financials (ch.15.6 table 15.4, 5-year Base case)
# (year, revenue, operating profit, paying shops at year end) — Milestone2_Final_v3.pdf table 15.4
FIN = [(1, 52113, -14679, '21'), (2, 193930, 71477, '57'), (3, 363362, 193068, '95'),
       (4, 489008, 309934, '116'), (5, 556902, 373083, '127')]
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
<section data-silk="right" data-cubes="none" data-sec="11" data-secname="Financials">
  <div class="abs" style="left:150px;top:180px">
    <div class="kick in" style="--i:1">financials --base --60m</div>
    <div class="h2 sm in" style="--i:2;margin-top:24px">ประมาณการ <span class="g">5 ปี.</span></div>
  </div>
  <div class="abs row in" style="left:150px;top:372px;gap:16px;--i:3"><span class="pill ai"><span class="dot"></span>รายได้ค่าสมาชิก (บาท)</span><span class="pill w3"><span class="dot"></span>กำไรจากการดำเนินงาน (บาท)</span></div>
  <div class="pod ai" style="left:150px;bottom:190px;width:1060px;height:440px">
''' + ''.join(fin_parts) + '''
  </div>
  <div class="ubl" style="left:1330px;top:372px;width:440px">
    <div class="ubl-i in" style="--i:6"><i data-i="clock"></i><div><b>เดือนที่ 9</b><span>เริ่มมีกำไรรายเดือน</span></div></div>
    <div class="ubl-i in" style="--i:7"><i data-i="trophy"></i><div><b>เดือนที่ 18</b><span>กำไรสะสมกลับเป็นบวก</span></div></div>
    <div class="ubl-i in" style="--i:8"><i data-i="users"></i><div><b>127 ร้าน</b><span>ชำระเงินสิ้นปีที่ 5 · รายได้ปีละ 556,902 บาท</span></div></div>
  </div>
  <div class="vl-note in" style="left:1330px;top:790px;width:440px;font-size:21px;--i:10"><i data-i="alert"></i><span>หลังปีที่ 3 โตช้าลง: ร้านใหม่ปีละ 84 ร้าน ใกล้เคียงร้านที่ยกเลิก (Churn 5%/เดือน)</span></div>
  <aside class="notes">
FINANCIALS 5 ปี (บทที่ 15.6 ตารางที่ 15.4 กรณี Base หน่วยบาท ตัวเลขในวงเล็บคือค่าติดลบ)
รายได้ปี 1–5: 52,113 / 193,930 / 363,362 / 489,008 / 556,902
ค่าใช้จ่ายรวม (เงินสด): 66,792 / 122,453 / 170,294 / 179,074 / 183,819
กำไรจากการดำเนินงาน: (14,679) / 71,477 / 193,068 / 309,934 / 373,083
ร้านที่ชำระเงินสิ้นปี: 21.2 / 57.4 / 95.4 / 115.9 / 127.0 · MRR เดือนสุดท้าย: 8,029 / 21,759 / 36,146 / 43,920 / 48,121
เงินสดคงเหลือปลายปี (รวมเงินทุน 60,000): 41,321 / 112,798 / 305,866 / 615,800 / 988,883
ตั้งแต่ปีที่ 4 ร้านใหม่ปีละ 84 ร้านใกล้เคียงร้านที่ยกเลิก จำนวนร้านเข้าใกล้ระดับคงที่ราว 140 ร้าน การเติบโตต้องอาศัยการลด churn หรือเพิ่มร้านใหม่
Scenario (15.7): ทุกกรณีเงินสดเป็นบวกตลอด 60 เดือน · กรณีเป้าหมาย 134 ร้านทำได้ในปีที่ 3 และสิ้นปีที่ 5 มีราว 182 ร้าน (3.2% ของ SAM)
Unit economics (15.8): ARPU สุทธิ 352.5 บาท · CAC 1,500 · LTV 7,050 · LTV:CAC 3.8 · CAC payback 5.3 เดือน
ไม่รวมภาษี ค่าโดเมน และค่าแรงที่จ่ายจริง ตัวเลขทั้งหมดเป็นประมาณการ
  </aside>
</section>''')

# ---------------------------------------------------------------- 12 The Ask (ch.15.4, 15.9, table 15.8)
ASK = [('18,900', 'ค่าโครงสร้างพื้นฐาน 12 เดือน', '#ffb27f', 0.0, 31.5),
       ('28,000', 'การตลาดและลงพื้นที่', '#ff8032', 31.5, 46.7),
       ('4,000', 'อุปกรณ์และสื่อเดโม', '#82a6ff', 78.2, 6.7),
       ('9,100', 'เงินสำรอง', '#3d6ef5', 84.9, 15.1)]
bar = ''.join(f'<i style="left:calc({l:.3f}% + {0 if k == 0 else 3}px);width:calc({w:.3f}% - 3px);background:{c};animation-delay:{3.1 + .15 * k:.2f}s"></i>'
              for k, (_, _, c, l, w) in enumerate(ASK))
legend = ''.join(f'<div class="in" style="--i:{6 + k}"><div class="h4" style="font-size:40px;color:#fff"><i style="display:inline-block;width:14px;height:14px;border-radius:4px;background:{c};margin-right:14px;vertical-align:middle;box-shadow:0 0 12px {c}"></i>{v}</div><div class="small" style="margin-top:8px;font-size:22px;color:rgba(255,255,255,.75)">{t}</div></div>'
                 for k, (v, t, c, _, _) in enumerate(ASK))
SLIDES.append('''
<section class="s-pp" data-silk="center" data-cubes="none" data-sec="12" data-secname="The Ask" data-pp-a="23928" data-pp-b="60000">
  <div class="burst"></div>
  <div class="abs c" style="left:0;right:0;top:230px">
    <div class="kick in" style="--i:1"><span class="pp-ks"><span class="pp-k0">cash_needed --base</span><span class="pp-k1">the_ask --covers base,downside,stress</span></span></div>
    <div class="pp-stage in grow" style="--i:2;margin-top:60px">
      <div class="pp-num pp-old"><span class="pp-strike"><span data-count="23928" data-dur="2" data-delay=".3" style="display:inline-block;line-height:.9">23,928</span></span><small>บาท</small><div class="pp-was">เงินสุทธิสูงสุดที่ต้องใช้ กรณี Base</div></div>
      <div class="pp-num pp-new"><span class="pp-n" style="display:inline-block;line-height:.9">60,000</span><small>บาท</small></div>
    </div>
  </div>
  <div class="pp-after">
  <div class="pbar in soft" style="left:150px;right:150px;top:690px;--i:4">''' + bar + '''</div>
  <div class="abs" style="left:150px;right:150px;top:752px;display:grid;grid-template-columns:repeat(4,1fr);gap:24px">''' + legend + '''</div>
  <div class="abs row in" style="left:0;right:0;top:900px;justify-content:center;align-items:center;gap:20px;--i:9"><i class="ic sm" data-i="shield"></i><span class="h4" style="font-size:34px">กรณี Stress (MMP ล่าช้า 6 เดือน) เงินสดต่ำสุดยังเหลือ 5,622 บาท</span></div>
  </div>
  <span class="fragment step"></span>
  <aside class="notes">
THE ASK (บทที่ 15.4 และ 15.9) เริ่มจากตัวเลข 23,928 บาท = เงินสุทธิสูงสุดที่กรณี Base ต้องใช้
[กด] ตัวเลขถูกขีดฆ่า แล้วนับขึ้นเป็น 60,000 บาท = เงินทุนที่ขอ ครอบคลุมกรณี Base (23,928), Downside (40,680) และ Stress (54,378) โดยไม่ต้องหาเงินเพิ่ม
การใช้เงิน (ตารางที่ 15.8): โครงสร้างพื้นฐาน 18,900 (31.5%) · การตลาดและลงพื้นที่ 28,000 (46.7%) · สื่อเดโม 4,000 (6.7%) · เงินสำรอง 9,100 (15.2%)
  </aside>
</section>''')

# ---------------------------------------------------------------- Q&A (prototype link, ch.5.6)
SLIDES.append('''
<section data-silk="cover" data-cubes="none" data-sec="12" data-secname="Q&amp;A">
  <div class="abs" style="left:150px;top:300px">
    <div class="kick in" style="--i:1">q_and_a</div>
    <div class="statement in" style="--i:2;margin-top:30px;font-size:150px"><span class="g">Q&amp;A</span></div>
    <div class="lede in" style="--i:4;margin-top:40px">ลองใช้เว็บต้นแบบ <span class="g">Khonnai MVP2</span></div>
  </div>
  <div class="qr in grow" style="left:1330px;top:250px;width:440px;height:440px;--i:5"><img src="{QR}" alt="QR code: micro-erp-green.vercel.app"></div>
  <div class="qr-l in" style="left:1280px;top:725px;width:540px;--i:7">micro-erp-green.vercel.app</div>
  <aside class="notes">
Q&amp;A · QR เปิดเว็บต้นแบบ https://micro-erp-green.vercel.app/
  </aside>
</section>''')

# Team cards: Thai name, then English name and student ID (given by the team).
# Photos are read from build/assets/team-1..5.(jpg|png|webp) in this order.
TEAM = [
    ('บวร กุลธรรมโยธิน', 'Borworn Kultumyotin<br>67130500017'),
    ('รพีพงษ์ นักสาร', 'Rapeepong Naksan<br>67130500032'),
    ('นันทภัทร์ จันทขูศักดิ์', 'Nantapat Chantachoosak<br>67130500094'),
    ('สุรพจน์ ทองเพชร', 'Surapoj Thongphet<br>67130500120'),
    ('ชิชากร สุวรรณาศรัย', 'Chichakorn Suwannasai<br>67130501029'),
]
