class Proceso:
    def __init__(self, operador, operando_a, operando_b, tiempo, numero_proceso) -> None:
        self._operacion_realizar = operador
        self._operando_a = operando_a
        self._operando_b = operando_b
        self._tiempo_medio_estimado = int(tiempo)
        self._tiempo_transcurrido = 0
        self._tiempo_restante = int(tiempo)
        self._resultado = 0.0
        self._id = numero_proceso
        self._terminado = False
        self._timer_bloqueado = 0
        self._error = False
        
    
    
    
    def esta_bloqueado(self):
        return self._timer_bloqueado > 0
    
    def set_bloqueado(self):
        self._timer_bloqueado = 8
    def tiempo_bloqueado(self):
        if self._timer_bloqueado > 0:
            self._timer_bloqueado -= 1
    
    def ejecutar(self):
        if self._operacion_realizar == '+':
            self._resultado = self._operando_a + self._operando_b
        elif self._operacion_realizar == '-':
            self._resultado = self._operando_a - self._operando_b
        elif self._operacion_realizar == '*':
            self._resultado = self._operando_a * self._operando_b
        elif self._operacion_realizar == '/':
            if self._operando_b != 0:
                self._resultado = round(self._operando_a / self._operando_b)
            else:
                self._resultado = 0
        elif self._operacion_realizar == '%':
            self._resultado = round(((self._operando_a / 100) * self._operando_b), 2)
        elif self._operacion_realizar == '%%':
            self._resultado = self._operando_a % self._operando_b
    def segundo_transcurrido(self):
        if self._tiempo_restante > 0:
            self._tiempo_restante -= 1
            self._tiempo_transcurrido += 1
    
    @property
    def operacion(self) -> str:
        return self._operacion_realizar
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
        return int(self._tiempo_medio_estimado)
    @tiempo.setter
    def tiempo(self, tiempo):
        self._tiempo_medio_estimado = tiempo
    
    @property
    def id(self) -> int:
        return self._id
    @id.setter
    def id(self, numero_proceso):
        self._id = numero_proceso
    
    @property
    def resultado(self):
        return self._resultado
    @resultado.setter
    def resultado(self, res):
        if res == 'e':
            self._terminado = True
            self._error = True
        self._resultado = res

    @property
    def terminado(self):
        return self._terminado and not self._error and self._tiempo_restante == 0 
        
    @terminado.setter
    def terminado(self, valor):
        self._terminado = valor
    
    @property
    def tiempo_transcurrido(self):
        return self._tiempo_transcurrido
    @tiempo_transcurrido.setter
    def tiempo_transcurrido(self, tiempo):
        self._tiempo_transcurrido = tiempo
    
    @property
    def tiempo_restante(self):
        return self._tiempo_restante
    
    
            
    
