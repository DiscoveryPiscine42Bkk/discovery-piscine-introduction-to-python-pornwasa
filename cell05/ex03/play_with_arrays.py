#!/usr/bin/env python3

# original array
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# สร้าง new_array โดย:
# 1. กรองค่าที่มากกว่า 5
# 2. บวก 2 ให้ทุกตัว
new_array = [x + 2 for x in original_array if x > 5]

# แปลงเป็น set เพื่อลบค่าที่ซ้ำ
unique_values = set(new_array)

# แสดงผล
print(original_array)
print(unique_values)
