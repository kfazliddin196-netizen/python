from customtkinter import *
from tkinter import *
a=CTk()
a.geometry('800x600')
set_appearance_mode("dark")
def rasm():
    if e.get()=='Chillak' and e1.get()=='2':
        l.config(image=Chillak2)
    elif e.get()=='Chillak' and e1.get()=='3':
        l.config(image=Chillak3)
    elif e.get()=='Chillak' and e1.get()=='4':
        l.config(image=Chillak4)
    elif e.get()=='Chillak' and e1.get()=='5':
        l.config(image=Chillak5)
    elif e.get()=='Chillak' and e1.get()=='6':
        l.config(image=Chillak6)
    elif e.get()=='Chillak' and e1.get()=='7':
        l.config(image=Chillak7)
    elif e.get()=='Chillak' and e1.get()=='8':
        l.config(image=Chillak8)
    elif e.get()=='Chillak' and e1.get()=='9':
        l.config(image=Chillak9)
    elif e.get()=='Chillak' and e1.get()=='10':
        l.config(image=Chillak10)
    elif e.get()=='Chillak' and e1.get()=='Tuz':
        l.config(image=Chillak11)
#............................................................
    elif e.get()=='G\'isht' and e1.get()=='2':
        l.config(image=Gisht2)
    elif e.get()=='G\'isht' and e1.get()=='3':
        l.config(image=Gisht3)
    elif e.get()=='G\'isht' and e1.get()=='4':
        l.config(image=Gisht4)
    elif e.get()=='G\'isht' and e1.get()=='5':
        l.config(image=Gisht5)
    elif e.get()=='G\'isht' and e1.get()=='6':
        l.config(image=Gisht6)
    elif e.get()=='G\'isht' and e1.get()=='7':
        l.config(image=Gisht7)
    elif e.get()=='G\'isht' and e1.get()=='8':
        l.config(image=Gisht8)
    elif e.get()=='G\'isht' and e1.get()=='9':
        l.config(image=Gisht9)
    elif e.get()=='G\'isht' and e1.get()=='10':
        l.config(image=Gisht10)
    elif e.get()=='G\'isht' and e1.get()=='Tuz':
        l.config(image=Gisht11)
#.....................................................................
    elif e.get()=='Qarg\'a' and e1.get()=='2':
        l.config(image=qarga2)
    elif e.get()=='Qarg\'a' and e1.get()=='3':
        l.config(image=qarga3)
    elif e.get()=='Qarg\'a' and e1.get()=='4':
        l.config(image=qarga4)
    elif e.get()=='Qarg\'a' and e1.get()=='5':
        l.config(image=qarga5)
    elif e.get()=='Qarg\'a' and e1.get()=='6':
        l.config(image=qarga6)
    elif e.get()=='Qarg\'a' and e1.get()=='7':
        l.config(image=qarga7)
    elif e.get()=='Qarg\'a' and e1.get()=='8':
        l.config(image=qarga8)
    elif e.get()=='Qarg\'a' and e1.get()=='9':
        l.config(image=qarga9)
    elif e.get()=='Qarg\'a' and e1.get()=='10':
        l.config(image=qarga10)
    elif e.get()=='Qarg\'a' and e1.get()=='Tuz':
        l.config(image=qarga11)
#.................................................................
    elif e.get()=='Olma' and e1.get()=='2':
        l.config(image=Olma2)
    elif e.get()=='Olma' and e1.get()=='3':
        l.config(image=Olma3)
    elif e.get()=='Olma' and e1.get()=='4':
        l.config(image=Olma4)
    elif e.get()=='Olma' and e1.get()=='5':
        l.config(image=Olma5)
    elif e.get()=='Olma' and e1.get()=='6':
        l.config(image=Olma6)
    elif e.get()=='Olma' and e1.get()=='7':
        l.config(image=Olma7)
    elif e.get()=='Olma' and e1.get()=='8':
        l.config(image=Olma8)
    elif e.get()=='Olma' and e1.get()=='9':
        l.config(image=Olma9)
    elif e.get()=='Olma' and e1.get()=='10':
        l.config(image=Olma10)
    elif e.get()=='Olma' and e1.get()=='Tuz':
        l.config(image=Olma11)
    else:
        l.config(text="Noto'g'ri ma'lumot")
#................................................................................
e1=CTkEntry(master=a,width=155,corner_radius=32,placeholder_text='Karta qiymatini kiriting')
e1.place(x=50,y=20)
e=CTkEntry(master=a,corner_radius=32,placeholder_text='Karta turini kiriting')
e.place(x=50,y=50)
b=Button(width=10,command=rasm)
b.place(x=50,y=80)
Chillak2=PhotoImage(file='Chillak 2.png')
Chillak3=PhotoImage(file='Chillak 3.png')
Chillak4=PhotoImage(file='chillak 4.png')
Chillak5=PhotoImage(file='chillak 5.png')
Chillak6=PhotoImage(file='chillak 6.png')
Chillak7=PhotoImage(file='chillak 7.png')
Chillak8=PhotoImage(file='chillak 8.png')
Chillak9=PhotoImage(file='chillak 9.png')
Chillak10=PhotoImage(file='chillak 10.png')
Chillak11=PhotoImage(file='Chillak tuz.png')

Gisht2=PhotoImage(file='G\'isht 2.png')
Gisht3=PhotoImage(file='G\'isht 3.png')
Gisht4=PhotoImage(file='G\'isht 4.png')
Gisht5=PhotoImage(file='g\'isht 5.png')
Gisht6=PhotoImage(file='G\'ishd 6.png')
Gisht7=PhotoImage(file='G\'isht 7.png')
Gisht8=PhotoImage(file='g\'isht 8.png')
Gisht9=PhotoImage(file='G\'isht 9.png')
Gisht10=PhotoImage(file='G\'isht 10.png')
Gisht11=PhotoImage(file='G\'isht Tuz.png')

qarga2=PhotoImage(file='qarg\'a 2 .png')
qarga3=PhotoImage(file='Qarg\'a 3.png')
qarga4=PhotoImage(file='Qarg\'a 4.png')
qarga5=PhotoImage(file='Qarg\'a 5.png')
qarga6=PhotoImage(file='Qarg\'a 6.png')
qarga7=PhotoImage(file='Qarg\'a 7.png')
qarga8=PhotoImage(file='Qarg\'a 8.png')
qarga9=PhotoImage(file='Qarg\'a 9.png')
qarga10=PhotoImage(file='Qarg\'a 10.png')
qarga11=PhotoImage(file='Qarg\'a tuz.png')


Olma2=PhotoImage(file='Olma 2.png')
Olma3=PhotoImage(file='Olma 3.png')
Olma4=PhotoImage(file='Olma 4.png')
Olma5=PhotoImage(file='Olma 5.png')
Olma6=PhotoImage(file='Olma 6.png')
Olma7=PhotoImage(file='Olma 7.png')
Olma8=PhotoImage(file='Olma 8.png')
Olma9=PhotoImage(file='Olma 9.png')
Olma10=PhotoImage(file='Olma 10.png')
Olma11=PhotoImage(file='Olma tuz.png')
l=Label()
l.pack(expand=1)
a.mainloop()