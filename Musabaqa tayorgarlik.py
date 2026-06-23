#Celciy va Farengeyt (Harorat va haroratni olchash tizimi )
#C=float(input('C'))
#f=(C*9/5)+32
#print(f'Farengey:{f}F')
#..........................................................
#Soni ildizi
#import math
#N=int(input())
#ildiz=math.sqrt(N)
#print(f'{N} ning ildizi {ildiz}')
#.............................................................
#soni Faxtorian (kopaytmasini)
#N=int(input())
#faktoial=1
#for i in range(1,N+1):
#    faktoial*=i
#print(f'{N} ning fakorial: {faktoial}')
#.........................................................
#eng katta sonni aniqlash
#a=int(input())
#b=int(input())
#d=int(input())
#if a==d==b:
#    print('teng')
#elif a >= b >= d:
#    print(f'{a} Katta')
#elif a <= b >= d:
#    print(f'{b} Katta')
#elif a <= d >= b:
#    print(f'{d} Katta')
#
#.........................................................
#y=0
#for i in range(0,101):
#    if i%2==0:
#        y+=i
#print(f'yeg\'indi{y}')
#.........................................
# savol 5 va 15 javob: chiqadi 6, 8, 10, 12, 14
#a=int(input())
#b=int(input())
#for i in range(a,b):
# if i%2==0:
#  print(i)
#...............................................
#n = int(input("Sonni kiriting: "))
#yigindi = 0
#
## 1 dan n gacha bo'lgan sonlar ichida n ga bo‘linadiganlarni yig‘amiz
#for i in range(1, n + 1):
#    if n % i == 0:  # Agar i n ga bo‘linadigan bo‘lsa
#        yigindi += i  # i ni yig‘indiga qo‘shamiz
#
#print(f"{n} ning bo‘linuvchilari yig‘indisi: {yigindi}")
#.............................................................
#Palindrom
#n = input("Sonni kiriting: ")
#
#if n == n[::-1]:  # Teskari tartibda tekshirish
#    print(f"{n} palindrom son")
#else:
#    print(f"{n} palindrom son emas")
#.....................................................................
#5 va 3 bolinadigan
#a=int(input())
#if a%3==0:
#    print('son 3 ga bolinadi')
#elif a%5==0:
#    print('son 5 ga bolinadi')
#elif a%3==0 or a%3==0:
#    print('5 va 3 ga bolinadi')
#else:
#    print('5 va 3 ga bolinmidi')
#......................................................................
#a=int(input())
#print('2,3,4,5')
#f=int(input())
#swich={
#    2:a**2,
#    3:a**3,
#    4:a**4,
#    5:a**5
#}
#print(swich.get(f))
#.........................................................

# Foydalanuvchidan son olish
#son = input("Sonni kiriting: ")
#
## Raqamlarni yig'indisi va sonini hisoblash
#raqamlar_yigindi = 0
#raqamlar_soni = 0
#
#for raqam in son:
#    raqamlar_yigindi += int(raqam)  # Raqamni yig'indiga qo'shish
#    raqamlar_soni += 1  # Raqamlar sonini hisoblash
#
## O'rtacha qiymatni hisoblash
#if raqamlar_soni > 0:
#    ortacha_qiymat = raqamlar_yigindi / raqamlar_soni
#    print("Raqamlar o'rtacha qiymati:", ortacha_qiymat)
#else:
#    print("Raqamlar yo'q.")
#.........................................................
#raqamlar orasidan Juft va toq aniqlash
#a=input()
#toq_raqamlar=''
#juft_raqamlar=''
#for raqam in a:
#    if int(raqam)% 2 !=0:
#        toq_raqamlar+=raqam
#for r in a:
#    if int(r)%2==0:
#        juft_raqamlar+=r
#print(f'{juft_raqamlar}, {toq_raqamlar}')
#....................................................
#raqamlar ichida eng katta va eng kichik sinlarn ayirmasi
#a=input()
#katta_son=int(a[0])
#kichik_son=int(a[0])
#for raqam in a:
#    raqam=int(raqam)
#    if raqam>katta_son:
#        katta_son=raqam
#    if raqam<kichik_son:
#        kichik_son=raqam
#farq=katta_son-kichik_son
#print(f'{katta_son} Katta son')
#print(f'{kichik_son} Kichik son')
#print(f'{farq} yeg\'indi')
#......................................................................
#
#raqamlar = input("5 ta sonni kiriting (masalan: 35179): ")
#if len(raqamlar) == 5:
#    sonlar = list(map(int, raqamlar))
#    min_yigindi = sum(sonlar) - max(sonlar)
#    max_yigindi = sum(sonlar) - min(sonlar)
#    print(min_yigindi, max_yigindi)
#else:
#    print("Faqat 5 ta raqam kiriting!")
#raqamlar = input("Sonlarni kiriting (masalan: 12345): ")  # Masalan, "12345"
#sonlar = list(map(int, raqamlar))  # Har bir raqamni son qilib ro‘yxatga aylantirish
#print(sonlar)
#..............................................................................................
#bir birga qoshish
#s=int(input())
#a,b,c=map(int,input().split())
#m=a+b+c
#if m>=s:
#  print("Yes")
#else:
#  print("No")
#...............................................
#a=list(map(int,input().split(',')))
#total=0
#for num in a:
#    if num%3==0:
#        total+=num
#print(total)
#................................................
#n = int(input("n ni kiriting: "))
#count = 0
#for num in range(2, n):
#    M = True
#    for i in range(2, int(num ** 0.5) + 1):
#        if num % i == 0:
#            M = False
#            break
#    if M:
#        count += 1
#print(f"{n} dan kichik tub sonlar soni: {count}")
#...........................................................
#juft=0
#toq=0
#a=int(input())
#for i in range(1,a+1):
# if i%2==0:
#     juft+=1
# else:
#     toq+=1
#print(f'{toq},{juft}')
#..........................................................................
#a = int(input("n ni kiriting: "))  # Foydalanuvchidan n sonini olish
#for i in range(1, a + 1):
#    print(f"{i} ning kvadrati: {i * i}")
#..........................................................................
#a = int(input("n ni kiriting: "))
#y=0
#for i in range(1,a+1):
#    if i%2==0:
#       y+=i
#print(f'{y}')
#....................................................................
#a = int(input())
#yegindi = 0
#for i in range(1, a + 1):
# kub=i**3
# yegindi=kub+i+i+i
# print(f'{kub} yegindi ,{yegindi}')
#..............................................................
#a=int(input())
#for i in range(1,a+1):
# if i%2!=0:
#  print(f'{i},{i ** 2}')
#..............................................................
#y=0
#a=int(input())
#for i in range(1,a+1):
# if i%2==0:
#     y+=i
#print(f'{i} javobi: {y}')
#............................................................
#a=int(input())
#y=1
#for i in range(1,a+1):
#   y*=i
#print(f'!{a},{y}')
#..............................................................
#a=int(input())
#y=0
#for i in range(1,a+1):
# if i%2:
#     print(f'{i}')
#     y+=i
#print(f'{y}')
#.........................................................
#a=int(input())
#y=0
#for i in range(1,a+1):
# y+=i**3
# print(f'{i} ning kubi: {i ** 3}, Joriy yig\'indi: {y}')
#......................................................................
