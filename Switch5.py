a=int(input())
b=int(input())
k=int(input('1-Qoshish 2-bolish 3-ayrish 4-Kopaytrish'))
Switch={
    1:a+b,
    2:a*b,
    3:a//b,
    4:a-b,
}
print(Switch.get(k))