import tkinter as tk
from tkinter import ttk

def add_option():
    listbox.insert(0, option.get())
def delete_options():
    selected=listbox.curselection()
    for i in selected:          
        listbox.delete(selected[0]) 

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")

options=tk.StringVar()
options.set(["你是在說哈囉嗎? " + str(i) for i in range(20)])
listbox=tk.Listbox(win, bg="cyan", listvariable=options)
listbox.pack(side=tk.LEFT, fill=tk.Y)
scrollbar=tk.Scrollbar(win)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set) 
scrollbar.config(command=listbox.yview)
win.mainloop()