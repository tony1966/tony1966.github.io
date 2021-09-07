import tkinter as tk
from tkinter import ttk

def get_selected_options():
    selected=listbox.curselection()
    label_1.config(text="curselection=" + str(selected))
    selected_options=[]
    for i in selected:
        selected_options.append(listbox.get(i))
    label_2["text"]=" 選取: " + ",".join(selected_options)

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("400x350")

var=tk.StringVar()
var.set(("Python", "Javascript", "R", "Julia"))
listbox=tk.Listbox(win, bg="cyan", listvariable=var)
listbox.selection_set(1)
listbox.pack()
tk.Button(win, text="確定", command=get_selected_options).pack()
label_1=tk.Label(win)
label_1.pack()
label_2=tk.Label(win)
label_2.pack()
win.mainloop()