import tkinter as tk
from tkinter import ttk

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("400x200")                                
label1=tk.Label(win, text="Hello World")
label1.pack()
label2=tk.Label(win, text="你是在說哈囉嗎?", underline=3)
label2.pack()
label3=tk.Label(win, text="洪車瑛(全汝斌)", padx=5, pady=5, relief="solid")
label3.pack()
label4=tk.Label(win, text="文森佐(宋仲基)", bg="aqua", fg="blue")
label4.pack()
label5=tk.Label(win, text="黑道律師文森佐", font="微軟正黑體 16 bold")
label5.config(bd=3, relief="solid")
label5.pack()
win.mainloop()
