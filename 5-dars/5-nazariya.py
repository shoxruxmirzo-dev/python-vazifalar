"""
Sana: 25.04.2024
Dars: 5-dars / Nazariya
Mavzu: STRING (MATN)
       STRING ma'lumot turi va uning ustida amallar
"""

# STRING VA UNICODE

"""
STRING (matn) —Pythondagi eng mashxur ma'lumot turlaridan biri. Avvalgi darsda ko'rganimizdek, 
o'zgaruvchiga matn yuklash uchun matn qo'shtirnoq (" ") yoki birtirnoq (' ') ichida yozilishi kerak.

Pythonda matnlar Unicode (https://symbl.cc/en/unicode-table/) jadvalidagi istalgan belgilaridan iborat bo'lishi mumkin 
(jumladan o'zbek, arab, hind, xitoy alifbosidagi harflar yoki turli emoji-smayliklar). 
"""

joy =""
print(joy)
print(type(joy))  # <class 'str'>

shahar = "Qo'qon"
viloyat = "Farg'ona"
print(shahar, "shahri", viloyat, "viloyati!")

matn = "Men yangi 📱 oldim"
print(matn)


# STRING USTIDA AMALLAR

# Matnlarni qo'shish operatori (+)
ism1 = "Mark"
familiya1 = "Zuckerberg"
info1 = "\nMen " + ism1 + " " + familiya1 + "ning do'stiman"
print(info1)

# Matnlarni ko'paytirish operatori (*)
meva = "Olma"
info = (meva + " ") * 10
print(info)

# f-string
# Ikki (va undan ko'p) matn ko'rinishidagi o'zgaruvchilarni birlashtirish
# uchun f-string usulidan  f"{matn1} {matn2}" ham foydalansak bo'ladi:
ism2 = "Anvar"
familiya2 = "Narzullayev"
info2 = f"{ism2} {familiya2} mening ustozim"
print(info2)

# Mahsus belgilar
# Matnga bo'shliq qo'shish uchun \t belgisidan,
# yangi qatordan boshlash uchun \n belgisidan foydalanamiz
salom1 = "Hello World!"
salom2 = "Hello \tWorld!"
salom3 = "Hello \nWorld!"
print(salom1)
print(salom2)
print(salom3)

# Matndan belgini olish
matn = "Assalom!"
print(matn, matn[2], matn[0:4], matn[-1])


# STRING METODLARI
"""
Pythonda string ustida amalga oshirish mumkin bo'lgan tayyor amallar to'plami mavjud. 
Bunday amallar to'plami metodlar deb ataladi. 
Metodlarni qo'llash uchun metod nomi matndan so'ng .metod_nomi() ko'rinishida yoziladi.
"""

# upper() va lower() metodlari
# upper() metodi matndagi har bir harfni katta harfga o'zgartiradi.
ism2 = "Anvar"
familiya2 = "Narzullayev"
info2 = f"\n{ism2} {familiya2} mening ustozim"
print(info2.upper())

# lower() metodi esa aksincha, har bir harfni kichik harfga o'zgartiradi.
info2 = f"{ism2} {familiya2} mening ustozim"
print(info2.lower())


# title() va capitalize() metodlari
# title() metodi matndagi har bir so'zning birinchi harfini katta harf bilan yozadi.
info2 = f"{ism2} {familiya2} mening ustozim"
print(info2.title())

# capitalize() esa faqatgina eng birinchi so'zning birinchi harfini katta bilan yozadi.
info2 = f"{ism2} {familiya2} mening ustozim"
print(info2.capitalize())

# Metodlarni faqat o'zgaruvchilarga emas, balki to'g'ridan-to'g'ri matnga ham qo'llash mumkin
# (aslida o'zgaruvchi ham matnning (yoki boshqa ma'lumotning) manzili xolos)
info2 = f"{ism2} {familiya2} mening ustozim".upper()
print(info2)

# swapcase() metodi matndagi har bir kichik harfni kattaga va kattasini esa kichik harfga o'zgartiradi
info2 = f"{ism2} {familiya2} mening ustozim"
print(info2.swapcase())


# strip(), rstrip() va lstrip() metodlari
# Bu metodlar matnning boshi va oxiridagi bo'sh joylarni olib tashlaydi.
# lstrip() — matn boshidagi bo'shliqni,
# rstrip() – matn oxiridagi bo'shliqni,
# strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi
meva = "\tolma\t"
print(f"\nMen {meva} yaxshi ko'raman!")
print(f"Men {meva.lstrip()} yaxshi ko'raman!")
print(f"Men {meva.rstrip()} yaxshi ko'raman!")
print(f"Men {meva.strip()} yaxshi ko'raman!")

# Matnlar bilan ishlaydigan metodlar ko'p. Ularning ba'zilari bilan kelajakda
# yana tanishamiz, to'liq ro'yhatni esa quyidagi sahifa (https://www.w3schools.com/python/python_ref_string.asp) da ko'rishingiz mumkin.

"""Metodlar o'zgaruvchi ichidagi asl matnni o'zgartirmaydi!"""

# INPUT —FOYDALANUVCHI BILAN MULOQOT
"""
Shu paytgacha biz o'zgaruvchilarning qiymatini dasturning ichida berayotgan edik. 
Endi qiymatni o'zimiz emas, balki dastur foydalanuvchilariga kiritish imkonini beramiz. 
Buning uchun input() funktsyasidan foydalanamiz. 
"""

ism = input("\nIsmingizni kiriting:\n>>> ").capitalize()
familiya = input(f"{ism} familiyangiz nima?\n>>> ").capitalize()
info = f"Assalomu Aleykum {ism} {familiya}. Safimizga hush kelibsiz!"
print(info)

