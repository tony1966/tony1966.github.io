import tkinter as tk
from tkinter import messagebox as msgbox

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x200")

def new_file():
    msgbox.showinfo("Info", "開新檔案")
    
def old_file():
    msgbox.showinfo("Info", "開啟舊檔")    

def save_file():
    msgbox.showinfo("Info", "儲存檔案")

def about():
    msgbox.showinfo("Info", "這是 tkinter 測試")

def version():
    msgbox.showinfo("Info", "v 1.0.0")

menubar=tk.Menu(win)
file_menu=tk.Menu(menubar, tearoff=False)
file_menu.add_command(label="開新檔案", command=new_file)
file_menu.add_command(label="開啟舊檔", command=old_file)
file_menu.add_command(label="儲存檔案", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="關閉", command=win.destroy)
menubar.add_cascade(label="檔案", menu=file_menu)
help_menu=tk.Menu(menubar, tearoff=False)
help_menu.add_command(label="版本", command=version)
help_menu.add_command(label="關於", command=about)
menubar.add_cascade(label="幫助", menu=help_menu)
win.config(menu=menubar)
win.mainloop()