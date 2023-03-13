import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x200")

# Define custom style for the messagebox
style = ttk.Style()
style.configure('Custom.TButton', font=('Helvetica', 10, 'bold'), foreground='white', background='green')
style.configure('Custom.TLabel', font=('Helvetica', 12), foreground='blue')

# Define custom function for the messagebox
def custom_askokcancel(title, message):
    result = messagebox.askokcancel(title, message, icon='warning')
    if result:
        messagebox.showinfo(title='Success', message='Operation Successful!', icon='info')
    else:
        messagebox.showerror(title='Error', message='Operation Failed!', icon='error')

# Create a button to show the custom messagebox
def show_custom_messagebox():
    custom_askokcancel('Custom Title', 'Custom Message')

button = tk.Button(root, text='Show Custom Messagebox', command=show_custom_messagebox)
button.pack(pady=20)

root.mainloop()
