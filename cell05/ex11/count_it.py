#!/usr/bin/env python3
import sys

args = sys.argv[1:]  # ตัด argv[0] ออก (ชื่อไฟล์)

if len(args) == 0:
    print("none")
else:
    print(f"parameters: {len(args)}")
    for arg in args:
        print(f"{arg}: {len(arg)}")
