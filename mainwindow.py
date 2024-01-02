import random
import threading
import time
from collections import deque
from math import ceil
from unittest.mock import patch

from PySide2.QtCore import QTimer, Signal, Slot
from PySide2.QtGui import QFontMetrics
from PySide2.QtWidgets import QMainWindow, QPushButton, QLineEdit, QPlainTextEdit, QSpinBox, QFrame, QLabel, \
    QProgressBar

from memoria import Memoria
from proceso import *
from ui_mainwindow import Ui_MainWindow

# MEMORIA
TAMANIO_UNIDADES = 220
TAMANIO_MARCO = 5
TAMANIO_SO = 4

TIEMPO_MIN = 6
TIEMPO_MAX = 16
# TIEMPO_MAX = 8 Para pruebas
RANGO_MIN = 0
RANGO_MAX = 1000
TAM_MIN = 6
TAM_MAX = 26


def crea_proceso(numero_programa):  # Aleatorio
    operadores = ['+', '-', '*', '/', '%', "%%"]
    operador = random.choice(operadores)
    operando_a = random.randint(RANGO_MIN, RANGO_MAX)
    operando_b = random.randint(RANGO_MIN, RANGO_MAX)
    tamanio = random.randint(TAM_MIN, TAM_MAX)
    tiempo = str(random.randint(TIEMPO_MIN, TIEMPO_MAX))
    return Proceso(operador, operando_a, operando_b, tiempo, numero_programa, tamanio)


def not_num(num):
    try:
        float(num)
        return False
    except ValueError:
        return True


def simular_segundo_transcurrido_pruebas():
    with patch('time.sleep') as mock_sleep:
        mock_sleep.return_value = None
        time.sleep(1)  # Simula un segundo transcurrido


def calcula_porcentaje(marco):
    if marco is None:
        return 0
    unidades = marco.get_unidades_llenas()
    porcentaje = (unidades / TAMANIO_MARCO) * 100
    return porcentaje


def change_progress_state(state):
    # Configurar la hoja de estilo según el estado
    if state == "Listo":
        style_sheet = """
            QProgressBar {
            }
            QProgressBar::chunk {
                background-color: #0055ff;  /*  para el estado listo */
            }
        """
    elif state == "Ejecucion":
        style_sheet = ""
    elif state == "Bloqueado":
        style_sheet = """
            QProgressBar {
            }

            QProgressBar::chunk {
                background-color: #ff0000;  /* Otro color para el estado bloqueado */
            }
        """
    else:
        # Establecer un estilo predeterminado si el estado no es reconocido
        style_sheet = ""
    return style_sheet


