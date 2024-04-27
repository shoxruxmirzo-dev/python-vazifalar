"""
Sana: 27.04.2024
Dars: 11-dars / Amaliyot
Mavzu: BIR NECHTA SHARTLARNI TEKSHIRISH
       if-elif-else zanjiri, "and", "or", "not" operatorlari bilan tanishamiz
"""

# Quyidagi dasturlarni alohida fayllarga yozing va bajaring:

# 5. Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang.
# Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yangi, bor_mahsulotlar degan ro'yxatga,
# do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati
# bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda
# esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

mahsulotlar = ["olma", "nok", "banan", "novvot", "tuxum", "sut", "kofe", "non", "choy", "go'sht", "yog'"]
savat = []

print("5 ta mahsulot kiriting: ")
for i in range(5):
    savat.append(input(f"Savatga {i+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot.lower() in mahsulotlar:
        bor_mahsulotlar.append(mahsulot.lower())
    else:
        mavjud_emas.append(mahsulot.lower())

if mavjud_emas:
    print(f"Quyidagi mahsulotlar do'konimizda yo'q:")
    for x in mavjud_emas:
        print(x)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

