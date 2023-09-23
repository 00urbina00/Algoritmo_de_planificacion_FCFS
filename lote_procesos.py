from proceso import Proceso
from collections import deque


class Memoria:
    def __init__(self, num_lote):
        self.__procesos = deque()

    def agregar_proceso(self, proceso) -> bool:
        if len(self.__procesos) < 4:
            self.__procesos.append(proceso)
            return True
        return False

    def isvoid(self) -> bool:
        return not self.__procesos

    def saca_proceso(self):
        if self.isvoid():
            return None
        else:
            return self.__procesos.popleft()

    def get_procesos(self):
        return self.__procesos
