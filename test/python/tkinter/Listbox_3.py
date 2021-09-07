import tkinter as tk
from tkinter import ttk

def get_options():
    size=listbox.size()
    options=listbox.get(0, size)
    result_label["text"]="size=" + str(size) + " " + str(options)

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("400x350")

var=tk.StringVar()
var.set(("Python", "Javascript", "R", "Julia"))
listbox=tk.Listbox(win, bg="cyan", listvariable=var, height=8)
listbox.pack()
tk.Button(win, text="確定", command=get_options).pack()
result_label=tk.Label(win)
result_label.pack()
win.mainloop()