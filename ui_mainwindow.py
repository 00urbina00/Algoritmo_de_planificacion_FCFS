# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1372, 979)
        MainWindow.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(self.frame_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(130, 0))
        self.label.setMaximumSize(QSize(160, 16777215))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.le_memoria_restante = QLineEdit(self.groupBox_4)
        self.le_memoria_restante.setObjectName(u"le_memoria_restante")
        self.le_memoria_restante.setMinimumSize(QSize(120, 25))
        self.le_memoria_restante.setMaximumSize(QSize(50, 16777215))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        self.le_memoria_restante.setFont(font1)
        self.le_memoria_restante.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.le_memoria_restante.setFrame(False)
        self.le_memoria_restante.setAlignment(Qt.AlignCenter)
        self.le_memoria_restante.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.le_memoria_restante)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.frame_5 = QFrame(self.groupBox_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(900, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_8)

        self.pb_iniciar = QPushButton(self.frame_5)
        self.pb_iniciar.setObjectName(u"pb_iniciar")
        self.pb_iniciar.setMinimumSize(QSize(100, 25))
        self.pb_iniciar.setFont(font)
        self.pb_iniciar.setStyleSheet(u"\n"
"QPushButton {\n"
"   \n"
"	background-color: rgb(220, 220, 220);\n"
"	\n"
"	color: rgb(0, 85, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"   \n"
"	background-color: rgb(190, 190, 190);\n"
"	\n"
"	color: rgb(0, 170, 0);\n"
"}")
        self.pb_iniciar.setCheckable(False)

        self.horizontalLayout_13.addWidget(self.pb_iniciar)

        self.pb_re_iniciar = QPushButton(self.frame_5)
        self.pb_re_iniciar.setObjectName(u"pb_re_iniciar")
        self.pb_re_iniciar.setMinimumSize(QSize(70, 25))
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(True)
        font2.setWeight(50)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.pb_re_iniciar.setFont(font2)
        self.pb_re_iniciar.setAcceptDrops(False)
        self.pb_re_iniciar.setStyleSheet(u"\n"
"QPushButton {\n"
"   \n"
"	background-color: rgb(220, 220, 220);\n"
"	\n"
"	color: rgb(255, 85, 0);\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.pb_re_iniciar)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(70, 0))
        self.label_12.setMaximumSize(QSize(80, 16777215))
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_12)

        self.sb_quantum = QSpinBox(self.frame_5)
        self.sb_quantum.setObjectName(u"sb_quantum")
        self.sb_quantum.setMinimumSize(QSize(40, 25))
        self.sb_quantum.setFont(font1)
        self.sb_quantum.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sb_quantum.setWrapping(False)
        self.sb_quantum.setFrame(True)
        self.sb_quantum.setAlignment(Qt.AlignCenter)
        self.sb_quantum.setReadOnly(False)
        self.sb_quantum.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.sb_quantum.setMinimum(3)
        self.sb_quantum.setMaximum(15)
        self.sb_quantum.setValue(5)

        self.horizontalLayout_13.addWidget(self.sb_quantum)

        self.horizontalSpacer_9 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)

        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(111, 0))
        self.label_10.setMaximumSize(QSize(220, 16777215))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_10)

        self.sb_num_procesos = QSpinBox(self.frame_5)
        self.sb_num_procesos.setObjectName(u"sb_num_procesos")
        self.sb_num_procesos.setMinimumSize(QSize(40, 25))
        self.sb_num_procesos.setFont(font1)
        self.sb_num_procesos.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sb_num_procesos.setWrapping(False)
        self.sb_num_procesos.setFrame(True)
        self.sb_num_procesos.setAlignment(Qt.AlignCenter)
        self.sb_num_procesos.setReadOnly(False)
        self.sb_num_procesos.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.sb_num_procesos.setMinimum(1)
        self.sb_num_procesos.setValue(5)

        self.horizontalLayout_13.addWidget(self.sb_num_procesos)

        self.pb_agregar_procesos = QPushButton(self.frame_5)
        self.pb_agregar_procesos.setObjectName(u"pb_agregar_procesos")
        self.pb_agregar_procesos.setMinimumSize(QSize(0, 25))
        self.pb_agregar_procesos.setFont(font)
        self.pb_agregar_procesos.setStyleSheet(u"\n"
"QPushButton {\n"
"   \n"
"	background-color: rgb(220, 220, 220);\n"
"	\n"
"	color: rgb(0, 85, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"   \n"
"	background-color: rgb(190, 190, 190);\n"
"	\n"
"	color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_13.addWidget(self.pb_agregar_procesos)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(111, 0))
        self.label_9.setMaximumSize(QSize(220, 16777215))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.le_procesos_nuevos = QLineEdit(self.frame_5)
        self.le_procesos_nuevos.setObjectName(u"le_procesos_nuevos")
        self.le_procesos_nuevos.setMinimumSize(QSize(50, 25))
        self.le_procesos_nuevos.setMaximumSize(QSize(50, 16777215))
        self.le_procesos_nuevos.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.le_procesos_nuevos.setFrame(False)
        self.le_procesos_nuevos.setAlignment(Qt.AlignCenter)
        self.le_procesos_nuevos.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.le_procesos_nuevos)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_4.addWidget(self.frame_5)


        self.gridLayout_4.addWidget(self.groupBox_4, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 1000))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.groupBox = QGroupBox(self.frame_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 350))
        self.groupBox.setMaximumSize(QSize(495, 600))
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(0, 85, 255);")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pte_listos = QPlainTextEdit(self.groupBox)
        self.pte_listos.setObjectName(u"pte_listos")
        self.pte_listos.setMinimumSize(QSize(378, 0))
        self.pte_listos.setMaximumSize(QSize(1677777, 16777215))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(10)
        self.pte_listos.setFont(font3)
        self.pte_listos.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 253, 51);")
        self.pte_listos.setReadOnly(True)
        self.pte_listos.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_6.addWidget(self.pte_listos, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(400, 350))
        self.groupBox_2.setMaximumSize(QSize(16777215, 600))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(0, 170, 0);")
        self.gridLayout_7 = QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pte_ejecucion = QPlainTextEdit(self.groupBox_2)
        self.pte_ejecucion.setObjectName(u"pte_ejecucion")
        self.pte_ejecucion.setFont(font3)
        self.pte_ejecucion.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 253, 51);")
        self.pte_ejecucion.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_7.addWidget(self.pte_ejecucion, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(500, 350))
        self.groupBox_3.setMaximumSize(QSize(16777215, 600))
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(255, 0, 0);")
        self.gridLayout_8 = QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.pte_terminados = QPlainTextEdit(self.groupBox_3)
        self.pte_terminados.setObjectName(u"pte_terminados")
        self.pte_terminados.setFont(font3)
        self.pte_terminados.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 253, 51);")
        self.pte_terminados.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_8.addWidget(self.pte_terminados, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_3)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.groupBox_9 = QGroupBox(self.frame_4)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMinimumSize(QSize(0, 190))
        self.groupBox_9.setFont(font)
        self.groupBox_9.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(0, 85, 255);")
        self.gridLayout_12 = QGridLayout(self.groupBox_9)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.pte_bloqueados = QPlainTextEdit(self.groupBox_9)
        self.pte_bloqueados.setObjectName(u"pte_bloqueados")
        self.pte_bloqueados.setFont(font3)
        self.pte_bloqueados.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 253, 51);")
        self.pte_bloqueados.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_12.addWidget(self.pte_bloqueados, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_9, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.groupBox_5 = QGroupBox(self.frame_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(0, 50))
        self.groupBox_5.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(111, 0))
        self.label_2.setMaximumSize(QSize(111, 16777215))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_tiempo_global = QLineEdit(self.groupBox_5)
        self.le_tiempo_global.setObjectName(u"le_tiempo_global")
        self.le_tiempo_global.setMinimumSize(QSize(100, 25))
        self.le_tiempo_global.setMaximumSize(QSize(100, 16777215))
        self.le_tiempo_global.setFont(font)
        self.le_tiempo_global.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.le_tiempo_global.setFrame(False)
        self.le_tiempo_global.setAlignment(Qt.AlignCenter)
        self.le_tiempo_global.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.le_tiempo_global)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_2)

        self.frame_6 = QFrame(self.groupBox_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(900, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_52 = QSpacerItem(43, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_52)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(111, 0))
        self.label_3.setMaximumSize(QSize(111, 16777215))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.le_tiempo_global_2 = QLineEdit(self.frame_6)
        self.le_tiempo_global_2.setObjectName(u"le_tiempo_global_2")
        self.le_tiempo_global_2.setMinimumSize(QSize(120, 25))
        self.le_tiempo_global_2.setMaximumSize(QSize(100, 16777215))
        self.le_tiempo_global_2.setFont(font)
        self.le_tiempo_global_2.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.le_tiempo_global_2.setFrame(False)
        self.le_tiempo_global_2.setAlignment(Qt.AlignCenter)
        self.le_tiempo_global_2.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.le_tiempo_global_2)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_2 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.lb_pausa = QLabel(self.frame_6)
        self.lb_pausa.setObjectName(u"lb_pausa")
        self.lb_pausa.setMinimumSize(QSize(111, 0))
        self.lb_pausa.setFont(font)
        self.lb_pausa.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.lb_pausa.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lb_pausa)

        self.horizontalSpacer_7 = QSpacerItem(260, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)


        self.horizontalLayout_7.addWidget(self.frame_6)


        self.gridLayout_5.addWidget(self.groupBox_5, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 160))
        self.frame_7.setMaximumSize(QSize(16777215, 180))
        self.frame_7.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox_6 = QGroupBox(self.frame_7)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(100, 140))
        self.groupBox_6.setMaximumSize(QSize(16777215, 170))
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet(u"background-color: rgb(190, 190, 190);")
        self.gridLayout_10 = QGridLayout(self.groupBox_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.Marco_memoria = QFrame(self.groupBox_6)
        self.Marco_memoria.setObjectName(u"Marco_memoria")
        self.Marco_memoria.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.Marco_memoria.setFrameShape(QFrame.StyledPanel)
        self.Marco_memoria.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.Marco_memoria)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.marco7_3 = QFrame(self.Marco_memoria)
        self.marco7_3.setObjectName(u"marco7_3")
        self.marco7_3.setMinimumSize(QSize(100, 20))
        self.marco7_3.setMaximumSize(QSize(160, 30))
        self.marco7_3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco7_3.setFrameShape(QFrame.StyledPanel)
        self.marco7_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_40 = QGridLayout(self.marco7_3)
        self.gridLayout_40.setSpacing(0)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(0, 0, 0, 0)
        self.progressBar_25 = QProgressBar(self.marco7_3)
        self.progressBar_25.setObjectName(u"progressBar_25")
        self.progressBar_25.setValue(0)
        self.progressBar_25.setTextVisible(False)

        self.gridLayout_40.addWidget(self.progressBar_25, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco7_3, 2, 6, 1, 1)

        self.marco8_2 = QFrame(self.Marco_memoria)
        self.marco8_2.setObjectName(u"marco8_2")
        self.marco8_2.setMinimumSize(QSize(100, 20))
        self.marco8_2.setMaximumSize(QSize(160, 30))
        self.marco8_2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco8_2.setFrameShape(QFrame.StyledPanel)
        self.marco8_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.marco8_2)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.progressBar_15 = QProgressBar(self.marco8_2)
        self.progressBar_15.setObjectName(u"progressBar_15")
        self.progressBar_15.setValue(0)
        self.progressBar_15.setTextVisible(False)

        self.gridLayout_30.addWidget(self.progressBar_15, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco8_2, 1, 7, 1, 1)

        self.marco4 = QFrame(self.Marco_memoria)
        self.marco4.setObjectName(u"marco4")
        self.marco4.setMinimumSize(QSize(0, 20))
        self.marco4.setMaximumSize(QSize(160, 30))
        self.marco4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco4.setFrameShape(QFrame.StyledPanel)
        self.marco4.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.marco4)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.progressBar_44 = QProgressBar(self.marco4)
        self.progressBar_44.setObjectName(u"progressBar_44")
        self.progressBar_44.setStyleSheet(u"QProgressBar {\n"
"\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"                \n"
"	background-color: rgb(0, 85, 255);\n"
"}")
        self.progressBar_44.setValue(100)
        self.progressBar_44.setTextVisible(False)

        self.gridLayout_15.addWidget(self.progressBar_44, 0, 1, 1, 1)


        self.gridLayout_11.addWidget(self.marco4, 0, 3, 1, 1)

        self.marco9_2 = QFrame(self.Marco_memoria)
        self.marco9_2.setObjectName(u"marco9_2")
        self.marco9_2.setMinimumSize(QSize(100, 20))
        self.marco9_2.setMaximumSize(QSize(160, 30))
        self.marco9_2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco9_2.setFrameShape(QFrame.StyledPanel)
        self.marco9_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.marco9_2)
        self.gridLayout_31.setSpacing(0)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.progressBar_16 = QProgressBar(self.marco9_2)
        self.progressBar_16.setObjectName(u"progressBar_16")
        self.progressBar_16.setValue(0)
        self.progressBar_16.setTextVisible(False)

        self.gridLayout_31.addWidget(self.progressBar_16, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco9_2, 1, 8, 1, 1)

        self.marco10 = QFrame(self.Marco_memoria)
        self.marco10.setObjectName(u"marco10")
        self.marco10.setMinimumSize(QSize(100, 20))
        self.marco10.setMaximumSize(QSize(160, 30))
        self.marco10.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco10.setFrameShape(QFrame.StyledPanel)
        self.marco10.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.marco10)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.progressBar_6 = QProgressBar(self.marco10)
        self.progressBar_6.setObjectName(u"progressBar_6")
        self.progressBar_6.setValue(0)
        self.progressBar_6.setTextVisible(False)

        self.gridLayout_21.addWidget(self.progressBar_6, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco10, 0, 9, 1, 1)

        self.marco8_4 = QFrame(self.Marco_memoria)
        self.marco8_4.setObjectName(u"marco8_4")
        self.marco8_4.setMinimumSize(QSize(100, 20))
        self.marco8_4.setMaximumSize(QSize(160, 30))
        self.marco8_4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco8_4.setFrameShape(QFrame.StyledPanel)
        self.marco8_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_52 = QGridLayout(self.marco8_4)
        self.gridLayout_52.setSpacing(0)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.gridLayout_52.setContentsMargins(0, 0, 0, 0)
        self.progressBar_37 = QProgressBar(self.marco8_4)
        self.progressBar_37.setObjectName(u"progressBar_37")
        self.progressBar_37.setValue(0)
        self.progressBar_37.setTextVisible(False)

        self.gridLayout_52.addWidget(self.progressBar_37, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco8_4, 3, 7, 1, 1)

        self.marco8_3 = QFrame(self.Marco_memoria)
        self.marco8_3.setObjectName(u"marco8_3")
        self.marco8_3.setMinimumSize(QSize(100, 20))
        self.marco8_3.setMaximumSize(QSize(160, 30))
        self.marco8_3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco8_3.setFrameShape(QFrame.StyledPanel)
        self.marco8_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_41 = QGridLayout(self.marco8_3)
        self.gridLayout_41.setSpacing(0)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
        self.progressBar_26 = QProgressBar(self.marco8_3)
        self.progressBar_26.setObjectName(u"progressBar_26")
        self.progressBar_26.setValue(0)
        self.progressBar_26.setTextVisible(False)

        self.gridLayout_41.addWidget(self.progressBar_26, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco8_3, 2, 7, 1, 1)

        self.marco1_2 = QFrame(self.Marco_memoria)
        self.marco1_2.setObjectName(u"marco1_2")
        self.marco1_2.setMinimumSize(QSize(100, 20))
        self.marco1_2.setMaximumSize(QSize(160, 30))
        self.marco1_2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco1_2.setFrameShape(QFrame.StyledPanel)
        self.marco1_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.marco1_2)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.progressBar_8 = QProgressBar(self.marco1_2)
        self.progressBar_8.setObjectName(u"progressBar_8")
        self.progressBar_8.setValue(0)
        self.progressBar_8.setTextVisible(False)

        self.gridLayout_23.addWidget(self.progressBar_8, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco1_2, 1, 0, 1, 1)

        self.marco10_8 = QFrame(self.Marco_memoria)
        self.marco10_8.setObjectName(u"marco10_8")
        self.marco10_8.setMinimumSize(QSize(100, 20))
        self.marco10_8.setMaximumSize(QSize(160, 30))
        self.marco10_8.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco10_8.setFrameShape(QFrame.StyledPanel)
        self.marco10_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_33 = QGridLayout(self.marco10_8)
        self.gridLayout_33.setSpacing(0)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setContentsMargins(0, 0, 0, 0)
        self.progressBar_18 = QProgressBar(self.marco10_8)
        self.progressBar_18.setObjectName(u"progressBar_18")
        self.progressBar_18.setValue(0)
        self.progressBar_18.setTextVisible(False)

        self.gridLayout_33.addWidget(self.progressBar_18, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco10_8, 1, 10, 1, 1)

        self.marco9_4 = QFrame(self.Marco_memoria)
        self.marco9_4.setObjectName(u"marco9_4")
        self.marco9_4.setMinimumSize(QSize(100, 20))
        self.marco9_4.setMaximumSize(QSize(160, 30))
        self.marco9_4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco9_4.setFrameShape(QFrame.StyledPanel)
        self.marco9_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_53 = QGridLayout(self.marco9_4)
        self.gridLayout_53.setSpacing(0)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.gridLayout_53.setContentsMargins(0, 0, 0, 0)
        self.progressBar_38 = QProgressBar(self.marco9_4)
        self.progressBar_38.setObjectName(u"progressBar_38")
        self.progressBar_38.setValue(0)
        self.progressBar_38.setTextVisible(False)

        self.gridLayout_53.addWidget(self.progressBar_38, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco9_4, 3, 8, 1, 1)

        self.marco3_4 = QFrame(self.Marco_memoria)
        self.marco3_4.setObjectName(u"marco3_4")
        self.marco3_4.setMinimumSize(QSize(100, 20))
        self.marco3_4.setMaximumSize(QSize(160, 30))
        self.marco3_4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco3_4.setFrameShape(QFrame.StyledPanel)
        self.marco3_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_47 = QGridLayout(self.marco3_4)
        self.gridLayout_47.setSpacing(0)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.gridLayout_47.setContentsMargins(0, 0, 0, 0)
        self.progressBar_32 = QProgressBar(self.marco3_4)
        self.progressBar_32.setObjectName(u"progressBar_32")
        self.progressBar_32.setValue(0)
        self.progressBar_32.setTextVisible(False)

        self.gridLayout_47.addWidget(self.progressBar_32, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco3_4, 3, 2, 1, 1)

        self.marco6_4 = QFrame(self.Marco_memoria)
        self.marco6_4.setObjectName(u"marco6_4")
        self.marco6_4.setMinimumSize(QSize(100, 20))
        self.marco6_4.setMaximumSize(QSize(160, 30))
        self.marco6_4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco6_4.setFrameShape(QFrame.StyledPanel)
        self.marco6_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_50 = QGridLayout(self.marco6_4)
        self.gridLayout_50.setSpacing(0)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_50.setContentsMargins(0, 0, 0, 0)
        self.progressBar_35 = QProgressBar(self.marco6_4)
        self.progressBar_35.setObjectName(u"progressBar_35")
        self.progressBar_35.setValue(0)
        self.progressBar_35.setTextVisible(False)

        self.gridLayout_50.addWidget(self.progressBar_35, 1, 1, 1, 1)


        self.gridLayout_11.addWidget(self.marco6_4, 3, 5, 1, 1)

        self.marco5 = QFrame(self.Marco_memoria)
        self.marco5.setObjectName(u"marco5")
        self.marco5.setMinimumSize(QSize(100, 20))
        self.marco5.setMaximumSize(QSize(160, 30))
        self.marco5.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco5.setFrameShape(QFrame.StyledPanel)
        self.marco5.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.marco5)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.progressBar_1 = QProgressBar(self.marco5)
        self.progressBar_1.setObjectName(u"progressBar_1")
        self.progressBar_1.setValue(0)
        self.progressBar_1.setTextVisible(False)

        self.gridLayout_16.addWidget(self.progressBar_1, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco5, 0, 4, 1, 1)

        self.marco10_3 = QFrame(self.Marco_memoria)
        self.marco10_3.setObjectName(u"marco10_3")
        self.marco10_3.setMinimumSize(QSize(100, 20))
        self.marco10_3.setMaximumSize(QSize(160, 30))
        self.marco10_3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco10_3.setFrameShape(QFrame.StyledPanel)
        self.marco10_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_43 = QGridLayout(self.marco10_3)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setHorizontalSpacing(0)
        self.gridLayout_43.setContentsMargins(0, 0, 0, 0)
        self.progressBar_28 = QProgressBar(self.marco10_3)
        self.progressBar_28.setObjectName(u"progressBar_28")
        self.progressBar_28.setValue(0)
        self.progressBar_28.setTextVisible(False)

        self.gridLayout_43.addWidget(self.progressBar_28, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco10_3, 2, 9, 1, 1)

        self.marco5_2 = QFrame(self.Marco_memoria)
        self.marco5_2.setObjectName(u"marco5_2")
        self.marco5_2.setMinimumSize(QSize(100, 20))
        self.marco5_2.setMaximumSize(QSize(160, 30))
        self.marco5_2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco5_2.setFrameShape(QFrame.StyledPanel)
        self.marco5_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.marco5_2)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.progressBar_12 = QProgressBar(self.marco5_2)
        self.progressBar_12.setObjectName(u"progressBar_12")
        self.progressBar_12.setValue(0)
        self.progressBar_12.setTextVisible(False)

        self.gridLayout_27.addWidget(self.progressBar_12, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco5_2, 1, 4, 1, 1)

        self.marco1_3 = QFrame(self.Marco_memoria)
        self.marco1_3.setObjectName(u"marco1_3")
        self.marco1_3.setMinimumSize(QSize(100, 20))
        self.marco1_3.setMaximumSize(QSize(160, 30))
        self.marco1_3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco1_3.setFrameShape(QFrame.StyledPanel)
        self.marco1_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_34 = QGridLayout(self.marco1_3)
        self.gridLayout_34.setSpacing(0)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(0, 0, 0, 0)
        self.progressBar_19 = QProgressBar(self.marco1_3)
        self.progressBar_19.setObjectName(u"progressBar_19")
        self.progressBar_19.setValue(0)
        self.progressBar_19.setTextVisible(False)

        self.gridLayout_34.addWidget(self.progressBar_19, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco1_3, 2, 0, 1, 1)

        self.marco4_2 = QFrame(self.Marco_memoria)
        self.marco4_2.setObjectName(u"marco4_2")
        self.marco4_2.setMinimumSize(QSize(100, 20))
        self.marco4_2.setMaximumSize(QSize(160, 30))
        self.marco4_2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco4_2.setFrameShape(QFrame.StyledPanel)
        self.marco4_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.marco4_2)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.progressBar_11 = QProgressBar(self.marco4_2)
        self.progressBar_11.setObjectName(u"progressBar_11")
        self.progressBar_11.setValue(0)
        self.progressBar_11.setTextVisible(False)

        self.gridLayout_26.addWidget(self.progressBar_11, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco4_2, 1, 3, 1, 1)

        self.marco5_3 = QFrame(self.Marco_memoria)
        self.marco5_3.setObjectName(u"marco5_3")
        self.marco5_3.setMinimumSize(QSize(100, 20))
        self.marco5_3.setMaximumSize(QSize(160, 30))
        self.marco5_3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco5_3.setFrameShape(QFrame.StyledPanel)
        self.marco5_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_38 = QGridLayout(self.marco5_3)
        self.gridLayout_38.setSpacing(0)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(0, 0, 0, 0)
        self.progressBar_23 = QProgressBar(self.marco5_3)
        self.progressBar_23.setObjectName(u"progressBar_23")
        self.progressBar_23.setValue(0)
        self.progressBar_23.setTextVisible(False)

        self.gridLayout_38.addWidget(self.progressBar_23, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco5_3, 2, 4, 1, 1)

        self.marco9_3 = QFrame(self.Marco_memoria)
        self.marco9_3.setObjectName(u"marco9_3")
        self.marco9_3.setMinimumSize(QSize(100, 20))
        self.marco9_3.setMaximumSize(QSize(160, 30))
        self.marco9_3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco9_3.setFrameShape(QFrame.StyledPanel)
        self.marco9_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_42 = QGridLayout(self.marco9_3)
        self.gridLayout_42.setSpacing(0)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setContentsMargins(0, 0, 0, 0)
        self.progressBar_27 = QProgressBar(self.marco9_3)
        self.progressBar_27.setObjectName(u"progressBar_27")
        self.progressBar_27.setValue(0)
        self.progressBar_27.setTextVisible(False)

        self.gridLayout_42.addWidget(self.progressBar_27, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco9_3, 2, 8, 1, 1)

        self.marco3_3 = QFrame(self.Marco_memoria)
        self.marco3_3.setObjectName(u"marco3_3")
        self.marco3_3.setMinimumSize(QSize(100, 20))
        self.marco3_3.setMaximumSize(QSize(160, 30))
        self.marco3_3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco3_3.setFrameShape(QFrame.StyledPanel)
        self.marco3_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_36 = QGridLayout(self.marco3_3)
        self.gridLayout_36.setSpacing(0)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(0, 0, 0, 0)
        self.progressBar_21 = QProgressBar(self.marco3_3)
        self.progressBar_21.setObjectName(u"progressBar_21")
        self.progressBar_21.setValue(0)
        self.progressBar_21.setTextVisible(False)

        self.gridLayout_36.addWidget(self.progressBar_21, 0, 1, 1, 1)


        self.gridLayout_11.addWidget(self.marco3_3, 2, 2, 1, 1)

        self.marco1_4 = QFrame(self.Marco_memoria)
        self.marco1_4.setObjectName(u"marco1_4")
        self.marco1_4.setMinimumSize(QSize(100, 20))
        self.marco1_4.setMaximumSize(QSize(160, 30))
        self.marco1_4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco1_4.setFrameShape(QFrame.StyledPanel)
        self.marco1_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_45 = QGridLayout(self.marco1_4)
        self.gridLayout_45.setSpacing(0)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(0, 0, 0, 0)
        self.progressBar_30 = QProgressBar(self.marco1_4)
        self.progressBar_30.setObjectName(u"progressBar_30")
        self.progressBar_30.setValue(0)
        self.progressBar_30.setTextVisible(False)

        self.gridLayout_45.addWidget(self.progressBar_30, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco1_4, 3, 0, 1, 1)

        self.marco6 = QFrame(self.Marco_memoria)
        self.marco6.setObjectName(u"marco6")
        self.marco6.setMinimumSize(QSize(100, 20))
        self.marco6.setMaximumSize(QSize(160, 30))
        self.marco6.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco6.setFrameShape(QFrame.StyledPanel)
        self.marco6.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.marco6)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.progressBar_2 = QProgressBar(self.marco6)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(0)
        self.progressBar_2.setTextVisible(False)

        self.gridLayout_17.addWidget(self.progressBar_2, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco6, 0, 5, 1, 1)

        self.marco10_4 = QFrame(self.Marco_memoria)
        self.marco10_4.setObjectName(u"marco10_4")
        self.marco10_4.setMinimumSize(QSize(100, 20))
        self.marco10_4.setMaximumSize(QSize(160, 30))
        self.marco10_4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco10_4.setFrameShape(QFrame.StyledPanel)
        self.marco10_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_54 = QGridLayout(self.marco10_4)
        self.gridLayout_54.setSpacing(0)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.gridLayout_54.setContentsMargins(0, 0, 0, 0)
        self.progressBar_39 = QProgressBar(self.marco10_4)
        self.progressBar_39.setObjectName(u"progressBar_39")
        self.progressBar_39.setValue(0)
        self.progressBar_39.setTextVisible(False)

        self.gridLayout_54.addWidget(self.progressBar_39, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco10_4, 3, 9, 1, 1)

        self.marco3 = QFrame(self.Marco_memoria)
        self.marco3.setObjectName(u"marco3")
        self.marco3.setMinimumSize(QSize(100, 20))
        self.marco3.setMaximumSize(QSize(160, 30))
        self.marco3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco3.setFrameShape(QFrame.StyledPanel)
        self.marco3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.marco3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.progressBar_43 = QProgressBar(self.marco3)
        self.progressBar_43.setObjectName(u"progressBar_43")
        self.progressBar_43.setStyleSheet(u"QProgressBar {\n"
"\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"                \n"
"	background-color: rgb(0, 85, 255);\n"
"}")
        self.progressBar_43.setValue(100)
        self.progressBar_43.setTextVisible(False)

        self.horizontalLayout_8.addWidget(self.progressBar_43)


        self.gridLayout_11.addWidget(self.marco3, 0, 2, 1, 1)

        self.marco8 = QFrame(self.Marco_memoria)
        self.marco8.setObjectName(u"marco8")
        self.marco8.setMinimumSize(QSize(100, 20))
        self.marco8.setMaximumSize(QSize(160, 30))
        self.marco8.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco8.setFrameShape(QFrame.StyledPanel)
        self.marco8.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.marco8)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.progressBar_4 = QProgressBar(self.marco8)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setValue(0)
        self.progressBar_4.setTextVisible(False)

        self.gridLayout_19.addWidget(self.progressBar_4, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco8, 0, 7, 1, 1)

        self.marco2 = QFrame(self.Marco_memoria)
        self.marco2.setObjectName(u"marco2")
        self.marco2.setMinimumSize(QSize(100, 20))
        self.marco2.setMaximumSize(QSize(160, 30))
        self.marco2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco2.setFrameShape(QFrame.StyledPanel)
        self.marco2.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.marco2)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.progressBar_42 = QProgressBar(self.marco2)
        self.progressBar_42.setObjectName(u"progressBar_42")
        self.progressBar_42.setStyleSheet(u"QProgressBar {\n"
"\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"                \n"
"	background-color: rgb(0, 85, 255);\n"
"}")
        self.progressBar_42.setValue(100)
        self.progressBar_42.setTextVisible(False)

        self.gridLayout_14.addWidget(self.progressBar_42, 0, 1, 1, 1)


        self.gridLayout_11.addWidget(self.marco2, 0, 1, 1, 1)

        self.marco7_2 = QFrame(self.Marco_memoria)
        self.marco7_2.setObjectName(u"marco7_2")
        self.marco7_2.setMinimumSize(QSize(100, 20))
        self.marco7_2.setMaximumSize(QSize(160, 30))
        self.marco7_2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco7_2.setFrameShape(QFrame.StyledPanel)
        self.marco7_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.marco7_2)
        self.gridLayout_29.setSpacing(0)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.progressBar_14 = QProgressBar(self.marco7_2)
        self.progressBar_14.setObjectName(u"progressBar_14")
        self.progressBar_14.setValue(0)
        self.progressBar_14.setTextVisible(False)

        self.gridLayout_29.addWidget(self.progressBar_14, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco7_2, 1, 6, 1, 1)

        self.marco4_4 = QFrame(self.Marco_memoria)
        self.marco4_4.setObjectName(u"marco4_4")
        self.marco4_4.setMinimumSize(QSize(100, 20))
        self.marco4_4.setMaximumSize(QSize(160, 30))
        self.marco4_4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco4_4.setFrameShape(QFrame.StyledPanel)
        self.marco4_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_48 = QGridLayout(self.marco4_4)
        self.gridLayout_48.setSpacing(0)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_48.setContentsMargins(0, 0, 0, 0)
        self.progressBar_33 = QProgressBar(self.marco4_4)
        self.progressBar_33.setObjectName(u"progressBar_33")
        self.progressBar_33.setValue(0)
        self.progressBar_33.setTextVisible(False)

        self.gridLayout_48.addWidget(self.progressBar_33, 0, 2, 1, 1)


        self.gridLayout_11.addWidget(self.marco4_4, 3, 3, 1, 1)

        self.marco6_3 = QFrame(self.Marco_memoria)
        self.marco6_3.setObjectName(u"marco6_3")
        self.marco6_3.setMinimumSize(QSize(100, 20))
        self.marco6_3.setMaximumSize(QSize(160, 30))
        self.marco6_3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco6_3.setFrameShape(QFrame.StyledPanel)
        self.marco6_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_39 = QGridLayout(self.marco6_3)
        self.gridLayout_39.setSpacing(0)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(0, 0, 0, 0)
        self.progressBar_24 = QProgressBar(self.marco6_3)
        self.progressBar_24.setObjectName(u"progressBar_24")
        self.progressBar_24.setValue(0)
        self.progressBar_24.setTextVisible(False)

        self.gridLayout_39.addWidget(self.progressBar_24, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco6_3, 2, 5, 1, 1)

        self.marco3_2 = QFrame(self.Marco_memoria)
        self.marco3_2.setObjectName(u"marco3_2")
        self.marco3_2.setMinimumSize(QSize(100, 20))
        self.marco3_2.setMaximumSize(QSize(160, 30))
        self.marco3_2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco3_2.setFrameShape(QFrame.StyledPanel)
        self.marco3_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.marco3_2)
        self.gridLayout_25.setSpacing(0)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.progressBar_10 = QProgressBar(self.marco3_2)
        self.progressBar_10.setObjectName(u"progressBar_10")
        self.progressBar_10.setValue(0)
        self.progressBar_10.setTextVisible(False)

        self.gridLayout_25.addWidget(self.progressBar_10, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco3_2, 1, 2, 1, 1)

        self.marco5_4 = QFrame(self.Marco_memoria)
        self.marco5_4.setObjectName(u"marco5_4")
        self.marco5_4.setMinimumSize(QSize(100, 20))
        self.marco5_4.setMaximumSize(QSize(160, 30))
        self.marco5_4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco5_4.setFrameShape(QFrame.StyledPanel)
        self.marco5_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_49 = QGridLayout(self.marco5_4)
        self.gridLayout_49.setSpacing(0)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.gridLayout_49.setContentsMargins(0, 0, 0, 0)
        self.progressBar_34 = QProgressBar(self.marco5_4)
        self.progressBar_34.setObjectName(u"progressBar_34")
        self.progressBar_34.setValue(0)
        self.progressBar_34.setTextVisible(False)

        self.gridLayout_49.addWidget(self.progressBar_34, 0, 2, 1, 1)


        self.gridLayout_11.addWidget(self.marco5_4, 3, 4, 1, 1)

        self.marco7 = QFrame(self.Marco_memoria)
        self.marco7.setObjectName(u"marco7")
        self.marco7.setMinimumSize(QSize(100, 20))
        self.marco7.setMaximumSize(QSize(160, 30))
        self.marco7.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco7.setFrameShape(QFrame.StyledPanel)
        self.marco7.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.marco7)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.progressBar_3 = QProgressBar(self.marco7)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setValue(0)
        self.progressBar_3.setTextVisible(False)

        self.gridLayout_18.addWidget(self.progressBar_3, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco7, 0, 6, 1, 1)

        self.marco10_5 = QFrame(self.Marco_memoria)
        self.marco10_5.setObjectName(u"marco10_5")
        self.marco10_5.setMinimumSize(QSize(100, 20))
        self.marco10_5.setMaximumSize(QSize(160, 30))
        self.marco10_5.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco10_5.setFrameShape(QFrame.StyledPanel)
        self.marco10_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_44 = QGridLayout(self.marco10_5)
        self.gridLayout_44.setSpacing(0)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setContentsMargins(0, 0, 0, 0)
        self.progressBar_29 = QProgressBar(self.marco10_5)
        self.progressBar_29.setObjectName(u"progressBar_29")
        self.progressBar_29.setValue(0)
        self.progressBar_29.setTextVisible(False)

        self.gridLayout_44.addWidget(self.progressBar_29, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco10_5, 2, 10, 1, 1)

        self.marco10_7 = QFrame(self.Marco_memoria)
        self.marco10_7.setObjectName(u"marco10_7")
        self.marco10_7.setMinimumSize(QSize(100, 20))
        self.marco10_7.setMaximumSize(QSize(160, 30))
        self.marco10_7.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco10_7.setFrameShape(QFrame.StyledPanel)
        self.marco10_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_55 = QGridLayout(self.marco10_7)
        self.gridLayout_55.setSpacing(0)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.gridLayout_55.setContentsMargins(0, 0, 0, 0)
        self.progressBar_40 = QProgressBar(self.marco10_7)
        self.progressBar_40.setObjectName(u"progressBar_40")
        self.progressBar_40.setValue(0)
        self.progressBar_40.setTextVisible(False)

        self.gridLayout_55.addWidget(self.progressBar_40, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco10_7, 3, 10, 1, 1)

        self.marco2_3 = QFrame(self.Marco_memoria)
        self.marco2_3.setObjectName(u"marco2_3")
        self.marco2_3.setMinimumSize(QSize(100, 20))
        self.marco2_3.setMaximumSize(QSize(160, 30))
        self.marco2_3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco2_3.setFrameShape(QFrame.StyledPanel)
        self.marco2_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.marco2_3)
        self.gridLayout_35.setSpacing(0)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(0, 0, 0, 0)
        self.progressBar_20 = QProgressBar(self.marco2_3)
        self.progressBar_20.setObjectName(u"progressBar_20")
        self.progressBar_20.setValue(0)
        self.progressBar_20.setTextVisible(False)

        self.gridLayout_35.addWidget(self.progressBar_20, 0, 2, 1, 1)


        self.gridLayout_11.addWidget(self.marco2_3, 2, 1, 1, 1)

        self.marco1 = QFrame(self.Marco_memoria)
        self.marco1.setObjectName(u"marco1")
        self.marco1.setMinimumSize(QSize(100, 20))
        self.marco1.setMaximumSize(QSize(160, 30))
        self.marco1.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco1.setFrameShape(QFrame.StyledPanel)
        self.marco1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.marco1)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.progressBar_41 = QProgressBar(self.marco1)
        self.progressBar_41.setObjectName(u"progressBar_41")
        self.progressBar_41.setStyleSheet(u"QProgressBar {\n"
"\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"                \n"
"	background-color: rgb(0, 85, 255);\n"
"}")
        self.progressBar_41.setValue(100)
        self.progressBar_41.setTextVisible(False)

        self.horizontalLayout_12.addWidget(self.progressBar_41)


        self.gridLayout_11.addWidget(self.marco1, 0, 0, 1, 1)

        self.marco7_4 = QFrame(self.Marco_memoria)
        self.marco7_4.setObjectName(u"marco7_4")
        self.marco7_4.setMinimumSize(QSize(100, 20))
        self.marco7_4.setMaximumSize(QSize(160, 30))
        self.marco7_4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco7_4.setFrameShape(QFrame.StyledPanel)
        self.marco7_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_51 = QGridLayout(self.marco7_4)
        self.gridLayout_51.setSpacing(0)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.gridLayout_51.setContentsMargins(0, 0, 0, 0)
        self.progressBar_36 = QProgressBar(self.marco7_4)
        self.progressBar_36.setObjectName(u"progressBar_36")
        self.progressBar_36.setValue(0)
        self.progressBar_36.setTextVisible(False)

        self.gridLayout_51.addWidget(self.progressBar_36, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco7_4, 3, 6, 1, 1)

        self.marco10_6 = QFrame(self.Marco_memoria)
        self.marco10_6.setObjectName(u"marco10_6")
        self.marco10_6.setMinimumSize(QSize(100, 20))
        self.marco10_6.setMaximumSize(QSize(160, 30))
        self.marco10_6.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco10_6.setFrameShape(QFrame.StyledPanel)
        self.marco10_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.marco10_6)
        self.gridLayout_22.setSpacing(0)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.progressBar_7 = QProgressBar(self.marco10_6)
        self.progressBar_7.setObjectName(u"progressBar_7")
        self.progressBar_7.setValue(0)
        self.progressBar_7.setTextVisible(False)

        self.gridLayout_22.addWidget(self.progressBar_7, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco10_6, 0, 10, 1, 1)

        self.marco9 = QFrame(self.Marco_memoria)
        self.marco9.setObjectName(u"marco9")
        self.marco9.setMinimumSize(QSize(100, 20))
        self.marco9.setMaximumSize(QSize(160, 30))
        self.marco9.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco9.setFrameShape(QFrame.StyledPanel)
        self.marco9.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.marco9)
        self.gridLayout_20.setSpacing(0)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.progressBar_5 = QProgressBar(self.marco9)
        self.progressBar_5.setObjectName(u"progressBar_5")
        self.progressBar_5.setValue(0)
        self.progressBar_5.setTextVisible(False)

        self.gridLayout_20.addWidget(self.progressBar_5, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco9, 0, 8, 1, 1)

        self.marco4_3 = QFrame(self.Marco_memoria)
        self.marco4_3.setObjectName(u"marco4_3")
        self.marco4_3.setMinimumSize(QSize(100, 20))
        self.marco4_3.setMaximumSize(QSize(160, 30))
        self.marco4_3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco4_3.setFrameShape(QFrame.StyledPanel)
        self.marco4_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_37 = QGridLayout(self.marco4_3)
        self.gridLayout_37.setSpacing(0)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(0, 0, 0, 0)
        self.progressBar_22 = QProgressBar(self.marco4_3)
        self.progressBar_22.setObjectName(u"progressBar_22")
        self.progressBar_22.setValue(0)
        self.progressBar_22.setTextVisible(False)

        self.gridLayout_37.addWidget(self.progressBar_22, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco4_3, 2, 3, 1, 1)

        self.marco2_4 = QFrame(self.Marco_memoria)
        self.marco2_4.setObjectName(u"marco2_4")
        self.marco2_4.setMinimumSize(QSize(100, 20))
        self.marco2_4.setMaximumSize(QSize(160, 30))
        self.marco2_4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco2_4.setFrameShape(QFrame.StyledPanel)
        self.marco2_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_46 = QGridLayout(self.marco2_4)
        self.gridLayout_46.setSpacing(0)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setContentsMargins(0, 0, 0, 0)
        self.progressBar_31 = QProgressBar(self.marco2_4)
        self.progressBar_31.setObjectName(u"progressBar_31")
        self.progressBar_31.setValue(0)
        self.progressBar_31.setTextVisible(False)

        self.gridLayout_46.addWidget(self.progressBar_31, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco2_4, 3, 1, 1, 1)

        self.marco2_2 = QFrame(self.Marco_memoria)
        self.marco2_2.setObjectName(u"marco2_2")
        self.marco2_2.setMinimumSize(QSize(100, 20))
        self.marco2_2.setMaximumSize(QSize(160, 30))
        self.marco2_2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco2_2.setFrameShape(QFrame.StyledPanel)
        self.marco2_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.marco2_2)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.progressBar_9 = QProgressBar(self.marco2_2)
        self.progressBar_9.setObjectName(u"progressBar_9")
        self.progressBar_9.setValue(0)
        self.progressBar_9.setTextVisible(False)

        self.gridLayout_24.addWidget(self.progressBar_9, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco2_2, 1, 1, 1, 1)

        self.marco10_2 = QFrame(self.Marco_memoria)
        self.marco10_2.setObjectName(u"marco10_2")
        self.marco10_2.setMinimumSize(QSize(100, 20))
        self.marco10_2.setMaximumSize(QSize(160, 30))
        self.marco10_2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco10_2.setFrameShape(QFrame.StyledPanel)
        self.marco10_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.marco10_2)
        self.gridLayout_32.setSpacing(0)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.progressBar_17 = QProgressBar(self.marco10_2)
        self.progressBar_17.setObjectName(u"progressBar_17")
        self.progressBar_17.setValue(0)
        self.progressBar_17.setTextVisible(False)

        self.gridLayout_32.addWidget(self.progressBar_17, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco10_2, 1, 9, 1, 1)

        self.marco6_2 = QFrame(self.Marco_memoria)
        self.marco6_2.setObjectName(u"marco6_2")
        self.marco6_2.setMinimumSize(QSize(100, 20))
        self.marco6_2.setMaximumSize(QSize(160, 30))
        self.marco6_2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco6_2.setFrameShape(QFrame.StyledPanel)
        self.marco6_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.marco6_2)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.progressBar_13 = QProgressBar(self.marco6_2)
        self.progressBar_13.setObjectName(u"progressBar_13")
        self.progressBar_13.setValue(0)
        self.progressBar_13.setTextVisible(False)

        self.gridLayout_28.addWidget(self.progressBar_13, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco6_2, 1, 5, 1, 1)


        self.gridLayout_10.addWidget(self.Marco_memoria, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_6, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_7, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1372, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simulador de procesos", None))
        self.groupBox_4.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Memoria disponible:", None))
        self.le_memoria_restante.setPlaceholderText(QCoreApplication.translate("MainWindow", u"200 MB / 220 MB", None))
        self.pb_iniciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.pb_re_iniciar.setText(QCoreApplication.translate("MainWindow", u"Reiniciar", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Quantum: ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Procesos iniciales: ", None))
        self.pb_agregar_procesos.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Procesos nuevos", None))
        self.le_procesos_nuevos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Listo", None))
        self.pte_listos.setPlainText("")
        self.pte_listos.setPlaceholderText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Ejecuci\u00f3n", None))
        self.pte_ejecucion.setPlaceholderText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Terminados", None))
        self.pte_terminados.setPlaceholderText("")
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n", None))
        self.groupBox_5.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Tiempo Global:", None))
        self.le_tiempo_global.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Memoria en uso:", None))
        self.le_tiempo_global_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u" 20 MB / 220 MB", None))
        self.lb_pausa.setText(QCoreApplication.translate("MainWindow", u"Ejecuci\u00f3n", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Memoria", None))
    # retranslateUi

