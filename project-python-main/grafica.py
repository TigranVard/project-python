from tkinter import *

root = Tk("Моя программа")
frame = Frame(root,padx=10,pady=10)
frame.grid()
Label(frame,text="Привет Боб!").grid(column=0,row=0)

button = Button(frame,text="dada",activebackground="red",
foreground="blue",width=10,height=3)
button.grid(column=0,row=2)

root.mainloop()
