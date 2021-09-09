import tkinter as tk
from tkinter import ttk

def move_left():
    for i in listbox_2.curselection():          
        listbox_1.insert(0, listbox_2.get(i))
        listbox_2.delete(i)
def move_right():
    for i in listbox_1.curselection():          
        listbox_2.insert(0, listbox_1.get(i))
        listbox_1.delete(i)

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")

listbox_1=tk.Listbox(win, bg="cyan")
names=('張無忌', '趙敏', '周芷若', '小昭', '殷離', '楊不悔', '朱九貞')
for name in names:
    listbox_1.insert(0, name)
listbox_1.grid(row=0, column=0, rowspan=2)
tk.Button(win, text=">>", command=move_right).grid(row=0, column=1)
tk.Button(win, text="<<", command=move_left).grid(row=1, column=1)
listbox_2=tk.Listbox(win, bg="ivory")
listbox_2.grid(row=0, column=2, rowspan=2)
win.mainloop()