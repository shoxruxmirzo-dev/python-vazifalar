"""
Sana: 27.04.2024
Dars: 11-dars / Nazariya
Mavzu: BIR NECHTA SHARTLARNI TEKSHIRISH
       if-elif-else zanjiri, "and", "or", "not" operatorlari bilan tanishamiz
"""

# if-elif-else KETMA-KETLIGI

# Dastur davomida bir nechta shartni tekshirish talab qilinishi mumkin.
# Bunday holatda biz if-elif-else ketma-ketligidan foydalanamiz

# Diqqat! if-elif-else ketma-ketlikda biror shart bajarilishi bilan, Python qolgan shartlarni tekshirmaydi.

"""
Keling bir misol ko'ramiz. Hayvonot bo'giga kirish quyidagicha belgilangan:
- 4 yoshdan kichik bo'lganlarga kirish bepul
- 4 yoshdan 12 yoshgacha kirish 5000 so'm
- 12 yoshdan kattalarga 10000 so'm
Foydalanuvchidan yoshini so'rab, hayvonot bog'iga kirish chiptasi narhini chiqaruvchi dastur yozamiz.
"""
yosh = 32  # int(input("Yoshingiz nechida? "))
if yosh <= 4:
    print("Sizga kirish bepul")
elif yosh <= 12:
    print("Sizga kirish 5000 so'm")
else:
    print("Sizga kirish 10000 so'm")


# Kod yozishda yaxshi amaliyotlardan biri, kodlarni qisqa yozish va buyruqlarni
# qayta-qayta takrorlamaslik. Bu kelajakda kodni o'zgartirishda ham juda qo'l keladi.
yosh = 10  # int(input("Yoshingiz nechida? "))
if yosh <= 4:
    narh = 0
elif yosh <= 12:
    narh = 5000
elif yosh < 65:
    narh = 10000
else:
    narh = 8000
print(f"Sizga kirish {narh} so'm")


# if-elif-else zanjirida ham else qismi majburiy emas:
yosh = 2  # int(input("Yoshingiz nechida? "))
if yosh <= 4:
    narh = 0
elif yosh <= 12:
    narh = 5000
elif yosh < 65:
    narh = 10000
elif yosh >= 65:
    narh = 8000
print(f"Sizga kirish {narh} so'm")


# AND, OR, NOT OPERATORLARI

# OR OPERATORI
# OR ingliz tilidan "yoki" deb tarjima qilinadi, va ikki va undan ko'p
# shartlardan biri bajarilishini tekshirishda ishlatiladi

kun = "yakshanba"  # input("Bugun nima kun?>>> ")
if kun.lower() == "shanba" or kun.lower() == "yakshanba":
    print("Bugun dam olish kuni.")
else:
    print("Bugun ish kuni")

# AND OPERATORI
# AND ingliz tilidan "va" deb tarjima qilinadi, va ikki va undan ko'p
# shartlarning barchasi bajarilishini tekshirishda ishlatiladi

kun = "shanba"  # input("Bugun nima kun? ")
harorat = 28  # float(input("Havo harorati qanday? "))
if kun.lower() == "yakshanba" and harorat >= 30:
    print("Cho'milgani ketdik!")
elif kun.lower() == "yakshanba" and harorat < 30:
    print("Uyda dam olamiz!")


# BIR NECHTA SHARTLARNI KETMA-KET YOZISH
kun = "juma"  # input("Bugun nima kun? ")
harorat = 32  # float(input("Havo harorati qanday? "))
if (kun.lower() == "shanba" or kun.lower() == "yakshanba") and harorat > 30:
    print("Cho'milgani ketdik1")
elif (kun.lower() == "shanba" or kun.lower() == "yakshanba") and harorat < 30:
    print("Uyda dam olamiz!")
elif (kun.lower() != "shanba" or kun.lower() != "yakshanba") and harorat > 0:
    print("Bugun dam olish kuni emas, hech qayerga borolmaymiz")


# BOOLEAN MA'LUMOTLAR TURI

# Avvalgi darsimizda biz turli ifodalarni solishtirishda TRUE yoki FALSE qiymatlari qaytishini ko'rdik.
# Bu qiymatlar boolean (mantiqiy) qiymatlar deb ataladi, va dasturlashda juda keng qo'llaniladi.
# Pythonda o'zgaruvchilarda boolean qiymatlarni ham saqlash mumkin.

narh = 15000
choy = True
salat = False
if choy and salat:
    narh = narh + 10000
elif choy or salat:
    narh = narh + 5000
print(f"Ja'mi {narh} so'm")

# E'tibor bering, choy va salat boolean (mantiqiy) qiymatlar bo'gani uchun,
# 5 va 7-qatorlarda biz choy==True yoki salat==True deb yozib o'tirishimiz shart emas

# Boolean o'zgaruvchilarni saqlashda TRUE va FALSE qiymatlari o'rniga 1 va 0 sonlarini ham ishlatish mumkin.


# SHARTLARNI KETMA-KET TEKSHIRISH

narh = 15000
choy = True
salat = False
non = True
kompot = True
assorti = False
if choy:
    narh = narh + 3000
    print("\nMijoz choy oldi")
if salat:
    narh = narh + 5000
    print("Mijoz salat oldi")
if non:
    narh = narh + 2000
    print("Mijoz non oldi")
if kompot:
    narh = narh + 5000
    print("Mijoz kompot oldi")
if assorti:
    narh = narh + 15000
    print("Mijoz assorti oldi")
print(f"Ja'mi {narh} so'm")


# RO'YXAT TARKIBINI TEKSHIRISH

# in operatori yordamida biz ro'yxatning tarkibida ma'lum bir element borligini tekshirishimiz mumkin.
menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
print('manti' in menu)
print("osh" in menu)

menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
ovqat = "osh"  # input("Nima ovqat buyurasiz? ")
if ovqat.lower() in menu:
    print("Buyurtma qabul qilindi")
else:
    print(f"Afsuski bizda {ovqat} yo'q")


# not in OPERATORI
# not in operatori yordamida esa biror element ro'yxatda yo'qligini tekshirishimiz mumkin.
menu = ['osh','qazonkabob','shashlik','norin','somsa']
print("manti" not in menu)
print("osh" not in menu)


menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
ovqat = "osh"  # input("Nima ovqat buyurasiz? ")
if ovqat.lower() not in menu:
    print(f"Afsuski bizda {ovqat} yo'q")
else:
    print("Buyurtma qabul qilindi", end="\n\n")

# not operatorini boshqa shartlarning oldidan ham qo'yishimiz mumkin.
# Misol uchun: if not a==5 ifodasi if a!=5 ifodasi bilan bir hil natija qaytaradi.


# IKKI RO'YXATNI SOLISHTIRISH

buyurtmalar = ["osh","somsa","manti", "shashlik"]
menu = ['osh','qozonkabob','shashlik','norin','somsa']

for taom in buyurtmalar:
    if taom in menu:
        print(f"Menyuda {taom} bor")
    else:
        print(f"Kechirasz, menyuda {taom} yo'q")


# RO'YXAT BO'SH EMASLIGINI TEKSHIRISH

menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = []

if buyurtmalar:  # buyurtmalar: buyurtmalar == [] sharti bilan bir xil
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menyuda {taom} bor")
        else:
            print(f"Kechirasz, menyuda {taom} yo'q")
else:
    print("Buyurtma bermadingiz")


