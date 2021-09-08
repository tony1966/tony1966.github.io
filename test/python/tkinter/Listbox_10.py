import tkinter as tk
from tkinter import ttk

def reset_listbox():
    var.set(("Python", "Javascript", "R", "Julia"))
def delete_option():
    listbox.delete(0)

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("400x350")

var=tk.StringVar()
var.set(("Python", "Javascript", "R", "Julia"))
listbox=tk.Listbox(win, bg="cyan", listvariable=var, selectmode="multiple")
listbox.pack()
tk.Button(win, text="重設", command=reset_listbox).pack()
tk.Button(win, text="刪除", command=delete_option).pack()
label=tk.Label(win)
label.pack()
win.mainloop()