from tkinter import *

def rectangulo(y, color):
    jj = Canvas(width= 50, height= 25, background="white")
    jj.place(x = 200, y = y)
    jj.create_rectangle(0, 0, 50, 25, fill = color)
    return jj



root = Tk()
root.geometry("800x600+560+240")
frame= Frame(root)


dsd = Button(text = "odjshfjjs")
dsd.grid(column=3, row= 3)


a = rectangulo(20, "blue")
b = rectangulo(50, "pink")
c = rectangulo(80, "green")
d = rectangulo(110, "yellow")
e = rectangulo(140, "white")
f = rectangulo(170, "gray")


root.mainloop()



