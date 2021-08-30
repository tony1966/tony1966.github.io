import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox

def clear():
    account.set("")
    pwd.set("")
def login():
    if account.get() == "admin" and pwd.get() == "admin":
        msgbox.showinfo("Info", "登入成功")
    else:
        msgbox.showinfo("Info", "帳號或密碼錯誤")

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("350x150")

account=tk.StringVar()
pwd=tk.StringVar()
ttk.Label(win, text="帳號").grid(row=0, column=0)
ttk.Entry(win, textvariable=account).grid(row=0, column=1)
ttk.Label(win, text="密碼").grid(row=1, column=0)
ttk.Entry(win, show="*", textvariable=pwd).grid(row=1, column=1)
ttk.Button(text="清除", command=clear).grid(row=2, column=0, sticky=tk.W)
ttk.Button(text="登入", command=login).grid(row=2, column=1, sticky=tk.W)
win.mainloop()