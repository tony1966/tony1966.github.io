import tkinter as tk
from tkinter import ttk

def show_value():
    label["text"]=var.get()

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x200")

var=tk.StringVar()
var.set("Python")
values=("Python", "Javascript", "R", "Julia", "PHP")
combobox=ttk.Combobox(win, values=values, textvariable=var)
combobox.pack()
ttk.Button(win, text="確定", command=show_value).pack()
label=ttk.Label(win)
label.pack()
win.mainloop()