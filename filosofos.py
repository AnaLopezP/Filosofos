import random
import threading
import time

class Filosofo(threading.Thread):
    def __init__(self, num, tenedor):
        threading.Thread.__init__(self)
        self.tenedor = tenedor
        self.num = num
        self.temp = self.num + 1%5