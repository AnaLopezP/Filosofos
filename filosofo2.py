
import time
import random
import threading
from tkinter import *
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
        self.verificar(self.izquierda(self.id))
        self.verificar(self.derecha(self.id))
        filosofo.semaforo.release() #YA TERMINO DE MANIPULAR TENEDORES

    def comer(self):
        print("FILOSOFO {} COMIENDO".format(self.id))
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

    for f in lista:
        f.join() #BLOQUEA HASTA QUE TERMINA EL THREAD
    




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

log = Entry(frame, width= 100)
log.grid(column= 4, row = 3)
log.insert(index = 1, string= "Aqui tiene que poner lo que haya en el terminal")

iniciar = Button(frame, text= "INICIAR", command= main)
iniciar.grid(column= 2, row=7)

finalizar = Button(frame, text= "SALIR", command= root.destroy)
finalizar.grid(column= 4, row=7)

root.mainloop()

'''def cambiar_color(fil, color):
    Canvas.itemconfigure(fil, fill = color)'''

'''def hola():
    for i in filosofo.estado:
        if filosofo.estado[i] == 'PENSANDO':
            '''


'''if __name__=="__main__":
    main()'''