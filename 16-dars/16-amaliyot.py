"""
Sana: 28.04.2024
Dars: 16-dars / Amaliyot
Mavzu: NESTING
       Lug'at ichida ro'yxat, ro'yxat ichida lug'at?
"""

# 1. Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxslar
# haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga
# joylang va har bir shaxs haqidagi ma'lumotni konsolga chiqaring

shaxs_1 = {
    "ism": "bill",
    "familiya": "gates",
    "t_yil": 1955,
    "dasturlar": ["windows xp", "windows 7", "windows 8", "windows 10", "windows 11"],
    "kapital": 128.0
}
shaxs_2 = {
    "ism": "sergey",
    "familiya": "brin",
    "t_yil": 1973,
    "dasturlar": ["google.com", "youtube.com", "google play", "android"],
    "kapital": 136.6
}
shaxs_3 = {
    "ism": "larry",
    "familiya": "page",
    "t_yil": 1973,
    "dasturlar": ["google.com", "youtube.com", "google play", "android"],
    "kapital": 142.5
}
shaxs_4 = {
    "ism": "mark",
    "familiya": "zuckerberg",
    "t_yil": 1984,
    "dasturlar": ["facebook.com", "instagram.com", "whatsApp"],
    "kapital": 155.7
}
shaxs_5 = {
    "ism": "pavel",
    "familiya": "durov",
    "t_yil": 1984,
    "dasturlar": ["vkontakte.com", "telegram.org"],
    "kapital": 15.5
}

liderlar = [shaxs_1, shaxs_2, shaxs_3, shaxs_4, shaxs_5]
for lider in liderlar:
    print(f"{lider['ism'].title()} {lider['familiya'].title()} {lider['t_yil']}-yilda tug'ilgan. "
          f"Hozirda uning kapitali {lider['kapital']} mlrd $.")


# 2. Yuqoridagi lug'atlarga har bir shaxsning yaratgan mashxur ishlari ro'yxatini ham qo'shing.
# for tsikli yordamida muallifning ismi va uning ishlarini konsolga chiqaring

for lider in liderlar:
    print(f"\n{lider['ism'].title()} {lider['familiya'].title()} yaratgan mashxur platformalar:")
    for dastur in lider['dasturlar']:
          print(dastur)


# 3. Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-serial haqida so'rang.
# Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'atga saqlang.
# Natijani konsolga chiqaring

