"""
Sana: 27.04.2024
Dars: 10-dars / Amaliyot
Mavzu: IF-ELSE
       Dasturni tarmoqlashni o'rganamiz
"""

# 1. Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat
# elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == "gm":
        car = car.upper()
    else:
        car = car.capitalize()
    print(car)
print("")


# 2. Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != "gm":
        car = car.capitalize()
    else:
        car = car.upper()
    print(car)


# 3. Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin.
# Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda,
# "Xush kelibsiz, {foydalanuvchi_ismi}! "  matnini konsolga chiqaring.
login = input("Loginingizni kiriting:>>> ")
if login.lower() == "admin":
    print(f"Hush kelibsiz, {login.capitalize()}."
          f"\nFoydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Hush kelibsiz, {login.capitalize()}!")


# 4. Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa,
# "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
print("Ikita son kiriting: ")
a = int(input("1-son: "))
b = int(input("2-son: "))
if a == b: print(f"{a} va {b} soni o'zaro teng")


# 5. Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa
# konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
son = int(input("Istalgan son kiriting: "))
print("Manfiy son") if son < 0 else print("Musbat son")


# 6. Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab
# konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
x = int(input("Son kiriting: "))
print(f"{x} ning ildizi {x**0.5}") if x > 0 else print("Musbat son kiriting")

