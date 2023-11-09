from collections import deque
from math import ceil
TAM_SO = 4


def crea_marco(proceso, unidades):
    marco = []
    for i in range(unidades):
        if len(marco)<5:
            marco.append(proceso.id)
    return marco


class Memoria:  # Tamanio memoria es 220
    def __init__(self, unidades, tamanio_marco):
        self._cola_de_listos = deque()
        self._cola_de_ejecucion = deque()
        self._cola_de_bloqueados = deque()
        self._ESPACIO_MAXIMO = unidades
        self._espacio_disponible = unidades
        self._paginas_disponibles = ceil(unidades / tamanio_marco)
        self._espacio_de_memoria = [None] * ceil(unidades / tamanio_marco) # 44 páginas de 5 Megabytes cada una
        self._tamanio_marco = tamanio_marco
        self.inicializa_so(TAM_SO)

    # Propiedades (decoradores) ----------------------------------------------------------------
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
    def espacio_de_memoria(self):
        return self._espacio_de_memoria

    def procesos_en_memoria(self):
        if len(self._cola_de_listos) > 0 or len(self._cola_de_ejecucion) > 0 or len(self._cola_de_bloqueados) > 0:
            return True
        return False
    # Métodos agregacion/eliminacion ------------------------------------------------------------

    def imprimir_estructura_de_memoria(self):
        for i, pagina in enumerate(self._espacio_de_memoria):
            print(f"Página {i}:")
            if pagina is None:
                print("  - Vacía")
            else:
                for j, marco in enumerate(pagina):
                    print(f"  Marco {j}: {marco}")

    def inicializa_so(self, tamanio_so):
        # Inicializa el sistema operativo en la memoria
        # Memoria = [Marco[SO], Marco[SO], Marco[SO], Marco[SO], None, None, ...]
        for i in range(tamanio_so):
            marco = ["SO"] * 5 # macor = [SO, SO, SO, SO, SO]
            self._espacio_de_memoria[i] = marco
            self._espacio_disponible -= 5
            self._paginas_disponibles -= 1
        # self.imprimir_estructura_de_memoria()

    def encuentra_marcos_libres(self):
        marcos_libres = []
        for i, marco in enumerate(self._espacio_de_memoria):
            if marco is None:
                marcos_libres.append(i)
        return marcos_libres

    def _agrega_a_cola(self, cola, proceso):
        if proceso is None:
            raise ValueError("Cannot add None process to the queue.")
        if self.hay_espacio(proceso.tamanio):   # Se calcula si hay suficientes páginas para el proceso
            paginas_necesarias = ceil(proceso.tamanio / self._tamanio_marco)
            contador_unidades = proceso.tamanio
            marcos = []
            self._espacio_disponible -= proceso.tamanio
            # Creacion de marcos
            for i in range(paginas_necesarias):
                if contador_unidades > self._tamanio_marco:
                    marco = crea_marco(proceso, self._tamanio_marco)
                    marcos.append(marco)
                    contador_unidades -= self._tamanio_marco
                else:
                    marco = crea_marco(proceso, contador_unidades)
                    marcos.append(marco)

            libres = self.encuentra_marcos_libres()
            # Asignacion de marcos a memoria
            for marco in marcos:
                if self._espacio_de_memoria[libres[0]] is None:
                    self._espacio_de_memoria[libres[0]] = marco
                    self._paginas_disponibles -= 1
                    libres.pop(0)
            cola.append(proceso)
            # self.imprimir_estructura_de_memoria()
            return True
        return False
    def liberar_espacio_de_proceso(self, proceso):
        for i, marco in enumerate(self._espacio_de_memoria):
            if marco is not None and marco[0] == proceso.id:
                self._espacio_de_memoria[i] = None
                self._paginas_disponibles += 1
        self._espacio_disponible += proceso.tamanio
    def _saca_de_cola(self, cola):
        if len(cola) > 0: # Si la cola no esta vacia
            proceso = cola.popleft()
            self.liberar_espacio_de_proceso(proceso)
            return proceso
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
    # Otros -------------------------------------------------------------------------------------
    def entra_proceso_ejecucion(self):
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
