a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
k = int(input("1-Qo‘shish, 2-Ayirish, 3-Bo‘lish, 4-Ko‘paytirish: "))

s = {
    1: a + b,
    2: a - b,
    3: a / b if b != 0 else "Nolga bo‘lish mumkin emas!",
    4: a * b,
}

natija = s.get(k)
if k not in [1, 2, 3, 4]:
    print("Noto‘g‘ri amal!")
elif k == 3 and b == 0:
    print(natija)
else:
    print(f"Natija: {natija}")