from tkinter import *

root = Tk("Моя программа")
root.geometry("500x300")
root.resizable(width=True,height=False)
root["bg"] = "#9117b0"
root.grid

frame = Frame(root,padx=100,pady=10,width=200,height=200)
frame.place(anchor="center", relx=0.5, rely=0.5)
frame.grid()
Button(frame,text="кнопочка в фрейм1",fg="white",bg="green",width=10,height=10,wraplenght=100).pack()

frame2 = Frame(root,padx=100,pady=10,width=200,height=200)
frame2["bg"] = "red"
frame2.grid()

frame = Frame(root,padx=100,pady=10,width=200,height=200)
frame.place(anchor="center", relx=0.1, rely=0.3)
frame2["bg"] = "orange"
frame.grid()

root.mainloop()