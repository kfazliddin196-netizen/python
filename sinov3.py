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

        # Start tugmalarni yaratish
        self.start_button1 = Button(root, text="Start 1", command=self.start_animation1)  # 1-marta kinopka
        self.start_button1.place(x=100, y=80)
        self.start_button2 = Button(root, text="Start 2", command=self.start_animation2)  # 2-marta kinopka
        self.start_button2.place(x=200, y=80)
        self.start_button3 = Button(root, text="Start 3", command=self.start_animation3)  # 3-marta kinopka
        self.start_button3.place(x=300, y=80)

        self.angle = 0  # Strelka boshlang'ich burchagi
        self.center_x = 400  # Strelka markazining x o'qi
        self.center_y = 200  # Strelka markazining y o'qi
        self.size = 50  # Strelka uzunligi
        self.animating = False  # Animatsiya holati

        self.labels = []  # Label ro'yxati
        self.label_texts = ["10", "20", "30", "40", "50", "60", "100", "110", "120", "130", "140", "150", "160", "170",
                            "180", "190", "200", '1000']  # Label matnlari
        self.create_labels()  # Label'larni yaratish
        # Additional labels for total sums
        self.sum1 = 0
        self.l11 = Label(self.root, text="Ball ", bg='black', fg='white')
        self.l11.place(x=100, y=50)
        self.sum2 = 0
        self.l12 = Label(self.root, text="Ball ", bg='black', fg='white')
        self.l12.place(x=200, y=50)
        self.sum3 = 0
        self.l13 = Label(self.root, text="Ball ", bg='black', fg='white')
        self.l13.place(x=300, y=50)
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

    def reset_label_colors(self):
        for label in self.labels:
            label.config(bg='black')

    def start_animation1(self):
        if not self.animating:
            self.reset_label_colors()
            self.animating = True  # Animatsiyani boshlash
            self.angle = random.randint(10, 360)  # Tasodifiy burchak
            self.root.after(3000, self.stop_animation1)  # 3 soniyadan keyin to'xtash
            self.animate()  # Animatsiyani boshlash

    def start_animation2(self):
        if not self.animating:
            self.reset_label_colors()
            self.animating = True  # Animatsiyani boshlash
            self.angle = random.randint(10, 360)  # Tasodifiy burchak
            self.root.after(3000, self.stop_animation2)  # 3 soniyadan keyin to'xtash
            self.animate()  # Animatsiyani boshlash

    def start_animation3(self):
        if not self.animating:
            self.reset_label_colors()
            self.animating = True  # Animatsiyani boshlash
            self.angle = random.randint(10, 360)  # Tasodifiy burchak
            self.root.after(3000, self.stop_animation3)  # 3 soniyadan keyin to'xtash
            self.animate()  # Animatsiyani boshlash

    def stop_animation1(self):
        self.animating = False
        highlighted = self.highlight_label()
        self.sum1 += int(self.labels[highlighted].cget("text"))
        self.l11.config(text=f" {self.sum1}", fg='red')

        # Highlight the selected label
        self.labels[highlighted].config(bg='red')

        # Check if maximum score reached
        if self.sum1 >= 1000:
            messagebox.showinfo(message=f'Tabriklman {self.F1.get()} siz yutingiz')
            self.reset_game()

    def stop_animation2(self):
        self.animating = False
        highlighted1 = self.highlight_label()
        self.sum2 += int(self.labels[highlighted1].cget("text"))
        self.l12.config(text=f" {self.sum2}", fg='red')

        # Highlight the selected label
        self.labels[highlighted1].config(bg='yellow')

        # Check if maximum score reached
        if self.sum2 >= 1000:
            messagebox.showinfo(message=f'Tabriklman {self.F2.get()} siz yutingiz')
            self.reset_game()

    def stop_animation3(self):
        self.animating = False
        highlighted2 = self.highlight_label()
        self.sum3 += int(self.labels[highlighted2].cget("text"))
        self.l13.config(text=f" {self.sum3}", fg='red')

        # Highlight the selected label
        self.labels[highlighted2].config(bg='green')

        # Check if maximum score reached
        if self.sum3 >= 1000:
            messagebox.showinfo(message=f'Tabriklman {self.F3.get()} siz yutingiz')
            self.reset_game()

    def reset_game(self):
        # Reset all values and UI elements
        self.sum1 = 0
        self.l11.config(text="Ball ", fg='white')
        self.sum2 = 0
        self.l12.config(text="Ball ", fg='white')
        self.sum3 = 0
        self.l13.config(text="Ball ", fg='white')
        self.M23.config(text="")
        self.M24.config(text="")
        self.M25.config(text="")
        self.F1.delete(0, END)
        self.F2.delete(0, END)
        self.F3.delete(0, END)
        self.reset_label_colors()

# DrumSimulation obyektini yaratish va ilovani ishga tushirish
drum_simulation = DrumSimulation(a)

a.mainloop()  # Ilovaning ishga tushirilishi
