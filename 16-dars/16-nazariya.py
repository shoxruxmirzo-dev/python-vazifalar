"""
Sana: 28.04.2024
Dars: 16-dars / Nazariya
Mavzu: NESTING
       Lug'at ichida ro'yxat, ro'yxat ichida lug'at?
"""

# NESTING
# Ba'zida dasturlash jarayonida lug'atning ichida ro'yxatlar yoki boshqa lug'atni, yoki aksincha
# ro'yxat ichida lug'atni saqlash ham qo'l kelishi mumkin. Bu ingliz tilida Nesting deyilad


# LUG'ATLAR RO'YXATI

car_0 = {
    "marka": "chevrolet",
    "model": "malibu",
    "rang": "qora",
    "yil": 2020,
    "km": 5000,
    "korobka": "avtomat",
    "narh": 30000
}

car_1 = {
    "marka": "kia",
    "model": "sorento",
    "rang": "oq",
    "yil": 2022,
    "km": 10000,
    "korobka": "avtomat",
    "narh": 35000
}

car_2 = {
    "marka": "hyundai",
    "model": "sonata",
    "rang": "kulrang",
    "yil": 2021,
    "km": 15000,
    "korobka": "avtomat",
    "narh": 28000
}

# Agar biz har bir lug'atga alohida murojat qiladigan bo'lsak,
# lug'atlarning nomlarini yodlab qolishimiz talab qilinar edi:

car = car_0
print(f"{car['marka'].title()} {car['model'].title()} rangi {car['rang']}. "
      f"{car['yil']}-yil {car['km']} km yurgan, narhi {car['narh']} $")

car = car_1
print(f"{car['marka'].title()} {car['model'].title()} rangi {car['rang']}. "
      f"{car['yil']}-yil {car['km']} km yurgan, narhi {car['narh']} $")

car = car_2
print(f"{car['marka'].title()} {car['model'].title()} rangi {car['rang']}. "
      f"{car['yil']}-yil {car['km']} km yurgan, narhi {car['narh']} $")
print("")

# Keling, barcha avtolarni bitta ro'yxatga joylaymiz,
# va for tsikli yordamida birma-bir konsolga chiqaramiz:

cars = [car_0, car_1, car_2]
for car in cars:
    print(f"{car['marka'].title()} {car['model'].title()} rangi {car['rang']}. "
          f"{car['yil']}-yil {car['km']} km yurgan, narhi {car['narh']} $")
print("")

# E'tibor bering, ishimiz bir muncha yengillashdi, kodimiz ham qisqardi. Natija esa bir hil.
# Endi biz ro'yxat ichidagi istalgan lug'atga indeks bo'yicha murojat
# qilaveramiz (lug'at nomini yodlab qolish shart emas).

print(cars[0])
print("")

# Biror lug'atdagi elementga murojat qilish uchun esa quyidagi usuldan foydalanishimiz mumkin:

print(cars[0]['marka'].title())
print(f"{cars[1]['rang'].title()} {cars[1]['marka'].title()} {cars[1]['model'].title()}")
print("")


# for tsikli yordamida biz bo'sh lug'atlar ro'yxatini ham yaratib olishimiz mumkin:

malibus = []
for n in range(10):
    new_car = {
        "marka": "chevrolet",
        "model": "malibu",
        "rang": " ",
        "yil": 2024,
        "km": 0,
        "korobka": "avtomat",
        "narh": 0
    }
    malibus.append(new_car)

# Ishlab chiqarish jarayonida mashinalarga turli ranglarni berishimiz mumkin.
# Misol uchun birinchi 3 ta mashinaga qizil rang beramiz:

for malibu in malibus[:3]:
    malibu['rang'] = "oq"

# Keyingi 3 tasiga esa qora:

for malibu in malibus[3:6]:
    malibu['rang'] = "qora"

# Oxirgi 4 ta avtoni qora, lekin korobkasini mexanika qilamiz:

for malibu in malibus[6:]:
    malibu['rang'] = "kulrang"
    malibu['korobka'] = "mexanika"

# Keling endi, mashinalarning korobkasidan chiqqan holda narh belgilaymiz:

for malibu in malibus:
    if malibu['korobka'] == "avtomat":
        malibu['narh'] = 35000
    else:
        malibu['narh'] = 30000

print(malibus)
print("")

for malibu in malibus:
    print(f"{malibu['rang'].title()} {malibu['marka'].title()} {malibu['model'].title()} "
          f"korobkasi {malibu['korobka']}. {malibu['yil']}-yil "
          f"{malibu['km']} km yurgan narhi {malibu['narh']} $")


# LUG'AT ICHIDA RO'YXAT

# Bir kalitga bir nechta qiymatlar berish talab qilinganda,
# qiymatlarni ro'yxat ko'rinishida yozish o'rinlidir.

dasturchilar = {
    'ali': ['python', 'c++'],
    'vali': ['html', 'css', 'js'],
    'hasan': ['php', 'sql'],
    'husan': ['kotlin', 'ruby'],
    'maryam': ['c++', 'c#']
}

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end=" ")
    for til in tillar:
        print(til.upper(), end=", ")

print("")


# LUG'AT ICHIDA LUG'AT

# Bunday qilish tavsiya etilmasada, istisno holatlarda lug'at
# ichidagi qiymatlarni lug'at ko'rinishida ham saqlash mumkin

hamkasblar = {
    'ali': {
        'familiya': 'valiyev',
        't_yil': 1995,
        'malumot': 'oliy',
        'tillar': ['python', 'c++']
    },
    'vali': {
        'familiya': 'aliyev',
        't_yil': 2001,
        'malumot': 'o\'rta-maxsus',
        'tillar': ['html', 'css', 'js']

    },
    'hasan': {
        'familiya': 'husanov',
        't_yil': 1999,
        'malumot': 'maxsus',
        'tillar': ['java', 'php']

    }
}

# Hamkasblar to'g'risidagi ma'lumotlarni esa quyidagicha ko'rish mumkin:

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['t_yil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          f"Quyidagi dasturlash tillarini biladi:", end=" ")
    for til in info['tillar']:
        print(til.upper(), end=", ")
