from customtkinter import *
a=CTk()
a.title('Segment button')
a.geometry('500x500')
def F(b):
        l.configure(text=b)
l=CTkLabel(master=a,text='')
l.place(x=40,y=60)
v=["Qish",'bahor','Yoz','kuz']
s=CTkSegmentedButton(master=a,values=v,
                     width=300,height=40,
                     text_color='red',
                     fg_color='red',
                     border_width=5,
                     corner_radius=100,
                     selected_color='yellow',
                     selected_hover_color='orange',
                     unselected_color='cyan',
                     font=('Arial',20),command=F)
s.place(x=10,y=10)
s.set('Qish')
a.mainloop()