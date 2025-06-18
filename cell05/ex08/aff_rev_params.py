#!/usr/bin/env python3
import sys

# ไม่รวม sys.argv[0] ซึ่งเป็นชื่อไฟล์
params = sys.argv[1:]

if len(params) < 2:
    print("none")
else:
    for param in reversed(params):
        print(param)
