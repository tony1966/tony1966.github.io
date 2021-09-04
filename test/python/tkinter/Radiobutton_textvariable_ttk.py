import tkinter as tk
from tkinter import ttk

def show_selection():
    result_label.config(text="性別: " + gender.get())
def english():
    option1.set("Male")
    option2.set("Female")
def chinese():
    option1.set("男")
    option2.set("女")    

win=tk.Tk()                                                      
win.title("tkinter GUI 測試") 
gender=tk.StringVar()
gender.set("none")
option1=tk.StringVar()
option1.set("男")
option2=tk.StringVar()
option2.set("女")
ttk.Label(text="性別 : ", width=30, background="cyan").pack()
ttk.Radiobutton(win, 
               variable=gender,
               textvariable=option1,
               value="M",
               command=show_selection).pack()
ttk.Radiobutton(win, 
               variable=gender,
               textvariable=option2,
               value="F",
               command=show_selection).pack()
result_label=ttk.Label(text="性別 : ", width=30, background="ivory")
result_label.pack()
ttk.Button(win, text="英文", command=english).pack(side="left")
ttk.Button(win, text="中文", command=chinese).pack(side="right")
win.mainloop()


