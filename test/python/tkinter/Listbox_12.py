import tkinter as tk
from tkinter import ttk

def add_option():
    listbox.insert(0, option.get())
def delete_options():
    selected=list(listbox.curselection())
    selected.sort(reverse=True)
    for i in selected:          
        listbox.delete(i) 

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("400x400")

listbox=tk.Listbox(win, bg="cyan", selectmode=tk.MULTIPLE)
listbox.pack()
option=tk.StringVar()
tk.Entry(win, textvariable=option).pack()
tk.Button(win, text="新增", command=add_option).pack()
tk.Button(win, text="刪除", command=delete_options).pack()
label=tk.Label(win)
label.pack()
win.mainloop()