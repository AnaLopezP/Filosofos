
import time
import random
import threading
from tkinter import *
from tkinter import scrolledtext as sc

N = 5
TIEMPO_TOTAL = 3

class filosofo(threading.Thread):
    semaforo = threading.Lock() #SEMAFORO BINARIO ASEGURA LA EXCLUSION MUTUA
    estado = [] #PARA CONOCER EL ESTADO DE CADA FILOSOFO
    tenedores = [] #ARRAY DE SEMAFOROS PARA SINCRONIZAR ENTRE FILOSOFOS, MUESTRA QUIEN ESTA EN COLA DEL TENEDOR
    count=0
    

    def __init__(self):
        super().__init__()      #HERENCIA
        self.id=filosofo.count #DESIGNA EL ID AL FILOSOFO
        filosofo.count+=1 #AGREGA UNO A LA CANT DE FILOSOFOS
        filosofo.estado.append('PENSANDO') #EL FILOSOFO ENTRA A LA MESA EN ESTADO PENSANDO
        filosofo.tenedores.append(threading.Semaphore(0)) #AGREGA EL SEMAFORO DE SU TENEDOR( TENEDOR A LA IZQUIERDA)
        print("FILOSOFO {0} - PENSANDO".format(self.id))
        
    def __del__(self):
        print("FILOSOFO {0} - Se para de la mesa".format(self.id))  #NECESARIO PARA SABER CUANDO TERMINA EL THREAD
        

    def pensar(self):
        time.sleep(random.randint(0,5)) #CADA FILOSOFO SE TOMA DISTINTO TIEMPO PARA PENSAR, ALEATORIO

    def derecha(self,i):
        return (i-1)%N #BUSCAMOS EL INDICE DE LA DERECHA

    def izquierda(self,i):
        return(i+1)%N #BUSCAMOS EL INDICE DE LA IZQUIERDA

    def verificar(self,i):
        if filosofo.estado[i] == 'HAMBRIENTO' and filosofo.estado[self.izquierda(i)] != 'COMIENDO' and filosofo.estado[self.derecha(i)] != 'COMIENDO':
            filosofo.estado[i]='COMIENDO'
            filosofo.tenedores[i].release()  #SI SUS VECINOS NO ESTAN COMIENDO AUMENTA EL SEMAFORO DEL TENEDOR Y CAMBIA SU ESTADO A COMIENDO
        
    def tomar(self):
        filosofo.semaforo.acquire() #SEÑALA QUE TOMARA LOS TENEDORES (EXCLUSION MUTUA)
        filosofo.estado[self.id] = 'HAMBRIENTO'
        self.verificar(self.id) #VERIFICA SUS VECINOS, SI NO PUEDE COMER NO SE BLOQUEARA EN EL SIGUIENTE ACQUIRE
        filosofo.semaforo.release() #SEÑALA QUE YA DEJO DE INTENTAR TOMAR LOS TENEDORES (CAMBIAR EL ARRAY ESTADO)
        filosofo.tenedores[self.id].acquire() #SOLO SI PODIA TOMARLOS SE BLOQUEARA CON ESTADO COMIENDO

    def soltar(self):
        filosofo.semaforo.acquire() #SEÑALA QUE SOLTARA LOS TENEDORES
        filosofo.estado[self.id] = 'PENSANDO'
        #cambiar_color(self.id, "white")
        self.verificar(self.izquierda(self.id))
        self.verificar(self.derecha(self.id))
        filosofo.semaforo.release() #YA TERMINO DE MANIPULAR TENEDORES

    def comer(self):
        print("FILOSOFO {} COMIENDO".format(self.id))
        #cambiar_color(self.id, "yellow")
        time.sleep(2) #TIEMPO ARBITRARIO PARA COMER
        print("FILOSOFO {} TERMINO DE COMER".format(self.id))

    def run(self):
        for i in range(TIEMPO_TOTAL):
            self.pensar() #EL FILOSOFO PIENSA
            self.tomar() #AGARRA LOS TENEDORES CORRESPONDIENTES
            self.comer() #COME
            self.soltar() #SUELTA LOS TENEDORES

