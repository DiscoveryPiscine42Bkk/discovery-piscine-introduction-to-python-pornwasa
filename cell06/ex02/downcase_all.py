import sys  # ใช้สำหรับรับ argument จาก command line

def downcase_it(text):
    return text.lower()

if len(sys.argv) == 1:
    print("none")
else:
    for arg in sys.argv[1:]:
        print(downcase_it(arg))

