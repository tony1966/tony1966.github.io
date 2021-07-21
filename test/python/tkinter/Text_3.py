import tkinter as tk
from tkinter import ttk
win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("400x300")                                 
text=tk.Text(win, width=30, height=10, bg="aqua")
text.config(padx=5, pady=5, font="Helvetic 12")
text.insert(tk.INSERT, "Hello World!\n")
text.insert(tk.INSERT, "width=" + str(text["width"]) + "\n")             
text.insert(tk.INSERT, "height=" + str(text["height"]) + "\n")
text.insert(tk.INSERT, "font=" + str(text["font"]) + "\n")
text.insert(tk.INSERT, "padx=" + str(text["padx"]) + "\n")
text.insert(tk.INSERT, "pady=" + str(text["pady"]) + "\n")
text.insert(tk.INSERT, "bg=" + str(text["bg"]) + "\n")
text.insert(tk.INSERT, "fg=" + str(text["fg"]) + "\n")
text.insert(tk.END, "你是在說哈囉嗎?")
text.pack()

def delete_all():
    text.delete(1.0, "end")

def delete_row_1():
    text.delete(1.0, 2.0)
    
btn1=ttk.Button(win, text="刪除全部", command=delete_all)
btn1.pack(side=tk.LEFT)
btn2=ttk.Button(win, text="刪除第一列", command=delete_row_1)
btn2.pack(side=tk.LEFT)
win.mainloop()