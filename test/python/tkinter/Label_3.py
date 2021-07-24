import tkinter as tk

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("400x200")                                
label1=tk.Label(win, text="relief='flat'", relief="flat")
label1.pack()
label2=tk.Label(win, text="relief='sunken'", relief="sunken")
label2.pack()
label3=tk.Label(win, text="relief='groove'", relief="groove")
label3.pack()
label4=tk.Label(win, text="relief='raised'", relief="raised")
label4.pack()
label5=tk.Label(win, text="relief='ridge'", relief="ridge")
label5.pack()
label5=tk.Label(win, text="relief='solid'", relief="solid")
label5.pack()

win.mainloop()