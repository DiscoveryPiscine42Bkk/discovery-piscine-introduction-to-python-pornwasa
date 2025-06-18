#!/usr/bin/env python3
import sys
import re

# ดึง argument (ไม่เอาชื่อไฟล์)
args = sys.argv[1:]

# ตรวจว่าต้องมีพารามิเตอร์ 2 ตัว
if len(args) != 2:
    print("none")
else:
    keyword = args[0]
    text = args[1]

    # ใช้ re.findall เพื่อหาคำ keyword
    matches = re.findall(re.escape(keyword), text)

    if not matches:
        print("none")
    else:
        print(len(matches))
