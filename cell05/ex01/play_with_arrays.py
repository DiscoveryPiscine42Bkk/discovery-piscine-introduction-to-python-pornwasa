#!/usr/bin/env python3

# กำหนด array แรก
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# สร้าง array ใหม่ โดยเพิ่มแต่ละค่าจาก original_array ทีละ 2
new_array = [x + 2 for x in original_array]

# แสดงผลลัพธ์
print("Original array:", original_array)
print("New array:", new_array)
