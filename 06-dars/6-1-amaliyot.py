"""
Sana: 25.04.2024
Dars: 6-dars / Amaliyot
Mavzu: SONLAR
       Pythonda sonlar bilan ishlashni o'rganamiz
"""

# Quyidagi dasturlarning har birini alohida fayl ko'rinishida yozing va bajaring:

# 1. Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur

savol = "Istalgan son kiriting: \n>>>"
son = int(input(savol))
javob = f"{son} ning kvadrati {son**2} ga teng,"
javob += f"\n{son} ning kubi {son**3} ga teng!"
print(javob)