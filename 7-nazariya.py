"""
Sana: 25.04.2024
Dars: 7-dars / Nazariya
Mavzu: LIST (RO'YXAT)
       List yordamida bir o'zgaruvchida ko'p qiymatlar saqlashni o'rganamiz.
"""

# LIST BILAN TANISHAMIZ

"""
Bugun o'rganadigan navbatdagi mal'umot turi List (ro'yxat) deb ataladi. Ro'yxat o'z nomi bilan, 
bitta o'zgaruvchida bir nechta qiymatlarni saqlash imkonini beradi. Bu qiymatlar List elementlari deyiladi. 
Ro'yxatda son, matn yoki aralash turdagi elementlarni saqlash mumkin.

Ro'yxat saqlaydigan o'zgaruvchilarni nomlashda -lar  (ko'plik) 
qo'shimchasini qo'shish maqsadga muvofiq bo'ladi (inlgiz tilida -s). 

Misol uchun: mevalar, uylar, cars, toys, books 
"""

nomsiz = []  # bo'sh ro'yxat
mevalar = ["olma", "anjir", "shaftoli", "o'rik"]  # matnlar ro'yxati
b_sonlar = [100, 500, 1000, 5000, 50, 10]  # butun sonlar ro'yxati
o_sonlar = [10.5, 500.25, 1000.80, 5000.0, 50.66, 10.478]  # o'nlik sonlar ro'yxati
aralash = ["olma", "anor", 100, 500, 10.55, 3.14]  # aralash ma'lumot turlari
r_royxat = [[1,5,10], ["olma", "anor", "anjir"], [3.14, 2.25, 50.655], [5, "besh", 5.0]] # ro'yxatli ro'yxat


# LIST ELEMENTLARI

# Ro'yxatdagi har bir element tartib bilan joylashgani sababli, biz istalgan elementga
# uning tartib raqami (indeksi) bo'yicha murojat qilishimiz mumkin.

# Dasturlash olamida indeks 0 dan boshlanadi! Ya'ni Listning birinchi elementing
# tartib raqami (indeksi) 0 ga, ikkinchi elementning indeksi 1 ga teng va hokazo.
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
print(f"Birinchi meva: {mevalar[0]}")
print(f"Ikkinchi meva: {mevalar[1]}")
print(f"Ohirgi meva: {mevalar[-1]}")

# Agar list ichidagi elementlar matn ko'rinishid bo'lsa, ularga string metodlarni qo'llashimiz mumkin:
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
print(f"Birinchi meva: {mevalar[0].upper()}")

# List elementlari ustida arifmetik amallar bajarish:
narhlar = [12000, 18000, 10900, 22000]
print(f"{narhlar[1]} + {narhlar[-1]} = {narhlar[1]+narhlar[-1]}")
print(f"{narhlar[1]} - {narhlar[0]} = {narhlar[1]-narhlar[0]}")
print(f"{narhlar[0]} x 10 = {narhlar[0]*10}")
print(f"{narhlar[2]} / 100 = {narhlar[2]//100}")

# Pythonda Listning eng oxirgi elementiga -1 indeksi orqali ham murojat qilish mumkin.
# Bu usul Listning uzunligini bilmaganda juda asqotadi.
car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
print(car_models[-1])


# ELEMENTLARNI QO'SHISH, O'CHIRISH VA O'ZGARTIRISH

# Elementni o'zgartirish
# Ro'yxatdagi biror elementning qiymatini o'zgartirish uchun, o'sha elementga
# indeksi bo'yicha murojat qilamiz va yangi qiymat yuklaymiz
narhlar = [12000, 18000, 10900, 22000]
narhlar[0] = 12
narhlar[-1] = 22
narhlar[1] = narhlar[1] + 1000
print(narhlar)

# Yangi element qo'shish
# Ro'yxatga yangi element qo'shishning oson usuli bu .append()
# metodi yordamida ro'yxatning oxiriga qiymat qo'shish:
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.append("banan")
mevalar.append("kivi")
print(mevalar)

cars = []
cars.append("Onix")
cars.append("Tracker")
cars.append("Equinox")
cars.append("Malibu")
print(cars)

# o'yxatning istalgan joyiga yangi element qo'shish uchun .insert() metodidan
# foydalanamiz. .insert() metodi ichida yangi elementning indeksi va qiymati beriladi:
cars = ['Onix', 'Tracker', 'Equinox', 'Malibu']
cars.insert(0, "Spark")
cars.insert(2, "Lacetti")
print(cars)

# Elementni o'chirish
# Ro'yxatdan biror elementni olib tashlash uchun uning indeksini yoki qiymatini bilishimiz lozim.
# Indeks yordamida olib tashlash uchun del operatoridan foydalanamiz:
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
del mevalar[0]
del mevalar[-1]
print(mevalar)

# Element qiymati bo'yichi o'chirish uchun esa .remove(qiymat) metodidan foydalanamiz.
# Buning uchun qavs ichida o'chirib tashlash kerak bo'lgan qiymatni yozamiz
cars = ['Spark', 'Onix', 'Lacetti', 'Tracker', 'Equinox', 'Malibu']
cars.remove("Lacetti")
cars.remove("Spark")
print(cars)
# .remove(qiymat) metodi ro'yxatda uchragan birinchi mos keluvchi qiymatni o'chiradi. Agar ro'yxatning
# ichida 2 va undan ko'p bir hil qiymatli elementlar bo'lsa, ulardan eng birinchisi o'chadi.

hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
hayvonlar.remove("mushuk")
print(hayvonlar)

# Elementni sug'urib olish
# Ba'zida biror elementni butunlay o'chirib tashlash emas, balki uni ro'yxatdan sug'urib olish va
# undan foydalanish talab qilinishi mumkin. Buning uchun Pythonda .pop(indeks) metodidan foydalanmiz.
bozorlik = ["yog'", "un", "piyoz", "banan", "go'sht"]
mahsulot = bozorlik.pop(1)
print(f"Men bozordan {mahsulot} sotib oldim")
print(f"Olinmagam mahsulotlar: {bozorlik}")

# Agar .pop() metodida indeks berilmasa, ro'yxatdan o'xirgi qiymat sug'urib olinadi.
cars = ["Spark", "Onix", "Lacetti", "Tracker", "Equinox", "Malibu"]
car = cars.pop()
print(f"Avtosalonga 10 ta yangi {car} keldi")

