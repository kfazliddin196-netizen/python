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
        self.FM1 = Entry(root, width=5)
        self.FM1.place(x=100, y=80)
        self.FM2 = Entry(root, width=5)
        self.FM2.place(x=200, y=80)
        self.FM3 = Entry(root, width=5)
        self.FM3.place(x=300, y=80)

        # Start tugmasini yaratish
        self.start_button = Button(root, text="Start", command=self.start_animation)
        self.start_button.place(x=200, y=110)

        self.angle = 0  # Strelka boshlang'ich burchagi
        self.center_x = 400  # Strelka markazining x o'qi
        self.center_y = 200  # Strelka markazining y o'qi
        self.size = 100  # Strelka uzunligi
        self.animating = False  # Animatsiya holati

        self.labels = []  # Label ro'yxati
        self.label_texts = ['1A', '2B', '3C', '4D', '5E', '6F', '7G', '8H', '9I', '10J', '11K', '12L', '13M', '14N',
                            '15O', '16P']  # Label matnlari
        self.create_labels()  # Label'larni yaratish

        # Ballar uchun label yaratish
        self.scores = [0, 0, 0]
        self.l1 = Label(self.root, text="Player 1: 0", bg='black', fg='white')
        self.l1.place(x=100, y=50)
        self.l2 = Label(self.root, text="Player 2: 0", bg='black', fg='white')
        self.l2.place(x=200, y=50)
        self.l3 = Label(self.root, text="Player 3: 0", bg='black', fg='white')
        self.l3.place(x=300, y=50)

    def create_labels(self):
        radius = 100  # Label'lar uchun radius
        num_labels = len(self.label_texts)

        for i in range(num_labels):
            angle = 2 * math.pi * i / num_labels  # Label burchagi
            x = self.center_x + radius * math.cos(angle)  # Label x koordinatasi
            y = self.center_y + radius * math.sin(angle)  # Label y koordinatasi
            label_text = self.label_texts[i]
            label = Label(self.root, text=label_text[:-1], bg='black', fg='white')  # Faqat raqamni ko'rsatish
            label.place(x=x, y=y, anchor="center")  # Labelni joylash
            self.labels.append((label, label_text[-1]))  # Labelni ro'yxatga qo'shish

    def draw_arrow(self, angle):
        self.canvas.delete("all")  # Hamma narsani o'chirish
        arrow_angle = math.radians(angle)  # Burchakni radianlarga aylantirish
        end_x = self.center_x + self.size * math.cos(arrow_angle)  # Strelka oxirgi x koordinatasi
        end_y = self.center_y + self.size * math.sin(arrow_angle)  # Strelka oxirgi y koordinatasi
        self.canvas.create_line(self.center_x, self.center_y, end_x, end_y, arrow=LAST, fill='yellow',
                                width=2)  # Strelka chizish

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
        chosen_label, hidden_char = self.labels[highlighted]
        chosen_number = int(chosen_label.cget("text"))

        entries = [self.FM1, self.FM2, self.FM3]

        for i, entry in enumerate(entries):
            if entry.get().isdigit() and int(entry.get()) == chosen_number:
                self.scores[i] += 10  # Mos kelgan bo'lsa 10 bal qo'shish
                self.update_score_labels()

        if max(self.scores) >= 100:
            messagebox.showinfo(message='Tabriklayman, siz yutdingiz!')
            self.reset_game()
        else:
            self.show_hidden_char(hidden_char)  # Yashirin harfni ko'rsatish

    def show_hidden_char(self, hidden_char):
        messagebox.showinfo(message=f"Tanlangan raqam orqasida yashirilgan harf: {hidden_char}")

    def update_score_labels(self):
        self.l1.config(text=f"Player 1: {self.scores[0]}")
        self.l2.config(text=f"Player 2: {self.scores[1]}")
        self.l3.config(text=f"Player 3: {self.scores[2]}")

    def reset_game(self):
        # Barcha qiymatlar va UI elementlarini tiklash
        self.scores = [0, 0, 0]
        self.update_score_labels()

        # Entry maydonlarini tozalash
        self.FM1.delete(0, END)
        self.FM2.delete(0, END)
        self.FM3.delete(0, END)
        

        # O'yinni qayta ishga tushirish
        self.animating = False
        self.angle = 0
        self.draw_arrow(self.angle)


# O'yinni ishga tushirish
game = DrumSimulation(a)
a.mainloop()
