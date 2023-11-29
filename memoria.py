from collections import deque
from math import ceil
from marco import *

"""
Clase llamada Memoria que representa un sistema de memoria. Tiene métodos para agregar procesos a diferentes colas, asignar y liberar espacio de memoria para procesos y realizar diversas operaciones en la memoria.
Uso de ejemplo
memoria = Memoria(220, 5) # Crea un sistema de memoria con 220 unidades y tamaño de fotograma de 5
proceso1 = Proceso(1, 10) # Crea un proceso con ID 1 y tamaño 10
proceso2 = Proceso(2, 15) # Crea un proceso con ID 2 y tamaño 15

memoria.agrega_a_listo(proceso1) # Agregar proceso1 a la cola listo
memoria.agrega_a_listo(proceso2) # Agregar proceso2 a la cola listo

proceso_en_ejecucion = memoria.entra_proceso_ejecucion() # Obtener el proceso de la cola de ejecución

memoria.imprimir_estructura_de_memoria() # Imprime la estructura de la memoria

memoria.release() # Libera toda la memoria y borra las colas

Análisis de código

Principales funcionalidades
Agregar procesos a diferentes colas (listo, en ejecución, bloqueado)
Asignar y liberar espacio de memoria para procesos.
Comprobar si hay suficiente espacio en la memoria para un proceso
Comprobar si hay procesos en las colas
Obtener el proceso actual en ejecución
 
Métodos
__init__(self, unidades, tamanio_marco): Inicializa el sistema de memoria con el número de unidades y tamaño de cuadro dado.
agrega_a_listo(self, proceso): Agrega un proceso a la cola de listos.
agrega_a_ejecucion(self, proceso): Agrega un proceso a la cola de ejecución.
agrega_a_bloqueados(self, proceso): Agrega un proceso a la cola bloqueada.
saca_de_listo(self): Elimina un proceso de la cola listo.
saca_de_ejecucion(self): Elimina un proceso de la cola de ejecución.
saca_de_bloqueado(self): Elimina un proceso de la cola bloqueada.
liberación (auto): libera toda la memoria y borra las colas.
hay_espacio(self, unidades): Comprueba si hay suficiente espacio en memoria para un proceso con el número de unidades dado.
hay_bloqueados(self): Comprueba si hay procesos en la cola bloqueada.
hay_ejecucion(self): Comprueba si hay procesos en la cola de ejecución.
hay_listos(self): Comprueba si hay procesos en la cola listos.
get_proceso_en_ejecucion(self): Obtiene el proceso actual en ejecución.
 
Campos
_cola_de_listos: Cola para almacenar procesos en estado listo.
_cola_de_ejecucion: Cola para almacenar procesos en estado de ejecución.
_cola_de_bloqueados: Cola para almacenar procesos en estado bloqueado.
_ESPACIO_MAXIMO: Espacio máximo de memoria en unidades.
_espacio_disponible: Espacio de memoria disponible en unidades.
_paginas_disponibles: Páginas de memoria disponibles.
_espacio_de_memoria: Estructura de la memoria representada como una lista de fotogramas.
_tamanio_marco: Tamaño de cada cuadro.
idx_marco: Índice actual de la memoria (fotogramas).
"""


