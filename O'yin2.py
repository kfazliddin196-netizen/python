from tkinter import *
from tkinter import ttk
import random
import math
import tkinter.messagebox as messagebox

# Tkinter oynasini yaratish
a = Tk()
a.title("Drum Simulation")  # Sarlavha
a.geometry('800x400')  # Oyna o'lchami

# DrumSimulation klassini yaratish
class DrumSimulation:
    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(root, width=800, height=400, bg='black')  # Kanvas yaratish
        self.canvas.pack()
        # Entrylar son tanlash uchun
        self.FM = Entry(root, width=5)
        self.FM.place(x=100, y=80)
        self.FM1 = Entry(root, width=5)
        self.FM1.place(x=200, y=80)
        self.FM2 = Entry(root, width=5)
        self.FM2.place(x=300, y=80)
        # Start tugmasini yaratish
        self.start_button = Button(root, text="Start", command=self.start_animation)  # 1-marta kinopka
        self.start_button.place(x=200, y=110)

        self.angle = 0  # Strelka boshlang'ich burchagi
        self.center_x = 400  # Strelka markazining x o'qi
        self.center_y = 200  # Strelka markazining y o'qi
        self.size = 50  # Strelka uzunligi
        self.animating = False  # Animatsiya holati

        self.labels = []  # Label ro'yxati
        self.label_texts = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']  # Label matnlari
        self.create_labels()  # Label'larni yaratish
        # Additional labels for total sums
        self.sum1 = 0
        self.sum2 = 0
        self.sum3 = 0
        self.l1 = Label(self.root, text="Ball ", bg='black', fg='white')
        self.l1.place(x=100, y=50)
        self.l2 = Label(self.root, text="Ball ", bg='black', fg='white')
        self.l2.place(x=200, y=50)
        self.l3 = Label(self.root, text="Ball ", bg='black', fg='white')
        self.l3.place(x=300, y=50)

        self.M23 = Label(self.root, bg='black', fg='green')
        self.M23.place(x=100, y=30)
        self.M24 = Label(self.root, bg='black', fg='green')
        self.M24.place(x=200, y=30)
        self.M25 = Label(self.root, bg='black', fg='green')
        self.M25.place(x=300, y=30)

        self.F1 = Entry(self.root, width=10)
        self.F1.place(x=550, y=80)

        def e(event):
            self.M1["text"] = "Tayorman"

        def l(event):
            self.M1["text"] = "Tayormisiz"

        self.M1 = ttk.Button(self.root, text='Tayormisiz', command=self.M100)
        self.M1.place(x=550, y=110)
        self.M1.bind("<Enter>", e)
        self.M1.bind("<Leave>", l)

        self.F2 = Entry(self.root, width=10)
        self.F2.place(x=550, y=140)

        def e1(event):
            self.M2["text"] = "Tayorman"

        def l1(event):
            self.M2["text"] = "Tayormisiz"

        self.M2 = ttk.Button(self.root, text='Tayormisiz', command=self.M101)
        self.M2.place(x=550, y=170)
        self.M2.bind("<Enter>", e1)
        self.M2.bind("<Leave>", l1)

        self.F3 = Entry(self.root, width=10)
        self.F3.place(x=550, y=200)

        def e2(event):
            self.M3["text"] = "Tayorman"

        def l2(event):
            self.M3["text"] = "Tayormisiz"

        self.M3 = ttk.Button(self.root, text='Tayormisiz', command=self.M102)
        self.M3.place(x=550, y=230)
        self.M3.bind("<Enter>", e2)
        self.M3.bind("<Leave>", l2)

    def M100(self):
        self.M23.config(text=f"{self.F1.get()}")

    def M101(self):
        self.M24.config(text=f'{self.F2.get()}')

    def M102(self):
        self.M25.config(text=f'{self.F3.get()}')

    def create_labels(self):
        radius = 80  # Label'lar uchun radius
        num_labels = len(self.label_texts)

        for i in range(num_labels):
            angle = 2 * math.pi * i / num_labels  # Label burchagi
            x = self.center_x + radius * math.cos(angle)  # Label x koordinatasi
            y = self.center_y + radius * math.sin(angle)  # Label y koordinatasi
            label = Label(self.root, text=self.label_texts[i], bg='black', fg='white')  # Label yaratish
            label.place(x=x, y=y, anchor="center")  # Labelni joylash
            self.labels.append(label)  # Labelni ro'yxatga qo'shish

    def draw_arrow(self, angle):
        self.canvas.delete("all")  # Hamma narsani o'chirish
        arrow_angle = math.radians(angle)  # Burchakni radianlarga aylantirish
        end_x = self.center_x + self.size * math.cos(arrow_angle)  # Strelka oxirgi x koordinatasi
        end_y = self.center_y + self.size * math.sin(arrow_angle)  # Strelka oxirgi y koordinatasi
        self.canvas.create_line(self.center_x, self.center_y, end_x, end_y, arrow=LAST, fill='yellow', width=2)  # Strelka chizish

    def animate(self):
        if self.animating:
            self.draw_arrow(self.angle)  # Strelkani chizish
            self.angle += random.randint(10, 30)  # Burchakni o'zgartirish
            if self.angle >= 360:
                self.angle -= 360
            self.root.after(100, self.animate)  # Keyingi animatsiya uchun to'xtash vaqti
        else:
            self.draw_arrow(self.angle)
            self.highlight_label()

    def highlight_label(self):
        closest_label_index = round(self.angle / 360 * len(self.label_texts)) % len(self.label_texts)
        return closest_label_index

    def start_animation(self):
        if not self.animating:
            self.animating = True  # Animatsiyani boshlash
            self.angle = random.randint(10, 360)  # Tasodifiy burchak
            self.root.after(3000, self.stop_animation)  # 3 soniyadan keyin to'xtash
            self.animate()  # Animatsiyani boshlash

    def stop_animation(self):
        self.animating = False
        highlighted = self.highlight_label()
        chosen_number = int(self.labels[highlighted].cget("text"))

        if self.FM.get().isdigit() and int(self.FM.get()) == chosen_number:
            self.sum1 += 10  # Mos kelgan bo'lsa 10 bal qo'shish
        if self.FM1.get().isdigit() and int(self.FM1.get()) == chosen_number:
            self.sum2 += 10  # Mos kelgan bo'lsa 10 bal qo'shish
        if self.FM2.get().isdigit() and int(self.FM2.get()) == chosen_number:
            self.sum3 += 10  # Mos kelgan bo'lsa 10 bal qo'shish

        self.l1.config(text=f" {self.sum1}", fg='red')
        self.l2.config(text=f" {self.sum2}", fg='red')
        self.l3.config(text=f" {self.sum3}", fg='red')

        # Har bir o'yinchi ballini yangilagandan so'ng, Entry maydonlarini tozalash
        self.FM.delete(0, END)
        self.FM1.delete(0, END)
        self.FM2.delete(0, END)

        if self.sum1 >= 100 or self.sum2 >= 100 or self.sum3 >= 100:
            messagebox.showinfo(message='Tabriklayman, siz yutdingiz!')
            self.reset_game()

    def reset_game(self):
        # Barcha qiymatlar va UI elementlarini tiklash
        self.sum1 = 0
        self.sum2 = 0
        self.sum3 = 0
        self.l1.config(text="Ball ", fg='white')
        self.l2.config(text="Ball ", fg='white')
        self.l3.config(text="Ball ", fg='white')

        # Entry maydonlarini tozalash
        self.FM.delete(0, END)
        self.FM1.delete(0, END)
        self.FM2.delete(0, END)

    # O'yinni ishga tushirish
game = DrumSimulation(a)
a.mainloop()
