from customtkinter import *
a=CTk()
a.title('Segment button')
a.geometry('500x500')
f=CTkScrollableFrame(master=a,label_text='knopka',
                     label_fg_color='green',
                     label_font=("Arial",15),
                     width=300,height=200,
                     border_width=5,
                     border_color='cyan',
                     fg_color='black',
                     scrollbar_button_color='grey',
                     scrollbar_button_hover_color='brown',
                     scrollbar_fg_color='blue')
f.pack(pady=40)
for x in range(20):
    CTkButton(master=f,text='Man Kimman').pack(pady=10)
a.mainloop()