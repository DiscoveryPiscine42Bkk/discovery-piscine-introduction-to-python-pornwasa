def array_of_names(persons):
    result = []
    for first, last in persons.items():
        # ใช้ .capitalize() เพื่อทำให้ตัวอักษรตัวแรกเป็นตัวพิมพ์ใหญ่
        full_name = f"{first.capitalize()} {last.capitalize()}"
        result.append(full_name)
    return result


# ตัวอย่างสำหรับทดสอบ
if __name__ == "__main__":
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }

    print(array_of_names(persons))
