d=int(input("kunni kriting"))
m=int(input("oy kriting"))
if m==1:
    if d>19:
        print("qovga")
    else:
        m="echki"
        print(d,m)
elif m==2:
    if d>18:
        print("baliq")
    else:
        m="qovga"
        print(d,m)
elif m==3:
    if d>20:
        print("qoy")
    else:
        m="baliq"
        print(d,m)
elif m==4:
    if d>19:
        print("buzoq")
    else:
        m="qoy"
        print(d,m)
elif m==5:
    if d>20:
        print("egizak")
    else:
        m="buzoq"
        print(d,m)
elif m==6:
    if d>21:
        print("qisqichbaqa")
    else:
        m="egizak"
        print(d,m)
elif m==7:
    if d>22:
        print("arslon")
    else:
        m="qisqichbaqa"
        print(d,m)
elif m==8:
    if d>22:
        print("parizod")
    else:
        m="arslon"
        print(d,m)
elif m==9:
    if d>22:
        print("tarozi")
    else:
        m="parizod"
        print(d,m)
elif m==10:
    if d>22:
        print("chayon")
    else:
        m="tarozi"
        print(d,m)
elif m==11:
    if d>22:
        print("o'qotar")
    else:
        m="chayon"
        print(d,m)
elif m==12:
    if d>21:
        print("qovga")
    else:
        m="oq otar"
        print(d,m)