import tkinter as tk
from tkinter import messagebox as msgbox

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x200")

def say_hello():
    msgbox.showinfo("Info", "Hello World!")

menubar=tk.Menu(win)
hello_menu=tk.Menu(menubar, tearoff=False)
hello_menu.add_command(label="Hello-1", command=say_hello)
hello_menu.add_command(label="Hello-2", command=say_hello)
hello_menu.add_separator()
hello_menu.add_command(label="Hello-3", command=say_hello)
hello_menu.add_command(label="Hello-4", command=say_hello)
hello_menu.add_separator()
hello_menu.add_command(label="Hello-5", command=say_hello)
menubar.add_cascade(label="Hello", menu=hello_menu)
menubar.add_command(label="Quit", command=win.destroy)
win.config(menu=menubar)
win.mainloop()