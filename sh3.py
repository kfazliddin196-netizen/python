
D = int(input("Kunni kiriting (1-31): "))
M = int(input("Oyni kiriting (1-12): "))


if (M == 1 and D >= 20) or (M == 2 and D <= 18):
    burj = "Qovg'a"
elif (M == 2 and D >= 19) or (M == 3 and D <= 20):
    burj = "Baliq"
elif (M == 3 and D >= 21) or (M == 4 and D <= 19):
    burj = "Qoy"
elif (M == 4 and D >= 20) or (M == 5 and D <= 20):
    burj = "Buzoq"
elif (M == 5 and D >= 21) or (M == 6 and D <= 21):
    burj = "Egizaklar"
elif (M == 6 and D >= 22) or (M == 7 and D <= 22):
    burj = "Qisqichbaqa"
elif (M == 7 and D >= 23) or (M == 8 and D <= 22):
    burj = "Arslon"
elif (M == 8 and D >= 23) or (M == 9 and D <= 22):
    burj = "Parizod"
elif (M == 9 and D >= 23) or (M == 10 and D <= 22):
    burj = "Tarozi"
elif (M == 10 and D >= 23) or (M == 11 and D <= 22):
    burj = "Chayon"
elif (M == 11 and D >= 23) or (M == 12 and D <= 21):
    burj = "O'q otar"
elif (M == 12 and D >= 22) or (M == 1 and D <= 19):
    burj = "Echki"
else:
    burj = "Noma'lum burj"

print("Berilgan sana burji:",burj)
