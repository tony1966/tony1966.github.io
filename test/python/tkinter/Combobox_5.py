import tkinter as tk
from tkinter import ttk

def show_value(value):
    label["text"]=var.get()

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x200")

var=tk.StringVar()
var.set("Python")
values=("Python", "Javascript", "R", "Julia", "PHP")
combobox=ttk.Combobox(win, values=values, textvariable=var)
combobox.bind('<<ComboboxSelected>>', show_value)
combobox.pack()
label=ttk.Label(win)
label.pack()
win.mainloop()