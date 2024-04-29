"""
Sana: 27.04.2024
Dars: 11-dars / Amaliyot
Mavzu: BIR NECHTA SHARTLARNI TEKSHIRISH
       if-elif-else zanjiri, "and", "or", "not" operatorlari bilan tanishamiz
"""

# Quyidagi dasturlarni alohida fayllarga yozing va bajaring:

# 6. foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi
# login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi
# bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!"
# aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

users = ["admin", "sarvar", "lochin", "sher", "polvon", "alisher"]
login = input("Yangi login tanlang: ")
if login.lower() in users:
    print("Login band, yangi login tanlang!")
else:
    print(f"Hush kelibsiz {login}")

