from tkinter import *

root = Tk("��� ���������")
root.geometry("500x300")
root.resizable(width=True,height=False)
root["bg"] = "#9117b0"

frame = Frame(root,padx=100,pady=10)
frame.grid()
Label(frame, text="������ ���!")
Label(frame, text="Hello world!")

button = Button(frame, text="��� ������ ������",background="#b34b4b",foreground="#ffffff",width=10,height=3,wraplenghtt=100)
button.grid(column=0,row=2)

root.mainloop()