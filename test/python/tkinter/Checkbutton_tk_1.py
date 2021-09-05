import tkinter as tk
from tkinter import ttk

def show_selection():
    selection=[]
    if var1.get() == True:
        selection.append("英語")
    if var2.get() == True:
        selection.append("日語")
    if var3.get() == True:
        selection.append("韓語")        
    result_label["text"]="選取結果 : " + ",".join(selection)

win=tk.Tk()                                                      
win.title("tkinter GUI 測試") 
ttk.Label(text="外語能力 : ", width=30, background="cyan").pack()
var1=tk.BooleanVar()
var1.set(0)
var2=tk.BooleanVar()
var2.set(0)
var3=tk.BooleanVar()
var3.set(0)
tk.Checkbutton(win, text="英語",
               variable=var1,
               command=show_selection).pack()
tk.Checkbutton(win, text="日語",
               variable=var2,
               command=show_selection).pack()
tk.Checkbutton(win, text="韓語",
               variable=var3,
               command=show_selection).pack()
result_label=tk.Label(text="選取結果 : ", width=30, background="ivory")
result_label.pack()
win.mainloop()