"""
Sana: 27.04.2024
Dars: 11-dars / Amaliyot
Mavzu: BIR NECHTA SHARTLARNI TEKSHIRISH
       if-elif-else zanjiri, "and", "or", "not" operatorlari bilan tanishamiz
"""

# Quyidagi dasturlarni alohida fayllarga yozing va bajaring:

# 7. Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni
# 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.

son = int(input("Istalgan butun son kiriting: "))
for i in range(2, 11):
    if son % i == 0:   # if not (son % i):
        print(f"{son} soni {i} ga qoldiqsiz bo'linadi")