class MainWindow(QMainWindow):
    actualizar_interfaz_signal = Signal(int, float, object)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Colas de procesos (5 Estados)
        self.cola_de_nuevos = deque()  # Procesos en espera
        self.memoria = Memoria(TAMANIO_UNIDADES, TAMANIO_MARCO, TAMANIO_SO)  # Maximo de procesos
        self.cola_de_terminados = deque()  # Procesos terminados
        self.cola_de_suspendidos = deque()  # Procesos suspendidos
        self.bandera_prioridad = False
        # self.contador_suspendidos = 0 = len(self.cola_de_suspendidos)
        # self.id_suspendido = id del proceso suspendido
        # self.tam_suspendido = tamaño del proceso suspendido
        # self.pag_suspendido = páginas del proceso suspendido

        # Hilo de ejecucion
        self.hilo = None
        self.pause_condition = threading.Condition()
        self.proceso_nulo = Proceso('+', 1, 2, 1000000, -1)
        # Timer de actualziacion de la interfaz
        # Crear un QTimer para actualizar la interfaz cada 1 segundo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_interfaz)
        self.timer.start(1000)  # Intervalo en milisegundos (1 segundo)

        # Actualizacion datos de la interfaz:
        # - Texto de las colas
        # ----------------------------------------------------------------|
        self.textos_procesos_sistema = {
            "nuevos": "0", "listos": "0", "bloqueados": "0", "suspendidos": "0", "terminados": "0"
        }
        self.textos_proximos_nuevos = {"id_nuevo": "0", "tam_nuevo": "0", "pag_nuevo": "0"}
        self.textos_proximos_suspendidos = {"id_suspendido": "0", "tam_suspendido": "0", "pag_suspendido": "0"}
        self.texto_nuevos = "0"
        self.texto_listos = "Sin procesos listos."
        self.texto_ejecucion = "Sin procesos en ejecucion."
        self.texto_terminados = "No hay procesos terminados."
        self.texto_bloqueados = "No hay procesos bloqueados."
        self.texto_quantum = "5"
        self.tiempo_quantum_restante = 0
        # ----------------------------------------------------------------|
        # - Contadores
        # ----------------------------------------------------------------|
        self.texto_memoria_restante = str(TAMANIO_UNIDADES)
        self.texto_memoria_uso = "0"
        self.texto_tiempo_global = "0"

        self.id_proceso = 0
        self.tiempo_global = 0
        # ----------------------------------------------------------------|
        # - Banderas - automaticas
        # ----------------------------------------------------------------|
        self.continuar = False
        self.en_ejecucion = False
        self.bandera_limpiar_campos = False
        self.bandera_proceso_automatico = True
        self.bandera_detener = False  # Bandera para truncar el programa
        self.tiempo_de_cpu = 0
        self.bandera_proceso = False
        # - Banderas - pulsaciones
        # ----------------------------------------------------------------|
        self.bandera_i = False
        self.bandera_e = False
        self.bandera_p = False
        self.bandera_c = False
        self.bandera_n = False
        self.bandera_b = False
        self.bandera_t = False
        self.bandera_s = False  # New
        self.bandera_r = False  # New
        # ----------------------------------------------------------------|
        # Definicion de widgets
        # ----------------------------------------------------------------------------------------|
        # Label
        self.label_ejecucion = self.findChild(QLabel, "lb_pausa")
        # Boton
        self.btn_iniciar = self.findChild(QPushButton, "pb_iniciar")
        self.btn_reiniciar = self.findChild(QPushButton, "pb_re_iniciar")
        self.btn_reiniciar.setEnabled(False)  # Deshabilitar el boton
        self.btn_reiniciar.setStyleSheet("QPushButton:disabled { color: gray; border:none;}")
        self.btn_agregar = self.findChild(QPushButton, "pb_agregar")
        self.btn_habilitar_capturar_proceso = self.findChild(QPushButton, "pb_capturar_procesos")
        self.btn_agregar_procesos = self.findChild(QPushButton, "pb_agregar_procesos")
        self.btn_limpiar = self.findChild(QPushButton, "btn_limpiar")
        # PlainTextEdit
        self.pte_listos = self.findChild(QPlainTextEdit, "pte_listos")
        self.pte_ejecucion = self.findChild(QPlainTextEdit, "pte_ejecucion")
        self.pte_terminados = self.findChild(QPlainTextEdit, "pte_terminados")
        self.pte_bloqueados = self.findChild(QPlainTextEdit, "pte_bloqueados")
        # LineEdit
        # Entrada
        self.le_tiempo_max = self.findChild(QLineEdit, "le_tiempo_max")
        self.le_operador = self.findChild(QLineEdit, "le_operador")
        self.le_operando_a = self.findChild(QLineEdit, "le_operando_a")
        self.le_operando_b = self.findChild(QLineEdit, "le_operando_b")
        # Salida
        # PROXIMOS
        self.le_siguiente_id_nuevo = self.findChild(QLineEdit, "le_siguiente_id_nuevo")
        self.le_siguiente_tam_nuevo = self.findChild(QLineEdit, "le_siguiente_tam_nuevo")
        self.le_siguiente_pag_nuevo = self.findChild(QLineEdit, "le_siguiente_pag_nuevo")
        self.le_siguiente_id_suspendido = self.findChild(QLineEdit, "le_siguiente_id_suspendido")
        self.le_siguiente_tam_suspendido = self.findChild(QLineEdit, "le_siguiente_tam_suspendido")
        self.le_siguiente_pag_suspendido = self.findChild(QLineEdit, "le_siguiente_pag_suspendido")
        # FRAME PROXIMO SUSPENDIDO
        self.frame_proximo_suspendido = self.findChild(QFrame, "frame_proximo_suspendido")
        # Procesos del sistema
        self.le_procesos_nuevos = self.findChild(QLineEdit, "le_procesos_nuevos")
        self.le_procesos_listos = self.findChild(QLineEdit, "le_procesos_listos")
        self.le_procesos_bloqueados = self.findChild(QLineEdit, "le_procesos_bloqueados")
        self.le_procesos_suspendidos = self.findChild(QLineEdit, "le_procesos_suspendidos")
        self.le_procesos_terminados = self.findChild(QLineEdit, "le_procesos_terminados")

        self.le_memoria_restante = self.findChild(QLineEdit, "le_memoria_restante")
        self.le_memoria_uso = self.findChild(QLineEdit, "le_memoria_uso")
        self.le_marcos_libres = self.findChild(QLineEdit, "le_marcos_libres")
        self.le_tiempo_global = self.findChild(QLineEdit, "le_tiempo_global")
        # Spinbox numero de procesos
        self.sb_num_procesos = self.findChild(QSpinBox, "sb_num_procesos")
        # Spinbx quantum inicial
        self.sb_quantum = self.findChild(QSpinBox, "sb_quantum")
        # Frame captura de datos
        self.frame_captura = self.findChild(QFrame, "frame_7")
        self.habilitar_campos()
        # Frames Memoria
        """
        self.frames = []    # Lista de frames de memoria
        for i in range(1, 45):
            frame = self.findChild(QFrame, f"content{i}")
            self.frames.append(frame)
        """
        self.barras_de_progreso = []
        # Encontrar las QProgressBar existentes y agregarlas a la lista
        for i in range(1, 45):
            nombre_progress_bar = f"progressBar_{i}"
            progress_bar = self.findChild(QProgressBar, nombre_progress_bar)
            self.barras_de_progreso.append(progress_bar)

        # Inicializar lista de etiquetas asociadas a las barras de progreso
        self.etiquetas = []
        for i in range(1, 41):
            nombre_label = f"lbl_pb{i}"
            label = self.findChild(QLabel, nombre_label)
            self.etiquetas.append(label)
        # ----------------------------------------------------------------------------------------|
        # Eventos
        # -------------------------------------------------------------------------|
        # Ejecutar el simulador
        self.btn_iniciar.clicked.connect(self.back_end)
        self.btn_reiniciar.clicked.connect(self.reiniciar_programa)
        # Agregar proceso
        self.btn_agregar_procesos.clicked.connect(self.agregar_proceso)
        # Limpiar consolas
        # self.btn_limpiar.clicked.connect(self.limpiar)
        self.mostrar_textos()
        # Conecta la señal a la ranura
        self.actualizar_interfaz_signal.connect(self.actualizar_barras)
        # -------------------------------------------------------------------------|

    # Funciones
    # -----------------------------------------------------------------------------------
    def busca_estado_proceso(self, id_proceso):
        for proceso in self.cola_de_nuevos:
            if proceso.id == id_proceso:
                return proceso.get_estado()
        for proceso in self.memoria.cola_de_listos:
            if proceso.id == id_proceso:
                return proceso.get_estado()
        estado = self.memoria.busca_estado_proceso(id_proceso)
        if estado is not None:
            return estado

    def actualizar_barras_de_progreso(self):
        # Obtén el espacio de memoria actualizado
        espacio_de_memoria = self.memoria.espacio_de_memoria
        indice_memoria = TAMANIO_SO
        for i, barra in enumerate(self.barras_de_progreso[:40]):
            if indice_memoria < 44:  # Solo se actualizan las primeras 40 barras (41 - 44) son del SO
                marco = espacio_de_memoria[indice_memoria]
                porcentaje = calcula_porcentaje(marco)
                current_thread = threading.current_thread()
                if barra is not None and isinstance(barra, QProgressBar) and current_thread.name == "MainThread":
                    if marco is not None:
                        marco.set_estado(self.busca_estado_proceso(marco.get_id()))
                        barra.setStyleSheet(change_progress_state(marco.get_estado()))
                        barra.setValue(porcentaje)
                        titulo = marco.get_id()
                        etiqueta = self.etiquetas[i]
                        etiqueta.setText(f"Marco {i + 4}: Proceso: {titulo}")
                    else:
                        etiqueta = self.etiquetas[i]
                        etiqueta.setText(f"Marco {i + 4}")
                        barra.setValue(0)
                else:
                    self.actualizar_interfaz_signal.emit(i, porcentaje, marco)
                indice_memoria += 1

    @Slot(int, float)
    def actualizar_barras(self, indice, porcentaje, marco):
        # Realiza la actualización de la interfaz aquí
        # Por ejemplo, actualiza una barra de progreso
        barra = self.barras_de_progreso[indice]
        etiqueta = self.etiquetas[indice]
        if marco is not None:
            titulo = marco.get_id()
            etiqueta.setText(f"Proceso: {titulo}")
        else:
            etiqueta.setText(f"Marco {indice + 4}")
        barra.setValue(porcentaje)

    def reiniciar_programa(self):
        self.btn_reiniciar.setEnabled(False)  # Deshabilitar el boton
        self.btn_reiniciar.setStyleSheet("QPushButton:disabled { color: gray; border:none;}")
        self.release_memory()
        self.id_proceso = 0
        self.tiempo_global = 0
        for barra in self.barras_de_progreso[:40]:
            barra.setValue(0)
        self.mostrar_textos()

    def release_memory(self):
        self.cola_de_nuevos.clear()
        self.cola_de_terminados.clear()
        self.memoria.release()

    def closeEvent(self, event):  # Detectar si se va a cerrar el programa y protegerlo
        if self.en_ejecucion and not self.bandera_detener:
            self.bandera_detener = True
            event.ignore()  # Evita que la ventana se cierre
        else:
            if self.bandera_p or self.bandera_b:
                with self.pause_condition:
                    self.pause_condition.notify()
            self.release_memory()
            event.accept()  # Permite que la ventana se cierre

    def keyPressEvent(self, event):
        texto_tecla = str(event.text())
        if texto_tecla == 'i':
            self.bandera_i = True
        elif texto_tecla == 'e':
            self.bandera_e = True
        elif texto_tecla == 'p':
            self.label_ejecucion.setText("o      Pausa      o")
            self.label_ejecucion.setStyleSheet("color: red; background-color: white;")
            self.bandera_p = True
        elif texto_tecla == 'c':
            self.label_ejecucion.setText("Ejecución")
            self.label_ejecucion.setStyleSheet("color: green; background-color: white;")
            self.bandera_p = False
            self.bandera_b = False
            self.bandera_t = False
            with self.pause_condition:
                self.pause_condition.notify()
        elif texto_tecla == 'n':
            self.bandera_n = True
        elif texto_tecla == 'b':
            self.label_ejecucion.setText("o      Pausa      o")
            self.label_ejecucion.setStyleSheet("color: red; background-color: white;")
            self.bandera_b = True
        elif texto_tecla == 't':
            self.label_ejecucion.setText("o      Pausa      o")
            self.label_ejecucion.setStyleSheet("color: red; background-color: white;")
            self.bandera_t = True
        elif texto_tecla == 's':
            self.bandera_s = True
        elif texto_tecla == 'r':
            self.bandera_r = True

    def habilitar_campos(self):
        if self.frame_captura.isEnabled():
            # Si está habilitado, deshabilitarlo
            self.frame_captura.setEnabled(False)
            self.bandera_proceso_automatico = True
        else:
            # Si está deshabilitado, habilitarlo
            self.frame_captura.setEnabled(True)
            self.bandera_proceso_automatico = False

    def actualizar_interfaz(self):
        # Esta función se llama cada vez que el QTimer se dispara
        self.pte_listos.setPlainText(self.texto_listos)
        self.pte_ejecucion.setPlainText(self.texto_ejecucion)
        self.pte_terminados.setPlainText(self.texto_terminados)
        self.pte_bloqueados.setPlainText(self.texto_bloqueados)

        self.texto_quantum = str(self.sb_quantum.value())

        # Proximo proceso nuevo
        self.le_siguiente_id_nuevo.setText(self.textos_proximos_nuevos["id_nuevo"])
        self.le_siguiente_tam_nuevo.setText(self.textos_proximos_nuevos["tam_nuevo"])
        self.le_siguiente_pag_nuevo.setText(self.textos_proximos_nuevos["pag_nuevo"])

        # Proximo proceso suspendido
        self.le_siguiente_id_suspendido.setText(self.textos_proximos_suspendidos["id_suspendido"])
        self.le_siguiente_tam_suspendido.setText(self.textos_proximos_suspendidos["tam_suspendido"])
        self.le_siguiente_pag_suspendido.setText(self.textos_proximos_suspendidos["pag_suspendido"])

        # Uso de memoria
        self.le_memoria_restante.setText(self.texto_memoria_restante + " MB / " + str(TAMANIO_UNIDADES) + " MB")
        self.le_memoria_uso.setText(self.texto_memoria_uso + " MB / " + str(TAMANIO_UNIDADES) + " MB")
        self.le_marcos_libres.setText(str(self.memoria.paginas_disponibles) + " / 44")

        # Procesos del sistema
        self.le_procesos_nuevos.setText(self.textos_procesos_sistema["nuevos"])  # Procesos pendientes
        self.le_procesos_listos.setText(self.textos_procesos_sistema["listos"])
        self.le_procesos_bloqueados.setText(self.textos_procesos_sistema["bloqueados"])
        self.le_procesos_suspendidos.setText(self.textos_procesos_sistema["suspendidos"])
        self.le_procesos_terminados.setText(self.textos_procesos_sistema["terminados"])

        # Tiempo global
        self.le_tiempo_global.setText(self.texto_tiempo_global)  # Tiempo global

        if self.bandera_limpiar_campos:
            self.le_tiempo_max.clear()
            self.le_operador.clear()
            self.le_operando_a.clear()
            self.le_operando_b.clear()
            self.bandera_limpiar_campos = False

        if self.en_ejecucion:
            self.actualizar_barras_de_progreso()
        if self.bandera_prioridad:
            self.frame_proximo_suspendido.setStyleSheet("background-color: red;")
        else:
            self.frame_proximo_suspendido.setStyleSheet("background-color: rgb(159, 159, 159);")

    def actualiza_texto_contadores(self):
        self.texto_memoria_restante = str(self.memoria.espacio_disponible)
        self.texto_memoria_uso = str(self.memoria.get_memoria_en_uso())
        self.texto_tiempo_global = str(self.tiempo_global)

        self.textos_procesos_sistema["nuevos"] = str(len(self.cola_de_nuevos))
        self.textos_procesos_sistema["listos"] = str(len(self.memoria.cola_de_listos))
        self.textos_procesos_sistema["bloqueados"] = str(len(self.memoria.cola_de_bloqueados))
        self.textos_procesos_sistema["suspendidos"] = str(len(self.cola_de_suspendidos))
        self.textos_procesos_sistema["terminados"] = str(len(self.cola_de_terminados))

        if self.cola_de_nuevos:
            self.textos_proximos_nuevos["id_nuevo"] = str(self.cola_de_nuevos[0].id)
            self.textos_proximos_nuevos["tam_nuevo"] = str(self.cola_de_nuevos[0].tamanio)
            self.textos_proximos_nuevos["pag_nuevo"] = str(ceil(self.cola_de_nuevos[0].tamanio / TAMANIO_MARCO))
        else:
            self.textos_proximos_nuevos["id_nuevo"] = "0"
            self.textos_proximos_nuevos["tam_nuevo"] = "0"
            self.textos_proximos_nuevos["pag_nuevo"] = "0"

        if self.cola_de_suspendidos:
            self.textos_proximos_suspendidos["id_suspendido"] = str(self.cola_de_suspendidos[0].id)
            self.textos_proximos_suspendidos["tam_suspendido"] = str(self.cola_de_suspendidos[0].tamanio)
            self.textos_proximos_suspendidos["pag_suspendido"] = (
                str(ceil(self.cola_de_suspendidos[0].tamanio / TAMANIO_MARCO))
            )
        else:
            self.textos_proximos_suspendidos["id_suspendido"] = "0"
            self.textos_proximos_suspendidos["tam_suspendido"] = "0"
            self.textos_proximos_suspendidos["pag_suspendido"] = "0"

    def iniciliza_textos(self):
        if not self.cola_de_terminados:
            self.texto_terminados = "No hay procesos terminados."
        if not self.memoria.cola_de_listos:
            self.texto_listos = "Sin procesos listos."
        if not self.memoria.cola_de_ejecucion:
            self.texto_ejecucion = "Sin procesos en ejecucion."
        if not self.memoria.cola_de_bloqueados:
            self.texto_bloqueados = "No hay procesos bloqueados."

    def terminar_hilo(self):
        if self.en_ejecucion:
            self.en_ejecucion = False

    def back_end(self):
        if not self.en_ejecucion and self.cola_de_nuevos:
            if self.hilo:
                self.hilo.join()
            self.en_ejecucion = True
            self.sb_quantum.setEnabled(False)
            self.hilo = threading.Thread(target=self.correr_interfaz)
            self.hilo.start()

    def correr_interfaz(self):
        if self.cola_de_nuevos:  # Si hay procesos en la cola de nuevos
            self.correr_rr()  # Correr el algoritmo RR
        else:
            self.en_ejecucion = False

    def captura_proceso(self) -> Proceso:
        operador = self.le_operador.text()
        operando_a = float(self.le_operando_a.text())
        operando_b = float(self.le_operando_b.text())
        tiempo = int(self.le_tiempo_max.text())
        self.id_proceso += 1
        return Proceso(operador, operando_a, operando_b, tiempo, self.id_proceso)

    def crea_procesos(self, num_procesos):
        while num_procesos > 0:
            self.id_proceso += 1
            proceso = crea_proceso(self.id_proceso)
            self.cola_de_nuevos.append(proceso)
            self.mostrar_textos()
            num_procesos -= 1

    def ingresa_procesos_a_listos(self):
        # Mientras quede espacio en memoria y la cola de nuevos no esté vacía: agregar a listos
        # Calcular el numero de paginas a ingresar
        if self.cola_de_suspendidos and self.cola_de_suspendidos[0].prioridad:    # Si hay procesos suspendidos
            proceso = self.cola_de_suspendidos.popleft()    # Se saca un proceso de la cola de suspendidos
            if not self.memoria.recupeara_proceso(proceso):     # Si no se pudo recuperar el proceso
                self.bandera_prioridad = True
                self.cola_de_suspendidos.append(proceso)    # Se regresa el proceso a la cola de suspendidos
            else:   # Si se pudo recuperar el proceso
                self.bandera_prioridad = False  # Se quita la bandera de prioridad
                proceso.set_prioridad(False)  # Se le quita la prioridad al proceso
        else:
            while self.cola_de_nuevos:
                proceso = self.cola_de_nuevos.popleft()  # Se saca un proceso de la cola de nuevos
                if self.memoria.hay_espacio(proceso.tamanio):
                    proceso.tiempo_llegada = self.tiempo_global
                    proceso.set_estado("Listo")
                    self.memoria.agrega_a_listo(proceso, True)  # Se asigna memoria al proceso en listos
                    self.mostrar_textos()
                else:
                    proceso.set_estado("Nuevo")
                    self.cola_de_nuevos.appendleft(proceso)  # Se regresa el proceso a la cola de nuevos
                    break
        # La cola de listos esta llena - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    def correr_rr(self):
        self.bandera_detener = False
        while self.cola_de_nuevos and not self.bandera_detener:  # Este ciclo recorre la cola de nuevos O(n)
            self.ingresa_procesos_a_listos()  # Ingresa todos los procesos posibles a listos
            while (
                    self.memoria.procesos_en_memoria() or self.cola_de_suspendidos) and not self.bandera_detener:  # Mientras haya procesos en listos:
                self.mostrar_textos()  # Se formatea el texto de los procesos en listo
                self.ingresa_procesos_a_listos()  # Verifica si hay espacio y, agrega otro proceso a listos
                proceso = self.memoria.entra_proceso_ejecucion()  # Mete proceso a la cola de ejecucion (solo cabe 1)
                self.mostrar_textos()
                self.ejecucion_del_proceso(proceso)
        self.mostrar_textos()
        self.muestra_datos_de_procesos()
        self.bandera_detener = False
        self.terminar_hilo()
        self.btn_reiniciar.setStyleSheet("QPushButton:enabled { color: red; }")
        self.btn_reiniciar.setEnabled(True)  # Deshabilitar el boton
        self.sb_quantum.setEnabled(True)  # Habilitar el spinbox
        self.actualizar_barras_de_progreso()
        # Se terminaron todos los procesos!

    def calcular_tiempos_listos(self):
        colas = [self.memoria.cola_de_listos, self.memoria.cola_de_ejecucion, self.memoria.cola_de_bloqueados]
        for cola in colas:
            if cola:
                for proceso in cola:
                    proceso.calcula_tiempo_espera(self.tiempo_global)

    def administrar_pausa(self):
        if self.bandera_b:
            self.calcular_tiempos_listos()
            self.muestra_bcp()  # Mostrar BCP
        elif self.bandera_t:
            pass
        while self.bandera_p or self.bandera_b or self.bandera_t and not self.bandera_detener:
            self.pause_condition.wait()

    def administrar_interrupcion(self, proceso):
        # Proceso entra a bloqueados
        self.bandera_i = False
        proceso.set_bloqueado()
        self.memoria.saca_de_ejecucion()
        self.memoria.agrega_a_bloqueados(proceso)
        self.muestra_texto_ejecucion()
        self.muestra_texto_listos()
        self.mostrar_textos()

    def administrar_error(self, proceso):
        # Proceso finalizado por error (sale a terminados)
        proceso.set_resultado(None)  # Se da por terminado
        proceso.tiempo_finalizacion = self.tiempo_global
        proceso.calcula_tiempo_retorno()
        proceso.calcula_tiempo_servicio()
        proceso.calcula_tiempo_espera()
        self.memoria.saca_de_ejecucion(True)
        self.cola_de_terminados.append(proceso)
        self.bandera_e = False
        self.bandera_proceso = False  # El proceso ya terminó su ejecución
        self.mostrar_textos()

    def administrar_nuevo(self):
        self.id_proceso += 1
        proceso = crea_proceso(self.id_proceso)
        self.cola_de_nuevos.append(proceso)
        self.mostrar_textos()
        self.bandera_n = False

    def proceso_completado(self, proceso):
        proceso.ejecutar()
        proceso.tiempo_finalizacion = self.tiempo_global
        proceso.calcula_tiempo_retorno()
        proceso.calcula_tiempo_servicio()
        proceso.calcula_tiempo_espera()
        self.cola_de_terminados.append(proceso)
        self.memoria.saca_de_ejecucion(True)

    def tiempo_de_ejecucion(self, proceso):
        if proceso is not None:
            proceso.segundo_transcurrido()
            proceso.incrementa_tiempo_servicio()
            self.mostrar_textos()
            self.texto_tiempo_global = str(self.tiempo_global)
            if not proceso.atendido:
                proceso.atendido = True
                proceso.calcula_tiempo_respuesta(self.tiempo_global)
            if proceso.tiempo_restante == 0:
                proceso.terminado = True

    def mostrar_textos(self):
        colas_a_mostrar = [
            (self.memoria.cola_de_listos, self.muestra_texto_listos),
            (self.memoria.cola_de_ejecucion, self.muestra_texto_ejecucion),
            (self.memoria.cola_de_bloqueados, self.muestra_texto_bloqueados),
            (self.cola_de_terminados, self.muestra_texto_terminados)
        ]
        for cola, funcion_muestra in colas_a_mostrar:
            if cola:
                funcion_muestra()
            else:
                self.iniciliza_textos()
        self.actualiza_texto_contadores()

    def ejecucion_del_proceso(self, proceso):
        if not self.bandera_proceso:  # Inicializa el quantum para la primera vez que se ejecuta un proceso
            self.tiempo_quantum_restante = int(self.texto_quantum)  # Inicializa el quantum
            self.bandera_proceso = True  # El proceso ya inició su ejecución
        contador_quantum = self.tiempo_quantum_restante  # Es el tiempo que le queda al proceso en ejecución (ciclo act)
        if proceso is None and self.cola_de_suspendidos:    # Si no hay procesos en ejecución y hay suspendidos
            self.mostrar_textos()
            with self.pause_condition:  # Consumo de tiempo de CPU
                self.administrar_pausa()    # Caso de pausa
            if self.bandera_r:  # Caso de recuperación de proceso
                proceso_r = self.cola_de_suspendidos.popleft()
                if not self.memoria.recupeara_proceso(proceso_r):
                    self.bandera_prioridad = True
                    self.cola_de_suspendidos.append(proceso_r)    # Si no se pudo recuperar, se regresa a la cola
                self.bandera_r = False
            if self.bandera_n:
                self.administrar_nuevo()
            self.consume_tiempo_global()  # Simula 1s transcurrido
        else:
            while proceso.tiempo_restante > 0 and not self.bandera_detener:  # O(16) tiempo maximo
                self.mostrar_textos()
                with self.pause_condition:  # Consumo de tiempo de CPU
                    self.administrar_pausa()
                if self.bandera_r:
                    if self.cola_de_suspendidos:
                        proceso_r = self.cola_de_suspendidos.popleft()
                        if not self.memoria.recupeara_proceso(proceso_r):
                            self.bandera_prioridad = True
                            self.cola_de_suspendidos.append(proceso_r)   # Si no se pudo recuperar, se regresa a la cola
                        self.bandera_r = False
                        break
                    self.bandera_r = False
                if self.bandera_s:
                    proceso_s = self.memoria.suspender_proceso()  # Suspende el proceso actual si hay bloqueados
                    if proceso_s is not None:
                        self.cola_de_suspendidos.append(proceso_s)
                        self.bandera_s = False
                        break
                    self.bandera_s = False
                if self.bandera_i:
                    if self.memoria.hay_ejecucion():
                        self.administrar_interrupcion(proceso)
                        break
                    else:
                        self.bandera_i = False
                if self.bandera_e:
                    self.administrar_error(proceso)
                    break
                if self.bandera_n:
                    self.administrar_nuevo()
                    break
                else:
                    # Casos generales (Bloqueado / Ejecución)
                    if self.memoria.hay_bloqueados() and (
                            self.memoria.hay_ejecucion() and contador_quantum > 0):  # Hay ejecución y bloqueados
                        if self.memoria.hay_bloqueados():  # Hay bloqueados
                            self.memoria.ciclo_bloqueados()
                        if self.memoria.hay_ejecucion():  # Hay ejecución
                            self.tiempo_de_ejecucion(proceso)
                            contador_quantum -= 1
                            self.tiempo_quantum_restante -= 1
                        self.consume_tiempo_global()  # Simula 1s transcurrido
                    elif not self.memoria.hay_bloqueados() and (
                            self.memoria.hay_ejecucion() and contador_quantum > 0):  # Solo ejecución normal
                        self.tiempo_de_ejecucion(proceso)  # Ciclo Ejecución
                        contador_quantum -= 1
                        self.tiempo_quantum_restante -= 1
                        self.consume_tiempo_global()  # Simula 1s transcurrido
                    elif self.memoria.hay_bloqueados() and not self.memoria.hay_ejecucion():  # Solo bloqueados
                        # En cada ciclo de "tiempo" se descontará una unidad de tiempo a cada proceso bloqueado
                        # Si el proceso termina su estado bloqueado sale y entra de nuevo a listo (en clase Memoria)
                        self.memoria.ciclo_bloqueados()
                        self.consume_tiempo_global()  # Simula 1s transcurrido
                    elif self.memoria.hay_ejecucion() and contador_quantum <= 0:
                        self.memoria.saca_de_ejecucion()  # Saca si el proceso actual ya termino su quantum
                        self.memoria.agrega_a_listo(proceso)  # Se agrega a listos
                        self.bandera_proceso = False  # El proceso ya terminó su quantum de ejecución
                        break
                    else:
                        break
                    self.mostrar_textos()  # Actualiza consolas

                    if self.memoria.hay_listos() and not self.memoria.hay_ejecucion():
                        break  # Si puede entrar un proceso a ejecución, le da la oportunidad

            if proceso is not None and proceso.terminado and not proceso.error:
                self.bandera_proceso = False  # El proceso ya terminó su ejecución
                self.proceso_completado(proceso)
                self.mostrar_textos()

    def consume_tiempo_global(self):
        # tiempo global
        time.sleep(1)
        self.tiempo_global += 1
        self.mostrar_textos()

    # Validaciones de campos de la interfaz
    def campos_validos(self) -> bool:  # Campo vacio
        if (self.le_tiempo_max.text() == "" or self.le_operador.text() not in self.operadores
                or self.le_operando_a.text() == "" or
                self.le_operando_b.text() == "" or not_num(self.le_operando_a.text()) or
                not_num(self.le_operando_b.text()) or (self.le_operador.text() == '/' and
                                                       self.le_operando_b.text() == '0') or (
                        self.le_operador.text() == '%%' and self.le_operando_b.text() == '0')):
            return False
        elif 0 < int(self.le_tiempo_max.text()) <= 10:  # 0 < tiempo <= 10
            numero = self.id_proceso + 1
            if any(proceso.get_id() == numero for proceso in self.cola_de_nuevos):  # ID existente
                return False
            else:
                return True
        else:
            return False

    def agregar_proceso(self):
        if not self.bandera_proceso_automatico:
            if self.campos_validos():
                proceso = self.captura_proceso()
                self.cola_de_nuevos.append(proceso)
                self.bandera_limpiar_campos = True
            # "PEGRILOSO" modificar interfaz desde hilo
            elif self.le_tiempo_max.text() == "":
                self.le_tiempo_max.setText("Llene el campo con sus datos!")
            elif self.le_operador.text() == "":
                self.le_operador.setText("Llene el campo con sus datos!")
            elif self.le_operador.text() not in self.operadores:
                self.le_operador.setText("Llene el campo con sus datos!")
            elif self.le_operando_a.text() == "":
                self.le_operando_a.setText("Llene el campo con sus datos!")
            elif self.le_operando_a.text() == "0" or not_num(self.le_operando_a.text()):
                self.le_operando_a.setText("NUM ERR")
            elif self.le_operando_b.text() == "":
                self.le_operando_b.setText("Llene el campo con sus datos!")
            elif self.le_operando_b.text() == "0" or not_num(self.le_operando_b.text()):
                self.le_operando_b.setText("DIV 0/NUM")
            else:
                self.le_nombre_prog.setText("Hay algún error de captura")
        else:
            numero_procesos = self.sb_num_procesos.value()
            self.crea_procesos(numero_procesos)
        self.mostrar_textos()

    def muestra_texto_listos(self):
        self.texto_listos = ""
        procesos = self.memoria.cola_de_listos
        # Crea una cadena de texto para almacenar el formato
        texto_formateado = ""

        # Encabezados de la tabla
        headers = ["ID", "TME", "TT"]
        ancho_text_edit = self.pte_listos.width()  # Obtener el ancho actual del QPlainTextEdit

        # Obtener la fuente actual del QPlainTextEdit
        fuente = self.pte_listos.font()

        # Obtener las métricas de la fuente para calcular el ancho de cada columna en píxeles
        metrics = QFontMetrics(fuente)
        ancho_letra = metrics.averageCharWidth()

        # Calcular el ancho de cada columna de manera proporcional al ancho del QPlainTextEdit
        # ancho_columna = (ancho_text_edit - 49) / len(headers)
        ancho_columna = (ancho_text_edit - (len(headers) - 1) * 3 * 7) / len(headers)

        # Formatear los encabezados con el ancho calculado
        texto_formateado += " | ".join(f"{header:^{int(ancho_columna / ancho_letra)}}"
                                       for header in headers) + "\n"

        # Agregar una fila de guiones bajos (_) debajo de los encabezados
        # texto_formateado += " | ".join(['_' * int(ancho_columna / ancho_letra) for _ in headers]) + "\n"

        # Lista para almacenar las líneas de guiones bajos para cada columna
        lineas_guiones = []

        # Calcular el ancho de cada columna en función del contenido más largo en esa columna
        for header in headers:
            ancho_guiones = max(len(header), int(ancho_columna / ancho_letra))
            lineas_guiones.append("_" * ancho_guiones)

        # Crear una línea de encabezado con guiones bajos concatenados
        texto_formateado += " | ".join(lineas_guiones) + "\n"

        # Datos de los procesos
        for proceso in procesos:
            # Formatear los datos de cada proceso con el ancho calculado
            texto_formateado += f"{proceso.id:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{proceso.tiempo:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{proceso.tiempo_transcurrido:^{int(ancho_columna / ancho_letra)}}\n"
        self.texto_listos = texto_formateado

    def muestra_texto_ejecucion(self):
        self.texto_ejecucion = ""
        procesos_ejecucion = self.memoria.cola_de_ejecucion
        # Crea una cadena de texto para almacenar el formato
        texto_formateado = ""
        # Encabezados de la tabla
        headers = ["ID", "Ope", "OpeA", "OpeB", "TME", "TT", "TR"]

        # Obtener el ancho actual del QPlainTextEdit
        ancho_text_edit = self.pte_ejecucion.width()

        # Obtener la fuente actual del QPlainTextEdit
        fuente = self.pte_ejecucion.font()

        # Obtener las métricas de la fuente para calcular el ancho de cada columna en píxeles
        metrics = QFontMetrics(fuente)
        ancho_letra = metrics.averageCharWidth()

        # Calcular el ancho de cada columna de manera proporcional al ancho del QPlainTextEdit
        # ancho_columna = (ancho_text_edit - 133) / len(headers)
        # 3 son los espacios de ' | ', 7 es el ancho de cada caracter en la fuente actual
        ancho_columna = ((ancho_text_edit - (len(headers) - 1) * 3 * 7) / len(headers)) - 3

        # Formatear los encabezados con el ancho calculado
        texto_formateado += " | ".join(f"{header:^{int(ancho_columna / ancho_letra)}}"
                                       for header in headers) + "\n"

        # Agregar una fila de guiones bajos (_) debajo de los encabezados
        lineas_guiones = []

        # Calcular el ancho de cada columna en función del contenido más largo en esa columna
        for header in headers:
            ancho_guiones = max(len(header), int(ancho_columna / ancho_letra))
            lineas_guiones.append("_" * ancho_guiones)

        # Crear una línea de encabezado con guiones bajos concatenados
        texto_formateado += " | ".join(lineas_guiones) + "\n"

        # Datos de los procesos en ejecución
        for proceso in procesos_ejecucion:
            # Formatear los datos de cada proceso con el ancho calculado
            texto_formateado += f"{proceso.id:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{proceso.operacion:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{proceso.operando_a:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{proceso.operando_b:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{proceso.tiempo:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{proceso.tiempo_transcurrido:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{proceso.tiempo_restante:^{int(ancho_columna / ancho_letra)}}\n"

        self.texto_ejecucion = texto_formateado

    def muestra_texto_terminados(self):
        self.texto_terminados = ""
        procesos_terminados = self.cola_de_terminados
        # Crea una cadena de texto para almacenar el formato
        texto_formateado = ""
        # Encabezados de la tabla
        headers = ["ID", "OpeA", "Ope", "OpeB", "Res"]

        ancho_text_edit = self.pte_terminados.width()  # Obtener el ancho actual del QPlainTextEdit
        fuente = self.pte_terminados.font()
        metrics = QFontMetrics(fuente)
        ancho_letra = metrics.averageCharWidth()

        # ancho_columna = (ancho_text_edit - 91) / len(headers)
        ancho_columna = (ancho_text_edit - (len(headers) - 1) * 3 * 7) / len(headers)

        # Formatear los encabezados con el ancho calculado
        texto_formateado += " | ".join(f"{header:^{int(ancho_columna / ancho_letra)}}"
                                       for header in headers) + "\n"

        # Lista para almacenar las líneas de guiones bajos para cada columna
        lineas_guiones = []

        # Calcular el ancho de cada columna en función del contenido más largo en esa columna
        for header in headers:
            ancho_guiones = max(len(header), int(ancho_columna / ancho_letra))
            lineas_guiones.append("_" * ancho_guiones)

        # Crear una línea de guiones bajos concatenados
        texto_formateado += " | ".join(lineas_guiones) + "\n"

        # Datos de los procesos terminados
        for proceso in procesos_terminados:
            if proceso.resultado is None:
                resultado = "error"
            else:
                resultado = proceso.resultado
            # Formatear los datos de cada proceso con el ancho calculado
            texto_formateado += f"{proceso.id:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{proceso.operando_a:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{proceso.operacion:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{proceso.operando_b:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{resultado:^{int(ancho_columna / ancho_letra)}}\n"

        self.texto_terminados = texto_formateado

    def muestra_texto_bloqueados(self):
        self.texto_bloqueados = ""
        procesos_bloqueados = self.memoria.cola_de_bloqueados
        # Crea una cadena de texto para almacenar el formato
        texto_formateado = ""
        # Encabezados de la tabla
        headers = ["ID", "TTB"]

        ancho_text_edit = self.pte_bloqueados.width()  # Obtener el ancho actual del QPlainTextEdit
        fuente = self.pte_bloqueados.font()
        metrics = QFontMetrics(fuente)
        ancho_letra = metrics.averageCharWidth()
        ancho_columna = (ancho_text_edit - 28) / len(headers)
        # ancho_columna = (ancho_text_edit - (len(headers) - 1) * 3 * 7) / len(headers)

        # Formatear los encabezados con el ancho calculado
        texto_formateado += " | ".join(f"{header:^{int(ancho_columna / ancho_letra)}}"
                                       for header in headers) + "\n"

        # Lista para almacenar las líneas de guiones bajos para cada columna
        lineas_guiones = []

        # Calcular el ancho de cada columna en función del contenido más largo en esa columna
        for header in headers:
            ancho_guiones = max(len(header), int(ancho_columna / ancho_letra))
            lineas_guiones.append("_" * ancho_guiones)

        # Crear una línea de guiones bajos concatenados
        texto_formateado += " | ".join(lineas_guiones) + "\n"

        # Datos de los procesos bloqueados
        for proceso in procesos_bloqueados:
            ttb = proceso.dame_tiempo_transcurrido_bloqueado()  # Calcula el TTB
            # Formatear los datos de cada proceso con el ancho calculado
            texto_formateado += f"{proceso.id:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{ttb:^{int(ancho_columna / ancho_letra)}}\n"

        self.texto_bloqueados = texto_formateado

    def muestra_datos_de_procesos(self):
        self.texto_bloqueados = ""
        procesos_terminados = self.cola_de_terminados
        # Crea una cadena de texto para almacenar el formato
        texto_formateado = ""
        # Encabezados de la tabla
        headers = ["ID", "OpeA", "Ope", "OpeB", "Res", "TME", "TLl", "TFin", "TRet", "TRes", "TE", "TS"]

        ancho_text_edit = self.pte_bloqueados.width()  # Obtener el ancho actual del QPlainTextEdit
        fuente = self.pte_bloqueados.font()
        metrics = QFontMetrics(fuente)

        ancho_letra = metrics.averageCharWidth()

        ancho_columna = (ancho_text_edit - 226) / len(headers)

        # Formatear los encabezados con el ancho calculado
        texto_formateado += " | ".join(f"{header:^{int(ancho_columna / ancho_letra)}}"
                                       for header in headers) + "\n"

        # Lista para almacenar las líneas de guiones bajos para cada columna
        lineas_guiones = []

        # Calcular el ancho de cada columna en función del contenido más largo en esa columna
        for header in headers:
            ancho_guiones = max(len(header), int(ancho_columna / ancho_letra))
            lineas_guiones.append("_" * ancho_guiones)

        # Crear una línea de guiones bajos concatenados
        texto_formateado += " | ".join(lineas_guiones) + "\n"

        # Datos de los procesos terminados
        for proceso in procesos_terminados:
            if proceso.resultado is None:
                resultado = "error"
            else:
                resultado = proceso.resultado

            tme = proceso.tiempo
            tllegada = proceso.tiempo_llegada

            tfin = proceso.tiempo_finalizacion
            tret = proceso.tiempo_retorno
            tres = proceso.tiempo_respuesta
            te = proceso.tiempo_espera
            ts = proceso.tiempo_servicio

            # Formatea todos los datos, incluyendo los nuevos valores
            texto_formateado += f"{proceso.id:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{proceso.operando_a:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{proceso.operacion:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{proceso.operando_b:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{resultado:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{tme:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{tllegada:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{tfin:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{tret:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{tres:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{te:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{ts:^{int(ancho_columna / ancho_letra)}}\n"

        self.texto_bloqueados = texto_formateado

    def muestra_bcp(self):
        colas = {
            "Nuevo": self.cola_de_nuevos,
            "Listo": self.memoria.cola_de_listos,
            "Ejecucion": self.memoria.cola_de_ejecucion,
            "Bloqueado": self.memoria.cola_de_bloqueados,
            "Suspendido": self.cola_de_suspendidos,
            "Terminado": self.cola_de_terminados
        }

        # Encabezados de la tabla
        headers = ["Estado", "ID", "OpeA", "Ope", "OpeB", "Res", "TME", "TR", "TLl", "TFin", "TRet", "TRes", "TE", "TS"]

        # Obtener el ancho actual del QPlainTextEdit
        ancho_text_edit = self.pte_bloqueados.width()
        fuente = self.pte_bloqueados.font()
        metrics = QFontMetrics(fuente)
        ancho_letra = metrics.averageCharWidth()
        ancho_columna = (ancho_text_edit - 275) / len(headers)

        # Formatear los encabezados con el ancho calculado
        texto_formateado = " | ".join(f"{header:^{int(ancho_columna / ancho_letra)}}" for header in headers) + "\n"

        # Lista para almacenar las líneas de guiones bajos para cada columna
        lineas_guiones = ["_" * int(ancho_columna / ancho_letra) for _ in headers]

        # Crear una línea de guiones bajos concatenados
        texto_formateado += " | ".join(lineas_guiones) + "\n"

        # Datos de los procesos en cada cola
        for nombre_cola, cola in colas.items():
            for proceso in cola:
                """ 
                if nombre_cola == "Suspendido":
                    # Para la cola de suspendidos, solo mostrar el ID
                    texto_formateado += f"{nombre_cola:^{int(ancho_columna / ancho_letra)}} | " \
                                        f"{proceso.id:^{int(ancho_columna / ancho_letra)}}\n"
                """
                resultado = "N/A" if proceso.resultado is None else proceso.resultado
                tme = "N/A" if proceso.tiempo is None else proceso.tiempo
                tllegada = "N/A" if proceso.tiempo_llegada is None else proceso.tiempo_llegada
                tfin = "N/A" if proceso.tiempo_finalizacion is None else proceso.tiempo_finalizacion
                tret = "N/A" if proceso.tiempo_retorno is None else proceso.tiempo_retorno
                tres = "N/A" if proceso.tiempo_respuesta is None else proceso.tiempo_respuesta
                te = "N/A" if proceso.tiempo_espera is None else proceso.tiempo_espera
                ts = "N/A" if proceso.tiempo_servicio is None else proceso.tiempo_servicio

                # Calcular el Tiempo Restante (TR) como TME - tiempo_transcurrido
                tr = "N/A" if proceso.tiempo is None else proceso.tiempo - proceso.tiempo_transcurrido

                # Formatea todos los datos, incluyendo los nuevos valores
                texto_formateado += f"{nombre_cola:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{proceso.id:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{proceso.operando_a:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{proceso.operacion:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{proceso.operando_b:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{resultado:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{tme:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{tr:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{tllegada:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{tfin:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{tret:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{tres:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{te:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{ts:^{int(ancho_columna / ancho_letra)}}\n"

        self.texto_bloqueados = texto_formateado
