from customtkinter import *
a=CTk()
a.title('Segment button')
a.geometry('500x500')
v=['qiw','bahor','yoz','kuz']
s=CTkSegmentedButton(master=a,values=v)
s.place(x=10,y=10)
s.set('qiw')
a.mainloop()