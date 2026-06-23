import random

# Tasodifiy son tanlanadi
f = random.randint(1, 10)

# 3 ta imkoniyat uchun tsikl
for urinish in range(3):
    # Foydalanuvchidan son kiritish so‘raladi
    a = int(input("1 dan 10 gacha son kiriting: "))

    # Agar son to‘g‘ri bo‘lsa
    if a == f:
        print("Tabriklayman, topdingiz!")
        break  # O‘yin tugaydi
    elif a<f:
        print("Siz kiritgan son kichikroq, kattaroq son kiriting!")
    elif a>f:
        print("Siz kiritgan son kattaroq, kichikroq son kiriting!")
        # Qolgan urinishlar sonini ko‘rsatish
    print(f"Qolgan urinishlar: {2 - urinish}")

# Agar 3 ta urinish tugasa
if urinish == 2:  # Oxirgi urinish 2 indeksda bo‘ladi (0, 1, 2)
    print("O‘yin tugadi! Tasodifiy son:", f)