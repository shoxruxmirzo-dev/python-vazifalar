"""
Sana: 25.04.2024
Dars: 4-dars / Amaliyot
Mavzu: O'ZGARUVCHILAR
       Pythonda o'zgaruvchilar bilan ishlashni o'rganamiz
"""

# Quyidagi mashqlarni bajaring:

# 1. "Hello World!" matnini yangi o'zgaruvchiga yuklang va print() yordamida konsolga chiqaring
hello = "Hello World!"
h_world = "Hello World!"
print(hello)
print(h_world)

print(id(hello))
print(id(h_world))

# 2. xabar deb nomlangan o'zgaruvchiga biror matn yuklang va konsolga chiqaring,
# keyin esa o'zgaruvchiga yangi qiymat berib uni ham konsolga chiqaring.
xabar = "\nAssalomu aleykum Shoxruxmirzo!"
print(xabar)

xabar = "Va aleykum assalom. Nima gaplar?"
print(xabar)

# 3. class den nomlangan o'zgaruvchi yarating, unga biror qiymat bering
# va konsolga chiqaring (siz kutgan natija chiqdimi?)
# class = "Assalom"
# print(class) # SyntaxError: invalid syntax

# 4. Quyidagi kodni bajaring:

radius = 5
pi = 3.14159
doira_yuzi = pi*radius**2
print("Radiusi", radius, "ga teng bo'lgan doiraning yuzi", doira_yuzi, "ga teng")