"""
Sana: 26.04.2024
Dars: 8-dars / Amaliyot
Mavzu: RO'YXATLAR BILAN ISHLASH
       Ro'yxatlarning ustida turli amallar bajarishni o'rganamiz
"""

# 1. O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ["Angliya", "AQSH", "Germaniya", "Turkiya", "Singapur", "Avstraliya"]
print(davlatlar)

# 2. Ro'yxatning uzunligini konsolga chiqaring
print(f"Ro'yxatdagi ja'mi davlatlar soni {len(davlatlar)} ta")

# 3. sorted() funksiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(davlatlar))

# 4. sorted() funksiyasi yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(davlatlar, reverse=True))

# 5. Asl ro'yxatni qaytadan konsolga chiqaring
print(davlatlar)

# 6. reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()
print(davlatlar)

# 7. sort() metodi yordamida ro'yxatni avval alifbo bo'yicha,
# keyin esa alifboga teskari tartibda konsolga chiqaring
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

# 8. 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
juft_sonlar = list(range(120, 1200, 2))
print(juft_sonlar)

# 9. Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print(f"Ro'yxatdagi juft sonlarning yig'indisi {sum(juft_sonlar)} ga teng")

# 10. Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
print(f"\nRo'yxatdagi eng katta son {max(juft_sonlar)} dan "
      f"eng kichik son {min(juft_sonlar)} ni ayirsak {max(juft_sonlar)-min(juft_sonlar)} hosil bo'ladi")

# 11. Ro'yxatdagi elementlar sonini hisoblang
juft_sonlar = list(range(120, 1200, 2))
print(f"120 dan 1200 gacha ja'mi {len(juft_sonlar)} juft son bor ekan")

# 12. Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(f"\nRo'yxatning boshidagi 20 ta son: {juft_sonlar[:20]}")
print(f"Ro'yxatning o'rtasidagi 20 ta son: {juft_sonlar[(len(juft_sonlar)//2)-10:(len(juft_sonlar)//2)+10]}")
print(f"Ro'yxatning oxiridagi 20 ta son: {juft_sonlar[-20:]}")

# 13. taomlar degan ro'yxat yarating va ichiga istalgan 5 ta taomni kiriting
taomlar = ["osh", "lag'mon", "bifshteks", "somsa", "mastava"]

# 14. nonushta degan yangi ro'yxatga taomlar dan nusxa oling
nonushta = taomlar[:]

# 15. Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring va yana 2 ta taom qo'shing
nonushta.remove("lag'mon")
nonushta.remove("bifshteks")
nonushta.append("atala")
nonushta.append("tuxum")

# 16. Ikkala ro'yxat (taomlar va nonushta) ni ham konsolga chiqaring
print(f"\nBarcha taomlar: {taomlar}")
print(f"Faqat nonushtabop taomlar: {nonushta}")

# 17. Yuqoridagi nonushta ro'yxatini tuple o'zgarmas ro'yxatga aylantiring va 1-taomni o'zgartirib ko'ring
nonushta = tuple(nonushta)
print(nonushta)

