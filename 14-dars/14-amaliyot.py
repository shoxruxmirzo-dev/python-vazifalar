"""
Sana: 28.04.2024
Dars: 14-dars / Amaliyot
Mavzu: LUG'AT BILAN TANISHUV
       Yangi ma'lumot turi - Dictionary bilan tanishamiz.
"""

# 1. otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida
# kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo).
# Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :
# Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan

ukam = {
    "ism": "sardor",
    "t_yil": 1998,
    "shahar": "andijon",
    "ish_joyi": "AMZ AJ"
}
print(f"Ukamning ismi {ukam["ism"].title()}, {ukam["t_yil"]}-yilda {ukam["shahar"].title()} shahrida tug'ilgan")


# 2. Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi
# bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh

taomlar = {
    "men": "osh",
    "onasi": "monti",
    "qizim": "kartoshka-tuxum"
}
print(f"Mening sevimli taomim {taomlar["men"]}")
print(f"Ayolimning sevimli taomi {taomlar["onasi"]}")
print(f"Qizimning sevimli taomi {taomlar["qizim"]}")


# 3. Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting
# (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.

py_lugat = {
    "print": "print() funksiyasi ma'lumotlarni konsolga chiqaradishda ishlatiladi",
    "variable": "kompyuter xotirasida ma'lum bir qiymatni saqlash uchun ajratilgan joy",
    "string": "(str) belgilardan iborat matn ko'rinishidagi ma'lumot turi",
    "integer": "(int) butun sonlar ko'rinishidagi ma'lumot turi",
    "float": "(float) o'nlik sonlar ko'rinishidagi ma'lumot turi",
    "input": "input() funksiyasi foydalanuvchidan ma'lumot qabul qilish uchun ishlatiladi",
    "list": "(list) bir nechta qiymatlardan iborat ro'yxat ko'rinishidagi ma'lumot turi",
    "for": "(loop) tsikl operatori, biror amalni bir necha marta bajarish uchun ishlatiladi",
    "boolean": "(bool) mantiqiy qiymatlar (True, False) ko'rinishidagi ma'lumot turi",
    "dictionary": "(dict) lug'at (kalit so'z: qiymat) ko'rinishidagi ma'lumot turi"
}

# 4. Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib
# bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunday so'z mavjud emas" degan xabarni chiqaring.

kalit = input("\nPython tegishli biror kalit so'z kiriting: ").lower()
print(py_lugat.get(kalit, "Bunday so'z mavjud emas"))


# 5. Yuqoridagi vazifani if-else yordamida qiling va natijani
# ham foydalanuvchiga tushunarli ko'rinishda chiqaring.

izoh = py_lugat.get(kalit)
if izoh == None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {izoh}")

