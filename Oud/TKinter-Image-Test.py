import tkinter
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=160, height=160)
canvas.pack()
mijnafbeelding = PhotoImage(file='D:\Python\Basis\Img\ds6.gif')
canvas.create_image(82.5, 82.5, anchor=CENTER, image=mijnafbeelding)
tkinter.mainloop()