from customtkinter import *
a=CTk()
a.title()
a.geometry('500x500')
f=CTkScrollableFrame(master=a,
                     label_text='Kopkalar',)
f.pack(pady=40)
for i in range(20):
   a1= CTkButton(master=f,text='Man kimman')
   a1.pack(pady=10)
a.mainloop()
