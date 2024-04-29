"""
Sana: 28.04.2024
Dars: 15-dars / Amaliyot
Mavzu: LUG'AT ELEMENTLARI BILAN ISHLASH
       Lug'at ichida ro'yxat, lug'at ichida lug'at?
"""

# 1. Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har
# bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.

py_lugat = {
    "variable": "qiymatni saqlash uchun ajratilgan joy",
    "string": "matn ko'rinishidagi ma'lumot turi",
    "integer": "butun son",
    "float": "o'nlik son",
    "list": "ro'yxat ko'rinishidagi ma'lumot turi",
    "for": "biror amalni qayta-qayta bajarish tikli",
    "boolean": "mantiqiy qiymatlari",
    "dictionary": "lug'at ko'rinishidagi ma'lumot turi"
}
for key, value in sorted(py_lugat.items()):
    print(f"{key.title()} - {value.capitalize()}")


# 2. Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni,
# keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.

davlatlar = {
    "angliya": "london",
    "aqsh": "vashington",
    "germaniya": "berlin",
    "rossiya": "moskva",
    "turkiya": "anqara",
    "fransiya": "parij",
    "italiya": "rim",
    "kanada": "ottava",
    "baa": "abu-dabi"
}
print("\nDunyo davlatlari:")
for davlat in sorted(davlatlar.keys()):
    if davlat == "aqsh" or davlat == "baa":
        print(davlat.upper())
    else:
        print(davlat.title())

print("\nDavlatlarning poytaxtlari:")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())


# 3. Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring.
# Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

davlat = input("Davlat nomini kiriting: ").lower()
poytaxt = davlatlar.get(davlat)
if poytaxt == None:
    print("Bizday bunday ma'lumot yo'q")
else:
    print(f"{davlat.upper()} ning poytaxti {poytaxt.title()} shahri")


# 4. Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan
# 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring,
# agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

menu = {
    "osh": 25000,
    "mastava": 18000,
    "atala": 20000,
    "bifshteks": 22000,
    "lag'mon": 15000,
    "do'lma": 17000,
    "sho'rva": 25000,
    "monti": 24000,
    "kabob": 30000,
    "somsa": 24000
}
buyurtmalar = []
print("3 ta taomga buyurtma bering: ")
for i in range(3):
    buyurtmalar.append(input(f"{i+1}-taomingiz: ").lower())

for taom in buyurtmalar:
    if taom in menu.keys():
        print(f"{taom.title()} {menu[taom]} so'm")
    else:
        print(f"Bizda {taom} yo'q")
