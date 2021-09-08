import tkinter as tk
from tkinter import ttk

def add_option():
    listbox.insert(0, option.get())
def delete_options():
    selected=listbox.curselection()
    for i in range(len(selected)):          
        listbox.delete(selected[0]) 

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("400x400")

listbox=tk.Listbox(win, bg="cyan", selectmode=tk.EXTENDED)
listbox.pack()
option=tk.StringVar()
tk.Entry(win, textvariable=option).pack()
tk.Button(win, text="新增", command=add_option).pack()
tk.Button(win, text="刪除", command=delete_options).pack()
label=tk.Label(win)
label.pack()
win.mainloop()