import tkinter as tk
from tkinter import messagebox as msgbox

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x200")

def say_hello():
    msgbox.showinfo("Info", "Hello World!")

menubar=tk.Menu(win)
menubar.add_command(label="Hello", command=say_hello)
menubar.add_command(label="Quit", command=win.destroy)
win.config(menu=menubar)
win.mainloop()