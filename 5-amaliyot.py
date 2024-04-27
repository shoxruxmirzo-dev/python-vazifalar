"""
Sana: 25.04.2024
Dars: 5-dars / Nazariya
Mavzu: STRING (MATN)
       STRING ma'lumot turi va uning ustida amallar
"""

# Quyidagi mashqlarni bajaring:

# 1. Quyidagi o'zgaruvchilarni yarating:
kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"

# 2. Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
info = kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani, " + viloyat + " viloyati"
info1 = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(info, info1, sep="\n")

# 4. Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
info1 = f"\n{kocha} ko'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati"
print(info1)

# 5. Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
manzil = f"\n{kocha} ko'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati"

# 6. manzil ga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print("\n",manzil.capitalize(), sep="")
print(manzil.title())
print(manzil.upper())
print(manzil.lower())

# 3. Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat)
# qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
kocha2 = input("\nKo'cha nomi: ").capitalize()
mahalla2 = input("Mahalla nomi: ").capitalize()
tuman2 = input("Tuman: ").capitalize()
viloyat2 = input("Viloyat: ").capitalize()
info2 = f"{kocha2} ko'chasi, {mahalla2} mahallasi, {tuman2} tumani, {viloyat2} viloyati"
print(info2)

