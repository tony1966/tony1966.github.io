import tkinter as tk
from tkinter import ttk

def show_selection():
    result_label["text"]=var.get()

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("400x350")

var=tk.StringVar()
listbox=tk.Listbox(win, bg="cyan", listvariable=var)
listbox.insert(0, "Python")
listbox.insert(1, "Javascript")
listbox.insert(2, "R")
listbox.insert(3, "Julia")
listbox.pack()
tk.Button(win, text="確定", command=show_selection).pack()
result_label=tk.Label(win)
result_label.pack()
win.mainloop()