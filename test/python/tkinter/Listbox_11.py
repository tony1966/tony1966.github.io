import tkinter as tk
from tkinter import ttk

def add_option():
    listbox.insert(0, option.get())
def delete_option():
    listbox.delete(listbox.curselection())

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("400x350")

listbox=tk.Listbox(win, bg="cyan")
listbox.pack()
option=tk.StringVar()
tk.Entry(win, textvariable=option).pack()
tk.Button(win, text="新增", command=add_option).pack()
tk.Button(win, text="刪除", command=delete_option).pack()
label=tk.Label(win)
label.pack()
win.mainloop()