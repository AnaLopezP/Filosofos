from tkinter import *


def crear_texto(ventana, texto, color, poscol, posfil):
    a = Label(ventana, text = texto, bg = color).grid(column= poscol, row = posfil)
    return a

root = Tk()
frame = Frame(root)
frame.grid(column=60, row=40)
fil1 = crear_texto(frame, "Filosofo1", "white", 2, 2)
fil2 = crear_texto(frame, "Filosofo2", "white", 3, 3)
fil3 = crear_texto(frame, "Filosofo3", "white", 3, 5)
fil4 = crear_texto(frame, "Filosofo4", "white", 1, 5)
fil5 = crear_texto(frame, "Filosofo5", "white", 1, 3)
ten1 = crear_texto(frame, "1", "gray", 1, 2)
ten2 = crear_texto(frame, "2", "gray", 3, 2)
ten3 = crear_texto(frame, "3", "gray", 3, 4)
ten4 = crear_texto(frame, "4", "gray", 2, 5)
ten5 = crear_texto(frame, "5", "gray", 1, 4)

entry = Entry(frame)
entry.grid(column=4, row= 4)
entry.insert(index= 1, string = "fjdoifju")

root.mainloop()


