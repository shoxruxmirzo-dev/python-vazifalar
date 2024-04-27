"""
Sana: 26.04.2024
Dars: 9-dars / Amaliyot
Mavzu: FOR TAKRORLASH OPERATORI
       FOR operatori bilan ishlashni o'rganamiz
"""

# 1. Kamida 5 ta elementdan iborat ismlar degan ro'yxat tuzing
# va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar = ["Mark Zuckkerberg", "Bill Gates", "Steve Jobs", "Elon Musk", "Larry Page"]
for ism in ismlar:
    print(f"Men {ism} bilan uchrashmoqchiman")


# 2. Yuqoridagi tsikl tugaganidan so'ng, ekranda "kod n marta takrorlandi" degan
# xabar chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
ismlar = ["Mark Zuckkerberg", "Bill Gates", "Steve Jobs", "Elon Musk", "Larry Page"]
for ism in ismlar:
    print(f"Men {ism} bilan uchrashmoqchiman")
print(f"Kod {len(ismlar)} marta takrorlandi")


# 3. 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing.
# Ro'yxatdagi har bir element kubini yangi qatordan konsolga chiqaring
toq_sonlar = list(range(11, 100, 2))
for i in toq_sonlar:
    print(f"{i} ning kubi {i**3}")


# 4. Foydalanuvchidan 5 ta eng sevimli kinolarini kiritishni so'rang va
# kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
kinolar = []
print("5 ta eng sevimli kinolaringiz nomini kiriting: ")
for i in range(5):
    kinolar.append(input(f"{i+1}-sevimli kinoyingiz: "))
print(kinolar)

# 5. Foydalanuvchidan bugun nechta odam bilan uchrashganini so'rang va har bir suhbatlashgan
# odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring
son = int(input("Bugun nechta odam bilan ko'rishdingiz? "))
odamlar = []
for i in range(son):
    odamlar.append(input(f"{i+1} ko'rishgan odamingiz ismini kiriting: "))

print(odamlar)