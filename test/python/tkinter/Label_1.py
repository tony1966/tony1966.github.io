import tkinter as tk
from tkinter import ttk

win=tk.Tk()    
tk_label=tk.Label(win, text="Hello World!", bg="ivory")
tk_label.pack()
ttk_label=ttk.Label(win, text="你是在說哈囉嗎?", background="aqua")
ttk_label.pack()
print(tk_label.keys())
print(ttk_label.keys())
win.mainloop()