import tkinter as tk
from tkinter import ttk

def check_selection():
    label["text"]="selection_includes(2)=" + str(listbox.selection_includes(2))

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("400x350")

var=tk.StringVar()
var.set(("Python", "Javascript", "R", "Julia"))
listbox=tk.Listbox(win, bg="cyan", listvariable=var, selectmode="multiple")
listbox.pack()
tk.Button(win, text="確定", command=check_selection).pack()
label=tk.Label(win)
label.pack()
win.mainloop()