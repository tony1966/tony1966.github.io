import tkinter as tk

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("300x150")
button1=tk.Button(win, text="12345", width=10, bg="cyan")
#button1.config(activebackground="yellow", activeforeground="blue")
#button1.config(highlightcolor="green", highlightbackground="ivory")
button1.pack()
button2=tk.Button(win)
button2["text"]="abcde"
button2["background"]="ivory"
button2["padx"]=10
button2["pady"]=10
button2["relief"]=tk.SOLID
button2.pack()
button3=tk.Button(win, )
button3.config(width=6, fg="blue", relief="ridge")
button3.configure(text="你在說哈囉嗎")
button3.pack()
win.mainloop()

