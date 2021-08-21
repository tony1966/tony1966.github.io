import tkinter as tk
from tkinter import ttk

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("300x150")
button1=ttk.Button(win, text="12345", width=10)
print(button1.keys())
button1.pack()
button2=ttk.Button(win)
button2["text"]="abcde"
#button2["background"]="ivory" #TclError: unknown option "-background"
button2["padding"]=[10, 10, 10, 10]
# button2["relief"]=tk.SOLID  #TclError: unknown option "-relief"
button2.pack()
button3=ttk.Button(win)
button3.config(width=6)
#button3.config(foreground="blue") #TclError: unknown option "-foreground"
#button3.config(relief="ridge") #TclError: unknown option "-relief"
button3.configure(text="你在說哈囉嗎")
button3.pack()
win.mainloop()

