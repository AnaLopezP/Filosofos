import random
import threading
import time

class Filosofo(threading.Thread):
    def __init__(self, num, tenedor):
        threading.Thread.__init__(self) #Creamos un hilo
        self.tenedor = tenedor
        self.num = num #Número de filósofo
        self.temp = self.num + 1%5

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
