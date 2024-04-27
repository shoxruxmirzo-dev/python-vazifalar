"""
Sana: 25.04.2024
Dars: 4-dars / Nazariya
Mavzu: O'ZGARUVCHILAR
       Pythonda o'zgaruvchilar bilan ishlashni o'rganamiz
"""

# O'ZGARUVCHI (VARIABLE)

"""
O'zgaruvchi —kompyuter xotirasida ma'lum bir qiymatni saqlash uchun ajratilgan joy. 
Soddaroq qilib tushuntirsak, o'zgaruvchini quti, quti ichidagi narsani esa qiymat deb tasavvur qilish mumkin. 
Pythonda qiymatlar son, matn, ro'yxat va hokazo ko'rinishida bo'lishi mumkin.
"""

# O'ZGARUVCHILARNI NOMLASH
"""
O'zgaruvchilarga nom berishda quyidagi qoidalarga amal qiling:
- O'zgaruvchi nomi harf yoki pastki chiziq (_) bilan boshlanishi kerak
- O'zgaruvchi nomi raqam bilan boshlanishi mumkin emas
- O'zgaruvchi nomida faqatgina lotin alifbosi harflari (A-z), raqamlar (0-9) va pastki chiziq (_) qatnashishi mumkin
- O'zgaruvchi nomida bo'shliq (пробел) bo'lishi mumkin emas
- O'zgaruvchi nomida katta-kichik harflar turlicha talqin qilinadi (ism, ISM, va Ism uchta turli o'zgaruvchi)

Qo'shimcha qoida sifatida:
- O'zgaruvchi nomini kichik harflar bilan yozing. 
- O'zgaruvchi nomida 2 va undan ortiq so'z qatnashsa ularning orasini 
pastki chiziq (_) bilan ajrating (ism_sharif="Anvar Narzullaev")
- O'zgaruvchiga tushunarli nom bering (y=20 emas yosh=20, d="Korea" emas davlat = "Korea" va hokazo)
- Shuningdek o'zgaruvchilarga Pythonda ishlatiladigan funktsiyalar va maxsus kalit so'zlarning (keywords)
 nomini bermang. Kalit so'zlar ro'yhatini ko'rish uchun print(help("keywords")) deb yozing va Enter tugmasini bosing.
  Konsolda Pythondagi maxsus kalit so'zlar ro'yhati chiqadi:

"""

print(help("keywords"))

ism = "Abdulloh"
yosh = 25
print(ism, yosh, "yoshda")

ism = "Muhammdad"
yosh = 30
print(ism, yosh, "yoshda")

