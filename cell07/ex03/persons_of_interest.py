def famous_births(people):
    # เรียงตามวันเกิด (แปลง string เป็น int เพื่อให้เรียงถูกต้อง)
    sorted_people = sorted(people.values(), key=lambda person: int(person["date_of_birth"]))
    
    # แสดงผลลัพธ์
    for person in sorted_people:
        print(f'{person["name"]} is a great scientist born in {person["date_of_birth"]}.')

# ตัวอย่าง dictionary ของนักวิทยาศาสตร์หญิง
women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecilia Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

# เรียกใช้งานฟังก์ชัน
famous_births(women_scientists)
