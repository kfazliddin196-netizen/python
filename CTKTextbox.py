from customtkinter import *
a=CTk()
a.title()
a.geometry('500x500')
t=CTkTextbox(master=a,
             border_color='yellow',
             border_width=3,
             fg_color='grey',
             text_color='white',
             scrollbar_button_color='black',
             scrollbar_button_hover_color='white')
t.pack(pady=15)
a.mainloop()