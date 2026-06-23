# Foydalanuvchidan yoshni kiritishni so'rash
yosh = int(input("Yoshingizni kiriting (20-69): "))

# Yoshnni so'z bilan ifodalash
if 20 <= yosh <= 69:
    if yosh < 30:
        onlik = "yigirma"
    elif yosh < 40:
        onlik = "o'ttiz"
    elif yosh < 50:
        onlik = "qirq"
    elif yosh < 60:
        onlik = "ellik"
    else:
        onlik = "oltmish"

    b = yosh % 10
    birlik1 = ["", "bir", "ikki", "uch", "to'rt", "besh", "olti", "yetti", "sakkiz", "to'qqiz"][b]

    print(onlik,birlik1)
else:
    print("Kiritilgan yosh 20-69 oralig'ida emas!")
