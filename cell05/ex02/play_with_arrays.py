#!/usr/bin/env python3

# กำหนด array แรก
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# สร้าง array ใหม่: เฉพาะค่าที่มากกว่า 5 และบวก 2
new_array = [x + 2 for x in original_array if x > 5]

# แสดงผลลัพธ์
print("Original array:", original_array)
print("New array:", new_array)
