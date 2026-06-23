print('bankamatga xush kelibsiz')
d = 100000000
while True:
    a = int(input('Karta raqamingizni kiriting\n'))
    if a != 1111222233334444:
        print("Karta raqami xato")
        continue
    print("Tasdiqlandi")
    b = int(input("Paro'lini kiriting\n"))
    if b != 7777:
        print("Parol xato")
        continue
    print("Tasdiqlandi")
    m = input("Kartani pulini tekshirasizmi\n")
    if m == 'Ha':
        print(d)
    elif m == "Yo'q":
        print('Ok')
    else:
        print("Noto'g'ri kirish")
        continue
    d1 = input("Davom etrasizmi, Ha/Yo'q\n")
    if d1 == "Yo'q":
        continue
    elif d1 == "Ha":
        print('Ok')
    else:
        print("Noto'g'ri kirish")
        continue
    f1 = int(input("Kartadan pul yechish\n"))
    if 0 < f1 < 100000000:
        print("Xisobingizdan pul yechildi")
    else:
        print("Noto'g'ri kirish")
        continue
    f = input("Kartada qancha pul qolganligini tekshirasizmi\n")
    if f == 'Ha':
        print("Kartada shuncha pul qoldi", d - f1)
    elif f == "Yo'q":
        continue
    else:
        print("Noto'g'ri kirish")