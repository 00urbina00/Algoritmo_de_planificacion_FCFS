import random
import threading
import time
from collections import deque
from unittest.mock import patch

from PySide2.QtCore import QTimer
from PySide2.QtGui import QFontMetrics
from PySide2.QtWidgets import QMainWindow, QPushButton, QLineEdit, QPlainTextEdit, QSpinBox, QFrame, QLabel

from espacio_memoria import Memoria
from proceso import *
from ui_mainwindow import Ui_MainWindow

TAMANIO_MEMORIA = 5

def crea_proceso(numero_programa):  # Aleatorio
    operadores = ['+', '-', '*', '/', '%', "%%"]
    operador = random.choice(operadores)
    operando_a = random.randint(0, 1000)
    operando_b = random.randint(0, 1000)
    tiempo = str(random.randint(6, 16))
    return Proceso(operador, operando_a, operando_b, tiempo, numero_programa)


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


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Colas de procesos (5 Estados)
        self.cola_de_nuevos = deque()  # Procesos en espera
        self.memoria = Memoria(TAMANIO_MEMORIA)  # Maximo de procesos (Listos, Ejecución y Bloqueados)
        self.cola_de_terminados = deque()  # Procesos terminados

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
        self.texto_nuevos = "0"
        self.texto_listos = "Sin procesos listos."
        self.texto_ejecucion = "Sin procesos en ejecucion."
        self.texto_terminados = "No hay procesos terminados."
        self.texto_bloqueados = "No hay procesos bloqueados."

        # ----------------------------------------------------------------|
        # - Contadores
        # ----------------------------------------------------------------|
        self.texto_memoria_restante = str(TAMANIO_MEMORIA)
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
        # - Banderas - pulsaciones
        # ----------------------------------------------------------------|
        self.bandera_i = False
        self.bandera_e = False
        self.bandera_p = False
        self.bandera_c = False
        self.bandera_n = False
        self.bandera_b = False
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
        self.le_memoria = self.findChild(QLineEdit, "le_memoria_restante")
        self.le_procesos_nuevos = self.findChild(QLineEdit, "le_procesos_nuevos")
        self.le_tiempo_global = self.findChild(QLineEdit, "le_tiempo_global")
        # Spinbox numero de procesos
        self.sb_num_procesos = self.findChild(QSpinBox, "sb_num_procesos")
        # Frame captura de datos
        self.frame_captura = self.findChild(QFrame, "frame_7")
        self.habilitar_campos()
        # ----------------------------------------------------------------------------------------|
        # Eventos
        # -------------------------------------------------------------------------|
        # Habilitar / Deshabilitar frame
        self.btn_habilitar_capturar_proceso.clicked.connect(self.habilitar_campos)
        # Ejecutar el simulador
        self.btn_iniciar.clicked.connect(self.back_end)
        self.btn_reiniciar.clicked.connect(self.reiniciar_programa)
        # Agregar proceso
        self.btn_agregar.clicked.connect(self.agregar_proceso)
        self.btn_agregar_procesos.clicked.connect(self.agregar_proceso)
        # Limpiar consolas
        # self.btn_limpiar.clicked.connect(self.limpiar)
        # -------------------------------------------------------------------------|

    # Funciones
    # -----------------------------------------------------------------------------------
    def reiniciar_programa(self):
        self.btn_reiniciar.setEnabled(False)  # Deshabilitar el boton
        self.btn_reiniciar.setStyleSheet("QPushButton:disabled { color: gray; border:none;}")
        self.releaseMemory()
        self.id_proceso = 0
        self.actualiza_texto_contadores()
        self.iniciliza_textos()
    
    def releaseMemory(self):
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
            self.releaseMemory()
            event.accept()  # Permite que la ventana se cierre
            

    def keyPressEvent(self, event):
        texto_tecla = str(event.text())
        if texto_tecla == 'i':
            self.bandera_i = True
        elif texto_tecla == 'e':
            self.bandera_e = True
        elif texto_tecla == 'p':
            self.label_ejecucion.setText("Pausa")
            self.label_ejecucion.setStyleSheet("color: red;")
            self.bandera_p = True
        elif texto_tecla == 'c':
            self.label_ejecucion.setText("Ejecución")
            self.label_ejecucion.setStyleSheet("color: green;")
            self.bandera_p = False
            self.bandera_b = False
            with self.pause_condition:
                self.pause_condition.notify()
        elif texto_tecla == 'n':
            self.bandera_n = True
        elif texto_tecla == 'b':
            self.label_ejecucion.setText("Pausa")
            self.label_ejecucion.setStyleSheet("color: red;")
            self.bandera_b = True

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

        self.le_memoria.setText(self.texto_memoria_restante)  # Lotes pendientes
        self.le_procesos_nuevos.setText(self.texto_nuevos)  # Procesos pendientes

        self.le_tiempo_global.setText(self.texto_tiempo_global)  # Tiempo global
        if self.bandera_limpiar_campos:
            self.le_tiempo_max.clear()
            self.le_operador.clear()
            self.le_operando_a.clear()
            self.le_operando_b.clear()
            self.bandera_limpiar_campos = False

    def actualiza_texto_contadores(self):
        self.texto_nuevos = str(len(self.cola_de_nuevos))
        self.texto_memoria_restante = str(self.memoria.espacio)
        self.texto_tiempo_global = str(self.tiempo_global)

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
            # self.hilo.join()  # Espera a que el hilo termine de manera ordenada

    def back_end(self):
        if not self.en_ejecucion and self.cola_de_nuevos:
            if self.hilo:
                self.hilo.join()
            self.en_ejecucion = True
            self.hilo = threading.Thread(target=self.correr_interfaz)
            self.hilo.start()

    def correr_interfaz(self):
        if self.cola_de_nuevos:
            self.correr_fcfs()
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
            self.actualiza_texto_contadores()
            num_procesos -= 1

    def ingresa_procesos_a_listos(self):
        # Mientras quede espacio en memoria y la cola de nuevos no esté vacía: agregar a listos
        while self.memoria.hay_espacio() and self.cola_de_nuevos:  # Este ciclo llena la cola de listos O(5)
            proceso = self.cola_de_nuevos.popleft()
            proceso.tiempo_llegada = self.tiempo_global
            self.memoria.agrega_a_listo(proceso)
            self.actualiza_texto_contadores()
        # La cola de listos esta llena - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    def correr_fcfs(self):
        self.bandera_detener = False
        self.en_ejecucion = True
        while self.cola_de_nuevos and not self.bandera_detener:  # Este ciclo recorre la cola de nuevos O(n)
            self.ingresa_procesos_a_listos()  # Ingresa todos los procesos posibles a listos
            while self.memoria.procesos_en_memoria() and not self.bandera_detener:  # Mientras haya procesos en listos:
                self.iniciliza_textos()
                self.mostrar_textos()  # Se formatea el texto de los procesos en listo
                self.ingresa_procesos_a_listos()  # Verifica si hay espacio y, agrega otro proceso a listos
                proceso = self.memoria.entra_proceso_ejecucion()  # Mete proceso a la cola de ejecucion (solo cabe 1)
                self.mostrar_textos()
                self.ejecucion_del_proceso(proceso)
        self.iniciliza_textos()
        self.actualiza_texto_contadores()
        self.muestra_datos_de_procesos()
        self.en_ejecucion = False
        self.bandera_detener = False 
        self.terminar_hilo()
        self.btn_reiniciar.setStyleSheet("QPushButton:enabled { color: red; }")
        self.btn_reiniciar.setEnabled(True)  # Deshabilitar el boton
        # Se terminaron todos los procesos!

    def administrar_pausa(self):
        if self.bandera_b:
            self.muestra_bcp() # Mostrar BCP
        while self.bandera_p or self.bandera_b and not self.bandera_detener:
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
        self.memoria.saca_de_ejecucion()
        self.cola_de_terminados.append(proceso)
        self.bandera_e = False
        self.mostrar_textos()

    def administrar_nuevo(self):
        self.id_proceso += 1
        proceso = crea_proceso(self.id_proceso)
        self.cola_de_nuevos.append(proceso)
        self.actualiza_texto_contadores()
        self.bandera_n = False
    
    def proceso_completado(self, proceso):
        proceso.ejecutar()
        proceso.tiempo_finalizacion = self.tiempo_global
        proceso.calcula_tiempo_retorno()
        proceso.calcula_tiempo_servicio()
        proceso.calcula_tiempo_espera()
        self.cola_de_terminados.append(proceso)
        self.memoria.saca_de_ejecucion()

    def tiempo_de_ejecucion(self, proceso):
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

    def ejecucion_del_proceso(self, proceso):
        while proceso.tiempo_restante > 0 and not self.bandera_detener:  # O(16) tiempo maximo
            self.mostrar_textos()
            with self.pause_condition:  # Consumo de tiempo de CPU
                self.administrar_pausa()
            if self.bandera_i:
                if self.memoria.hay_ejecucion():
                    self.administrar_interrupcion(proceso)
                    print("Interrupcion")
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
                if self.memoria.hay_bloqueados():
                    self.muestra_texto_bloqueados()
                    # Se puede ejecutar bloqueados y continuar con la ejecucion normal del proceso
                    # Si hay algún proceso bloqueado
                    # En cada ciclo de "tiempo" se descontará una unidad de tiempo a cada proceso bloqueado
                    # Si el proceso termina su estado bloqueado sale y entra de nuevo a listo (en clase Memoria)
                    self.memoria.ciclo_bloqueados()
                    self.muestra_texto_bloqueados()
                    self.mostrar_textos()

                # Ejecución del proceso de manera normal

                # simular_segundo_transcurrido_pruebas()
                time.sleep(1)
                self.tiempo_global += 1  # El tiempo global corre siempre
                self.actualiza_texto_contadores()
                if self.memoria.cola_de_ejecucion:  # Solo ejecuta procesos en ejecucion
                    self.tiempo_de_ejecucion(proceso)
                else:   # En caso de no haber procesos en ejecucion se deteiene el ciclo
                    break

        if proceso is not None and proceso.terminado and not proceso.error:
            self.proceso_completado(proceso)
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
        self.actualiza_texto_contadores()

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
        ancho_columna = (ancho_text_edit - (len(headers) - 1) * 3 * 7) / len(headers)

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
        headers = ["ID", "OpeA", "Ope", "OpeB", "Res", "TME", "TLl", "TFin", "TRet", "TE", "TS"]

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
                                f"{te:^{int(ancho_columna / ancho_letra)}} | " \
                                f"{ts:^{int(ancho_columna / ancho_letra)}}\n"

        self.texto_bloqueados = texto_formateado
        
    def muestra_bcp(self):
        colas = {
            "Nuevo": self.cola_de_nuevos,
            "Listo": self.memoria.cola_de_listos,
            "Ejecucion": self.memoria.cola_de_ejecucion,
            "Bloqueado": self.memoria.cola_de_bloqueados,
            "Terminado": self.cola_de_terminados
        }

        # Encabezados de la tabla
        headers = ["Estado", "ID", "OpeA", "Ope", "OpeB", "Res", "TME", "TLl", "TFin", "TRet", "TE", "TS"]

        # Obtener el ancho actual del QPlainTextEdit
        ancho_text_edit = self.pte_bloqueados.width()
        fuente = self.pte_bloqueados.font()
        metrics = QFontMetrics(fuente)
        ancho_letra = metrics.averageCharWidth()
        ancho_columna = (ancho_text_edit - 226) / len(headers)

        # Formatear los encabezados con el ancho calculado
        texto_formateado = " | ".join(f"{header:^{int(ancho_columna / ancho_letra)}}" for header in headers) + "\n"

        # Lista para almacenar las líneas de guiones bajos para cada columna
        lineas_guiones = ["_" * int(ancho_columna / ancho_letra) for _ in headers]
        
        # Crear una línea de guiones bajos concatenados
        texto_formateado += " | ".join(lineas_guiones) + "\n"

        # Datos de los procesos en cada cola
        for nombre_cola, cola in colas.items():
            for proceso in cola:
                resultado = "N/A" if proceso.resultado is None else proceso.resultado
                tme = "N/A" if proceso.tiempo is None else proceso.tiempo
                tllegada = "N/A" if proceso.tiempo_llegada is None else proceso.tiempo_llegada
                tfin = "N/A" if proceso.tiempo_finalizacion is None else proceso.tiempo_finalizacion
                tret = "N/A" if proceso.tiempo_retorno is None else proceso.tiempo_retorno
                te = "N/A" if proceso.tiempo_espera is None else proceso.tiempo_espera
                ts = "N/A" if proceso.tiempo_servicio is None else proceso.tiempo_servicio

                # Formatea todos los datos, incluyendo los nuevos valores
                texto_formateado += f"{nombre_cola:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{proceso.id:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{proceso.operando_a:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{proceso.operacion:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{proceso.operando_b:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{resultado:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{tme:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{tllegada:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{tfin:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{tret:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{te:^{int(ancho_columna / ancho_letra)}} | " \
                                    f"{ts:^{int(ancho_columna / ancho_letra)}}\n"

        self.texto_bloqueados = texto_formateado