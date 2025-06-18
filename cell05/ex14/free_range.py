#!/usr/bin/env python3
import sys

# รับ argument ทั้งหมด ยกเว้นชื่อไฟล์
args = sys.argv[1:]

# ตรวจสอบว่ามีพารามิเตอร์ครบ 2 ตัวหรือไม่
if len(args) != 2:
    print("none")
else:
    try:
        # แปลงพารามิเตอร์เป็น int
        start = int(args[0])
        end = int(args[1])

        # ถ้าเริ่มต้นน้อยกว่าหรือเท่าปลาย → range ธรรมดา
        if start <= end:
            numbers = list(range(start, end + 1))
        else:
            # ถ้าค่าเริ่มมากกว่า → สร้าง range ถอยหลัง
            numbers = list(range(start, end - 1, -1))

        # แสดงลิสต์ที่สร้างได้
        print(numbers)
    except ValueError:
        # ถ้าแปลง int ไม่ได้
        print("none")
