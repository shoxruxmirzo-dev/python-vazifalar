"""
Sana: 28.04.2024
Dars: 15-dars / Nazariya
Mavzu: LUG'AT ELEMENTLARI BILAN ISHLASH
       Lug'at ichida ro'yxat, lug'at ichida lug'at?
"""

# .items() METODI
# Ushbu metod yordamida lug'at ichidagi barcha kalit-qiymat juftliklarini ko'rishimiz mumkin.

talaba_0 = {
    "ism": "alijon",
    "familiya": "shamshiyev",
    "yosh": 22,
    "fakultet": "informatika",
    "kurs": 4
}
print(talaba_0.items())

# Bu metodni to'g'ridan-to'g'ri emas, for tsikli yordamida chaqirish orqali
# lug'atdagi barcha elementlarni tushunarliroq shaklda ko'rishimiz mumkin.

for kalit, qiymat in talaba_0.items():
    print(f"Kalit {kalit}")
    print(f"Qiymat {qiymat}\n")


telefonlar = {
    "ali": "iphone 12",
    "vali": "galaxy s10",
    "olim": "galaxy a40",
    "orif": "galaxy note 10"
}

for ism, telefon in telefonlar.items():
    print(f"{ism.title()}ning telefoni {telefon.title()}")


# .keys() METODI
# Agar lug'atdagi kalit so'zlarni ko'rish talab qilinsa, .keys() metodidan foydalanishimiz mumkin.

mahsulotlar = {
    "olma": 15000,
    "banan": 25000,
    "anjir": 15000,
    "guruch": 20000,
    "qulupnay": 30000
}
print(mahsulotlar.keys())

print("Do'kondagi mahsulotlar: ")
for x in mahsulotlar.keys():
    print(f"{x.title()}")

# Yuqoridagi kodimizda, for tsiklida .keys() metodini ishlatmasak ham huddi shu natija chiqadi.
print("Do'kondagi mahsulotlar: ")
for x in mahsulotlar:
    print(f"{x.title()}")


# for tsikli va if sharti yordamida lug'atdagi biror qiymatlarni alohida chiqarishimiz ham mumkin:
bozorlik = ["anor", "uzum", "anjir", "baliq", "guruch"]
for mahsulot in mahsulotlar.keys():
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")


for buyum in bozorlik:
    if buyum in mahsulotlar.keys():
        print(f"{buyum.title()}dan 1 kilo paketga solib bering")
    else:
        print(f"Iltimos do'koningizga {buyum} ham olib keling")


# LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH

print("Do'konimizdagi mahsulotlar:")
for x in sorted(mahsulotlar.keys()):
    print(x.title())

for x in sorted(mahsulotlar.keys(), reverse=True):
    print(x.title())


# .values() METODI
# Agar lug'atdagi qiymatlarni chiqarish talab qilinsa .values() metodidan foydalanishimiz mumkin.

telefonlar = {
    "ali": "iphone 12",
    "vali": "galaxy s10",
    "olim": "galaxy a40",
    "orif": "galaxy note 10"
}
print(telefonlar.values())

print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
for phone in telefonlar.values():
    print(phone.title())

# Yuqoridagi usul bilan qiymatlarni chiqrganimizda, lug'atdagi barcha qiymatlar chiqib keladi.
# Agar, biror qiymat ko'p marta qaytarilsa, konsolga ham ko'p marta chiqib keladi.

telefonlar = {
    'ali': 'iphone x',
    'vali': 'galaxy s9',
    'olim': 'mi 10 pro',
    'orif': 'nokia 3310',
    'hamida': 'galaxy s9',
    'maryam': 'huawei p30',
    'tohir': 'iphone x',
    'umar': 'iphone x'
    }

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel.title())

# Yuoqirdagi natijaga e'tibor bersanigz, bir nechta foydalanuvchilar iphone x va galaxy
# s9 telefonidan foydalanishar ekan, va bu modellar qayta-qayta konsolga chiqdi.
# Buning oldini olish uchun set() funktsiyasidan foydalanishimiz mumkin.

print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
for phone in set(telefonlar.values()):
    print(phone.title())

"""
Pythonda set yana bir ma'lumot turi bo'lib, ro'yxat va lug'at kabi bir nechta 
elementlarni saqlashga mo'ljallangan. Lug'at va ro'yxatdan farqli ravishda, 
set ichidagi elementlar biror tartibda saqlanmaydi, va ularga indeks orqali 
murojat qilib bo'lmaydi. Shuningdek, set ichida bir hil elementlar bo'lmaydi.
"""




