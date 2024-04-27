"""
Sana: 25.04.2024
Dars: 3-dars / Nazariya
Mavzu: PRINT(), SINTEKS VA ARIFMETIK AMALLAR
       print() funktsiyasi, Python sintaksi va arifmetik amallar
"""

# PRINT()

# print() bu Pythondagi mahsus funktsiya bo'lib, () ichida berilgan matn yoki
# ifodalarni ekranga (konsolga) chiqarish vazifasini bajaradi.

"""
print() funksiyasining to'liq ko'rinishi:
print(object1, object2, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

object — obyekt который необходимо вывести;
sep — разделитель между объектами. В качестве своего значения можно передавать строку или None (по умолчанию пробел " ");
end — символ в конце строки (по умолчанию перенос строки \n);
file — file-like объект [поток] (по умолчанию sys.stdout);
flush — принудительный сброс потока [работает с версии Python 3.3] (по умолчанию False).
"""

print("Bir", "ikki", "uch", "to\'rt")
print("Bir", "ikki", "uch", "to\'rt", sep=None)
print("Bir", "ikki", "uch", "to\'rt", sep=" ")
print("Bir", "ikki", "uch", "to\'rt", sep="")
print("Bir", "ikki", "uch", "to\'rt", sep="/")
print("Bir", "ikki", "uch", "to\'rt", sep=" orasi ")
print("Bir", "ikki", "uch", "to\'rt", sep="\n")

print("Bir")
print("ikki")
print("uch")

print("Bir", end="")
print("ikki", end=" ")
print("uch", end="!")

print("Men \"Dell\" markasidagi noutbuk sotib oldim")
print("""\nBir, ikki, uch, to'rt
Akfa oynalari zo'r
Chidamli va mustahkam
Hozir bunaqasi kam""")

print("\nBir, ikki, uch, to'rt \nAkfa oynalari zo'r \nChidamli va mustahkam \nHozir bunaqasi kam")

print('\nBir, ikki, uch, to\'rt \
\nAkfa oynalari zo\'r \
\nChidamli va mustahkam \
\nHozir bunaqasi kam')


# ARIFMETIK AMALLAR

"""
- Python arifmetik amallarni bajarishda Matematika qoidalariga amal qiladi:
- Qavs ichidagi amallar qavs ortidagilardan avval bajariladi
- Darajaga oshirish (ildiz chiqarish) ko'paytirish va bo'lishdan avval bajariladi
- Ko'paytirish va bo'lish, qo'shish va ayirishdan avval bajariladi
- Boshqa holatlarda ifodalar chapdan o'ngga qarab bajariladi

Pythonda oddiy arifmetik amallar quyidagi jadvalda berilgan.

Operator          Tavsif                                      Misol 
   +              Qo'shish                                    5+6=11
   -              Ayirish                                     5-6=-1
   *              Ko'paytirish                                5*6=30
   /              Bo'lish                                     5/6=0.833333
   //             Bo'lish va butun qismini olish              5//6=0
   **             Exponenta (daraja/ildiz)                    5**6=15625
   %              Bo'linmaning qoldig'ini olish               15%6=3
"""

print(2+3+5, 2+3-1, sep=", ")
print(5+10*2, 5+10/2, sep=", ")
print(5+10//2)
print(10%2, 10%3, 10%4, sep=", ")
print(5**2, 5**3, 5**4, sep=", ")


print("To'qqizning kvadrati", 9**2, "ga teng!")
print("9 x 2 =", 9*2,)










