import tkinter as tk
win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("400x300")                                 
text=tk.Text(win, bg="#00ffff", fg="blue", width=30, height=10)
text.config(padx=5, pady=5, font="Helvetic 12 bold italic")
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
win.mainloop()