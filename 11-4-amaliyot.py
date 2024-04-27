"""
Sana: 27.04.2024
Dars: 11-dars / Amaliyot
Mavzu: BIR NECHTA SHARTLARNI TEKSHIRISH
       if-elif-else zanjiri, "and", "or", "not" operatorlari bilan tanishamiz
"""

# Quyidagi dasturlarni alohida fayllarga yozing va bajaring:

# 4. mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan
# bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang.
# Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa
# "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

mahsulotlar = ["olma", "nok", "banan", "novvot", "tuxum", "sut", "kofe", "non", "choy", "go'sht", "yog'"]
savat = []

son = int(input("Nechta mahsulot nomini kiritmoqchisz: "))
for i in range(son):
    savat.append(input(f"{i+1}-mahsulotingiz: "))

if savat:
    for mahsulot in savat:
        if mahsulot.lower() in mahsulotlar:
            print(f"{mahsulot.capitalize()} do'konimizda bor")
        else:
            print(f"{mahsulot.capitalize()} do'konimizda yo'q")
else:
    print("Savatingizda mahsulot yo'q")

