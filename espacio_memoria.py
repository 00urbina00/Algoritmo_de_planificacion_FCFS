from collections import deque

class Memoria:
    """
    Clase que simula el espacio de memoria para trabajar.
    En este caso, pueden entrar "TAMANIO" de procesos, distribuidos
    en cualquier cola, teniendo la posibilidad de recorrer las transiciones
    del diagrama de 5 estados.
    """
    def __init__(self, tamanio):
        self._espacio = tamanio                # Limite de memoria
        self._cola_de_listos = deque()         # Cola de listos en memoria
        self._cola_de_ejecucion = deque()      # Cola de ejecucion en memoria
        self._cola_de_bloqueados = deque()     # Cola de bloqueados en memoria

    @property
    def cola_de_listos(self):
        copia_listos = list(self._cola_de_listos)
        return copia_listos
    @property
    def espacio(self):
        return self._espacio
    
    def hay_espacio(self) -> bool:
        return self._espacio > 0
    
    def _agrega_a_cola(self, cola, proceso):
        if proceso is not None and self.hay_espacio():
            cola.append(proceso)
            self._espacio -= 1
            return True
        return False
    def _saca_de_cola(self, cola):
        if len(cola) > 0:
            self._espacio += 1
            return cola.popleft()
        return None
    
    def agrega_a_listo(self, proceso):
        return self._agrega_a_cola(self._cola_de_listos, proceso)
    def agrega_a_ejecucion(self, proceso):
         return self._agrega_a_cola(self._cola_de_ejecucion, proceso)
    def agrega_a_bloqueados(self, proceso):
        return self._agrega_a_cola(self._cola_de_bloqueados, proceso)
    def saca_de_listo(self):
        return self._saca_de_cola(self._cola_de_listos)
    def saca_de_ejecucion(self):
        return self._saca_de_cola(self._cola_de_ejecucion) 
    def saca_de_bloqueado(self):
        return self._saca_de_cola(self._cola_de_bloqueados)
    def hay_bloqueados(self):
        return len(self._cola_de_bloqueados) > 0
    def ciclo_bloqueados(self):
        # Le descuenta 1 unidad de tiempo bloqueado a cada proceso
        bloqueados_copia = list(self._cola_de_bloqueados)
        for proceso in bloqueados_copia:
            if proceso.esta_bloqueado():        # Si el proceso esta bloqueado aun:
                proceso.tiempo_bloqueado()      # Se reduce el tiempo bloqueado en 1
                print("Restando tiempo bloqueado")
            else:
                print("Vuelve a listo el proceso")
                self.agrega_a_listo(proceso)    # Si el proceso ya termino el tb
                self.saca_de_bloqueado()        # Se agrega de nuevo a listos y sale de bloqueados
