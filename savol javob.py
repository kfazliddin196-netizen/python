from tkinter import *

# Bosh oynani yaratish
a = Tk()
a.geometry('1920x1080')
# Foydalanuvchi ballini saqlash uchun o'zgaruvchi
ball = 0

# Ballni yangilash va ekranda ko'rsatish funksiyasi
def update_score():
    score_label.config(text=f"Ball: {ball}")
# Noto'g'ri javob funksiyasi
def Notogri():
    global ball
    ball -=1
    update_score()
    salute1 = Label(a, text="Notog'ri javob ❌", font=("Arial", 24), fg="red")
    salute1.place(x=600, y=500)
    a.after(2000, lambda: salute1.destroy())  # 2 soniyadan keyin yashiriladi

# To'g'ri javob funksiyasi
def show_salute():
    global ball
    ball += 1  # To'g'ri javob uchun ball qo'shiladi
    update_score()  # Ballni yangilash
    salute = Label(a, text="🎉 Tabriklaymiz! To'g'ri javob! 🎉", font=("Arial", 24), fg="green")
    salute.place(x=600, y=500)
    a.after(2000, lambda: salute.destroy())  # 2 soniyadan keyin yashiriladi

# To'g'ri javob tanlanganida ishlaydi
def r():
    show_salute()  # To'g'ri xabarni ko'rsatish
    change_question()  # Keyingi savolga o'tish

# Noto'g'ri javob tanlanganida ishlaydi
def wrong_answer(button):
    Notogri()  # Noto'g'ri xabarni ko'rsatish
    change_question() # Keyingi savolga o'tish
# Savolni o'zgartirish funksiyasi
def change_question():
    l.config(text="Dunyodagi eng baland tog' qaysi?")
    b.config(text='A) Kilimanjaro', command=lambda: wrong_answer(b))
    b1.config(text='B) Everest', command=r)  # To'g'ri javob
    b2.config(text='C) Elbrus', command=lambda: wrong_answer(b2))
    b3.config(text='D) K2', command=lambda: wrong_answer(b3))
    b4.config(text='E) Denali', command=lambda: wrong_answer(b4))


# Birinchi savol va tugmalar
l = Label(width=150, height=10, font=1000, bg='pink', text="O'zbekiston poytaxti qayer?")
l.place(x=60, y=10)

b = Button(width=150, height=1, bg='lightblue', font=50, text='A) Dushanbe', anchor='w', command=lambda: wrong_answer(b))
b.place(x=55, y=200)

b1 = Button(width=150, height=1, bg='lightblue', font=50, text='B) Nuyork', anchor='w', command=lambda: wrong_answer(b1))
b1.place(x=55, y=250)

b2 = Button(width=150, height=1, bg='lightblue', font=50, text='C) Pekin', anchor='w', command=lambda: wrong_answer(b2))
b2.place(x=55, y=300)

b3 = Button(width=150, height=1, bg='lightblue', font=50, text='F) Toshkent', anchor='w', command=r)
b3.place(x=55, y=350)

b4 = Button(width=150, height=1, bg='lightblue', font=50, text='M) Astana', anchor='w', command=lambda: wrong_answer(b4))
b4.place(x=55, y=400)
# Ballni ko'rsatish uchun label
score_label = Label(a, text=f"Ball: {ball}", font=("Arial", 20), fg="blue")
score_label.place(x=50, y=50)
a.mainloop()
