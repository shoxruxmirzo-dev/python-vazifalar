"""
Sana: 26.04.2024
Dars: 10-dars / Nazariya
Mavzu: IF-ELSE
       Dasturni tarmoqlashni o'rganamiz
"""

# TARMOQLANISH

# Aksar dasturlar ma'lum bir shart bajarilishi (yoki bajarilmaganiga) ko'ra kodning
# bir qismidan boshqa qismiga "sakrab" o'tishi tabiiy hol. Dasturlashda bu tarmoqlanish deb ataladi.

# Ushbu darsimizda biz if operatori yordamida shunday shartlarni yozishni, tekshirishni va
# tekshiruv natijasiga ko'ra kodning turli qismlarini bajarishni o'rganamiz.


# if OPERATORI

# if so'zi ingliz tilidan "agar" deb tarjima qilinadi va deyarli
# barcha dasturlash tillarida shartlarni yozish uchun foydalaniladi.

avtolar = ["audi", "bmw", "volvo", "kia", "hyundai"]
for avto in avtolar:
    if avto == "bmw":
        print(avto.upper())
    else:
        print(avto.capitalize())


# TRUE/FALSE

"""Yuqorida shartni tekshirish uchun == operatoridan foydalandik. Bu operatorni oddiy tilga 
tarjima qilsak "tengmi?" degan ma'noni beradi. Agar shartning ikki tarafidagi qiymatlar 
teng bo'lsa ifoda TRUE qiymatini qaytaradi ("True" so'zi ingliz tilidan "haqiqiy" yoki 
"to'g'ri" deb tarjima qilinadi). Aksincha, qiymatlar tenglik qanoatlantirilmasa, ifoda 
FALSE qiymatini qaytaradi ("False" so'zini ingliz tilidan "yolg'on" deb tarjima qilsak bo'ladi).    

Pyhondagi Standart False qiymatlar:
- bool(False), (a = False)
- int(0), (a = 0)
- float(0.0), (a = 0.0)
- str(""), (a = "")
- list([]), (a = [])

"""
ism = "Ali"
print(ism == "Ali")
print(ism == "Vali")

# Demak, if/else bog'lamasida, if ning badani ifoda True bo'lganda,
# else ning badani esa ifoda False bo'lganda bajariladi.


# MATNLARNI SOLISHTIRISH

ism = "Ali"
print(ism.lower() == "ali")


# QIYMATLARNING TENG EMASLIGINI TEKSHIRISH

# Agar ikki qiymatning teng emasligini tekshirish talab qilinsa, != operatoridan foydalanilamiz.
ism = input("Ismingiz nima?\n>>>")
if ism.lower() != "ali":
    print(f"Uzr {ism.capitalize()} biz Alini kutyapmiz.")
else:
    print(f"Hush kelibsiz {ism.capitalize()}")

# Shartlarda else qismi bo'lishi majburiy emas. Bunga keyingi bo'limlarda tushunarliroq misollar ko'ramiz.


# SONLARNI SOLISHTIRISH

"""
Sonlarni solishtirishda yuqoridagi teng (==) va teng emas (!=) shartlariga
qo'shimcha ravishda quyidagi mantiqiy shartlar ham qo'shiladi:
- Kichik: a<b
- Kichik yoki teng: a<=b
- Katta: a>b
- Katta yoki teng: a>=b
"""

javob = int(input("12 x 6 nehiga teng?\n>>>"))
if javob != 72:
    print(f"Noto'g'ri, javob {javob} emas!")
else:
    print(f"Ofarin siz to'g'ri topdingiz, javob {javob} edi")


yosh = int(input("Yoshingiz nechida?\n>>>"))
if yosh >= 18:
    print("Hush kelibsiz")
else:
    print(f"18 yoshga kirmaganlar uchun kirish mumkin emas")


login = input("Yangi login tanlang:>>> ")
if len(login) <= 5:
    print(f"Login 5 harfdan ko'proq bo'lishi shart")
else:
    print("Login qabul qilindi")


# Sonlarni solishtirishda arifmetik ifodalar ham yozishimiz mumkin:
yil = int(input("Tug'ilgan yilingizni kiriting:>>> "))
if 2024-yil < 18:
    print(f"Yoshingiz {2024-yil} da ekan")
    print("Kirish mumkin emas!")
else:
    print("Xush kelibsiz!")


# BIR QATOR if/else

# Qisqa kodlar uchun shart va uning badanini 1 qatorga jamlab yozishimiz ham mumkin:
yosh = input("Yoshingiz nechida?>>> ")
print(f"Siz {yosh}-yoshda ekansiz") if yosh else print("Yoshingizni kiriting")


# match - case operatori
print("1 - Komediya")
print("2 - Fantastika")
print("3 - Ujas")
genre = int(input("Qaysi janrga qiziqasz?>>> "))
match genre:
    case 1:
        print("Uyda yolg'iz")
    case 2:
        print("Avatar")
    case 3:
        print("Astral")
    case _:
        print("Yuqoridagi janrlardan birini tanlang")