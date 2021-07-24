import tkinter as tk
from tkinter import ttk

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("400x200")                                
label1=ttk.Label(win, text="relief='flat'", relief="flat")
label1.pack()
label2=ttk.Label(win, text="relief='sunken'", relief="sunken")
label2.pack()
label3=ttk.Label(win, text="relief='groove'", relief="groove")
label3.pack()
label4=ttk.Label(win, text="relief='raised'", relief="raised")
label4.pack()
label5=ttk.Label(win, text="relief='ridge'", relief="ridge")
label5.pack()
label6=ttk.Label(win, text="relief='solid'", relief="solid")
label6.pack()

win.mainloop()