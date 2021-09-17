import tkinter as tk
from tkinter import ttk

def show_value_1():
    label_1["text"]=combobox_1.get()
def show_value_2():
    label_2["text"]=combobox_2.get()

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x200")

values=("Python", "Javascript", "R", "Julia", "PHP")
combobox_1=ttk.Combobox(win, values=values)
combobox_1.pack()
ttk.Button(win, text="確定", command=show_value_1).pack()
label_1=ttk.Label(win)
label_1.pack()
combobox_2=ttk.Combobox(win, values=values, state="readonly")
combobox_2.pack()
ttk.Button(win, text="確定", command=show_value_2).pack()
label_2=ttk.Label(win)
label_2.pack()
win.mainloop()