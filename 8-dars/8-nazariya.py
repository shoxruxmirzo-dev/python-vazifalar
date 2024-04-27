"""
Sana: 26.04.2024
Dars: 8-dars / Nazariya
Mavzu: RO'YXATLAR BILAN ISHLASH
       Ro'yxatlarning ustida turli amallar bajarishni o'rganamiz
"""

# RO'YXATNI TARTIBLASH

# Aksar holatlarda ro'yxat ichidagi elementlarni alifbo ketma-ketligida tartiblash talab
# qilinishi mumkin. Buning uchun maxsus .sort() metodidan foydalanamiz.
cars = []
cars.append("Malibu")
cars.append("Nexia")
cars.append("Lacetti")
cars.append("Onix")
cars.append("Tracker")
cars.append("Equinox")
cars.append("Traverse")
cars.append("Cobalt")
cars.append("Tahoe")
cars.append("Captiva")
cars.append("Trailblazer")
print(cars)

cars = ['Malibu', 'Nexia', 'Lacetti', 'Onix', 'Tracker', 'Equinox', 'Traverse', 'Cobalt', 'Tahoe', 'Captiva', 'Trailblazer']
cars.sort()
print(cars)

# Diqqat! Tartiblashda katta harflar kichik harflardan avval kelishini hisobga oling. Agar matndagi so'zlarning
# bosh harfi katta-kichik aralash yozilgan bo'lsa, ularni bir ko'rinishga keltirib olish maqsadga muvofiq bo'ladi.
cars = ['Malibu', 'Nexia', 'Lacetti', 'Onix', 'Tracker', 'Equinox', 'Traverse', 'cobalt', 'Tahoe', 'captiva', 'Trailblazer']
cars.sort()
print(cars)

# Ro'yxatni teskari tartibda saqlash uchun .sort() metodi ichida reverse=True argumentini ham kiritamiz.
cars = ['Malibu', 'Nexia', 'Lacetti', 'Onix', 'Tracker', 'Equinox', 'Traverse', 'Cobalt', 'Tahoe', 'Captiva', 'Trailblazer']
cars.sort(reverse=True)
print(cars)

# Asl ro'yxat ichidagi elementlarning ketma-ketligini buzmagan holda ro'yxatni
# tartiblash talab qilinsa sorted() funktsiyasidan foydalanamiz:
mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
print(f"\nsorted() qaytargan ro'yxat: {sorted(mehmonlar)}")
print(f"Asl ro'yxat o'zgarmas qoldi: {mehmonlar}")

# sorted() funktsiyasi yordamida teskari tartiblash uchun ham reverse=True argumentini beramiz:
print(sorted(mehmonlar, reverse=True))

# Yuoqridagi ikki usul bilan sonli ro'yxatlarni ham tartiblashimiz mumkin:
sonlar = [100,5,26,75,-50,55,-7,15,0]
sonlar.sort()
print(sonlar)
print(sorted(sonlar), end="\n\n")


# RO'YXATNI AYLANTIRISH

# Ba'zida ro'yxatni aylantirish (boshini oxiriga, oxirini boshiga) talab
# qilinishi mumkin. Buning uchun .reverse() metodidan foydalanamiz.
mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
sonlar = [100,5,26,75,-50,55,-7,15,0]
mehmonlar.reverse()
sonlar.reverse()
print(mehmonlar)
print(sonlar)


# RO'YXATNING UZUNLIGINI BILISH

# Ro'yxatning uzunligi, ya'ni uning ichidagi elementlar sonini
# aniqlash uchun len() funktsiyasidan foydalanamiz:
fruits = ['pear','banana','apple','watermelon','lemon']
print(f"\nfruits ro'yxatida ja'mi {len(fruits)} ta element bor.")


# range() FUNKTSIYASI

# Bu funktsiya yordamida biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin.
# list() funktsiyasi yordamida esa bu oraliqni ro'yxat shaklida saqlab olamiz:
sonlar = list(range(10))
print(sonlar)

