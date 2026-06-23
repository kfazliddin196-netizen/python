from customtkinter import *
a=CTk()
a.title('segment button')
a.geometry('500x500')

t=CTkTabview(master=a)
t.pack(pady=10)

t1=t.add('Tab 1')
t2=t.add('Tab 2')

b=CTkButton(t1,text='mani bos!')
b.pack(pady=40)
a.mainloop()