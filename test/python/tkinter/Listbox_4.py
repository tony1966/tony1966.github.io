import tkinter as tk
from tkinter import ttk

def get_selected_option():
    selected=listbox.curselection()
    result_label["text"]="curselection=" + str(selected) + \
                         " 選取: " + listbox.get(selected[0])

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("400x350")

var=tk.StringVar()
var.set(("Python", "Javascript", "R", "Julia"))
listbox=tk.Listbox(win, bg="cyan", listvariable=var, height=8)
listbox.pack()
tk.Button(win, text="確定", command=get_selected_option).pack()
result_label=tk.Label(win)
result_label.pack()
win.mainloop()