from collections import deque
import time


class Memoria:
    """
    Clase que simula el espacio de memoria para trabajar con procesos.
    
    Attributes:
        _espacio (int): El límite de espacio de memoria.
        _cola_de_listos (deque): La cola de procesos listos en memoria.
        _cola_de_ejecucion (deque): La cola de procesos en ejecución en memoria.
        _cola_de_bloqueados (deque): La cola de procesos bloqueados en memoria.
    """

    def __init__(self, tamanio):
        self._espacio = tamanio
        self._cola_de_listos = deque()
        self._cola_de_ejecucion = deque()
        self._cola_de_bloqueados = deque()

    @property
    def espacio(self):
        return self._espacio

    @property
    def cola_de_listos(self):
        return self._cola_de_listos

    @property
    def cola_de_ejecucion(self):
        return self._cola_de_ejecucion

    @property
    def cola_de_bloqueados(self):
        return self._cola_de_bloqueados

    def procesos_en_memoria(self):
        if len(self._cola_de_listos) > 0 or len(self._cola_de_ejecucion) > 0 or len(self._cola_de_bloqueados) > 0:
            return True
        return False

    def procesos_en_listos(self) -> bool:
        return len(self._cola_de_listos) > 0

    def hay_espacio(self) -> bool:
        return bool(self._espacio)

    def _agrega_a_cola(self, cola, proceso):
        """
        Agrega un proceso a una cola específica.

        Args:
            cola (deque): La cola a la que se va a agregar el proceso.
            proceso: El proceso a agregar.

        Returns:
            bool: True si se pudo agregar el proceso a la cola, False de lo contrario.
        
        Raises:
            ValueError: Si se intenta agregar un proceso None a la cola.
        """
        if proceso is None:
            print("Proceso es Nulo")
            raise ValueError("Cannot add None process to the queue.")
        if self.hay_espacio():
            cola.append(proceso)
            self._espacio -= 1
            return True
        return False

    def _saca_de_cola(self, cola):
        """
        Saca un proceso de una cola específica.

        Args:
            cola (deque): La cola de la que se va a sacar el proceso.

        Returns:
            El proceso que se sacó de la cola, o None si la cola está vacía.
        """
        if len(cola) > 0:
            self._espacio += 1
            return cola.popleft()
        return None

    def get_proceso_en_ejecucion(self):
        """
        Devuelve el proceso que se encuentra en ejecución.

        Returns:
            El proceso que se encuentra en ejecución, o None si no hay ningún proceso en ejecución.
        """
        if self._cola_de_ejecucion:
            return self._cola_de_ejecucion[0]
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

    def entra_proceso_ejecucion(self):
        """
        Intenta mover un proceso de la cola de procesos listos a la cola de procesos en ejecución.

        Returns:
            Proceso: Proceso si se pudo mover de la cola de listos a la cola de ejecución,
            regresa el mismo proceso en ejecución.
            None de lo contrario.
        """
        # Si la cola de ejecucion esta vacia y la de listos aun tiene procesos:
        if not self._cola_de_ejecucion and self.cola_de_listos:
            proceso = self.saca_de_listo()
            self.agrega_a_ejecucion(proceso)
            return proceso
        if self._cola_de_ejecucion:  # Si la cola de ejecucion no esta vacia, regresa su proceso
            return self._cola_de_ejecucion[0]
        elif self._cola_de_bloqueados:
            return self._cola_de_bloqueados[0]
        else:
            return None

    def ciclo_bloqueados(self):
        """
        Realiza un ciclo de bloqueados, reduciendo el tiempo bloqueado de los procesos y moviéndolos de vuelta a la
        cola de procesos listos cuando su tiempo bloqueado se agota.
        """
        bloqueados_copia = deque(self._cola_de_bloqueados)
        for proceso in bloqueados_copia:
            if proceso.esta_bloqueado():
                proceso.tiempo_bloqueado()  # quita 1 segundo a tiempo bloqueado
            else:
                self.saca_de_bloqueado()
                self.agrega_a_listo(proceso)
