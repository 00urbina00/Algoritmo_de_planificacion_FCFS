import pandas as pd
import random
import threading
import time

from espacio_memoria import Memoria
from collections import deque

from PySide2.QtWidgets import QMainWindow, QPushButton, QLineEdit, QPlainTextEdit, QSpinBox, QFrame, QLabel
from PySide2.QtCore import QTimer
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
        print("No es un numero")
        return True


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Colas de procesos                         (5 Estados)
        self.cola_de_nuevos = deque()               # Procesos en espera
        self.memoria = Memoria(TAMANIO_MEMORIA)     # Maximo de procesos (Listos, Ejecución y Bloqueados)
        self.cola_de_terminados = deque()           # Procesos terminados

        # Hilo de ejecucion
        self.hilo = None
        self.pause_condition = threading.Condition()
        
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
        # ----------------------------------------------------------------|
        # Definicion de widgets
        # ----------------------------------------------------------------------------------------|
        # Label
        self.label_ejecucion = self.findChild(QLabel, "lb_pausa")
        # Boton
        self.btn_iniciar = self.findChild(QPushButton, "pb_iniciar")
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
        # Agregar proceso
        self.btn_agregar.clicked.connect(self.agregar_proceso)
        self.btn_agregar_procesos.clicked.connect(self.agregar_proceso)
        # Limpiar consolas
        self.btn_limpiar.clicked.connect(self.limpiar)
        # -------------------------------------------------------------------------|
    # Funciones
    # -----------------------------------------------------------------------------------
    def limpiar(self):
        if not self.en_ejecucion:
            # Liberar memoria de lotes antiguos
            for lote in self.cola_de_lotes_terminados:
                lote.clear()
            self.cola_de_lotes_terminados.clear()
            # Limpiar los paneles
            self.texto_lote_actual = "Sin lotes pendientes."
            self.texto_lotes_en_ejecucion = "Sin lotes a ejecutar."
            self.texto_lotes_terminados = "No hay lotes terminados."
        else:
            print("Proceso en ejecucion")

    def closeEvent(self, event):  # Detectar si se va a cerrar el programa y protegerlo
        if self.en_ejecucion and not self.bandera_detener:
            self.bandera_detener = True
            print("Se canceló la ejecución del programa.")
            event.ignore()  # Evita que la ventana se cierre
        else:
            event.accept()  # Permite que la ventana se cierre

    def keyPressEvent(self, event):
        texto_tecla = str(event.text())
        if texto_tecla == 'i':
            print("Interrupcion")
            self.bandera_i = True
        elif texto_tecla == 'e':
            print("Error")
            self.bandera_e = True
        elif texto_tecla == 'p':
            self.label_ejecucion.setText("Pausa")
            self.label_ejecucion.setStyleSheet("color: red;")
            print("Pausa")
            self.bandera_p = True
        elif texto_tecla == 'c':
            self.label_ejecucion.setText("Ejecución")
            self.label_ejecucion.setStyleSheet("color: green;")
            print("Continuar")
            self.bandera_p = False
            with self.pause_condition:
                self.pause_condition.notify()

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
            print("Limpiando campos")
            self.le_tiempo_max.clear()
            self.le_operador.clear()
            self.le_operando_a.clear()
            self.le_operando_b.clear()
            self.bandera_limpiar_campos = False

    def iniciar_hilo(self):
        if not self.en_ejecucion and self.cola_de_nuevos:
            self.en_ejecucion = True
            self.hilo = threading.Thread(target=self.correr_interfaz)
            self.hilo.start()
        elif not self.en_ejecucion and self.bandera_proceso_automatico:
            self.en_ejecucion = True
            self.hilo = threading.Thread(target=self.correr_interfaz)
            self.hilo.start()
        elif self.en_ejecucion:
            print("El hilo ya está en ejecución")
        else:
            print("Sin procesos a ejecutar")

    def detener_hilo(self):
        if self.en_ejecucion:
            self.en_ejecucion = False
            # self.hilo.join()  # Espera a que el hilo termine de manera ordenada
        else:
            print("El hilo no está en ejecución")

    def esperar_hilo(self):
        if self.hilo:
            self.hilo.join()

    def back_end(self):
        self.texto_procesos_pendientes = str(len(self.cola_de_nuevos))
        if not self.en_ejecucion:
            self.esperar_hilo()
            self.iniciar_hilo()
        else:
            print("En ejecución")

    def correr_interfaz(self):
        if self.cola_de_nuevos:
            self.correr_fcfs()
            self.texto_nuevos = str(len(self.cola_de_nuevos))
            self.texto_memoria_restante = str(self.memoria.espacio)
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
            num_procesos -= 1
        self.texto_nuevos = str(len(self.cola_de_nuevos))

    def ingresa_procesos_a_listos(self):
        # Mientras quede espacio en memoria y la cola de nuevos no esté vacía: agregar a listos
        while self.memoria.hay_espacio() and len(self.cola_de_nuevos) > 0: # Este ciclo llena la cola de listos O(5)
            proceso = self.cola_de_nuevos.popleft()
            print("Entró proceso a listos: " + str(proceso.id) + ", Tiempo restante: "+ str(proceso.tiempo_restante))
            self.texto_nuevos = str(len(self.cola_de_nuevos))
            self.memoria.agrega_a_listo(proceso)
        # La cola de listos esta llena - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    def correr_fcfs(self):
        self.texto_nuevos = str(len(self.cola_de_nuevos))
        proceso = None
        while self.cola_de_nuevos and not self.bandera_detener:      # Este ciclo recorre la cola de nuevos O(n)
            print("Cola de nuevos cantidad:" + str(len(self.cola_de_nuevos)))
            self.ingresa_procesos_a_listos()
            while len(self.memoria.cola_de_listos) > 0:                                 # O(5)  maximo numero de procesos
                self.ingresa_procesos_a_listos()    # Verifica y si es posible, agrega procesos a listos
                if self.bandera_detener:
                    break
                while proceso.tiempo_restante > 0 and not self.bandera_detener:          # O(16) tiempo maximo
                    # Ejecucion del proceso 
                    # -----------------------------------------------------------------------------
                    if self.memoria.hay_bloqueados():
                        print("Hay procesos bloqueados")
                        # Se puede ejecutar bloqueados y continuar con la ejecucion normal del proceso
                        # Si hay algún proceso bloqueado
                        # En cada ciclo de "tiempo" se descontará una unidad de tiempo a cada proceso bloqueado
                        # Si el proceso termina su estado bloqueado sale y entra de nuevo a listo (en clase Memoria)
                        self.memoria.ciclo_bloqueados()    
                        
                    with self.pause_condition:  # Consumo de tiempo de CPU (Proceso nulo)
                        while self.bandera_p and not self.bandera_detener:
                            self.pause_condition.wait()
                    
                    if self.bandera_i:
                        print("Interrupcion")
                        # Proceso entra a bloqueados
                        self.bandera_i = False
                        proceso.set_bloqueado()
                        self.memoria.agrega_a_bloqueados(proceso)
                        break
                
                    elif self.bandera_e:
                        print("Error")
                        # Proceso finalizado por error (sale a terminados)
                        proceso.resultado('e') # Se da por terminado
                        self.cola_de_terminados.append(proceso)
                        self.memoria.saca_de_listo()
                        self.bandera_e = False
                        break
                    else:
                        # Ejecucion del proceso de manera normal
                        # print("Tiempo restante: " + proceso.get_tiempo_restante())
                        proceso.segundo_transcurrido()
                        print("Proceso " + str(proceso.id) + ", Tiempo restante: "+ str(proceso.tiempo_restante))
                        time.sleep(1)  # Simula un segundo transcurrido
                        self.tiempo_global += 1
                        self.texto_tiempo_global = str(self.tiempo_global)
                        if proceso.tiempo_restante == 0:
                            proceso.terminado = True
                if proceso.terminado:
                    print("Proceso terminado!")
                    # Proceso terminado
                    proceso.ejecutar()
                    self.cola_de_terminados.append(proceso)
                    self.memoria.saca_de_listo()
        print("Todos los procesos han sido terminados")
        self.detener_hilo()
        self.bandera_detener = False
        print("Se terminaron todos los procesos!")

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
                self.texto_procesos_pendientes = str(len(self.cola_de_nuevos))
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
            print("Numero de procesos: " + str(numero_procesos))
            self.crea_procesos(numero_procesos)
            self.texto_procesos_pendientes = str(len(self.cola_de_nuevos))

    def formato_texto_lote_actual(self, lote):
        # Definir encabezados para el lote
        encabezados_lote = ["ID", "TME", "TT"]

        # Definir datos para el lote
        datos_lote = [f"{lote.get_num_lote()}", f"{lote.get_tiempo_maximo()}", f"{lote.get_tiempo_transcurrido()}"]

        # Column lengths configuration
        COLUMN_LENGTHS = {
            "encabezados_lote": 21,
            "datos_lote": 21,
            "encabezados_procesos": 17,
            "datos_procesos": 17,
            "encabezados_terminados": 13
        }

        # Get column length for a specific section
        def get_column_length(section):
            return COLUMN_LENGTHS.get(section, 0)

        # Use column length configuration
        formato_columna = lambda section: f"{{:^{get_column_length(section)}}}"

        # Construir una lista de líneas para la tabla
        lineas_tabla = []

        # Encabezados del lote
        linea_encabezado_lote = " | ".join(formato_columna("encabezados_lote").format(encabezado) for encabezado in encabezados_lote)
        lineas_tabla.append(linea_encabezado_lote)

        # Datos del lote
        linea_datos_lote = " | ".join(formato_columna("datos_lote").format(valor) for valor in datos_lote)
        lineas_tabla.append(linea_datos_lote)

        # Línea de separación para el lote
        linea_separacion_lote = "-".join([""] * (get_column_length("encabezados_lote") * len(encabezados_lote) + len(encabezados_lote) - 1))
        lineas_tabla.append(linea_separacion_lote)

        # Encabezados para los procesos en ejecución
        encabezados_procesos = ["IDP", "TMEP", "TT"]
        linea_encabezado_procesos = " | ".join(formato_columna("encabezados_procesos").format(encabezado) for encabezado in encabezados_procesos)
        lineas_tabla.append(linea_encabezado_procesos)

        # Datos de los procesos en ejecución
        procesos = lote.procesos
        lineas_tabla.extend(" | ".join(formato_columna("datos_procesos").format(proceso.id), formato_columna("datos_procesos").format(proceso.tiempo), formato_columna("datos_procesos").format(proceso.tiempo_transcurrido)) for proceso in procesos)

        # Unir todas las líneas en una sola cadena
        tabla_completa = "\n".join(lineas_tabla)
        self.texto_lote_actual = tabla_completa

    def formato_texto_lotes_en_ejecucion(self, proceso):
        """
        Generate a formatted text table for the running batches.

        Args:
            proceso (Proceso): The process object.

        Returns:
            None
        """
        # Definir encabezados
        encabezados = [" ID", "Ope", "TME", " TT", " TR"]

        # Definir datos como un DataFrame
        datos = pd.DataFrame({
            "ID": [proceso.get_id()],
            "Ope": [proceso.get_operacion()],
            "TME": [proceso.get_tiempo()],
            "TT": [proceso.get_tiempo_transcurrido()],
            "TR": [proceso.get_tiempo_restante()]
        })

        # Column lengths configuration
        COLUMN_LENGTHS = {
            "encabezados_lote": 21,
            "datos_lote": 21,
            "encabezados_procesos": 17,
            "datos_procesos": 17,
            "encabezados_terminados": 13
        }

        # Get column length for a specific section
        def get_column_length(section):
            return COLUMN_LENGTHS.get(section, 0)

        # Use column length configuration
        formato_columna = lambda section: f"{{:^{get_column_length(section)}}}"

        # Construir una lista de líneas para la tabla
        lineas_tabla = []

        # Encabezados
        linea_encabezado = " | ".join(formato_columna("encabezados_procesos").format(encabezado) for encabezado in encabezados)
        lineas_tabla.append(linea_encabezado)

        # Línea de separación
        linea_separacion = "-" * (get_column_length("encabezados_procesos") * len(encabezados) + len(encabezados) - 1)
        lineas_tabla.append(linea_separacion)

        # Datos
        for _, fila in datos.iterrows():
            linea_datos = " | ".join(formato_columna("datos_procesos").format(valor) for valor in fila)
            lineas_tabla.append(linea_datos)

        # Unir todas las líneas en una sola cadena
        tabla_completa = "\n".join(lineas_tabla)
        self.texto_lotes_en_ejecucion = tabla_completa

    def formato_texto_procesos_terminados(self, lote, proceso):
        # Definir encabezados
        encabezados = [" IDL", " IDP", " OA", " Ope", " OB", " Res"]
        # Column lengths configuration
        COLUMN_LENGTHS = {
            "encabezados_lote": 21,
            "datos_lote": 21,
            "encabezados_procesos": 17,
            "datos_procesos": 17,
            "encabezados_terminados": 13
        }

        # Get column length for a specific section
        def get_column_length(section):
            return COLUMN_LENGTHS.get(section, 0)

        # Use column length configuration
        formato_columna = lambda section: f"{{:^{get_column_length(section)}}}"

        # Construir una lista de líneas para la tabla
        lineas_tabla = []

        if self.texto_lotes_terminados == "No hay lotes terminados.":
            # Si es la primera vez que se agrega, imprimir el encabezado
            linea_encabezado = " | ".join(formato_columna("encabezados_terminados").format(encabezado) for encabezado in encabezados)
            lineas_tabla.append(linea_encabezado)
            # Línea de separación
            linea_separacion = "-" * (get_column_length("encabezados_terminados") * len(encabezados) + len(encabezados) - 1)
            lineas_tabla.append(linea_separacion)
        resultado = f"{proceso.get_resultado()}"
        if resultado == '-1':
            resultado = 'error'
        # Datos
        datos = [
            [f"{lote.get_num_lote()}", f"{proceso.get_id()}", f"{proceso.get_operando_a()}",
             f"{proceso.get_operacion()}", f"{proceso.get_operando_b()}", resultado]
        ]
        for fila in datos:
            linea_datos = " | ".join(formato_columna("encabezados_terminados").format(valor) for valor in fila)
            lineas_tabla.append(linea_datos)

        # Unir todas las líneas en una sola cadena
        tabla_completa = "\n".join(lineas_tabla)

        if self.texto_lotes_terminados == "No hay lotes terminados.":
            self.texto_lotes_terminados = tabla_completa
        else:
            self.texto_lotes_terminados += "\n" + tabla_completa
