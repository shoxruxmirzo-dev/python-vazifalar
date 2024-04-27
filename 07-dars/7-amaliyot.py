"""
Sana: 25.04.2024
Dars: 7-dars / Nazariya
Mavzu: LIST (RO'YXAT)
       List yordamida bir o'zgaruvchida ko'p qiymatlar saqlashni o'rganamiz.
"""

# Quyidagi mashqlarni bajaring:

# 1. ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
ismlar = ["Saidkamol", "Saidjon", "Ayubxon", "Sardor", "Rahmatillo"]

# 2. Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
print(f"Salom {ismlar[0]}, qachon to'planadigan bo'lyapmiz?")
print(f"{ismlar[1]} sen ham borasanmi piknikka?")
print(f"Men kecha {ismlar[2]} bilan gaplashgandim, u ham borarkan")
print(f"{ismlar[3]} ham borsa yaxshi bo'ladi, uni moshinasi borda")
print(f"{ismlar[-1]} Rossiyaga ketvoriptiyu")

# 3. sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
sonlar = [10, -45, 3.14, 50, -20.5]

# 4. Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring.
# Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
sonlar = [10, -45, 3.14, 50, -20.5]
print(f"{sonlar[0]} + {sonlar[2]} = {sonlar[0] + sonlar[2]}")
print(f"{sonlar[0]} x ({sonlar[1]}) = {sonlar[0] * sonlar[1]}")
sonlar[-1] = sonlar[-1] + 25.5
sonlar[1] = 200
print(sonlar)

# 5. t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan
# tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
t_shaxslar = ["Bill Gates", "Steve Jobs", "Jeff Bezos"]
z_shaxslar = ["Mark Zuckerberg", "Sergey Brin", "Larry Page"]

# 6. Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni
# sug'urib olib .pop(), quyidagi ko'rinishda chiqaring:
t_shaxs = t_shaxslar.pop(0)
z_shaxs = z_shaxslar.pop(0)
print(f"Men tarixiy shaxslardan {t_shaxs} bilan, zamonaviy shaxslardan esa "
      f"\n{z_shaxs} bilan ko'rishib suhbat qilishni istar edim")

# 7. friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida
# 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends = []
friends.append("Saidakamol")
friends.append("Saidjon")
friends.append("Ayubxon")
friends.append("Sardor")
friends.append("Rahmatillo")
print(friends)

# 8. Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chirib tashlang.
friends = ['Saidakamol', 'Saidjon', 'Ayubxon', 'Sardor', 'Rahmatillo']
friends.remove("Saidjon")
friends.remove("Rahmatillo")
print(friends)

# 9. Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends = ['Saidakamol', 'Ayubxon', 'Sardor']
friends.append("Abdurashid")
friends.insert(0, "Abror")
friends.insert(2, "Ahmadillo")
print(friends, end="\n\n")

# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida
# mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
friends = ['Abror', 'Saidakamol', 'Ahmadillo', 'Ayubxon', 'Sardor', 'Abdurashid']
print(f"Kelishi kuyilayotgan mehmonlar: {friends}")
mehmonlar = []
mehmonlar.append(friends.pop(4))
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(1))
print(f"Kelmaganlar: {friends}")
print(f"Kelganlari: {mehmonlar}")


