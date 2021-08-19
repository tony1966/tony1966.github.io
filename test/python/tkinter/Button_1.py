import tkinter as tk

def click_count():
    var.set(var.get() + 1)

win=tk.Tk()
win.geometry("300x150") 
var=tk.IntVar()
var.set(0)
label=tk.Label(win, textvariable=var)
label.pack()
button_1=tk.Button(text="增量", command=click_count)
button_1.pack()
button_2=tk.Button(text="歸零", command=lambda: var.set(0))
button_2.pack()
win.mainloop()