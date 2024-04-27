"""
Sana: 27.04.2024
Dars: 11-dars / Amaliyot
Mavzu: BIR NECHTA SHARTLARNI TEKSHIRISH
       if-elif-else zanjiri, "and", "or", "not" operatorlari bilan tanishamiz
"""

# Quyidagi dasturlarni alohida fayllarga yozing va bajaring:

# 3. Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va
# ularning teng yoki katta/kichikligi haqida xabarni chiqaring

print("2 ta son kiriting:")
a = int(input("1 son: "))
b = int(input("2 son: "))

if a > b:
    c = "> (katta)"
elif a < b:
    c = "< (kichik)"
else:
    c = "= (teng)"
print(f"{a} {c} {b}")