class Memoria:  # Tamanio memoria es 220
    def __init__(self, unidades, tamanio_marco, tamanio_so):
        self._cola_de_listos = deque()  # Cola de procesos listos
        self._cola_de_ejecucion = deque()  # Cola de procesos en ejecucion
        self._cola_de_bloqueados = deque()  # Cola de procesos bloqueados
        self._ESPACIO_MAXIMO = unidades  # Espacio maximo de memoria (En unidades)
        self._espacio_disponible = unidades  # Espacio disponible de memoria (En unidades)
        self._paginas_disponibles = ceil(unidades / tamanio_marco)  # Páginas disponibles de memoria
        self._espacio_de_memoria = [None for _ in range(ceil(unidades / tamanio_marco))]  # 44 páginas de 5 cada una
        self._tamanio_marco = tamanio_marco  # Tamaño de cada marco
        self._idx_marco = 0
        self.inicializa_so(tamanio_so)  # Inicializa el tamaño del sistema operativo en la memoria
        self.ultimo_estado = ""

    # Propiedades (decoradores) ----------------------------------------------------------------
    @property
    def paginas_disponibles(self):
        return self._paginas_disponibles

    @property
    def cola_de_listos(self):
        return self._cola_de_listos

    @property
    def cola_de_ejecucion(self):
        return self._cola_de_ejecucion

    @property
    def cola_de_bloqueados(self):
        return self._cola_de_bloqueados

    @property
    def espacio_disponible(self):
        return self._espacio_disponible

    @property
    def paginas_disponibles(self):
        return self._paginas_disponibles

    @property
    def espacio_de_memoria(self):
        return self._espacio_de_memoria

    def procesos_en_memoria(self):
        if len(self._cola_de_listos) > 0 or len(self._cola_de_ejecucion) > 0 or len(self._cola_de_bloqueados) > 0:
            return True
        return False

    # Métodos agregacion/eliminacion ------------------------------------------------------------

    def imprimir_estructura_de_memoria(self):
        for i, marco in enumerate(self._espacio_de_memoria):
            if marco is not None:
                print(f"Marco {i}: {marco}")

    def inicializa_so(self, tamanio_so):
        # Inicializa el sistema operativo en la memoria
        # Memoria = [Marco[SO], Marco[SO], Marco[SO], Marco[SO], None, None, ...]
        if tamanio_so > self._paginas_disponibles:
            raise ValueError("No hay suficiente memoria para el sistema operativo.")
        for i in range(tamanio_so):
            marco = Marco(None, None, self._tamanio_marco)
            self._espacio_de_memoria[i] = marco
            self._espacio_disponible -= self._tamanio_marco
            self._paginas_disponibles -= 1
            self._idx_marco += 1
        # self.imprimir_estructura_de_memoria()

    def encuentra_marcos_libres(self):
        marcos_libres = []
        for i, marco in enumerate(self._espacio_de_memoria):
            if marco is None:
                marcos_libres.append(i)
        return marcos_libres

    def _agrega_a_cola(self, cola, proceso, asignar_memoria):
        if proceso is None:
            raise ValueError("No se puede agregar un proceso Nulo.")
        if not asignar_memoria:
            cola.append(proceso)
            return True
        if proceso is not None and self.hay_espacio(proceso.tamanio):  # Se calcula si hay suficientes páginas
            paginas_necesarias = ceil(proceso.tamanio / self._tamanio_marco)  # Se calcula el número de páginas
            contador_unidades = proceso.tamanio  # Contador de unidades para crear marcos
            marcos = []  # Lista de marcos
            self._espacio_disponible -= proceso.tamanio
            # Creacion de marcos
            for i in range(paginas_necesarias):
                if contador_unidades > self._tamanio_marco:
                    if proceso.indice_inicial is None:
                        proceso.set_indices(self._idx_marco, self._idx_marco + paginas_necesarias - 1)
                    marco = Marco(proceso, self._tamanio_marco)
                    marcos.append(marco)
                    contador_unidades -= self._tamanio_marco
                else:
                    marco = Marco(proceso, contador_unidades)
                    marcos.append(marco)

            libres = self.encuentra_marcos_libres()
            # Asignacion de marcos a memoria
            for marco in marcos:
                if self._espacio_de_memoria[libres[0]] is None:  # Si el espacio esta vacio
                    i = libres.pop(0)
                    self._espacio_de_memoria[i] = marco  # Se asigna el marco
                    self._paginas_disponibles -= 1
                    self._idx_marco += 1
            cola.append(proceso)
            # self.imprimir_estructura_de_memoria()
            return True
        elif proceso is not None:
            proceso.set_estado(self.ultimo_estado)  # Se regresa el proceso a su ultimo estado
        return False

    def liberar_espacio_de_proceso(self, proceso):
        matching_marcos = [i for i, marco in enumerate(self._espacio_de_memoria) if
                           marco is not None and proceso.id in marco.get_marco()]
        for i in matching_marcos:  # Se recorren los marcos del proceso y se liberan
            self._espacio_de_memoria[i].release()  # Se libera el marco (marco.release())
            self._espacio_de_memoria[i] = None
            self._paginas_disponibles += 1
            self._idx_marco -= 1
        self._espacio_disponible += proceso.tamanio

    def _saca_de_cola(self, cola, liberar_memoria):  # Modo delete libera la memoria asignada al proceso
        if len(cola) > 0:  # Si la cola no esta vacia
            proceso = cola.popleft()
            if liberar_memoria:
                self.liberar_espacio_de_proceso(proceso)
            return proceso
        return None

    def agrega_a_listo(self, proceso, asignar_memoria=False):
        if proceso is not None:
            self.ultimo_estado = proceso.get_estado()  # Guarda el ultimo estado del proceso
            proceso.set_estado("Listo")
        return self._agrega_a_cola(self._cola_de_listos, proceso, asignar_memoria)

    def agrega_a_ejecucion(self, proceso, asignar_memoria=False):
        if proceso is not None:
            self.ultimo_estado = proceso.get_estado()  # Guarda el ultimo estado del proceso
            proceso.set_estado("Ejecucion")
        return self._agrega_a_cola(self._cola_de_ejecucion, proceso, asignar_memoria)

    def agrega_a_bloqueados(self, proceso, asignar_memoria=False):
        if proceso is not None:
            self.ultimo_estado = proceso.get_estado()  # Guarda el ultimo estado del proceso
            proceso.set_estado("Bloqueado")
        return self._agrega_a_cola(self._cola_de_bloqueados, proceso, asignar_memoria)

    def saca_de_listo(self, liberar_memoria=False):
        return self._saca_de_cola(self._cola_de_listos, liberar_memoria)

    def saca_de_ejecucion(self, liberar_memoria=False):
        return self._saca_de_cola(self._cola_de_ejecucion, liberar_memoria)

    def saca_de_bloqueado(self, liberar_memoria=False):
        return self._saca_de_cola(self._cola_de_bloqueados, liberar_memoria)

    def release(self):  # Liberar memoria (spanglish :( )
        for proceso in self._cola_de_listos:
            self._espacio_disponible += proceso.tamanio
            self._paginas_disponibles += ceil(proceso.tamanio / self._tamanio_marco)
        for proceso in self._cola_de_ejecucion:
            self._espacio_disponible += proceso.tamanio
            self._paginas_disponibles += ceil(proceso.tamanio / self._tamanio_marco)
        for proceso in self._cola_de_bloqueados:
            self._espacio_disponible += proceso.tamanio
            self._paginas_disponibles += ceil(proceso.tamanio / self._tamanio_marco)
        self._cola_de_listos.clear()
        self._cola_de_ejecucion.clear()
        self._cola_de_bloqueados.clear()
        for i, marco in enumerate(self._espacio_de_memoria):
            if marco is not None:
                marco.release()
                self._espacio_de_memoria[i] = None

    # Metodos logicos ---------------------------------------------------------------------------
    def hay_espacio(self, unidades) -> bool:
        paginas = ceil(unidades / self._tamanio_marco)
        if paginas <= self._paginas_disponibles:
            return True
        return False

    def hay_bloqueados(self):
        return len(self._cola_de_bloqueados) > 0

    def hay_ejecucion(self):
        return len(self._cola_de_ejecucion) > 0

    def hay_listos(self):
        return len(self._cola_de_listos) > 0

    def get_proceso_en_ejecucion(self):
        if self._cola_de_ejecucion:
            return self._cola_de_ejecucion[0]
        return None

    def get_memoria_en_uso(self):
        return self._ESPACIO_MAXIMO - self._espacio_disponible

    # Otros -------------------------------------------------------------------------------------
    def entra_proceso_ejecucion(self):
        # Si no hay procesos en ejecución y hay procesos en listos, mueve el primero de listos a ejecución
        if not self._cola_de_ejecucion and self.cola_de_listos:
            proceso = self.saca_de_listo()  # Sacar proceso de listos (Sin liberar memoria)
            proceso.set_estado("Ejecucion")
            self.agrega_a_ejecucion(proceso)  # Mover proceso a ejecución (Sin asignar memoria)
            return proceso
        if self._cola_de_ejecucion:  # Si la cola de ejecución no está vacía, regresa su proceso
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
                self.saca_de_bloqueado()  # Sacar proceso de bloqueados (Sin liberar memoria)
                proceso.set_estado("Listo")
                self.agrega_a_listo(proceso)  # Mover proceso a listos (Sin liberar memoria)

    def busca_estado_proceso(self, id_proceso):
        for proceso in self._cola_de_listos:
            if proceso.id == id_proceso:
                return proceso.get_estado()
        for proceso in self._cola_de_ejecucion:
            if proceso.id == id_proceso:
                return proceso.get_estado()
        for proceso in self._cola_de_bloqueados:
            if proceso.id == id_proceso:
                return proceso.get_estado()
        return None
