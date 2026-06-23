while True:
 import random

 a = input("Qaychi, Qog'oz, Bo'chka: ")

 m = ['Qaychi', 'Qog\'oz', 'Bo\'chka']
 n = random.choice(m)
 if a == n:
    print("Durrang! Beraberdik.")
 elif a == ('Qaychi' and n == 'Bo\'chka') or (a == 'Qog\'oz' and n == 'Qaychi') or (a == 'Bo\'chka' and n == 'qog\'oz'):
    print(f"Siz {a} ni tanladingiz, kompyuter {n} ni tanladi. Siz yutqazdingiz.")
 else:
    print(f"Siz {a} ni tanladingiz, kompyuter {n} ni tanladi. Siz yutdingiz!")
