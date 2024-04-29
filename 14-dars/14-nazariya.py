"""
Sana: 28.04.2024
Dars: 14-dars / Nazariya
Mavzu: LUG'AT BILAN TANISHUV
       Yangi ma'lumot turi - Dictionary bilan tanishamiz.
"""

# LUG'AT (DICTIONARY) NIMA?

# Odatda, lug'atdagi ma'umotlar ikki qismdan iborat bo'ladi: kalit so'z va izoh (yoki tarjima).
# Xuddi oddiy lug'atlardagi ka'bi Python lug'atidagi ma'lumotlar ham ikki qismdan iborat bo'ladi:
# kalit so'z va qiymat (ingliz tilida key-value pair yoki kalit so'z-qiymat juftligi deyiladi).

"""
Dasturlashda ko'p ishlatiladigan atamalarni ingliz tilida yodlab qolish juda muhim! 
Bu sizga kelajakda yangi ma'lumotlar izlashda, xatolar usitda ishlashda va umuman ish 
faoliyatingizda ko'p asqotadi. Shuing uchun variable, integer, float, string, list, 
tuple, dictionary, function, loop, va boshqa so'zlarni yaxshilab o'zlashtirib oling.
"""

# LUG'AT BILAN ISHLASH

# Pytonda lug'at kalit so'z-qiymat juftliklarining yi'ginidisi ekan.
# Lug'atdagi biror qiymatni ko'rish uchun unga kalit so'z orqali murojat qilamiz:

car_0 = {"model": "ferrari", "rang": "qizil"}
print(car_0["model"].capitalize())
print(car_0["rang"])

# Lug'atdagi qiymatlar son (int, float), matn (string),
# ro'yxat (list, tuple) va hatto boshqa lug'at ham bo'lishi mumkin.

talaba_0 = {
    "ism": "Murod Olimov",
    "yosh": 20,
    "t_yil": 2000
}
print(f"{talaba_0["ism"].title()} {talaba_0["t_yil"]}-yilda tug'ilgan, {talaba_0["yosh"]} yoshda.")

# YANGI JUFTLIK QO'SHISH

talaba_0["kurs"] = 4
talaba_0["fakultet"] = "informatika"

print(talaba_0)

# BO'SH LUG'AT

talaba_1 = {}  # bo'sh lug'at

talaba_1["ism"] = "qobil rasulov"
talaba_1["kurs"] = 3
talaba_1["yosh"] = 20
print(talaba_1)
print(f"Talaba {talaba_1["ism"].title()} {talaba_1["kurs"]}-kurs")

# Lug'atga kalit so'zlar qanday ketma-ketlikda kiritilsa, shu ketma-ketlik saqlanib qoladi.


# QIYMATNI O'ZGARTIRISH

# Biror kalit so'zga tegishli qiymatni o'zgartirish esa quyidgachia amalga oshiriladi:
talaba_1["ism"] = "murod nazarov"
print(f"Talaba {talaba_1["ism"].title()} {talaba_1["kurs"]}-kurs")


# KALIT SO'Z-QIYMAT JUFTLIGINI O'CHIRISH

# Lu'gatdagi biror juftlik kerak emas bo'lsa uni
# del operatori yordamida lug'atdan olib tashlashimiz mumkin:

talaba_0 = {
    "ism": "murod olimov",
    "yosh": 20,
    "t_yil": 2000
}
print(talaba_0)
del talaba_0["yosh"]
print(talaba_0)


# LUG'ATNI QATORLARGA BO'LIB YOZISH

telefonlar = {
    "ali": "iphone 12",
    "vali": "galaxy S21",
    "olim": "redmi 14",
    "orif": "iphone x"
}


# get() METODI

# Biz shu vaqtgacha lug'atdagi qiymatlarni ko'rish uchun to'g'ridan-to'g'ri
# kalit so'z orqali murojat qilayotgan edik. Bu usulning kamchiligi shundaki,
# agar lug'atda siz so'ragan kalit topilmasa, dastur KeyError xatoligi bilan to'xtab qoladi.

print(f"Alinig telefoni: {telefonlar["ali"].title()}")
# print(f"Hasannnig telefoni {telefonlar["hasan"].title()}")  -  KeyError: 'hasan'

print(f"Hasanning telefoni: {telefonlar.get("hasan", "Bunday ism lug'atda yo'q")}")
print(f"Hasanning telefoni: {telefonlar.get("orif", "Bunday ism lug'atda yo'q").title()}")

phone = telefonlar.get("husan", "Bunday ism lug'atda yo'q")
print(phone)
phone = telefonlar.get("vali", "Bunday ism lug'atda yo'q")
print(phone.title())

# Agar .get() metodida ikkinchi argumentni tashlab ketsangiz, va kalit mavjud bo'lmasa
# .get() metodi None degan qiymatni qaytaradi. None - qiymat mavjud emas degan ma'noni beradi.

phone = telefonlar.get("vali")
print(phone)

if phone == None:
    print("Lug'atda bunday ism yo'q")
else:
    print(f"Telefon modeli {phone.title()}")

