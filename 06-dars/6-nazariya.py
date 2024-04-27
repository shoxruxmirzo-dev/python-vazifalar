"""
Sana: 25.04.2024
Dars: 6-dars / Nazariya
Mavzu: SONLAR
       Pythonda sonlar bilan ishlashni o'rganamiz
"""

# INTEGERS — BUTUN SONLAR

# Butun sonlarni ham o'zgaruvchida saqlash, ularning ustida qo'shish (+), ayirish (-),
# ko'paytirish(*), bo'lish (/) kabi arifmetik amalarni bajarish mumkin:
a = 50
b = -30
c = a + b
print(c)

"""Python - operatorlar orasidagi bo'shliqlarni inobatga olmaydi. 
O'qishga qulay bo'lishi uchun yuqoridagi kabi (bo'shliqlar bilan) yozishingiz mumkin."""

# To'g'ri to'rtburchakning yuzini hisoblaymiz (S = a x b)
a = 20
b = 10
s = a * b
print(s)


# FLOATS — O'NLIK SONLAR

# Pythonda o'nlik sonlar floating point numbers yoki qisqa qilib floats deyiladi.

# Aylana uzunligini hisoblaymiz
pi = 3.14159
radius = 10
diametr = 2 * radius
l = 2 * pi * radius
javob = f"Aylana uzunligi {l} ga teng"
print(javob)


# BUTUN SONDAN O'NLIK SONGA

# Avval aytganimizdek ikki butun sonni bo'lish (/) natijasida o'nlik son hosil bo'ladi (natija butun bo'lsa ham)
a = -20
b = 40
c = b / a
print(c, end="\n\n")

# Shuningdek butun va o'nlik sonlar o'rtasidagi har qanday arifmetik amallarning natijasi ham o'nlik son bo'ladi.
a = 2
b = 3.0
print(a+b, a*b, a**b, 2*(a+b), sep="\n")


# UZUN SONLARNI KIRITISH

# Uzun sonlarni kiritishda, qulaylik uchun, raqamlarni pastki chiziq (_) yordamida guruhlash mumkin.
# Python - son tarkibidagi pastki chiziqlarni (_) inobatga olmasdan, uzun sonligicha qabul qiladi.
aholi_soni = 7_594_000_000
info = f"\nYer kurrasida {aholi_soni} ga yaqin odam yashaydi"
print(info)


# KONSTANTA

"""
Aksar dasturlash tillarida konstant qiymatlar tushunchasi bor. Konstantlar o'zgarmas bo'ladi (misol uchun 
𝜋 ning qiymati konstant, o'zgarmas qiymat). Pythonda konstant tushunchasi yo'q, shuning uchun dasturchilar 
bunday o'zgaruvchilarning nomini katta harflar bilan yozadilar (ogohlantirish sifatida). Bu albatta 
qat'iy qonun emas, lekin kelajakda o'zgaruvchilar orasida konstant qiymatlarni ajratish uchun yaxshi usul.
"""

PI = 3.14159
radius = 21.2


# BIR NECHTA O'ZGARUVCHIGA QIYMAT BERISH

# Birdaniga bir nechta o'zgaruvchiga qiymat berish uchun
# o'zgaruvchilar va ularga mos qiymatlar vergul (,) bilan ajratiladi:
x, y, z = 5, 10, 25
print(x, y, z, sep=", ")


# O'ZGARUVCHI TURINI ALMASHTIRISH

# Pythonda bir turdagi o'zgaruvchini boshqa turga o'tkazish mumkin, bu ingliz tilida typecasting detiladi.
# Buning uchun Pythonda mahsus funktsiyalar bor, keling ular bilan tanishamiz:
# str()— int yoki float turidagi sonlarni matnga o'zgartiradi.
# int()— matn yoki float ko'rinishidagi qiymatlarni butun songa o'zgartiradi. Bunda matn butun son ko'rinishida bo'lishi kerak.
# float()— matn yoki int ko'rinishidagi qiymatlarni o'nlik songa o'zgartiradi.

ism = "Anvar"
yosh = 20
xabar = f"{ism} {yosh} yoshda"
print(xabar)
xabar2 = ism + " " + str(yosh) + " yoshda"
print(xabar2)

# str(yosh) kodi yosh degan o'zgaruvchining qiymatini matn ko'rinishida ko'rsatdi xolos.
# Asl o'zgaruvchining qiymati sonligicha qoladi. int() va float()ham huddi shunday ishlaydi.


# O'ZGARUVCHI TURINI TEKSHIRISH

# Kodimizda o'zgaruvchilar ko'payib ketdi. Yuqoridagi kabi xatolar qilmaslik uchun ba'zida
# o'zgaruvchinig turini tekshrish talab qilinadi. Buning uchun type() funktsiyasidan foydalanamiz:
print(type(ism))
print(type(yosh))
print(type(xabar2))


# INPUT() VA SONLAR

# input() funksiyasi yordamida foydalanuvchining tug'ilgan yilini so'rab, uning yoshini hisoblab beramiz
j_yil = 2024
savol = "Tug'ilgan yilingizni kiriting: "
t_yil = input(savol)
yosh = j_yil - int(t_yil)
javob1 = "Siz " + str(yosh) + " yoshda ekansiz!"
print(javob1)
javob2 = f"Siz {yosh} yoshda ekansiz!"
print(javob2)

