import tkinter as tk
root = tk.Tk()
root.title("Simple Calculator")
entry = tk.Entry(root, width=20, font=("Arial", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4)
def t():
    entry.delete(0,)
def on_button_click(value):
    text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, text + str(value))
def clear_entry():
    entry.delete(0,)
def calculate_result():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root,text=button,padx=20,pady=20,font=("Arial", 14),command=lambda
        b=button: on_button_click(b) if b != '=' else calculate_result() ).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
tk.Button(root, text="C", padx=20, pady=20, font=("Arial", 14), command=clear_entry).grid(row=row_val, column=col_val)
root.mainloop()
