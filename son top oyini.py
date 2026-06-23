import random

f = random.randint(1, 10)

for urinish in range(3):
    try:
        a = int(input("1 dan 10 gacha son kiriting: "))
    except ValueError:
        print("Faqat son kiriting!")
        continue

    if a == f:
        print("Tabriklayman, topdingiz!")
        break
    elif a < f:
        print("Siz kiritgan son kichikroq, kattaroq son kiriting!")
    elif a > f:
        print("Siz kiritgan son kattaroq, kichikroq son kiriting!")

    print(f"Qolgan urinishlar: {2 - urinish}")

else:  # for tsikli break siz tugasa
    print(f"O'yin tugadi! To'g'ri son: {f}")