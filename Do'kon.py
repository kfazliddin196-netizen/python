print("Onlayn magazin")
t = 0
while True:
    a = input("Oziq ovqat/Suv/Kiyimlar\n")
    if a == 'Kiyimlar':
        b1 = input("Kurtka/Shapka/Paypoq/Etik/gamaj\n")
        if b1 == 'Kurtka':
            p = 150000
            print(p, "ming so'm\n12 oyga 12,500 ming so'm")
        elif b1 == "Shapka":
            p = 35000
            print(p, "ming so'm\n12 oyga 2,916 ming so'm")
        elif b1 == 'Paypoq':
            p = 5000
            print(p, "ming so'm\n6 oyga 833 ting")
        elif b1 == 'Etik':
            p = 80000
            print(p, "ming so'm\n12 oyga 6,666 ming so'm")
        elif b1 == 'gamaj':
            p = 100000
            print(p, "ming so'm\n12 oyga 8,333 ming so'm")
        else:
            print("Menda bu maxsulot yo'q")
            continue
        t += p
    elif a == "Suv":
        b = input("Pepsi/Fanta/Kola,Acu\n")
        if b == 'Pepsi':
            p = 15000
            print(p, "So'm\n12 oyga 1,250 ming so'm")
        elif b == 'Fanta':
            p = 15000
            print(p, "So'm\n12 oyga 1,250 ming so'm")
        elif b == 'Kola':
            p = 16000
            print(p, "So'm\n12 oyga 1,333 ming so'm")
        elif b == 'Acu':
            p = 10000
            print(p, "So'm\n6 oyga 1,666 ming so'm")
        else:
            print('Magazinda bu maxsulot qolmagan')
            continue
        t += p
    elif a == 'Oziq ovqat':
        d = input('Kalbasa/Sir/Sasiska\n')
        if d == 'Kalbasa':
            p = 21000
            print(p, "So'm\n12 oyga 1,750 ming so'm")
        elif d == 'Sir':
            p = 15000
            print(p, "So'm\n12 oyga 1,250 ming so'm")
        elif d == "Sasiska":
            p = 50000
            print("kilosi", p, "so'm\n12 oyga 4,166 ming so'm")
        else:
            print('Magazinda bu maxsulot qolmagan')
            continue
        t += p
    print("Jami to'lov:", t)
