from tkinter import *
from tkinter.messagebox import showinfo, showerror

# Ilova oynasi
a = Tk()
a.title("Maryam")
a.geometry("500x500")
a.configure(bg="Green")

# Faqat raqamli kiritishni tekshirish funksiyasi
def raqam_tekshir(tekst):
    return tekst.isdigit() or tekst == ""  # Faqat raqamlar va bo'sh joyga ruxsat

# Foydalanuvchi ma'lumotlarini tekshirish funksiyasi
def Регистрация():
    if b.get() == "Maryam" and c.get() == "12345":  # Masalan, raqamli parol 12345
        showinfo(title='Xabar', message='Toʻgʻri!')
    else:
        showerror(title='Xato', message='Login yoki parol notoʻgʻri!')

# Login maydoni
Label(a, text="Login:", bg="Green", fg="White").place(x=20, y=100)
b = Entry(a)
b.place(x=100, y=100)

# Parol maydoni (faqat raqamlar)
Label(a, text="Parol:", bg="Green", fg="White").place(x=20, y=150)
raqam_valid = a.register(raqam_tekshir)  # Validatsiya funksiyasini ro'yxatdan o'tkazish
c = Entry(a, validate="key", validatecommand=(raqam_valid, '%P'))  # Faqat raqamlar qabul qilinadi
c.place(x=100, y=150)

# Tugma
M = Button(a, text="Kirish", width=10, height=2, command=Регистрация)
M.place(x=100, y=200)

# Asosiy oynani ishga tushirish
a.mainloop()