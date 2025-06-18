#!/usr/bin/env python3
import sys

# รับ arguments (ไม่เอาชื่อไฟล์)
args = sys.argv[1:]

# เช็คจำนวน argument
if len(args) != 1:
    print("none")
else:
    param = args[0]
    user_input = input("What was the parameter? ")

    if user_input == param:
        print("Good job!")
    else:
        print("Nope, sorry...")
