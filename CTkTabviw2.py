from customtkinter import *
a=CTk()
a.title('segment button')
a.geometry('700x500')
tab=CTkTabview(master=a,
               width=600,height=250,
               corner_radius=25,fg_color="silver",
               text_color="black",border_color="green",border_width=3,
               segmented_button_fg_color="green",
               segmented_button_selected_color="white",
               segmented_button_selected_hover_color="green2",
               segmented_button_unselected_color="grey38",
               segmented_button_unselected_hover_color="white")
tab.pack(pady=10)
t1=tab.add('Tab 1')
t2=tab.add('Tab 2')
t3=tab.add('Tab 3')
b=CTkButton(t1,text='mani bos!')
b.pack(pady=40)
a.mainloop()