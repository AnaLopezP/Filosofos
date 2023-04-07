import random
import threading
import time

class Filosofo(threading.Thread):
    def __init__(self, num, tenedor):
        threading.Thread.__init__(self) #Creamos un hilo
        self.tenedor = tenedor
        self.num = num #Número de filósofo
        #self.temp = self.num + 1%5

    def comer(self):
        print("El filósofo " + str(self.num) + " come.")
    
    def pensar(self):
        print("El filósofo " + str(self.num) + " piensa.")

    def tenedorIzq(self):
        print("El filósofo " + str(self.num) + " obtiene el tenedor izquierdo.")
        self.tenedor[self.num].acquire() #Adquirimos un lock cerrado, bloqueando el hilo (tenedor).

    def tenedorDcha(self):
        print("El filósofo " + str(self.num) + " obtiene el tenedor derecho.")
        self.tenedor[self.num].acquire() #Lo mismo que con el izquierdo.

    def liberarIzq(self):
        print("El filósofo " + str(self.num) + " libera el tenedor izquierdo.")
        self.tenedor[self.num].release() #Liberamos el hilo (tenedor), es decir, abrimos el lock.

    def liberarDcho(self):
        print("El filósofo " + str(self.num) + " libera el tenedor derecho.")
        self.tenedor[self.num].release()

    def run(self): #función de acción del hilo
        while True:
            self.pensar()
            self.tenedorIzq()
            self.tenedorDcha()
            self.comer()
            self.liberarIzq()
            self.liberarDcho()

#CODIGO PRINCIPAL
Nfil = 5
tenedor = [1, 1, 1, 1, 1]

for i in range(0, 4):
    tenedor[i] = threading.BoundedSemaphore(1) #Creamos un semáforo para cada tenedor

for i in range(0, 4):
    Filosofo(i, tenedor).start()
    time.sleep(0.5)