"""
Sana: 26.04.2024
Dars: 9-dars / Nazariya
Mavzu: FOR TAKRORLASH OPERATORI
       FOR operatori bilan ishlashni o'rganamiz
"""

# for BILAN TANISHAMIZ
# "For" so'zi ingliz tilidan ""uchun deb tarjima qilinadi

for harf in "Assalomu Aleykum":
    print(harf, end="-")
matn = "Va aleykum assalom"
print("")
for harf in matn:
    print(harf, end="-")
print("", end="\n\n")

for son in [10, 20, 50, 100, 200, 500]:
    print(f"{son} ni 5 ga bo'lsa {son//5}")
print("")
sonlar = [10, 20, 50, 100, 200, 500]
for son in sonlar:
    print(f"{son} ni 10 ga bo'lsa {son // 10}")
print("")

for ism in ["Ali", "Vali", "Hasan", "Husan", "Olim"]:
    print(f"Hurmatli {ism}, sizni 9 may kuni nahorgi oshga taklif etamiz!")
print("")
ismlar = ["Ali", "Vali", "Hasan", "Husan", "Olim"]
for ism in ismlar:
    print(f"Hurmatli {ism}, keyingi hafta ohiriga aylanishga borasmi?")


# TSIKL YORDAMIDA RO'YXATLAR BILAN ISHLASH

sonlar = list(range(1,11))
for i in sonlar:
    print(f"{i} ning kvadrati {i**2} ga teng")
print("", end="\n")
sonlar = list(range(1, 11))
sonlar_kvadrati = []
for i in sonlar:
    sonlar_kvadrati.append(i**2)
print(sonlar)
print(sonlar_kvadrati)


# for va input()
dostlar = []
print(f"5 ta eng yaqin do'stingiz ismini kiriting: ")
for i in range(5):
    dostlar.append(input(f"{i+1}-do'stingiz ismi nima? ").capitalize())
print(dostlar)

