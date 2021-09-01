import tkinter as tk
from tkinter import ttk

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("500x300")
scrollbar=ttk.Scrollbar(win, orient=tk.HORIZONTAL)
scrollbar.pack(side=tk.TOP, fill=tk.X)
text=tk.Text(win, height=10, bg="aqua")
text.config(padx=5, pady=5, font="Helvetic 12", wrap=tk.NONE)
text.config(xscrollcommand=scrollbar.set)
scrollbar.config(command=text.xview)
str="Hello World!你是在說哈囉嗎?"
strlist=[]
for i in range(10):
    strlist.append(str)
text.insert("insert", "".join(strlist))
text.pack(side=tk.BOTTOM, fill=tk.X)
win.mainloop()