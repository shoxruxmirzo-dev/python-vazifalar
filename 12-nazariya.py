"""
Sana: 27.04.2024
Dars: 12-dars / Nazariya
Mavzu: 12 XATOLAR BILAN ISHLASH
       Dasturchi xato qiladi. Yaxshi dasturchi esa ko'p xato qiladi.
"""

# SyntaxError - SINTEKS XATOLIK

# Biz syntax error bilan 3-darsimizda tanishgan edik. Bu eng ko'p uchraydigan xato bo'lib,
# odatda dasturlash tili qoidalariga amal qilmaslik natijasida kelib chiqadi.

""" print "Hello World!"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello World!")?"""

# EOL va EOF xatolik
# EOL (End of Line - qator yakuni) xatoligi sintaks xatolikning bir turi bo'lib,
# odatda qator oxirida qo'shtirnoq (birtirnoq) ni yopish esdan chiqqanda yuzaga keladi.

""" print("Hello World!
SyntaxError: EOL while scanning string literal"""

# EOF (End of function - funktsiya yakuni) xatoligi esa
# funktsiya oxirida qavsni yopish esdan chiqqanda yuzaga keladi.

"""  print("Hello World!"
SyntaxError: unexpected EOF while parsing"""


# IndentationError - JOY TASHLASHDA XATOLIK
# Python tilida qator boshidan yoki joy tashlab yozish muhim ahamiyatga ega.
# Qator boshidan asossiz joy qoldirish IndentationError ga olib keladi.

""" _print("Hello World!")
IndentationError: unexpected indent

print("O'ngacha sanaymiz")
for n in range(10):
print(n+1)
IndentationError: expected an indented block """
# Qoida sifatida kamida 4 ta harflik joy yoki 1 ta TAB (klaviaturadagi tab tugmasi)
# joy tashlashni odat qilishimiz kerak. Va eng muhimi ikkalasini aralashtirmasligimiz lozim.


# RUN TIME ERROR - DASTURNI BAJARISHDA XATOLIK
# Run time error — dastur bajarish jarayonida kelib chiqadi va dasturning ishlashini to'xtatadi.

# TypeError
# Biror amalni (funktsiya, metod) noto'g'ri ma'lumot turi ustida bajarish.

""" son = input("Istalgan son kiriting: ")
print(f"{son} ning kvadrati {son**2} ga teng")
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int' """

# NameError
# O'zgaruvchi, funktsiya, obyekt nomini noto'g'ri yozish natijasida kelib chiquvchi xatolik.

""" prit("Hello World!")
NameError: name 'prit' is not defined

mevalar = ['olma','uzum','nok','anor','anjir']
for meva in mvealar:
    print(meva)
NameError: name 'mvealar' is not defined """


# ValueError
# Funktsiyaga noto'g'ri qiymatni yuborish natijasidagi xatolik

""" son = int(input("Istalgan son kiriting: "))
if son>=0:
    print("Musbat son")
else:
    print("Manfiy son")
ValueError: invalid literal for int() with base 10: '46.5' """


# IndexError
# Yangi dasturchilar yo'l qo'yadigan yana bir xato bu indeks xatolik.
# Ya'ni ro'yxat elementlariga murojat qilishda indeksni noto'g'ri kiritish.

"""mevalar = ['olma','anor','uzum']
print(mevalar[3])
IndexError: list index out of range """


# ZeroDivisionError
# Dastur jarayonida 0 ga bo'lish yuzaga kelgandagi xatolik

"""x, y = 50, 50
z = 250/(x-y)
ZeroDivisionError: division by zero """


# MANTIQIY XATOLAR
# Mantiqiy xatolar - dasturchi tomonidan yo'l qo'yilgan va kutilgan natijani berishda to'sqinlik
# qiluvchi xatolar. Bunday xatolar eng ko'p uchraydigan va aniqlash eng qiyin bo'lgan xatolar hisoblanadi.
# Aksar holatlarda Python mantiqiy xatolarni aniqlamaydi va dastur bajarilaveradi (lekin kutilgan natija chiqmaydi).

"""radius = 5
pi = 4.14
aylana_yuzi = pi*radius**2
print(aylana_yuzi)
Natija: 103.499999999     (pi=4.14 emas, 3.14 bo'lishi kerak edi) """

# Yana bir misol ko'raylik:
""" son = float(input("Istalgan son kiriting: "))
ildiz = son**1/2
print(f"{son} ning ildizi {ildiz} ga teng")
Natija: 9.0 ning ildizi 4.5 ga teng    (ildiz = son**(1/2) to'g'ri yozilishi)"""

