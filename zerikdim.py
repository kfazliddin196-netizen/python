from customtkinter import *
from tkinter import *
a=Tk()
a.geometry('500x400')
a.title('igra')
a.configure(bg='black')
def FM() :
  a1 = CTkToplevel()
  a1.title()
  a1.geometry('600x400')
  M=PhotoImage(file='Need For Speed.png')
  F=Label(master=a1,image=M)
  F.place(x=30, y=30)
  M1=PhotoImage(file='Plants of Zombies 3.png')
  F1=Label(master=a1,image=M1)
  F1.place(x=150, y=30)
  M2=PhotoImage(file='House Flipper.png')
  F2=Label(master=a1,image=M2)
  F2.place(x=270, y=30)
  M3=PhotoImage(file='Mini FootBall.png')
  F3=Label(master=a1,image=M3)
  F3.place(x=390, y=30)
  M4=PhotoImage(file='Real Boxing.png')
  F4=Label(master=a1,image=M4)
  F4.place(x=150, y=30)
  def Ulash():
      k = int(p.get() * 101)
      l.configure(text=f"{k}%-954 MB")
      if k < 100:
          a1.after(100, Ulash)
  def s100():
      p.start()
      Ulash()
  def m():
      p.stop()
      p.set(0)  # Reset the progress bar to 0
      l.configure(text="Progress: 0%")  # Reset the label to show 0%
  #.....................................................................................................
  def Ulash1():
      k1 = int(p1.get() * 101)
      l1.configure(text=f"{k1}%-700 MB")
      if k1 < 100:
          a1.after(100, Ulash1)
  def s101():
      p1.start()
      Ulash1()
  def m10():
      p1.stop()
      p1.set(0)  # Reset the progress bar to 0
      l1.configure(text="Progress: 0%")  # Reset the label to show 0%
  #.....................................................................................................
  def Ulash2():
      k2 = int(p2.get() * 101)
      l2.configure(text=f"{k2}%-300 MB")
      if k2 < 100:
          a1.after(100, Ulash2)
  def s102():
      p2.start()
      Ulash2()
  def m2():
      p2.stop()
      p2.set(0)  # Reset the progress bar to 0
      l2.configure(text="Progress: 0%")  # Reset the label to show 0%
  #.....................................................................................................
  def Ulash3():
      k3 = int(p3.get() * 101)
      l3.configure(text=f"{k3}%-1T")
      if k3 < 100:
          a1.after(100, Ulash3)
  def s103():
      p3.start()
      Ulash3()
  def m3():
      p3.stop()
      p3.set(0)  # Reset the progress bar to 0
      l3.configure(text="Progress: 0%")  # Reset the label to show 0%
  #.....................................................................................................
  s = CTkButton(master=a1, text="Start",height=20,width=30, command=s100)
  s.place(x=30, y=150)
  s = CTkButton(master=a1, text="stop",height=20,width=30,command=m)
  s.place(x=70, y=150)
  p = CTkProgressBar(master=a1, orientation='horizontal', determinate_speed=0.5,width=60)
  p.place(x=40, y=110)
  p.set(0)
  l = CTkLabel(master=a1, text="Progress: 0%")
  l.place(x=35, y=120)
  #........................................................................
  s1 = CTkButton(master=a1, text="Start",height=20,width=30, command=s101)
  s1.place(x=150, y=150)
  s1 = CTkButton(master=a1, text="stop",height=20,width=30,command=m10)
  s1.place(x=190, y=150)
  p1 = CTkProgressBar(master=a1, orientation='horizontal', determinate_speed=0.5,width=60)
  p1.place(x=160, y=110)
  p1.set(0)
  l1 = CTkLabel(master=a1, text="Progress: 0%")
  l1.place(x=155, y=120)
  #........................................................................
  s2 = CTkButton(master=a1, text="Start",height=20,width=30, command=s102)
  s2.place(x=270, y=150)
  s2 = CTkButton(master=a1, text="stop",height=20,width=30,command=m2)
  s2.place(x=310, y=150)
  p2 = CTkProgressBar(master=a1, orientation='horizontal', determinate_speed=0.5,width=60)
  p2.place(x=280, y=110)
  p2.set(0)
  l2 = CTkLabel(master=a1, text="Progress: 0%")
  l2.place(x=275, y=120)
  #........................................................................
  s3 = CTkButton(master=a1, text="Start",height=20,width=30, command=s103)
  s3.place(x=390, y=150)
  s3 = CTkButton(master=a1, text="stop",height=20,width=30,command=m3)
  s3.place(x=430, y=150)
  p3 = CTkProgressBar(master=a1, orientation='horizontal', determinate_speed=0.5,width=60)
  p3.place(x=400, y=110)
  p3.set(0)
  l3 = CTkLabel(master=a1, text="Progress: 0%")
  l3.place(x=395, y=120)
  a1.mainloop()
b=CTkButton(master=a,fg_color='black',
            bg_color='black',
            text='FORE GAME',
            hover_color='black',
            font=("Arial", 20),
            command=FM)
b.place(x=200,y=150)
a.mainloop()