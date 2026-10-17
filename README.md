# ค่ากะ-เบี้ยเลี้ยง — ไอคอนบนมือถือ (PWA launcher)

หน้าเว็บบน GitHub Pages สำหรับ "ติดตั้งลงหน้าจอมือถือ" ทั้ง 2 ระบบ (ตัวระบบยังอยู่บน Google Forms / Apps Script เหมือนเดิม)

- `v1/` → Google Form (ระบบ v1)
- `v2/` → Apps Script Web App + GPS (ระบบ v2)
- เปลี่ยนชุดไอคอน: แก้ตัวอักษรในไฟล์ `icon.txt` เป็น `A`, `B` หรือ `C` แล้ว commit — เว็บจะสร้างใหม่อัตโนมัติ (GitHub Actions รัน `make.py`)
- เปลี่ยนลิงก์ระบบ: แก้ค่า `@URL@` ในตัวแปร `APPS` ของ `make.py`
