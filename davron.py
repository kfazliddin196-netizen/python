from tkinter import *

# Oyna yaratish
oyna = Tk()
oyna.geometry('800x600')

# Dastlabki o'zgaruvchilar
ball = 0
joriy_savol = 0

# Savollar va javoblar ro'yxati
savollar_javoblar = [
    ("O'zbekiston poytaxti qayer?", ["Dushanbe", "Nuyork", "Pekin", "Toshkent", "Astana"], 3),
    ("Dunyodagi eng baland tog' qaysi?", ["Kilimanjaro", "Everest", "Elbrus", "K2", "Denali"], 1),
    ("Yerning sun'iy yo'ldoshi nima?", ["Oy", "Quyosh", "Mars", "Venus", "Saturn"], 0),
    ("5 + 7 = ?", ["10", "12", "11", "13", "15"], 1),
    ("Inson tanasidagi eng katta organ nima?", ["Jigar", "Terisi", "Miya", "Yurak", "O'pka"], 1),
]

# Ballni yangilash
def yangilash_ball():
    ball_label.config(text=f"Ball: {ball}")

# Savolni yangilash funksiyasi
def savolni_ozgartirish():
    global joriy_savol
    if joriy_savol >= len(savollar_javoblar):
        savol_yozuv.config(text=f"O'yin tugadi! Yig'ilgan ball: {ball}")
        for tugma in tugmalar:
            tugma.config(state=DISABLED)
        return

    savol, javoblar, togri_index = savollar_javoblar[joriy_savol]
    savol_yozuv.config(text=savol)

    for i, tugma in enumerate(tugmalar):
        tugma.config(text=javoblar[i], command=(togri_javob if i == togri_index else noto_gri_javob))

    joriy_savol += 1

# To'g'ri va noto'g'ri javoblar
def togri_javob():
    global ball
    ball += 1
    yangilash_ball()
    savolni_ozgartirish()

def noto_gri_javob():
    global ball
    ball -= 1
    yangilash_ball()
    savolni_ozgartirish()

# UI elementlari
savol_yozuv = Label(oyna, text="", font=("Arial", 16), wraplength=700, bg="pink", height=4)
savol_yozuv.place(x=50, y=20)

tugmalar = [
    Button(oyna, width=40, height=2, font=("Arial", 12), bg="lightblue") for _ in range(5)
]

# Tugmalar joylashuvi
tugmalar[0].place(x=100, y=150)
tugmalar[1].place(x=100, y=200)
tugmalar[2].place(x=100, y=250)
tugmalar[3].place(x=100, y=300)
tugmalar[4].place(x=100, y=350)

# Ballni ko'rsatish uchun label
ball_label = Label(oyna, text=f"Ball: {ball}", font=("Arial", 14), fg="blue")
ball_label.place(x=50, y=450)

# Dastlabki savolni ko'rsatish
savolni_ozgartirish()

oyna.mainloop()
