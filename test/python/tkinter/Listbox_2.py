import tkinter as tk
from tkinter import ttk

def get_listvariable():
    result_label["text"]=var.get()
def set_listvariable():
    var.set(("Python", "Javascript", "R", "Julia"))    

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("400x350")

var=tk.StringVar()
listbox=tk.Listbox(win, bg="cyan", listvariable=var, height=8)
listbox.pack()
tk.Button(win, text="設定", command=set_listvariable).pack()
tk.Button(win, text="確定", command=get_listvariable).pack()
result_label=tk.Label(win)
result_label.pack()
win.mainloop()