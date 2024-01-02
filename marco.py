class Marco:
    def __init__(self, proceso=None, unidades=None, tamanio_marco=None):
        self._marco = []
        self._estado_proceso = ""
        self._id = None
        if tamanio_marco is not None:
            for _ in range(tamanio_marco):
                self._marco.append("SO")  # 5 unidades de SO en cada marco
        elif proceso is not None and unidades is not None:
            self._estado_proceso = proceso.get_estado()
            for i in range(unidades):
                if len(self._marco) < 5:
                    self._marco.append(proceso.id)
            self._id = proceso.id

    def set_id(self, id_process):
        self._id = id_process

    def set_estado(self, estado):
        self._estado_proceso = estado

    def get_estado(self):
        return self._estado_proceso

    def get_marco(self):
        return self._marco

    def __str__(self):
        return str(self._marco)

    def get_unidades_llenas(self):
        return len(self._marco)

    def release(self):
        self._marco.clear()

    def get_id(self):
        return self._marco[0]
