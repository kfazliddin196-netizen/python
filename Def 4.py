def g():
 while True:
  import random

  # Tanlovlar ro'yxati
  t = ["Qog'oz", "Qaychi", "Bo'chka"]

  # Foydalanuvchi tanlovi
  a = int(input("1 - Qog'oz, 2 - Qaychi, 3 - Bo'chka: ")) - 1

  # Kompyuter tanlovi
  r = random.randint(0, 2)

  print("Sizning tanlovingiz:",t[a])
  print("Kompyuterning tanlovi:" ,t[r])

  # Natijani aniqlash
  if a == r:
      print("Durang!")
  elif (a == 0 and r == 2) or (a == 1 and r == 0) or (a == 2 and r == 1):
      print("Siz yutdingiz!")
  else:
      print("Kompyuter yutdi!")
g()