import tkinter as tk
from tkinter import ttk

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("500x300")
scrollbar=tk.Scrollbar(win)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text=tk.Text(win, height=10, bg="aqua")
text.config(padx=5, pady=5, font="Helvetic 12")
text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)
str="Hello World!\n你是在說哈囉嗎?"
strlist=[]
for i in range(10):
    strlist.append(str)
text.insert("insert", "\n".join(strlist))
text.pack(side=tk.LEFT, fill=tk.Y)
win.mainloop()