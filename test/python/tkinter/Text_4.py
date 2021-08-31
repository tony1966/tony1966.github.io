import tkinter as tk
from tkinter import ttk
win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("400x300")                                 
text=tk.Text(win, width=30, height=10, bg="aqua")
text.config(padx=5, pady=5, font="Helvetic 12")
text.insert(tk.INSERT, "Hello World!\n")
text.pack()

def disable_widget():
    text.config(state=tk.DISABLED, bg='gray', fg='yellow')   

def normal_widget():
    text.config(state=tk.NORMAL, bg='aqua', fg='black')       
    
btn1=ttk.Button(win, text="Disabled", command=disable_widget)
btn1.pack(side=tk.LEFT)
btn2=ttk.Button(win, text="Normal", command=normal_widget)
btn2.pack(side=tk.LEFT)
win.mainloop()