juft_sonlar = list(range(2,20,2))
toq_sonlar = list(range(1,20,2))
print(f"\n1-20 gacha ja'mi {len(juft_sonlar)} ta juft son bor va ular: {juft_sonlar}")
print(f"1-20 gacha {len(toq_sonlar)} ta toq son bor, ular: {toq_sonlar}")


# SONLI RO'YXAT USTIDA SODDA AMALLAR

"""
Pythonda ro'yxatlar ustida ba'zi sodda amallarni ham bajarish mumkin. Misol uchun ro'yxatdagi 
eng kichik sonni topish uchun min() funktsiyasidan, eng katta sonni topish uchun esa max()
funktsiyasidan, sonlarning yig'indisini topish uchun esa sum() funktsyasidan foydalansak bo'ladi:
"""

narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
arzon = min(narhlar)
qimmat = max(narhlar)
jami = sum(narhlar)

print(f"Eng arzon narh: {arzon}. Eng qimmati: {qimmat}. Ja'mi: {jami} so'm ekan!", end="\n\n")


# RO'YXATNI KESISH

# Ro'yxatning ma'lum bir bo'lagini ajratib olish uchun biz boshlang'ich va oxirgi indekslarni beramiz:
cars = ['Malibu', 'Nexia', 'Lacetti', 'Onix', 'Tracker', 'Equinox', 'Cobalt', 'Captiva', 'Trailblazer']
my_cars = cars[1:4]
my_cars2 = cars[4:7]
print(my_cars)
print(my_cars2)

# Agar boshlang'ich indeksni bermasangiz, Python avtomat ravishda 0 indeksdan boshlab kesadi.
# Agar 2-indeksni kiritmasangiz, ro'yxat oxirigacha kesadi:
print(cars[:3])
print(cars[4:])


# RO'YXATDAN NUSXA OLISH

# sonlar2 = sonlar deb yozsak yangi ro'yxat yaratish o'rniga, ikkala o'zgaruvchini ham
# bitta ro'yxatga bog'lab (yo'naltirib) qo'yamiz. Biz sonlar yoki sonlar2 ustida bajargan
# amallarimiz aslida bitta ro'yxat ustida bajariladi.

# Shuning uchun yuoqirdagi ka'bi ro'yxatni kesish usulidan foydalanamiz.
# Faqatgina, kvadrat qavs ichida ikkala indeksni ham ko'rsatmasdan, bo'sh qoldiramiz:

sonlar = [1,2,3,4,5,6,7,8,9]
sonlar2 = sonlar[:]
sonlar2.append(20)
sonlar2.append(30)
print(f"\nsonlar ro'yxati: {sonlar}")
print(f"sonlar2 ro'yxati: {sonlar2}")


# TUPLES - O'ZGARMAS RO'YXAT

# Pythonda o'zgarmas ro'yxatlar tuples deb yuritiladi. Tuple ichidagi qiymatlarni bir marta,
# dastur boshida beriladi va so'ngra o'zgartirib bo'lmaydi. List dan farqli ravishda,
# Tuple e'lon qilishda kvadrat qavslar [] o'rniga oddiy qavslar () ishlatiladi:
toq_sonlar = tuple(range(1,20,2))
print(toq_sonlar)

# Tuple ichidagi elementlarga huddi ro'yxat elementlariga murojat qilingani kabi murojat qilinaveradi:
toys = ('bus','car','bear','dino','snake','lizard')
print(toys[0])
print(toys[-1])
print(toys[1:4])

# Agar Tuple ga o'zgartirish talab qilinsa, yagona yo'li o'zgarmas ro'yxatni list() funktsiyasi
# yordamida List (oddiy ro'yxat) ko'rinishiga keltirib olish, o'zgarishlarni bajarsih va
# qaytarib tuple() funktsiyasi yordamida o'zgarmas ro'yxatga o'tkazish mumkin:
toys = ('bus','car','bear','dino','snake','lizard')
toys = list(toys)
toys.append("dragon")
toys.remove("bus")
toys[1] = "mcqueen"
toys = tuple(toys)
print(toys)

