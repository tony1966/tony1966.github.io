import tkinter as tk
from tkinter import ttk

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("400x250")
# tk
tk_label1=tk.Label(win, text="relief='flat'", relief="flat")
tk_label1.config(bd=3, padx=5, pady=5)
tk_label1.grid(row=0, column=0)
tk_label2=tk.Label(win, text="relief='sunken'", relief="sunken")
tk_label2.config(bd=3, padx=5, pady=5)
tk_label2.grid(row=1, column=0)
tk_label3=tk.Label(win, text="relief='groove'", relief="groove")
tk_label3.config(bd=3, padx=5, pady=5)
tk_label3.grid(row=2, column=0)
tk_label4=tk.Label(win, text="relief='raised'", relief="raised")
tk_label4.config(bd=3, padx=5, pady=5)
tk_label4.grid(row=3, column=0)
tk_label5=tk.Label(win, text="relief='ridge'", relief="ridge")
tk_label5.config(bd=3, padx=5, pady=5)
tk_label5.grid(row=4, column=0)
tk_label6=tk.Label(win, text="relief='solid'", relief="solid")
tk_label6.config(bd=3, padx=5, pady=5)
tk_label6.grid(row=5, column=0)
# ttk
ttk_label1=ttk.Label(win, text="relief='flat'", relief="flat")
ttk_label1.config(borderwidth=3, padding=[5, 5, 5, 5])
ttk_label1.grid(row=0, column=1)
ttk_label2=ttk.Label(win, text="relief='sunken'", relief="sunken")
ttk_label2.config(borderwidth=3, padding=[5, 5, 5, 5])
ttk_label2.grid(row=1, column=1)
ttk_label3=ttk.Label(win, text="relief='groove'", relief="groove")
ttk_label3.config(borderwidth=3, padding=[5, 5, 5, 5])
ttk_label3.grid(row=2, column=1)
ttk_label4=ttk.Label(win, text="relief='raised'", relief="raised")
ttk_label4.config(borderwidth=3, padding=[5, 5, 5, 5])
ttk_label4.grid(row=3, column=1)
ttk_label5=ttk.Label(win, text="relief='ridge'", relief="ridge")
ttk_label5.config(borderwidth=3, padding=[5, 5, 5, 5])
ttk_label5.grid(row=4, column=1)
ttk_label6=ttk.Label(win, text="relief='solid'", relief="solid")
ttk_label6.config(borderwidth=3, padding=(5, 5, 5, 5))
ttk_label6.grid(row=5, column=1)

win.mainloop()