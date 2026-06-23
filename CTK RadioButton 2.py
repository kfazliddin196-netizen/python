from customtkinter import *
a=CTk()
a.title("qwertyuiop[]")
a.geometry('700x700')
v=StringVar()
r=CTkRadioButton(master=a,text='Yes,I do',
                 font=('Arial',20),
                 variable=v,
                 text_color='blue',
                 fg_color='red',
                 border_color='blue',
                 hover_color='black',
                 )
r.place(x=100,y=100)
a.mainloop()