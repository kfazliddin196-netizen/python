# Foydalanuvchidan boshlang'ich yo'nalish va buyruqni so'raymiz
Y = input("Robotning boshlang'ich yo'nalishini kiriting (v-shimol, q-sharq, j-janub, g-g'arb): ")
K = int(input("Buyruqni kiriting (0-harakatni davom ettir, 1-chapga buril, 2-o'ngga buril): "))

# Robotning hozirgi yo'nalishi va buyruqqa qarab yangi yo'nalishini topamiz
if Y == 'v':  # Shimol
    if K == 0:
        yangi_Y = 'v'  # Davom ettir
    elif K == 1:
        yangi_Y = 'g'  # Chapga buril
    elif K == 2:
        yangi_Y = 'q'  # O'ngga buril
elif Y == 'q':  # Sharq
    if K == 0:
        yangi_Y = 'q'  # Davom ettir
    elif K == 1:
        yangi_Y = 'v'  # Chapga buril
    elif K == 2:
        yangi_Y = 'j'  # O'ngga buril
elif Y == 'j':  # Janub
    if K == 0:
        yangi_Y = 'j'  # Davom ettir
    elif K == 1:
        yangi_Y = 'q'  # Chapga buril
    elif K == 2:
        yangi_Y = 'g'  # O'ngga buril
elif Y == 'g':  # G'arb
    if K == 0:
        yangi_Y = 'g'  # Davom ettir
    elif K == 1:
        yangi_Y = 'j'  # Chapga buril
    elif K == 2:
        yangi_Y = 'v'  # O'ngga buril

print("Robotning yangi yo'nalishi:", yangi_Y)