def main():
    
    lista=[]
    for i in range(N):
        lista.append(filosofo()) #AGREGA UN FILOSOFO A LA LISTA

    for f in lista:
        f.start() #ES EQUIVALENTE A RUN()


    


def cerrar_ventana():
    root.destroy()
    

def crear_texto(ventana, texto, color, poscol, posfil):
    a = Label(ventana, text = texto, bg = color)
    a.place(x = poscol, y = posfil)
    a.config(font= ("Verdana", 16))
    return a

def rectangulo(y, color):
    jj = Canvas(width= 50, height= 25, background="white")
    jj.place(x = 500, y = y)
    jj.create_rectangle(0, 0, 50, 25, fill = color)
    return jj



root = Tk()
root.geometry("800x600+560+240")
'''frame = Frame(root)
frame.place(x=100, y=50)'''
fil1 = crear_texto(root, "Filosofo1", "white", 150, 20)
fil2 = crear_texto(root, "Filosofo2", "white", 250, 80)
fil3 = crear_texto(root, "Filosofo3", "white", 250, 160)
fil4 = crear_texto(root, "Filosofo4", "white", 100, 160)
fil5 = crear_texto(root, "Filosofo5", "white", 50, 80)
ten1 = crear_texto(root, "1", "gray", 300, 30)
ten2 = crear_texto(root, "2", "gray", 300, 120)
ten3 = crear_texto(root, "3", "gray", 210, 160)
ten4 = crear_texto(root, "4", "gray", 100, 120)
ten5 = crear_texto(root, "5", "gray", 100, 30)

a = rectangulo(20, "blue")
b = rectangulo(50, "pink")
c = rectangulo(80, "green")
d = rectangulo(110, "yellow")
e = rectangulo(140, "white")
f = rectangulo(170, "gray")

scroll = sc.ScrolledText(root, width = 50, height = 15)
scroll.place(x = 10, y = 300)
reg = Label(root, text = "Cuántas veces come cada uno")
reg.place(x = 500, y =300)
f1 = Label(root, text= "Filósofo 1").place(x = 500, y = 330)
f2 = Label(root, text= "Filósofo 2").place(x = 500, y = 360)
f3 = Label(root, text= "Filósofo 3").place(x = 500, y = 390)
f4 = Label(root, text= "Filósofo 4").place(x = 500, y = 420)
f5 = Label(root, text= "Filósofo 5").place(x = 500, y = 450)

e1 = Entry(root).place(x = 600, y = 330)
e2 = Entry(root).place(x = 600, y = 360)
e3 = Entry(root).place(x = 600, y = 390)
e4 = Entry(root).place(x = 600, y = 420)
e5 = Entry(root).place(x = 600, y = 450)

'''frame2 = Frame(root)
frame2.place(x = 100, y = 100)'''
iniciar = Button(root, text= "INICIAR", command= main)
iniciar.place(x = 150, y = 250)
iniciar.config(font= ("Verdana", 12))


finalizar = Button(root, text= "SALIR", command= cerrar_ventana)
finalizar.place(x = 300,  y = 250)
finalizar.config(font= ("Verdana", 12))

texa = Label(root, text= "Tenedor ocupado").place(x = 555, y = 20)
texb = Label(root, text= "Filósofo entra").place(x = 555, y = 50)
texc = Label(root, text= "Filósofo con 1 tenedor").place(x = 555, y = 80)
texd = Label(root, text= "Filósofo comiendo").place(x = 555, y = 110)
texe = Label(root, text= "Filósofo pensando").place(x = 555, y = 140)
texf = Label(root, text= "Tenedor libre").place(x = 555, y = 170)

root.mainloop()





