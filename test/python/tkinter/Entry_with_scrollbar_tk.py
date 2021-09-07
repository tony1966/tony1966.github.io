import tkinter as tk
from tkinter import ttk

win=tk.Tk()                                                      
win.title("tkinter GUI 測試") 

var=tk.StringVar()
var.set("Hello World! 你是在說哈囉嗎? Hello Tony")
entry=tk.Entry(win, textvariable=var)
scrollbar=tk.Scrollbar(win, orient=tk.HORIZONTAL)
entry.config(xscrollcommand=scrollbar.set)
scrollbar.config(command=entry.xview)   
scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
entry.pack(side=tk.TOP, fill=tk.Y)

win.mainloop()