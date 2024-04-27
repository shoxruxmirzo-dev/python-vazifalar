"""
Sana: 27.04.2024
Dars: 11-dars / Amaliyot
Mavzu: BIR NECHTA SHARTLARNI TEKSHIRISH
       if-elif-else zanjiri, "and", "or", "not" operatorlari bilan tanishamiz
"""

# Quyidagi dasturlarni alohida fayllarga yozing va bajaring:

# 1. Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa
# "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

son = int(input("Juft son kiriting: "))
if son % 2 == 0:  # son % 2:  print(f"{son} soni juft emas")
    print(f"Rahmat, {son} juft son")
else:
    print(f"{son} soni juft emas")

