#!/usr/bin/env python3
import sys

args = sys.argv[1:]  # ข้ามชื่อไฟล์ .py

if len(args) == 0:
    print("none")
else:
    for word in args:
        if not word.endswith("ism"):
            print(word + "ism")
