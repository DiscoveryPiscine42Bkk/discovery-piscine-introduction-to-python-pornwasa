#!/usr/bin/env python3

import sys

# ลบ 1 จากความยาวของ sys.argv เพราะ argv[0] คือชื่อไฟล์
number_of_parameters = len(sys.argv) - 1

print(f"Number of parameters: {number_of_parameters}.")
