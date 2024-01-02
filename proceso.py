import json
import os

TIEMPO_BLOQUEO = 8


class Proceso:
    def __init__(self, operador, operando_a, operando_b, tiempo, numero_proceso, tamanio=6) -> None:
        # Datos del proceso
        # ----------------------------------------
        self._id = numero_proceso
        self._tiempo_maximo_estimado = int(tiempo)
        self._operacion_realizar = operador
        self._operando_a = operando_a
        self._operando_b = operando_b
        self._tamanio = tamanio
        self._resultado = 0.0
        self._indice_inicial = None
        self._indice_final = None
        self.estado = 'Nuevo'
        self.prioridad = False
        # ----------------------------------------
        # Tiempos
        # ----------------------------------------
        self.timer_bloqueado = 0
        self._tiempo_transcurrido = 0
        self._tiempo_restante = int(tiempo)

        self.atendido = False

        self.tiempo_llegada = None
        self.tiempo_finalizacion = None
        self.tiempo_retorno = None
        self.tiempo_respuesta = None
        self.tiempo_espera = None
        self.tiempo_servicio = 0
        # ----------------------------------------
        # Estado / Otro
        # ----------------------------------------
        self._terminado = False
        self._error = False
        self._operations = {
            '+': self._operando_a + self._operando_b,
            '-': self._operando_a - self._operando_b,
            '*': self._operando_a * self._operando_b,
            '%': round(((self._operando_a / 100) * self._operando_b), 2),
            '%%': self._operando_a % self._operando_b if self._operando_b != 0 else None,
            '/': round(self._operando_a / self._operando_b) if self._operando_b != 0 else None
        }
        # ----------------------------------------

    def release(self):
        nombre_archivo = f'proceso_{self._id}.json'
        if os.path.exists(nombre_archivo):
            os.remove(nombre_archivo)

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

    def set_indices(self, indice_inicial, indice_final):
        self._indice_inicial = indice_inicial
        self._indice_final = indice_final

    def esta_bloqueado(self):
        return self.timer_bloqueado > 0

    def set_bloqueado(self):
        self.timer_bloqueado = TIEMPO_BLOQUEO

    def set_prioridad(self, valor):
        self.prioridad = valor

    def tiempo_bloqueado(self):
        if self.timer_bloqueado > 0:
            self.timer_bloqueado -= 1

    def ejecutar(self):
        if (self._operacion_realizar in ('/', '%%')) and self._operando_b == 0:
            self._resultado = None
        else:
            self._resultado = self._operations.get(self._operacion_realizar)

    def segundo_transcurrido(self):
        if self._tiempo_restante > 0:
            self._tiempo_restante -= 1
            self._tiempo_transcurrido += 1

    @property
    def indice_inicial(self):
        return self._indice_inicial

    @property
    def operacion(self) -> str:
        return self._operacion_realizar

    @property
    def tamanio(self):
        return self._tamanio

    @operacion.setter
    def operacion(self, operacion):
        self._operacion_realizar = operacion

    @property
    def operando_a(self):
        return self._operando_a

    @operando_a.setter
    def operando_a(self, operando_a):
        self._operando_a = operando_a

    @property
    def operando_b(self):
        return self._operando_b

    @operando_b.setter
    def operando_b(self, operando_b):
        self._operando_b = operando_b

    @property
    def tiempo(self) -> int:
        return int(self._tiempo_maximo_estimado)

    @tiempo.setter
    def tiempo(self, tiempo):
        self._tiempo_maximo_estimado = tiempo

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, numero_proceso):
        self._id = numero_proceso

    @property
    def resultado(self):
        return self._resultado

    @property
    def error(self):
        return self._error

    def set_resultado(self, res):
        if res is None:
            self._terminado = True
            self._error = True
            self._resultado = None
        else:
            self._resultado = res

    @property
    def terminado(self):
        return self._terminado and not self._error and self._tiempo_restante == 0

    @terminado.setter
    def terminado(self, valor):
        self._terminado = valor

    def dame_tiempo_transcurrido_bloqueado(self):
        return int(8 - self.timer_bloqueado)

    @property
    def tiempo_transcurrido(self):
        return int(self._tiempo_transcurrido)

    @tiempo_transcurrido.setter
    def tiempo_transcurrido(self, tiempo):
        self._tiempo_transcurrido = tiempo

    @property
    def tiempo_restante(self):
        return self._tiempo_restante

    def calcula_tiempo_retorno(self):
        if self.tiempo_finalizacion is not None and self.tiempo_llegada is not None:
            self.tiempo_retorno = self.tiempo_finalizacion - self.tiempo_llegada
        else:
            self.tiempo_retorno = 0

    def calcula_tiempo_respuesta(self, tiempo_atendido):
        if self.tiempo_llegada is not None:
            self.tiempo_respuesta = tiempo_atendido - self.tiempo_llegada
        else:
            self.tiempo_respuesta = 0

    def calcula_tiempo_servicio(self):
        if self._tiempo_transcurrido is not None:
            self.tiempo_servicio = self._tiempo_transcurrido
        else:
            self.tiempo_servicio = 0

    def calcula_tiempo_espera(self, tiempo_global=None):
        if self.tiempo_retorno is not None:
            self.tiempo_espera = max(0, self.tiempo_retorno - self._tiempo_transcurrido)
        elif tiempo_global is not None:
            self.tiempo_espera = max(0, (tiempo_global - self.tiempo_llegada) - self._tiempo_transcurrido)
        else:
            self.tiempo_espera = 0

    def incrementa_tiempo_servicio(self):
        self.tiempo_servicio += 1

    def save_to_dict(self):
        nombre_archivo = f'proceso_{self._id}.json'
        datos = {
            "_id": self._id,
            "_tiempo_maximo_estimado": self._tiempo_maximo_estimado,
            "_operacion_realizar": self._operacion_realizar,
            "_operando_a": self._operando_a,
            "_operando_b": self._operando_b,
            "_tamanio": self._tamanio,
            "_resultado": self._resultado,
            "_indice_inicial": self._indice_inicial,
            "_indice_final": self._indice_final,
            "estado": self.estado,
            "timer_bloqueado": self.timer_bloqueado,
            "_tiempo_transcurrido": self._tiempo_transcurrido,
            "_tiempo_restante": self._tiempo_restante,
            "atendido": self.atendido,
            "tiempo_llegada": self.tiempo_llegada,
            "tiempo_finalizacion": self.tiempo_finalizacion,
            "tiempo_retorno": self.tiempo_retorno,
            "tiempo_respuesta": self.tiempo_respuesta,
            "tiempo_espera": self.tiempo_espera,
            "tiempo_servicio": self.tiempo_servicio,
            "_terminado": self._terminado,
            "_error": self._error,
            "prioridad": self.prioridad
        }
        try:
            with open(nombre_archivo, 'w') as archivo:
                json.dump(datos, archivo, indent=2)
            return True
        except Exception as e:
            print(f"Error al guardar: {e}")
            return False

    def load_from_dict(self, nombre_archivo):
        # Carga los datos desde un diccionario a la instancia de la clase
        try:
            with open(nombre_archivo, 'r') as archivo:
                data = json.load(archivo)
        except Exception as e:
            print(f"Error al cargar: {e}")
            return False
        self._id = data["_id"]
        self._tiempo_maximo_estimado = data["_tiempo_maximo_estimado"]
        self._operacion_realizar = data["_operacion_realizar"]
        self._operando_a = data["_operando_a"]
        self._operando_b = data["_operando_b"]
        self._tamanio = data["_tamanio"]
        self._resultado = data["_resultado"]
        self._indice_inicial = data["_indice_inicial"]
        self._indice_final = data["_indice_final"]
        self.estado = data["estado"]
        self.timer_bloqueado = data["timer_bloqueado"]
        self._tiempo_transcurrido = data["_tiempo_transcurrido"]
        self._tiempo_restante = data["_tiempo_restante"]
        self.atendido = data["atendido"]
        self.tiempo_llegada = data["tiempo_llegada"]
        self.tiempo_finalizacion = data["tiempo_finalizacion"]
        self.tiempo_retorno = data["tiempo_retorno"]
        self.tiempo_respuesta = data["tiempo_respuesta"]
        self.tiempo_espera = data["tiempo_espera"]
        self.tiempo_servicio = data["tiempo_servicio"]
        self._terminado = data["_terminado"]
        self._error = data["_error"]
        self.prioridad = data["prioridad"]
        # Eliminar el archivo después de cargar la información
        try:
            os.remove(nombre_archivo)
        except Exception as e:
            print(f"Error al eliminar el archivo: {e}")
        return True


"""
proceso = Proceso(operador='+', operando_a=1, operando_b=2, tiempo=3, numero_proceso=1)
proceso.save_to_dict()
proceso.load_from_dict()
print(proceso.__dict__)
"""
