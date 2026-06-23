from customtkinter import *
from tkinter import messagebox  # For displaying message box

a = CTk()
a.title("Progress Bar Demo")
a.geometry("500x500")


def Ulash():
    # Get progress in percentage
    p1 = int(p.get() * 100)
    l.configure(text=f"Progress: {p1}%")

    # Stop progress and show message at 100%
    if p1 >= 100:
        p.stop()  # Stop the progress bar
        l.configure(text="Progress: 100% - Yuklanib oldi!")
        messagebox.showinfo("Progress", "Yuklanib bo'ldi!")
    else:
        a.after(100, Ulash)


def s():
    p.start()
    Ulash()


def m():
    p.stop()
    p.set(0)  # Reset the progress bar to 0
    l.configure(text="Progress: 0%")  # Reset the label to show 0%


# Start button
s_button = CTkButton(master=a, text="Start", command=s)
s_button.place(x=10, y=100)

# Stop button
m_button = CTkButton(master=a, text="Stop", command=m)
m_button.place(x=10, y=150)

# Progress bar
p = CTkProgressBar(master=a, orientation='horizontal', determinate_speed=0.5)
p.place(x=10, y=10)
p.set(0)

# Label to show the progress percentage
l = CTkLabel(master=a, text="Progress: 0%")
l.place(x=10, y=50)

a.mainloop()
