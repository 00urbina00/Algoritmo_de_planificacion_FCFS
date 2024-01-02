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
        MainWindow.resize(1592, 979)
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
        self.verticalLayout.setSpacing(3)
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
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.groupBox_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(900, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setSpacing(3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(3, 0, 3, 0)
        self.groupBox_8 = QGroupBox(self.frame_5)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(0, 48))
        self.groupBox_8.setMaximumSize(QSize(16777215, 48))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(10)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.groupBox_8.setAlignment(Qt.AlignCenter)
        self.gridLayout_57 = QGridLayout(self.groupBox_8)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.gridLayout_57.setHorizontalSpacing(10)
        self.gridLayout_57.setVerticalSpacing(0)
        self.gridLayout_57.setContentsMargins(9, 0, -1, 3)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_10 = QLabel(self.groupBox_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(111, 0))
        self.label_10.setMaximumSize(QSize(220, 16777215))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_10)

        self.sb_num_procesos = QSpinBox(self.groupBox_8)
        self.sb_num_procesos.setObjectName(u"sb_num_procesos")
        self.sb_num_procesos.setMinimumSize(QSize(40, 25))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        self.sb_num_procesos.setFont(font1)
        self.sb_num_procesos.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sb_num_procesos.setWrapping(False)
        self.sb_num_procesos.setFrame(True)
        self.sb_num_procesos.setAlignment(Qt.AlignCenter)
        self.sb_num_procesos.setReadOnly(False)
        self.sb_num_procesos.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.sb_num_procesos.setMinimum(1)
        self.sb_num_procesos.setValue(10)

        self.horizontalLayout_18.addWidget(self.sb_num_procesos)

        self.pb_agregar_procesos = QPushButton(self.groupBox_8)
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

        self.horizontalLayout_18.addWidget(self.pb_agregar_procesos)


        self.gridLayout_57.addLayout(self.horizontalLayout_18, 0, 4, 1, 1)

        self.pb_re_iniciar = QPushButton(self.groupBox_8)
        self.pb_re_iniciar.setObjectName(u"pb_re_iniciar")
        self.pb_re_iniciar.setMinimumSize(QSize(60, 25))
        self.pb_re_iniciar.setMaximumSize(QSize(80, 16777215))
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

        self.gridLayout_57.addWidget(self.pb_re_iniciar, 0, 2, 1, 1)

        self.pb_iniciar = QPushButton(self.groupBox_8)
        self.pb_iniciar.setObjectName(u"pb_iniciar")
        self.pb_iniciar.setMinimumSize(QSize(60, 25))
        self.pb_iniciar.setMaximumSize(QSize(80, 16777215))
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

        self.gridLayout_57.addWidget(self.pb_iniciar, 0, 1, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_12 = QLabel(self.groupBox_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(70, 0))
        self.label_12.setMaximumSize(QSize(80, 16777215))
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_12)

        self.sb_quantum = QSpinBox(self.groupBox_8)
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

        self.horizontalLayout_19.addWidget(self.sb_quantum)


        self.gridLayout_57.addLayout(self.horizontalLayout_19, 0, 3, 1, 1)


        self.horizontalLayout_9.addWidget(self.groupBox_8)

        self.groupBox_7 = QGroupBox(self.frame_5)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(0, 48))
        self.groupBox_7.setMaximumSize(QSize(16777215, 48))
        self.groupBox_7.setFont(font)
        self.groupBox_7.setStyleSheet(u"color: rgb(0, 0, 255);\n"
"color: rgb(0, 170, 0);")
        self.groupBox_7.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_17 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(5, 0, 5, -1)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_55 = QLabel(self.groupBox_7)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(28, 0))
        self.label_55.setMaximumSize(QSize(35, 25))
        self.label_55.setFont(font)
        self.label_55.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_55.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_55)

        self.le_siguiente_id_nuevo = QLineEdit(self.groupBox_7)
        self.le_siguiente_id_nuevo.setObjectName(u"le_siguiente_id_nuevo")
        self.le_siguiente_id_nuevo.setMinimumSize(QSize(30, 0))
        self.le_siguiente_id_nuevo.setMaximumSize(QSize(30, 25))
        self.le_siguiente_id_nuevo.setFont(font)
        self.le_siguiente_id_nuevo.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.le_siguiente_id_nuevo.setFrame(False)
        self.le_siguiente_id_nuevo.setAlignment(Qt.AlignCenter)
        self.le_siguiente_id_nuevo.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.le_siguiente_id_nuevo)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_56 = QLabel(self.groupBox_7)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(50, 0))
        self.label_56.setMaximumSize(QSize(55, 25))
        self.label_56.setFont(font)
        self.label_56.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_56.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_56)

        self.le_siguiente_tam_nuevo = QLineEdit(self.groupBox_7)
        self.le_siguiente_tam_nuevo.setObjectName(u"le_siguiente_tam_nuevo")
        self.le_siguiente_tam_nuevo.setMinimumSize(QSize(30, 0))
        self.le_siguiente_tam_nuevo.setMaximumSize(QSize(30, 25))
        self.le_siguiente_tam_nuevo.setFont(font)
        self.le_siguiente_tam_nuevo.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.le_siguiente_tam_nuevo.setFrame(False)
        self.le_siguiente_tam_nuevo.setAlignment(Qt.AlignCenter)
        self.le_siguiente_tam_nuevo.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.le_siguiente_tam_nuevo)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_58 = QLabel(self.groupBox_7)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(50, 0))
        self.label_58.setMaximumSize(QSize(55, 25))
        self.label_58.setFont(font)
        self.label_58.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_58.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_58)

        self.le_siguiente_pag_nuevo = QLineEdit(self.groupBox_7)
        self.le_siguiente_pag_nuevo.setObjectName(u"le_siguiente_pag_nuevo")
        self.le_siguiente_pag_nuevo.setMinimumSize(QSize(30, 0))
        self.le_siguiente_pag_nuevo.setMaximumSize(QSize(30, 25))
        self.le_siguiente_pag_nuevo.setFont(font)
        self.le_siguiente_pag_nuevo.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.le_siguiente_pag_nuevo.setFrame(False)
        self.le_siguiente_pag_nuevo.setAlignment(Qt.AlignCenter)
        self.le_siguiente_pag_nuevo.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.le_siguiente_pag_nuevo)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_9.addWidget(self.groupBox_7)

        self.groupBox_11 = QGroupBox(self.frame_5)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setMinimumSize(QSize(0, 48))
        self.groupBox_11.setMaximumSize(QSize(16777215, 48))
        self.groupBox_11.setFont(font)
        self.groupBox_11.setStyleSheet(u"color: rgb(0, 0, 255);\n"
"color: rgb(255, 0, 0);")
        self.groupBox_11.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_25 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_25.setSpacing(5)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(5, 0, 5, 9)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_57 = QLabel(self.groupBox_11)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(28, 0))
        self.label_57.setMaximumSize(QSize(35, 25))
        self.label_57.setFont(font)
        self.label_57.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_57)

        self.le_siguiente_id_suspendido = QLineEdit(self.groupBox_11)
        self.le_siguiente_id_suspendido.setObjectName(u"le_siguiente_id_suspendido")
        self.le_siguiente_id_suspendido.setMinimumSize(QSize(30, 0))
        self.le_siguiente_id_suspendido.setMaximumSize(QSize(30, 25))
        self.le_siguiente_id_suspendido.setFont(font)
        self.le_siguiente_id_suspendido.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.le_siguiente_id_suspendido.setFrame(False)
        self.le_siguiente_id_suspendido.setAlignment(Qt.AlignCenter)
        self.le_siguiente_id_suspendido.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.le_siguiente_id_suspendido)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_59 = QLabel(self.groupBox_11)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(50, 0))
        self.label_59.setMaximumSize(QSize(55, 25))
        self.label_59.setFont(font)
        self.label_59.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_59)

        self.le_siguiente_tam_suspendido = QLineEdit(self.groupBox_11)
        self.le_siguiente_tam_suspendido.setObjectName(u"le_siguiente_tam_suspendido")
        self.le_siguiente_tam_suspendido.setMinimumSize(QSize(30, 0))
        self.le_siguiente_tam_suspendido.setMaximumSize(QSize(30, 25))
        self.le_siguiente_tam_suspendido.setFont(font)
        self.le_siguiente_tam_suspendido.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.le_siguiente_tam_suspendido.setFrame(False)
        self.le_siguiente_tam_suspendido.setAlignment(Qt.AlignCenter)
        self.le_siguiente_tam_suspendido.setReadOnly(True)

        self.horizontalLayout_22.addWidget(self.le_siguiente_tam_suspendido)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_60 = QLabel(self.groupBox_11)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(50, 0))
        self.label_60.setMaximumSize(QSize(55, 25))
        self.label_60.setFont(font)
        self.label_60.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_60.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_60)

        self.le_siguiente_pag_suspendido = QLineEdit(self.groupBox_11)
        self.le_siguiente_pag_suspendido.setObjectName(u"le_siguiente_pag_suspendido")
        self.le_siguiente_pag_suspendido.setMinimumSize(QSize(30, 0))
        self.le_siguiente_pag_suspendido.setMaximumSize(QSize(30, 25))
        self.le_siguiente_pag_suspendido.setFont(font)
        self.le_siguiente_pag_suspendido.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.le_siguiente_pag_suspendido.setFrame(False)
        self.le_siguiente_pag_suspendido.setAlignment(Qt.AlignCenter)
        self.le_siguiente_pag_suspendido.setReadOnly(True)

        self.horizontalLayout_23.addWidget(self.le_siguiente_pag_suspendido)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_4 = QLabel(self.groupBox_11)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(50, 16777215))
        self.label_4.setStyleSheet(u"color: rgb(255, 85, 0);")

        self.horizontalLayout_21.addWidget(self.label_4)

        self.frame_proximo_suspendido = QFrame(self.groupBox_11)
        self.frame_proximo_suspendido.setObjectName(u"frame_proximo_suspendido")
        self.frame_proximo_suspendido.setMinimumSize(QSize(20, 0))
        self.frame_proximo_suspendido.setMaximumSize(QSize(20, 25))
        self.frame_proximo_suspendido.setStyleSheet(u"background-color: rgb(159, 159, 159);")
        self.frame_proximo_suspendido.setFrameShape(QFrame.StyledPanel)
        self.frame_proximo_suspendido.setFrameShadow(QFrame.Raised)
        self.frame_proximo_suspendido.setLineWidth(0)

        self.horizontalLayout_21.addWidget(self.frame_proximo_suspendido)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_9.addWidget(self.groupBox_11)

        self.groupBox_10 = QGroupBox(self.frame_5)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMinimumSize(QSize(48, 0))
        self.groupBox_10.setMaximumSize(QSize(600, 48))
        self.groupBox_10.setFont(font)
        self.groupBox_10.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.groupBox_10.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 5, 9)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.groupBox_10)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(55, 0))
        self.label_9.setMaximumSize(QSize(60, 16777215))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(0, 85, 255);\n"
"color: rgb(0, 170, 0);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.le_procesos_nuevos = QLineEdit(self.groupBox_10)
        self.le_procesos_nuevos.setObjectName(u"le_procesos_nuevos")
        self.le_procesos_nuevos.setMinimumSize(QSize(25, 11))
        self.le_procesos_nuevos.setMaximumSize(QSize(30, 25))
        self.le_procesos_nuevos.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"color: rgb(0, 170, 0);")
        self.le_procesos_nuevos.setFrame(False)
        self.le_procesos_nuevos.setAlignment(Qt.AlignCenter)
        self.le_procesos_nuevos.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.le_procesos_nuevos)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_14 = QLabel(self.groupBox_10)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(45, 0))
        self.label_14.setMaximumSize(QSize(50, 16777215))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_14)

        self.le_procesos_listos = QLineEdit(self.groupBox_10)
        self.le_procesos_listos.setObjectName(u"le_procesos_listos")
        self.le_procesos_listos.setMinimumSize(QSize(25, 11))
        self.le_procesos_listos.setMaximumSize(QSize(30, 25))
        self.le_procesos_listos.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.le_procesos_listos.setFrame(False)
        self.le_procesos_listos.setAlignment(Qt.AlignCenter)
        self.le_procesos_listos.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.le_procesos_listos)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_15 = QLabel(self.groupBox_10)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(75, 0))
        self.label_15.setMaximumSize(QSize(80, 16777215))
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"color: rgb(0, 85, 255);\n"
"color: rgb(255, 0, 0);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_15)

        self.le_procesos_bloqueados = QLineEdit(self.groupBox_10)
        self.le_procesos_bloqueados.setObjectName(u"le_procesos_bloqueados")
        self.le_procesos_bloqueados.setMinimumSize(QSize(25, 11))
        self.le_procesos_bloqueados.setMaximumSize(QSize(30, 25))
        self.le_procesos_bloqueados.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"color: rgb(255, 0, 0);")
        self.le_procesos_bloqueados.setFrame(False)
        self.le_procesos_bloqueados.setAlignment(Qt.AlignCenter)
        self.le_procesos_bloqueados.setReadOnly(True)

        self.horizontalLayout_24.addWidget(self.le_procesos_bloqueados)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_13 = QLabel(self.groupBox_10)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(80, 0))
        self.label_13.setMaximumSize(QSize(60, 16777215))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_13)

        self.le_procesos_suspendidos = QLineEdit(self.groupBox_10)
        self.le_procesos_suspendidos.setObjectName(u"le_procesos_suspendidos")
        self.le_procesos_suspendidos.setMinimumSize(QSize(25, 11))
        self.le_procesos_suspendidos.setMaximumSize(QSize(30, 25))
        self.le_procesos_suspendidos.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.le_procesos_suspendidos.setFrame(False)
        self.le_procesos_suspendidos.setAlignment(Qt.AlignCenter)
        self.le_procesos_suspendidos.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.le_procesos_suspendidos)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_11 = QLabel(self.groupBox_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(75, 0))
        self.label_11.setMaximumSize(QSize(80, 16777215))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: rgb(0, 85, 255);\n"
"color: rgb(255, 0, 0);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_11)

        self.le_procesos_terminados = QLineEdit(self.groupBox_10)
        self.le_procesos_terminados.setObjectName(u"le_procesos_terminados")
        self.le_procesos_terminados.setMinimumSize(QSize(25, 11))
        self.le_procesos_terminados.setMaximumSize(QSize(30, 25))
        self.le_procesos_terminados.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"color: rgb(255, 0, 0);")
        self.le_procesos_terminados.setFrame(False)
        self.le_procesos_terminados.setAlignment(Qt.AlignCenter)
        self.le_procesos_terminados.setReadOnly(True)

        self.horizontalLayout_20.addWidget(self.le_procesos_terminados)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_20)


        self.horizontalLayout_9.addWidget(self.groupBox_10)


        self.horizontalLayout_12.addWidget(self.frame_5)


        self.gridLayout_4.addWidget(self.groupBox_4, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 1000))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(1)
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 3)
        self.groupBox = QGroupBox(self.frame_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 350))
        self.groupBox.setMaximumSize(QSize(495, 600))
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(0, 85, 255);")
        self.groupBox.setAlignment(Qt.AlignCenter)
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
        self.groupBox_2.setAlignment(Qt.AlignCenter)
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
        self.groupBox_3.setAlignment(Qt.AlignCenter)
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
        self.groupBox_9.setAlignment(Qt.AlignCenter)
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
        self.groupBox_5.setMaximumSize(QSize(16777215, 55))
        self.groupBox_5.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.gridLayout_58 = QGridLayout(self.groupBox_5)
        self.gridLayout_58.setSpacing(0)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.gridLayout_58.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.groupBox_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(900, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(111, 0))
        self.label_2.setMaximumSize(QSize(111, 25))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_tiempo_global = QLineEdit(self.frame_6)
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

        self.horizontalSpacer_52 = QSpacerItem(20, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_52)

        self.groupBox_12 = QGroupBox(self.frame_6)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_59 = QGridLayout(self.groupBox_12)
        self.gridLayout_59.setSpacing(0)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.gridLayout_59.setContentsMargins(0, 0, 0, 0)
        self.lb_pausa = QLabel(self.groupBox_12)
        self.lb_pausa.setObjectName(u"lb_pausa")
        self.lb_pausa.setMinimumSize(QSize(300, 0))
        self.lb_pausa.setMaximumSize(QSize(400, 25))
        self.lb_pausa.setFont(font)
        self.lb_pausa.setStyleSheet(u"color: rgb(0, 170, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lb_pausa.setAlignment(Qt.AlignCenter)

        self.gridLayout_59.addWidget(self.lb_pausa, 0, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.groupBox_12)

        self.horizontalSpacer_53 = QSpacerItem(20, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_53)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_51 = QLabel(self.frame_6)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(80, 0))
        self.label_51.setMaximumSize(QSize(80, 25))
        self.label_51.setFont(font)
        self.label_51.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_51)

        self.le_marcos_libres = QLineEdit(self.frame_6)
        self.le_marcos_libres.setObjectName(u"le_marcos_libres")
        self.le_marcos_libres.setMinimumSize(QSize(30, 25))
        self.le_marcos_libres.setMaximumSize(QSize(50, 25))
        self.le_marcos_libres.setFont(font)
        self.le_marcos_libres.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.le_marcos_libres.setFrame(False)
        self.le_marcos_libres.setAlignment(Qt.AlignCenter)
        self.le_marcos_libres.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.le_marcos_libres)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalSpacer_11 = QSpacerItem(70, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_11)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setMaximumSize(QSize(100, 25))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.le_memoria_uso = QLineEdit(self.frame_6)
        self.le_memoria_uso.setObjectName(u"le_memoria_uso")
        self.le_memoria_uso.setMinimumSize(QSize(120, 0))
        self.le_memoria_uso.setMaximumSize(QSize(100, 25))
        self.le_memoria_uso.setFont(font)
        self.le_memoria_uso.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.le_memoria_uso.setFrame(False)
        self.le_memoria_uso.setAlignment(Qt.AlignCenter)
        self.le_memoria_uso.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.le_memoria_uso)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_12 = QSpacerItem(71, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(130, 0))
        self.label.setMaximumSize(QSize(100, 25))
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.le_memoria_restante = QLineEdit(self.frame_6)
        self.le_memoria_restante.setObjectName(u"le_memoria_restante")
        self.le_memoria_restante.setMinimumSize(QSize(120, 0))
        self.le_memoria_restante.setMaximumSize(QSize(25, 16777215))
        self.le_memoria_restante.setFont(font1)
        self.le_memoria_restante.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.le_memoria_restante.setFrame(False)
        self.le_memoria_restante.setAlignment(Qt.AlignCenter)
        self.le_memoria_restante.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.le_memoria_restante)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_10 = QSpacerItem(71, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)


        self.gridLayout_58.addWidget(self.frame_6, 0, 0, 1, 1)


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
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.groupBox_6 = QGroupBox(self.frame_7)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(100, 160))
        self.groupBox_6.setMaximumSize(QSize(16777215, 170))
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet(u"background-color: rgb(190, 190, 190);\n"
"color: rgb(0, 0, 255);")
        self.gridLayout_10 = QGridLayout(self.groupBox_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.Marco_memoria = QFrame(self.groupBox_6)
        self.Marco_memoria.setObjectName(u"Marco_memoria")
        self.Marco_memoria.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.Marco_memoria.setFrameShape(QFrame.StyledPanel)
        self.Marco_memoria.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.Marco_memoria)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(4)
        self.gridLayout_11.setVerticalSpacing(5)
        self.gridLayout_11.setContentsMargins(5, 5, 5, 5)
        self.marco7_3 = QFrame(self.Marco_memoria)
        self.marco7_3.setObjectName(u"marco7_3")
        self.marco7_3.setMinimumSize(QSize(100, 20))
        self.marco7_3.setMaximumSize(QSize(160, 25))
        self.marco7_3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco7_3.setFrameShape(QFrame.StyledPanel)
        self.marco7_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_40 = QGridLayout(self.marco7_3)
        self.gridLayout_40.setSpacing(0)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(0, 0, 0, 0)
        self.progressBar_25 = QProgressBar(self.marco7_3)
        self.progressBar_25.setObjectName(u"progressBar_25")
        self.progressBar_25.setMinimumSize(QSize(0, 9))
        self.progressBar_25.setMaximumSize(QSize(16777215, 14))
        self.progressBar_25.setValue(0)
        self.progressBar_25.setTextVisible(False)

        self.gridLayout_40.addWidget(self.progressBar_25, 1, 0, 1, 1)

        self.lbl_pb25 = QLabel(self.marco7_3)
        self.lbl_pb25.setObjectName(u"lbl_pb25")
        self.lbl_pb25.setMinimumSize(QSize(0, 9))
        self.lbl_pb25.setMaximumSize(QSize(16777215, 9))
        font4 = QFont()
        font4.setFamily(u"Times New Roman")
        font4.setPointSize(7)
        self.lbl_pb25.setFont(font4)
        self.lbl_pb25.setAlignment(Qt.AlignCenter)

        self.gridLayout_40.addWidget(self.lbl_pb25, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco7_3, 2, 6, 1, 1)

        self.marco8_2 = QFrame(self.Marco_memoria)
        self.marco8_2.setObjectName(u"marco8_2")
        self.marco8_2.setMinimumSize(QSize(100, 20))
        self.marco8_2.setMaximumSize(QSize(160, 25))
        self.marco8_2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco8_2.setFrameShape(QFrame.StyledPanel)
        self.marco8_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.marco8_2)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.progressBar_15 = QProgressBar(self.marco8_2)
        self.progressBar_15.setObjectName(u"progressBar_15")
        self.progressBar_15.setMinimumSize(QSize(0, 9))
        self.progressBar_15.setMaximumSize(QSize(16777215, 14))
        self.progressBar_15.setValue(0)
        self.progressBar_15.setTextVisible(False)

        self.gridLayout_30.addWidget(self.progressBar_15, 1, 0, 1, 1)

        self.lbl_pb15 = QLabel(self.marco8_2)
        self.lbl_pb15.setObjectName(u"lbl_pb15")
        self.lbl_pb15.setMinimumSize(QSize(0, 9))
        self.lbl_pb15.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb15.setFont(font4)
        self.lbl_pb15.setAlignment(Qt.AlignCenter)

        self.gridLayout_30.addWidget(self.lbl_pb15, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco8_2, 1, 7, 1, 1)

        self.marco4 = QFrame(self.Marco_memoria)
        self.marco4.setObjectName(u"marco4")
        self.marco4.setMinimumSize(QSize(0, 20))
        self.marco4.setMaximumSize(QSize(160, 25))
        self.marco4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco4.setFrameShape(QFrame.StyledPanel)
        self.marco4.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.marco4)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.marco4)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(0, 9))
        self.label_47.setMaximumSize(QSize(16777215, 9))
        self.label_47.setFont(font4)
        self.label_47.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_15.addWidget(self.label_47, 0, 1, 1, 1)

        self.progressBar_44 = QProgressBar(self.marco4)
        self.progressBar_44.setObjectName(u"progressBar_44")
        self.progressBar_44.setMinimumSize(QSize(0, 9))
        self.progressBar_44.setMaximumSize(QSize(16777215, 14))
        self.progressBar_44.setStyleSheet(u"QProgressBar {\n"
"\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"                \n"
"	background-color: rgb(0, 85, 255);\n"
"	\n"
"	background-color: rgb(85, 0, 0);\n"
"}")
        self.progressBar_44.setValue(100)
        self.progressBar_44.setTextVisible(False)

        self.gridLayout_15.addWidget(self.progressBar_44, 1, 1, 1, 1)


        self.gridLayout_11.addWidget(self.marco4, 0, 3, 1, 1)

        self.marco9_2 = QFrame(self.Marco_memoria)
        self.marco9_2.setObjectName(u"marco9_2")
        self.marco9_2.setMinimumSize(QSize(100, 20))
        self.marco9_2.setMaximumSize(QSize(160, 25))
        self.marco9_2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco9_2.setFrameShape(QFrame.StyledPanel)
        self.marco9_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.marco9_2)
        self.gridLayout_31.setSpacing(0)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.progressBar_16 = QProgressBar(self.marco9_2)
        self.progressBar_16.setObjectName(u"progressBar_16")
        self.progressBar_16.setMinimumSize(QSize(0, 9))
        self.progressBar_16.setMaximumSize(QSize(16777215, 14))
        self.progressBar_16.setValue(0)
        self.progressBar_16.setTextVisible(False)

        self.gridLayout_31.addWidget(self.progressBar_16, 1, 0, 1, 1)

        self.lbl_pb16 = QLabel(self.marco9_2)
        self.lbl_pb16.setObjectName(u"lbl_pb16")
        self.lbl_pb16.setMinimumSize(QSize(0, 9))
        self.lbl_pb16.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb16.setFont(font4)
        self.lbl_pb16.setAlignment(Qt.AlignCenter)

        self.gridLayout_31.addWidget(self.lbl_pb16, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco9_2, 1, 8, 1, 1)

        self.marco10 = QFrame(self.Marco_memoria)
        self.marco10.setObjectName(u"marco10")
        self.marco10.setMinimumSize(QSize(100, 20))
        self.marco10.setMaximumSize(QSize(160, 25))
        self.marco10.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco10.setFrameShape(QFrame.StyledPanel)
        self.marco10.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.marco10)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb6 = QLabel(self.marco10)
        self.lbl_pb6.setObjectName(u"lbl_pb6")
        self.lbl_pb6.setMinimumSize(QSize(0, 9))
        self.lbl_pb6.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb6.setFont(font4)
        self.lbl_pb6.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.lbl_pb6, 0, 0, 1, 1)

        self.progressBar_6 = QProgressBar(self.marco10)
        self.progressBar_6.setObjectName(u"progressBar_6")
        self.progressBar_6.setMinimumSize(QSize(0, 9))
        self.progressBar_6.setMaximumSize(QSize(16777215, 14))
        self.progressBar_6.setValue(0)
        self.progressBar_6.setTextVisible(False)

        self.gridLayout_21.addWidget(self.progressBar_6, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco10, 0, 9, 1, 1)

        self.marco8_4 = QFrame(self.Marco_memoria)
        self.marco8_4.setObjectName(u"marco8_4")
        self.marco8_4.setMinimumSize(QSize(100, 20))
        self.marco8_4.setMaximumSize(QSize(160, 25))
        self.marco8_4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco8_4.setFrameShape(QFrame.StyledPanel)
        self.marco8_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_52 = QGridLayout(self.marco8_4)
        self.gridLayout_52.setSpacing(0)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.gridLayout_52.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb37 = QLabel(self.marco8_4)
        self.lbl_pb37.setObjectName(u"lbl_pb37")
        self.lbl_pb37.setMinimumSize(QSize(0, 9))
        self.lbl_pb37.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb37.setFont(font4)
        self.lbl_pb37.setAlignment(Qt.AlignCenter)

        self.gridLayout_52.addWidget(self.lbl_pb37, 0, 0, 1, 1)

        self.progressBar_37 = QProgressBar(self.marco8_4)
        self.progressBar_37.setObjectName(u"progressBar_37")
        self.progressBar_37.setMinimumSize(QSize(0, 9))
        self.progressBar_37.setMaximumSize(QSize(16777215, 14))
        self.progressBar_37.setValue(0)
        self.progressBar_37.setTextVisible(False)

        self.gridLayout_52.addWidget(self.progressBar_37, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco8_4, 3, 7, 1, 1)

        self.marco8_3 = QFrame(self.Marco_memoria)
        self.marco8_3.setObjectName(u"marco8_3")
        self.marco8_3.setMinimumSize(QSize(100, 20))
        self.marco8_3.setMaximumSize(QSize(160, 25))
        self.marco8_3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco8_3.setFrameShape(QFrame.StyledPanel)
        self.marco8_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_41 = QGridLayout(self.marco8_3)
        self.gridLayout_41.setSpacing(0)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
        self.progressBar_26 = QProgressBar(self.marco8_3)
        self.progressBar_26.setObjectName(u"progressBar_26")
        self.progressBar_26.setMinimumSize(QSize(0, 9))
        self.progressBar_26.setMaximumSize(QSize(16777215, 14))
        self.progressBar_26.setValue(0)
        self.progressBar_26.setTextVisible(False)

        self.gridLayout_41.addWidget(self.progressBar_26, 1, 0, 1, 1)

        self.lbl_pb26 = QLabel(self.marco8_3)
        self.lbl_pb26.setObjectName(u"lbl_pb26")
        self.lbl_pb26.setMinimumSize(QSize(0, 9))
        self.lbl_pb26.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb26.setFont(font4)
        self.lbl_pb26.setAlignment(Qt.AlignCenter)

        self.gridLayout_41.addWidget(self.lbl_pb26, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco8_3, 2, 7, 1, 1)

        self.marco1_2 = QFrame(self.Marco_memoria)
        self.marco1_2.setObjectName(u"marco1_2")
        self.marco1_2.setMinimumSize(QSize(100, 20))
        self.marco1_2.setMaximumSize(QSize(160, 25))
        self.marco1_2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco1_2.setFrameShape(QFrame.StyledPanel)
        self.marco1_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.marco1_2)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb8 = QLabel(self.marco1_2)
        self.lbl_pb8.setObjectName(u"lbl_pb8")
        self.lbl_pb8.setMinimumSize(QSize(0, 9))
        self.lbl_pb8.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb8.setFont(font4)
        self.lbl_pb8.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.lbl_pb8, 0, 0, 1, 1)

        self.progressBar_8 = QProgressBar(self.marco1_2)
        self.progressBar_8.setObjectName(u"progressBar_8")
        self.progressBar_8.setMinimumSize(QSize(0, 9))
        self.progressBar_8.setMaximumSize(QSize(16777215, 14))
        self.progressBar_8.setValue(0)
        self.progressBar_8.setTextVisible(False)

        self.gridLayout_23.addWidget(self.progressBar_8, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco1_2, 1, 0, 1, 1)

        self.marco10_8 = QFrame(self.Marco_memoria)
        self.marco10_8.setObjectName(u"marco10_8")
        self.marco10_8.setMinimumSize(QSize(100, 20))
        self.marco10_8.setMaximumSize(QSize(160, 25))
        self.marco10_8.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco10_8.setFrameShape(QFrame.StyledPanel)
        self.marco10_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_33 = QGridLayout(self.marco10_8)
        self.gridLayout_33.setSpacing(0)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setContentsMargins(0, 0, 0, 0)
        self.progressBar_18 = QProgressBar(self.marco10_8)
        self.progressBar_18.setObjectName(u"progressBar_18")
        self.progressBar_18.setMinimumSize(QSize(0, 9))
        self.progressBar_18.setMaximumSize(QSize(16777215, 14))
        self.progressBar_18.setValue(0)
        self.progressBar_18.setTextVisible(False)

        self.gridLayout_33.addWidget(self.progressBar_18, 1, 0, 1, 1)

        self.lbl_pb18 = QLabel(self.marco10_8)
        self.lbl_pb18.setObjectName(u"lbl_pb18")
        self.lbl_pb18.setMinimumSize(QSize(0, 9))
        self.lbl_pb18.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb18.setFont(font4)
        self.lbl_pb18.setAlignment(Qt.AlignCenter)

        self.gridLayout_33.addWidget(self.lbl_pb18, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco10_8, 1, 10, 1, 1)

        self.marco9_4 = QFrame(self.Marco_memoria)
        self.marco9_4.setObjectName(u"marco9_4")
        self.marco9_4.setMinimumSize(QSize(100, 20))
        self.marco9_4.setMaximumSize(QSize(160, 25))
        self.marco9_4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco9_4.setFrameShape(QFrame.StyledPanel)
        self.marco9_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_53 = QGridLayout(self.marco9_4)
        self.gridLayout_53.setSpacing(0)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.gridLayout_53.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb38 = QLabel(self.marco9_4)
        self.lbl_pb38.setObjectName(u"lbl_pb38")
        self.lbl_pb38.setMinimumSize(QSize(0, 9))
        self.lbl_pb38.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb38.setFont(font4)
        self.lbl_pb38.setAlignment(Qt.AlignCenter)

        self.gridLayout_53.addWidget(self.lbl_pb38, 0, 0, 1, 1)

        self.progressBar_38 = QProgressBar(self.marco9_4)
        self.progressBar_38.setObjectName(u"progressBar_38")
        self.progressBar_38.setMinimumSize(QSize(0, 9))
        self.progressBar_38.setMaximumSize(QSize(16777215, 14))
        self.progressBar_38.setValue(0)
        self.progressBar_38.setTextVisible(False)

        self.gridLayout_53.addWidget(self.progressBar_38, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco9_4, 3, 8, 1, 1)

        self.marco3_4 = QFrame(self.Marco_memoria)
        self.marco3_4.setObjectName(u"marco3_4")
        self.marco3_4.setMinimumSize(QSize(100, 20))
        self.marco3_4.setMaximumSize(QSize(160, 25))
        self.marco3_4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco3_4.setFrameShape(QFrame.StyledPanel)
        self.marco3_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_47 = QGridLayout(self.marco3_4)
        self.gridLayout_47.setSpacing(0)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.gridLayout_47.setContentsMargins(0, 0, 0, 0)
        self.progressBar_32 = QProgressBar(self.marco3_4)
        self.progressBar_32.setObjectName(u"progressBar_32")
        self.progressBar_32.setMinimumSize(QSize(0, 9))
        self.progressBar_32.setMaximumSize(QSize(16777215, 14))
        self.progressBar_32.setValue(0)
        self.progressBar_32.setTextVisible(False)

        self.gridLayout_47.addWidget(self.progressBar_32, 1, 0, 1, 1)

        self.lbl_pb32 = QLabel(self.marco3_4)
        self.lbl_pb32.setObjectName(u"lbl_pb32")
        self.lbl_pb32.setMinimumSize(QSize(0, 9))
        self.lbl_pb32.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb32.setFont(font4)
        self.lbl_pb32.setAlignment(Qt.AlignCenter)

        self.gridLayout_47.addWidget(self.lbl_pb32, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco3_4, 3, 2, 1, 1)

        self.marco6_4 = QFrame(self.Marco_memoria)
        self.marco6_4.setObjectName(u"marco6_4")
        self.marco6_4.setMinimumSize(QSize(100, 20))
        self.marco6_4.setMaximumSize(QSize(160, 25))
        self.marco6_4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco6_4.setFrameShape(QFrame.StyledPanel)
        self.marco6_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_50 = QGridLayout(self.marco6_4)
        self.gridLayout_50.setSpacing(0)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_50.setContentsMargins(0, 0, 0, 0)
        self.progressBar_35 = QProgressBar(self.marco6_4)
        self.progressBar_35.setObjectName(u"progressBar_35")
        self.progressBar_35.setMinimumSize(QSize(0, 9))
        self.progressBar_35.setMaximumSize(QSize(16777215, 14))
        self.progressBar_35.setValue(0)
        self.progressBar_35.setTextVisible(False)

        self.gridLayout_50.addWidget(self.progressBar_35, 2, 1, 1, 1)

        self.lbl_pb35 = QLabel(self.marco6_4)
        self.lbl_pb35.setObjectName(u"lbl_pb35")
        self.lbl_pb35.setMinimumSize(QSize(0, 9))
        self.lbl_pb35.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb35.setFont(font4)
        self.lbl_pb35.setAlignment(Qt.AlignCenter)

        self.gridLayout_50.addWidget(self.lbl_pb35, 1, 1, 1, 1)


        self.gridLayout_11.addWidget(self.marco6_4, 3, 5, 1, 1)

        self.marco5 = QFrame(self.Marco_memoria)
        self.marco5.setObjectName(u"marco5")
        self.marco5.setMinimumSize(QSize(100, 20))
        self.marco5.setMaximumSize(QSize(160, 25))
        self.marco5.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco5.setFrameShape(QFrame.StyledPanel)
        self.marco5.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.marco5)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb1 = QLabel(self.marco5)
        self.lbl_pb1.setObjectName(u"lbl_pb1")
        self.lbl_pb1.setMinimumSize(QSize(0, 9))
        self.lbl_pb1.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb1.setFont(font4)
        self.lbl_pb1.setStyleSheet(u"")
        self.lbl_pb1.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.lbl_pb1, 0, 0, 1, 1)

        self.progressBar_1 = QProgressBar(self.marco5)
        self.progressBar_1.setObjectName(u"progressBar_1")
        self.progressBar_1.setMinimumSize(QSize(0, 9))
        self.progressBar_1.setMaximumSize(QSize(16777215, 14))
        self.progressBar_1.setStyleSheet(u"")
        self.progressBar_1.setValue(0)
        self.progressBar_1.setTextVisible(False)

        self.gridLayout_16.addWidget(self.progressBar_1, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco5, 0, 4, 1, 1)

        self.Marco = QFrame(self.Marco_memoria)
        self.Marco.setObjectName(u"Marco")
        self.Marco.setMinimumSize(QSize(100, 20))
        self.Marco.setMaximumSize(QSize(160, 25))
        self.Marco.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.Marco.setFrameShape(QFrame.StyledPanel)
        self.Marco.setFrameShadow(QFrame.Raised)
        self.gridLayout_43 = QGridLayout(self.Marco)
        self.gridLayout_43.setSpacing(0)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb28 = QLabel(self.Marco)
        self.lbl_pb28.setObjectName(u"lbl_pb28")
        self.lbl_pb28.setMinimumSize(QSize(0, 9))
        self.lbl_pb28.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb28.setFont(font4)
        self.lbl_pb28.setAlignment(Qt.AlignCenter)

        self.gridLayout_43.addWidget(self.lbl_pb28, 0, 0, 1, 1)

        self.progressBar_28 = QProgressBar(self.Marco)
        self.progressBar_28.setObjectName(u"progressBar_28")
        self.progressBar_28.setMinimumSize(QSize(0, 9))
        self.progressBar_28.setMaximumSize(QSize(16777215, 14))
        self.progressBar_28.setValue(0)
        self.progressBar_28.setTextVisible(False)

        self.gridLayout_43.addWidget(self.progressBar_28, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.Marco, 2, 9, 1, 1)

        self.marco5_2 = QFrame(self.Marco_memoria)
        self.marco5_2.setObjectName(u"marco5_2")
        self.marco5_2.setMinimumSize(QSize(100, 20))
        self.marco5_2.setMaximumSize(QSize(160, 25))
        self.marco5_2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco5_2.setFrameShape(QFrame.StyledPanel)
        self.marco5_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.marco5_2)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb12 = QLabel(self.marco5_2)
        self.lbl_pb12.setObjectName(u"lbl_pb12")
        self.lbl_pb12.setMinimumSize(QSize(0, 9))
        self.lbl_pb12.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb12.setFont(font4)
        self.lbl_pb12.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.lbl_pb12, 0, 0, 1, 1)

        self.progressBar_12 = QProgressBar(self.marco5_2)
        self.progressBar_12.setObjectName(u"progressBar_12")
        self.progressBar_12.setMinimumSize(QSize(0, 9))
        self.progressBar_12.setMaximumSize(QSize(16777215, 14))
        self.progressBar_12.setValue(0)
        self.progressBar_12.setTextVisible(False)

        self.gridLayout_27.addWidget(self.progressBar_12, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco5_2, 1, 4, 1, 1)

        self.marco1_3 = QFrame(self.Marco_memoria)
        self.marco1_3.setObjectName(u"marco1_3")
        self.marco1_3.setMinimumSize(QSize(100, 20))
        self.marco1_3.setMaximumSize(QSize(160, 25))
        self.marco1_3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco1_3.setFrameShape(QFrame.StyledPanel)
        self.marco1_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_34 = QGridLayout(self.marco1_3)
        self.gridLayout_34.setSpacing(0)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb19 = QLabel(self.marco1_3)
        self.lbl_pb19.setObjectName(u"lbl_pb19")
        self.lbl_pb19.setMinimumSize(QSize(0, 9))
        self.lbl_pb19.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb19.setFont(font4)
        self.lbl_pb19.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.lbl_pb19, 0, 0, 1, 1)

        self.progressBar_19 = QProgressBar(self.marco1_3)
        self.progressBar_19.setObjectName(u"progressBar_19")
        self.progressBar_19.setMinimumSize(QSize(0, 9))
        self.progressBar_19.setMaximumSize(QSize(16777215, 14))
        self.progressBar_19.setValue(0)
        self.progressBar_19.setTextVisible(False)

        self.gridLayout_34.addWidget(self.progressBar_19, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco1_3, 2, 0, 1, 1)

        self.marco4_2 = QFrame(self.Marco_memoria)
        self.marco4_2.setObjectName(u"marco4_2")
        self.marco4_2.setMinimumSize(QSize(100, 20))
        self.marco4_2.setMaximumSize(QSize(160, 25))
        self.marco4_2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco4_2.setFrameShape(QFrame.StyledPanel)
        self.marco4_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.marco4_2)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb11 = QLabel(self.marco4_2)
        self.lbl_pb11.setObjectName(u"lbl_pb11")
        self.lbl_pb11.setMinimumSize(QSize(0, 9))
        self.lbl_pb11.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb11.setFont(font4)
        self.lbl_pb11.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.lbl_pb11, 0, 0, 1, 1)

        self.progressBar_11 = QProgressBar(self.marco4_2)
        self.progressBar_11.setObjectName(u"progressBar_11")
        self.progressBar_11.setMinimumSize(QSize(0, 9))
        self.progressBar_11.setMaximumSize(QSize(16777215, 14))
        self.progressBar_11.setValue(0)
        self.progressBar_11.setTextVisible(False)

        self.gridLayout_26.addWidget(self.progressBar_11, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco4_2, 1, 3, 1, 1)

        self.marco5_3 = QFrame(self.Marco_memoria)
        self.marco5_3.setObjectName(u"marco5_3")
        self.marco5_3.setMinimumSize(QSize(100, 20))
        self.marco5_3.setMaximumSize(QSize(160, 25))
        self.marco5_3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco5_3.setFrameShape(QFrame.StyledPanel)
        self.marco5_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_38 = QGridLayout(self.marco5_3)
        self.gridLayout_38.setSpacing(0)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(0, 0, 0, 0)
        self.progressBar_23 = QProgressBar(self.marco5_3)
        self.progressBar_23.setObjectName(u"progressBar_23")
        self.progressBar_23.setMinimumSize(QSize(0, 9))
        self.progressBar_23.setMaximumSize(QSize(16777215, 14))
        self.progressBar_23.setValue(0)
        self.progressBar_23.setTextVisible(False)

        self.gridLayout_38.addWidget(self.progressBar_23, 1, 0, 1, 1)

        self.lbl_pb23 = QLabel(self.marco5_3)
        self.lbl_pb23.setObjectName(u"lbl_pb23")
        self.lbl_pb23.setMinimumSize(QSize(0, 9))
        self.lbl_pb23.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb23.setFont(font4)
        self.lbl_pb23.setAlignment(Qt.AlignCenter)

        self.gridLayout_38.addWidget(self.lbl_pb23, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco5_3, 2, 4, 1, 1)

        self.marco9_3 = QFrame(self.Marco_memoria)
        self.marco9_3.setObjectName(u"marco9_3")
        self.marco9_3.setMinimumSize(QSize(100, 20))
        self.marco9_3.setMaximumSize(QSize(160, 25))
        self.marco9_3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco9_3.setFrameShape(QFrame.StyledPanel)
        self.marco9_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_42 = QGridLayout(self.marco9_3)
        self.gridLayout_42.setSpacing(0)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setContentsMargins(0, 0, 0, 0)
        self.progressBar_27 = QProgressBar(self.marco9_3)
        self.progressBar_27.setObjectName(u"progressBar_27")
        self.progressBar_27.setMinimumSize(QSize(0, 9))
        self.progressBar_27.setMaximumSize(QSize(16777215, 14))
        self.progressBar_27.setValue(0)
        self.progressBar_27.setTextVisible(False)

        self.gridLayout_42.addWidget(self.progressBar_27, 1, 0, 1, 1)

        self.lbl_pb27 = QLabel(self.marco9_3)
        self.lbl_pb27.setObjectName(u"lbl_pb27")
        self.lbl_pb27.setMinimumSize(QSize(0, 9))
        self.lbl_pb27.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb27.setFont(font4)
        self.lbl_pb27.setAlignment(Qt.AlignCenter)

        self.gridLayout_42.addWidget(self.lbl_pb27, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco9_3, 2, 8, 1, 1)

        self.marco3_3 = QFrame(self.Marco_memoria)
        self.marco3_3.setObjectName(u"marco3_3")
        self.marco3_3.setMinimumSize(QSize(100, 20))
        self.marco3_3.setMaximumSize(QSize(160, 25))
        self.marco3_3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco3_3.setFrameShape(QFrame.StyledPanel)
        self.marco3_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_36 = QGridLayout(self.marco3_3)
        self.gridLayout_36.setSpacing(0)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb21 = QLabel(self.marco3_3)
        self.lbl_pb21.setObjectName(u"lbl_pb21")
        self.lbl_pb21.setMinimumSize(QSize(0, 9))
        self.lbl_pb21.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb21.setFont(font4)
        self.lbl_pb21.setAlignment(Qt.AlignCenter)

        self.gridLayout_36.addWidget(self.lbl_pb21, 0, 1, 1, 1)

        self.progressBar_21 = QProgressBar(self.marco3_3)
        self.progressBar_21.setObjectName(u"progressBar_21")
        self.progressBar_21.setMinimumSize(QSize(0, 9))
        self.progressBar_21.setMaximumSize(QSize(16777215, 14))
        self.progressBar_21.setValue(0)
        self.progressBar_21.setTextVisible(False)

        self.gridLayout_36.addWidget(self.progressBar_21, 1, 1, 1, 1)


        self.gridLayout_11.addWidget(self.marco3_3, 2, 2, 1, 1)

        self.marco1_4 = QFrame(self.Marco_memoria)
        self.marco1_4.setObjectName(u"marco1_4")
        self.marco1_4.setMinimumSize(QSize(100, 20))
        self.marco1_4.setMaximumSize(QSize(160, 25))
        self.marco1_4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco1_4.setFrameShape(QFrame.StyledPanel)
        self.marco1_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_45 = QGridLayout(self.marco1_4)
        self.gridLayout_45.setSpacing(0)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(0, 0, 0, 0)
        self.progressBar_30 = QProgressBar(self.marco1_4)
        self.progressBar_30.setObjectName(u"progressBar_30")
        self.progressBar_30.setMinimumSize(QSize(0, 9))
        self.progressBar_30.setMaximumSize(QSize(16777215, 14))
        self.progressBar_30.setValue(0)
        self.progressBar_30.setTextVisible(False)

        self.gridLayout_45.addWidget(self.progressBar_30, 1, 0, 1, 1)

        self.lbl_pb30 = QLabel(self.marco1_4)
        self.lbl_pb30.setObjectName(u"lbl_pb30")
        self.lbl_pb30.setMinimumSize(QSize(0, 9))
        self.lbl_pb30.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb30.setFont(font4)
        self.lbl_pb30.setAlignment(Qt.AlignCenter)

        self.gridLayout_45.addWidget(self.lbl_pb30, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco1_4, 3, 0, 1, 1)

        self.marco6 = QFrame(self.Marco_memoria)
        self.marco6.setObjectName(u"marco6")
        self.marco6.setMinimumSize(QSize(100, 20))
        self.marco6.setMaximumSize(QSize(160, 25))
        self.marco6.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco6.setFrameShape(QFrame.StyledPanel)
        self.marco6.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.marco6)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb2 = QLabel(self.marco6)
        self.lbl_pb2.setObjectName(u"lbl_pb2")
        self.lbl_pb2.setMinimumSize(QSize(0, 9))
        self.lbl_pb2.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb2.setFont(font4)
        self.lbl_pb2.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.lbl_pb2, 0, 0, 1, 1)

        self.progressBar_2 = QProgressBar(self.marco6)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setMinimumSize(QSize(0, 9))
        self.progressBar_2.setMaximumSize(QSize(16777215, 14))
        self.progressBar_2.setValue(0)
        self.progressBar_2.setTextVisible(False)

        self.gridLayout_17.addWidget(self.progressBar_2, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco6, 0, 5, 1, 1)

        self.marco10_4 = QFrame(self.Marco_memoria)
        self.marco10_4.setObjectName(u"marco10_4")
        self.marco10_4.setMinimumSize(QSize(100, 20))
        self.marco10_4.setMaximumSize(QSize(160, 25))
        self.marco10_4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco10_4.setFrameShape(QFrame.StyledPanel)
        self.marco10_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_54 = QGridLayout(self.marco10_4)
        self.gridLayout_54.setSpacing(0)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.gridLayout_54.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb39 = QLabel(self.marco10_4)
        self.lbl_pb39.setObjectName(u"lbl_pb39")
        self.lbl_pb39.setMinimumSize(QSize(0, 9))
        self.lbl_pb39.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb39.setFont(font4)
        self.lbl_pb39.setAlignment(Qt.AlignCenter)

        self.gridLayout_54.addWidget(self.lbl_pb39, 0, 0, 1, 1)

        self.progressBar_39 = QProgressBar(self.marco10_4)
        self.progressBar_39.setObjectName(u"progressBar_39")
        self.progressBar_39.setMinimumSize(QSize(0, 9))
        self.progressBar_39.setMaximumSize(QSize(16777215, 14))
        self.progressBar_39.setValue(0)
        self.progressBar_39.setTextVisible(False)

        self.gridLayout_54.addWidget(self.progressBar_39, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco10_4, 3, 9, 1, 1)

        self.marco3 = QFrame(self.Marco_memoria)
        self.marco3.setObjectName(u"marco3")
        self.marco3.setMinimumSize(QSize(100, 20))
        self.marco3.setMaximumSize(QSize(160, 25))
        self.marco3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco3.setFrameShape(QFrame.StyledPanel)
        self.marco3.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.marco3)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.progressBar_43 = QProgressBar(self.marco3)
        self.progressBar_43.setObjectName(u"progressBar_43")
        self.progressBar_43.setMinimumSize(QSize(0, 9))
        self.progressBar_43.setMaximumSize(QSize(16777215, 14))
        self.progressBar_43.setStyleSheet(u"QProgressBar {\n"
"\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"                \n"
"	background-color: rgb(0, 85, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	background-color: rgb(65, 65, 65);\n"
"	background-color: rgb(85, 0, 0);\n"
"}")
        self.progressBar_43.setValue(100)
        self.progressBar_43.setTextVisible(False)

        self.gridLayout_13.addWidget(self.progressBar_43, 1, 0, 1, 1)

        self.label_48 = QLabel(self.marco3)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(0, 9))
        self.label_48.setMaximumSize(QSize(16777215, 9))
        self.label_48.setFont(font4)
        self.label_48.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_13.addWidget(self.label_48, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco3, 0, 2, 1, 1)

        self.marco8 = QFrame(self.Marco_memoria)
        self.marco8.setObjectName(u"marco8")
        self.marco8.setMinimumSize(QSize(100, 20))
        self.marco8.setMaximumSize(QSize(160, 25))
        self.marco8.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco8.setFrameShape(QFrame.StyledPanel)
        self.marco8.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.marco8)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.progressBar_4 = QProgressBar(self.marco8)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setMinimumSize(QSize(0, 9))
        self.progressBar_4.setMaximumSize(QSize(16777215, 14))
        self.progressBar_4.setValue(0)
        self.progressBar_4.setTextVisible(False)

        self.gridLayout_19.addWidget(self.progressBar_4, 1, 0, 1, 1)

        self.lbl_pb4 = QLabel(self.marco8)
        self.lbl_pb4.setObjectName(u"lbl_pb4")
        self.lbl_pb4.setMinimumSize(QSize(0, 9))
        self.lbl_pb4.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb4.setFont(font4)
        self.lbl_pb4.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.lbl_pb4, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco8, 0, 7, 1, 1)

        self.marco2 = QFrame(self.Marco_memoria)
        self.marco2.setObjectName(u"marco2")
        self.marco2.setMinimumSize(QSize(100, 20))
        self.marco2.setMaximumSize(QSize(160, 25))
        self.marco2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco2.setFrameShape(QFrame.StyledPanel)
        self.marco2.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.marco2)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.marco2)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(0, 9))
        self.label_49.setMaximumSize(QSize(16777215, 9))
        self.label_49.setFont(font4)
        self.label_49.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_14.addWidget(self.label_49, 0, 1, 1, 1)

        self.progressBar_42 = QProgressBar(self.marco2)
        self.progressBar_42.setObjectName(u"progressBar_42")
        self.progressBar_42.setMinimumSize(QSize(0, 9))
        self.progressBar_42.setMaximumSize(QSize(16777215, 14))
        self.progressBar_42.setStyleSheet(u"QProgressBar {\n"
"\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"                \n"
"	background-color: rgb(0, 85, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	background-color: rgb(65, 65, 65);\n"
"	background-color: rgb(85, 0, 0);\n"
"}")
        self.progressBar_42.setValue(100)
        self.progressBar_42.setTextVisible(False)

        self.gridLayout_14.addWidget(self.progressBar_42, 1, 1, 1, 1)


        self.gridLayout_11.addWidget(self.marco2, 0, 1, 1, 1)

        self.marco7_2 = QFrame(self.Marco_memoria)
        self.marco7_2.setObjectName(u"marco7_2")
        self.marco7_2.setMinimumSize(QSize(100, 20))
        self.marco7_2.setMaximumSize(QSize(160, 25))
        self.marco7_2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco7_2.setFrameShape(QFrame.StyledPanel)
        self.marco7_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.marco7_2)
        self.gridLayout_29.setSpacing(0)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb14 = QLabel(self.marco7_2)
        self.lbl_pb14.setObjectName(u"lbl_pb14")
        self.lbl_pb14.setMinimumSize(QSize(0, 9))
        self.lbl_pb14.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb14.setFont(font4)
        self.lbl_pb14.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.lbl_pb14, 0, 0, 1, 1)

        self.progressBar_14 = QProgressBar(self.marco7_2)
        self.progressBar_14.setObjectName(u"progressBar_14")
        self.progressBar_14.setMinimumSize(QSize(0, 9))
        self.progressBar_14.setMaximumSize(QSize(16777215, 14))
        self.progressBar_14.setValue(0)
        self.progressBar_14.setTextVisible(False)

        self.gridLayout_29.addWidget(self.progressBar_14, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco7_2, 1, 6, 1, 1)

        self.marco4_4 = QFrame(self.Marco_memoria)
        self.marco4_4.setObjectName(u"marco4_4")
        self.marco4_4.setMinimumSize(QSize(100, 20))
        self.marco4_4.setMaximumSize(QSize(160, 25))
        self.marco4_4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco4_4.setFrameShape(QFrame.StyledPanel)
        self.marco4_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_48 = QGridLayout(self.marco4_4)
        self.gridLayout_48.setSpacing(0)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_48.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb33 = QLabel(self.marco4_4)
        self.lbl_pb33.setObjectName(u"lbl_pb33")
        self.lbl_pb33.setMinimumSize(QSize(0, 9))
        self.lbl_pb33.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb33.setFont(font4)
        self.lbl_pb33.setAlignment(Qt.AlignCenter)

        self.gridLayout_48.addWidget(self.lbl_pb33, 0, 2, 1, 1)

        self.progressBar_33 = QProgressBar(self.marco4_4)
        self.progressBar_33.setObjectName(u"progressBar_33")
        self.progressBar_33.setMinimumSize(QSize(0, 9))
        self.progressBar_33.setMaximumSize(QSize(16777215, 14))
        self.progressBar_33.setValue(0)
        self.progressBar_33.setTextVisible(False)

        self.gridLayout_48.addWidget(self.progressBar_33, 1, 2, 1, 1)


        self.gridLayout_11.addWidget(self.marco4_4, 3, 3, 1, 1)

        self.marco6_3 = QFrame(self.Marco_memoria)
        self.marco6_3.setObjectName(u"marco6_3")
        self.marco6_3.setMinimumSize(QSize(100, 20))
        self.marco6_3.setMaximumSize(QSize(160, 25))
        self.marco6_3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco6_3.setFrameShape(QFrame.StyledPanel)
        self.marco6_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_39 = QGridLayout(self.marco6_3)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setVerticalSpacing(0)
        self.gridLayout_39.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb24 = QLabel(self.marco6_3)
        self.lbl_pb24.setObjectName(u"lbl_pb24")
        self.lbl_pb24.setMinimumSize(QSize(0, 9))
        self.lbl_pb24.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb24.setFont(font4)
        self.lbl_pb24.setAlignment(Qt.AlignCenter)

        self.gridLayout_39.addWidget(self.lbl_pb24, 0, 0, 1, 1)

        self.progressBar_24 = QProgressBar(self.marco6_3)
        self.progressBar_24.setObjectName(u"progressBar_24")
        self.progressBar_24.setMinimumSize(QSize(0, 9))
        self.progressBar_24.setMaximumSize(QSize(16777215, 14))
        self.progressBar_24.setValue(0)
        self.progressBar_24.setTextVisible(False)

        self.gridLayout_39.addWidget(self.progressBar_24, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco6_3, 2, 5, 1, 1)

        self.marco3_2 = QFrame(self.Marco_memoria)
        self.marco3_2.setObjectName(u"marco3_2")
        self.marco3_2.setMinimumSize(QSize(100, 20))
        self.marco3_2.setMaximumSize(QSize(160, 25))
        self.marco3_2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco3_2.setFrameShape(QFrame.StyledPanel)
        self.marco3_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.marco3_2)
        self.gridLayout_25.setSpacing(0)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.progressBar_10 = QProgressBar(self.marco3_2)
        self.progressBar_10.setObjectName(u"progressBar_10")
        self.progressBar_10.setMinimumSize(QSize(0, 9))
        self.progressBar_10.setMaximumSize(QSize(16777215, 14))
        self.progressBar_10.setValue(0)
        self.progressBar_10.setTextVisible(False)

        self.gridLayout_25.addWidget(self.progressBar_10, 1, 0, 1, 1)

        self.lbl_pb10 = QLabel(self.marco3_2)
        self.lbl_pb10.setObjectName(u"lbl_pb10")
        self.lbl_pb10.setMinimumSize(QSize(0, 9))
        self.lbl_pb10.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb10.setFont(font4)
        self.lbl_pb10.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.lbl_pb10, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco3_2, 1, 2, 1, 1)

        self.marco5_4 = QFrame(self.Marco_memoria)
        self.marco5_4.setObjectName(u"marco5_4")
        self.marco5_4.setMinimumSize(QSize(100, 20))
        self.marco5_4.setMaximumSize(QSize(160, 25))
        self.marco5_4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco5_4.setFrameShape(QFrame.StyledPanel)
        self.marco5_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_49 = QGridLayout(self.marco5_4)
        self.gridLayout_49.setSpacing(0)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.gridLayout_49.setContentsMargins(0, 0, 0, 0)
        self.progressBar_34 = QProgressBar(self.marco5_4)
        self.progressBar_34.setObjectName(u"progressBar_34")
        self.progressBar_34.setMinimumSize(QSize(0, 9))
        self.progressBar_34.setMaximumSize(QSize(16777215, 14))
        self.progressBar_34.setValue(0)
        self.progressBar_34.setTextVisible(False)

        self.gridLayout_49.addWidget(self.progressBar_34, 1, 2, 1, 1)

        self.lbl_pb34 = QLabel(self.marco5_4)
        self.lbl_pb34.setObjectName(u"lbl_pb34")
        self.lbl_pb34.setMinimumSize(QSize(0, 9))
        self.lbl_pb34.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb34.setFont(font4)
        self.lbl_pb34.setAlignment(Qt.AlignCenter)

        self.gridLayout_49.addWidget(self.lbl_pb34, 0, 2, 1, 1)


        self.gridLayout_11.addWidget(self.marco5_4, 3, 4, 1, 1)

        self.marco7 = QFrame(self.Marco_memoria)
        self.marco7.setObjectName(u"marco7")
        self.marco7.setMinimumSize(QSize(100, 20))
        self.marco7.setMaximumSize(QSize(160, 25))
        self.marco7.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco7.setFrameShape(QFrame.StyledPanel)
        self.marco7.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.marco7)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.progressBar_3 = QProgressBar(self.marco7)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setMinimumSize(QSize(0, 9))
        self.progressBar_3.setMaximumSize(QSize(16777215, 14))
        self.progressBar_3.setValue(0)
        self.progressBar_3.setTextVisible(False)

        self.gridLayout_18.addWidget(self.progressBar_3, 1, 0, 1, 1)

        self.lbl_pb3 = QLabel(self.marco7)
        self.lbl_pb3.setObjectName(u"lbl_pb3")
        self.lbl_pb3.setMinimumSize(QSize(0, 9))
        self.lbl_pb3.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb3.setFont(font4)
        self.lbl_pb3.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.lbl_pb3, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco7, 0, 6, 1, 1)

        self.marco10_5 = QFrame(self.Marco_memoria)
        self.marco10_5.setObjectName(u"marco10_5")
        self.marco10_5.setMinimumSize(QSize(100, 20))
        self.marco10_5.setMaximumSize(QSize(160, 25))
        self.marco10_5.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco10_5.setFrameShape(QFrame.StyledPanel)
        self.marco10_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_44 = QGridLayout(self.marco10_5)
        self.gridLayout_44.setSpacing(0)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setContentsMargins(0, 0, 0, 0)
        self.progressBar_29 = QProgressBar(self.marco10_5)
        self.progressBar_29.setObjectName(u"progressBar_29")
        self.progressBar_29.setMinimumSize(QSize(0, 9))
        self.progressBar_29.setMaximumSize(QSize(16777215, 14))
        self.progressBar_29.setValue(0)
        self.progressBar_29.setTextVisible(False)

        self.gridLayout_44.addWidget(self.progressBar_29, 1, 0, 1, 1)

        self.lbl_pb29 = QLabel(self.marco10_5)
        self.lbl_pb29.setObjectName(u"lbl_pb29")
        self.lbl_pb29.setMinimumSize(QSize(0, 9))
        self.lbl_pb29.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb29.setFont(font4)
        self.lbl_pb29.setAlignment(Qt.AlignCenter)

        self.gridLayout_44.addWidget(self.lbl_pb29, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco10_5, 2, 10, 1, 1)

        self.marco10_7 = QFrame(self.Marco_memoria)
        self.marco10_7.setObjectName(u"marco10_7")
        self.marco10_7.setMinimumSize(QSize(100, 20))
        self.marco10_7.setMaximumSize(QSize(160, 25))
        self.marco10_7.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco10_7.setFrameShape(QFrame.StyledPanel)
        self.marco10_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_55 = QGridLayout(self.marco10_7)
        self.gridLayout_55.setSpacing(0)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.gridLayout_55.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb40 = QLabel(self.marco10_7)
        self.lbl_pb40.setObjectName(u"lbl_pb40")
        self.lbl_pb40.setMinimumSize(QSize(0, 9))
        self.lbl_pb40.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb40.setFont(font4)
        self.lbl_pb40.setAlignment(Qt.AlignCenter)

        self.gridLayout_55.addWidget(self.lbl_pb40, 0, 0, 1, 1)

        self.progressBar_40 = QProgressBar(self.marco10_7)
        self.progressBar_40.setObjectName(u"progressBar_40")
        self.progressBar_40.setMinimumSize(QSize(0, 9))
        self.progressBar_40.setMaximumSize(QSize(16777215, 14))
        self.progressBar_40.setValue(0)
        self.progressBar_40.setTextVisible(False)

        self.gridLayout_55.addWidget(self.progressBar_40, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco10_7, 3, 10, 1, 1)

        self.marco2_3 = QFrame(self.Marco_memoria)
        self.marco2_3.setObjectName(u"marco2_3")
        self.marco2_3.setMinimumSize(QSize(100, 20))
        self.marco2_3.setMaximumSize(QSize(160, 25))
        self.marco2_3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco2_3.setFrameShape(QFrame.StyledPanel)
        self.marco2_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.marco2_3)
        self.gridLayout_35.setSpacing(0)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb20 = QLabel(self.marco2_3)
        self.lbl_pb20.setObjectName(u"lbl_pb20")
        self.lbl_pb20.setMinimumSize(QSize(0, 9))
        self.lbl_pb20.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb20.setFont(font4)
        self.lbl_pb20.setAlignment(Qt.AlignCenter)

        self.gridLayout_35.addWidget(self.lbl_pb20, 0, 2, 1, 1)

        self.progressBar_20 = QProgressBar(self.marco2_3)
        self.progressBar_20.setObjectName(u"progressBar_20")
        self.progressBar_20.setMinimumSize(QSize(0, 9))
        self.progressBar_20.setMaximumSize(QSize(16777215, 14))
        self.progressBar_20.setValue(0)
        self.progressBar_20.setTextVisible(False)

        self.gridLayout_35.addWidget(self.progressBar_20, 1, 2, 1, 1)


        self.gridLayout_11.addWidget(self.marco2_3, 2, 1, 1, 1)

        self.marco1 = QFrame(self.Marco_memoria)
        self.marco1.setObjectName(u"marco1")
        self.marco1.setMinimumSize(QSize(100, 20))
        self.marco1.setMaximumSize(QSize(160, 25))
        self.marco1.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco1.setFrameShape(QFrame.StyledPanel)
        self.marco1.setFrameShadow(QFrame.Raised)
        self.gridLayout_56 = QGridLayout(self.marco1)
        self.gridLayout_56.setSpacing(0)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.gridLayout_56.setContentsMargins(0, 0, 0, 0)
        self.progressBar_41 = QProgressBar(self.marco1)
        self.progressBar_41.setObjectName(u"progressBar_41")
        self.progressBar_41.setMinimumSize(QSize(0, 9))
        self.progressBar_41.setMaximumSize(QSize(16777215, 14))
        self.progressBar_41.setStyleSheet(u"QProgressBar {\n"
"\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"                \n"
"	background-color: rgb(0, 85, 255);\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	\n"
"	background-color: rgb(65, 65, 65);\n"
"	background-color: rgb(85, 0, 0);\n"
"}")
        self.progressBar_41.setValue(100)
        self.progressBar_41.setTextVisible(False)

        self.gridLayout_56.addWidget(self.progressBar_41, 1, 0, 1, 1)

        self.label_50 = QLabel(self.marco1)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(0, 9))
        self.label_50.setMaximumSize(QSize(16777215, 9))
        self.label_50.setFont(font4)
        self.label_50.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_56.addWidget(self.label_50, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco1, 0, 0, 1, 1)

        self.marco7_4 = QFrame(self.Marco_memoria)
        self.marco7_4.setObjectName(u"marco7_4")
        self.marco7_4.setMinimumSize(QSize(100, 20))
        self.marco7_4.setMaximumSize(QSize(160, 25))
        self.marco7_4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco7_4.setFrameShape(QFrame.StyledPanel)
        self.marco7_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_51 = QGridLayout(self.marco7_4)
        self.gridLayout_51.setSpacing(0)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.gridLayout_51.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb36 = QLabel(self.marco7_4)
        self.lbl_pb36.setObjectName(u"lbl_pb36")
        self.lbl_pb36.setMinimumSize(QSize(0, 9))
        self.lbl_pb36.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb36.setFont(font4)
        self.lbl_pb36.setAlignment(Qt.AlignCenter)

        self.gridLayout_51.addWidget(self.lbl_pb36, 1, 0, 1, 1)

        self.progressBar_36 = QProgressBar(self.marco7_4)
        self.progressBar_36.setObjectName(u"progressBar_36")
        self.progressBar_36.setMinimumSize(QSize(0, 9))
        self.progressBar_36.setMaximumSize(QSize(16777215, 14))
        self.progressBar_36.setValue(0)
        self.progressBar_36.setTextVisible(False)

        self.gridLayout_51.addWidget(self.progressBar_36, 2, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco7_4, 3, 6, 1, 1)

        self.marco10_6 = QFrame(self.Marco_memoria)
        self.marco10_6.setObjectName(u"marco10_6")
        self.marco10_6.setMinimumSize(QSize(100, 20))
        self.marco10_6.setMaximumSize(QSize(160, 25))
        self.marco10_6.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco10_6.setFrameShape(QFrame.StyledPanel)
        self.marco10_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.marco10_6)
        self.gridLayout_22.setSpacing(0)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb7 = QLabel(self.marco10_6)
        self.lbl_pb7.setObjectName(u"lbl_pb7")
        self.lbl_pb7.setMinimumSize(QSize(0, 9))
        self.lbl_pb7.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb7.setFont(font4)
        self.lbl_pb7.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.lbl_pb7, 0, 0, 1, 1)

        self.progressBar_7 = QProgressBar(self.marco10_6)
        self.progressBar_7.setObjectName(u"progressBar_7")
        self.progressBar_7.setMinimumSize(QSize(0, 9))
        self.progressBar_7.setMaximumSize(QSize(16777215, 14))
        self.progressBar_7.setValue(0)
        self.progressBar_7.setTextVisible(False)

        self.gridLayout_22.addWidget(self.progressBar_7, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco10_6, 0, 10, 1, 1)

        self.marco9 = QFrame(self.Marco_memoria)
        self.marco9.setObjectName(u"marco9")
        self.marco9.setMinimumSize(QSize(100, 20))
        self.marco9.setMaximumSize(QSize(160, 25))
        self.marco9.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco9.setFrameShape(QFrame.StyledPanel)
        self.marco9.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.marco9)
        self.gridLayout_20.setSpacing(0)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.progressBar_5 = QProgressBar(self.marco9)
        self.progressBar_5.setObjectName(u"progressBar_5")
        self.progressBar_5.setMinimumSize(QSize(0, 9))
        self.progressBar_5.setMaximumSize(QSize(16777215, 14))
        self.progressBar_5.setValue(0)
        self.progressBar_5.setTextVisible(False)

        self.gridLayout_20.addWidget(self.progressBar_5, 1, 0, 1, 1)

        self.lbl_pb5 = QLabel(self.marco9)
        self.lbl_pb5.setObjectName(u"lbl_pb5")
        self.lbl_pb5.setMinimumSize(QSize(0, 9))
        self.lbl_pb5.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb5.setFont(font4)
        self.lbl_pb5.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.lbl_pb5, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco9, 0, 8, 1, 1)

        self.marco4_3 = QFrame(self.Marco_memoria)
        self.marco4_3.setObjectName(u"marco4_3")
        self.marco4_3.setMinimumSize(QSize(100, 20))
        self.marco4_3.setMaximumSize(QSize(160, 25))
        self.marco4_3.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco4_3.setFrameShape(QFrame.StyledPanel)
        self.marco4_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_37 = QGridLayout(self.marco4_3)
        self.gridLayout_37.setSpacing(0)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(0, 0, 0, 0)
        self.progressBar_22 = QProgressBar(self.marco4_3)
        self.progressBar_22.setObjectName(u"progressBar_22")
        self.progressBar_22.setMinimumSize(QSize(0, 9))
        self.progressBar_22.setMaximumSize(QSize(16777215, 14))
        self.progressBar_22.setValue(0)
        self.progressBar_22.setTextVisible(False)

        self.gridLayout_37.addWidget(self.progressBar_22, 1, 0, 1, 1)

        self.lbl_pb22 = QLabel(self.marco4_3)
        self.lbl_pb22.setObjectName(u"lbl_pb22")
        self.lbl_pb22.setMinimumSize(QSize(0, 9))
        self.lbl_pb22.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb22.setFont(font4)
        self.lbl_pb22.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.lbl_pb22, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco4_3, 2, 3, 1, 1)

        self.marco2_4 = QFrame(self.Marco_memoria)
        self.marco2_4.setObjectName(u"marco2_4")
        self.marco2_4.setMinimumSize(QSize(100, 20))
        self.marco2_4.setMaximumSize(QSize(160, 25))
        self.marco2_4.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco2_4.setFrameShape(QFrame.StyledPanel)
        self.marco2_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_46 = QGridLayout(self.marco2_4)
        self.gridLayout_46.setSpacing(0)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb31 = QLabel(self.marco2_4)
        self.lbl_pb31.setObjectName(u"lbl_pb31")
        self.lbl_pb31.setMinimumSize(QSize(0, 9))
        self.lbl_pb31.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb31.setFont(font4)
        self.lbl_pb31.setAlignment(Qt.AlignCenter)

        self.gridLayout_46.addWidget(self.lbl_pb31, 0, 0, 1, 1)

        self.progressBar_31 = QProgressBar(self.marco2_4)
        self.progressBar_31.setObjectName(u"progressBar_31")
        self.progressBar_31.setMinimumSize(QSize(0, 9))
        self.progressBar_31.setMaximumSize(QSize(16777215, 14))
        self.progressBar_31.setValue(0)
        self.progressBar_31.setTextVisible(False)

        self.gridLayout_46.addWidget(self.progressBar_31, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco2_4, 3, 1, 1, 1)

        self.marco2_2 = QFrame(self.Marco_memoria)
        self.marco2_2.setObjectName(u"marco2_2")
        self.marco2_2.setMinimumSize(QSize(100, 20))
        self.marco2_2.setMaximumSize(QSize(160, 25))
        self.marco2_2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco2_2.setFrameShape(QFrame.StyledPanel)
        self.marco2_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.marco2_2)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.progressBar_9 = QProgressBar(self.marco2_2)
        self.progressBar_9.setObjectName(u"progressBar_9")
        self.progressBar_9.setMinimumSize(QSize(0, 9))
        self.progressBar_9.setMaximumSize(QSize(16777215, 14))
        self.progressBar_9.setValue(0)
        self.progressBar_9.setTextVisible(False)

        self.gridLayout_24.addWidget(self.progressBar_9, 1, 0, 1, 1)

        self.lbl_pb9 = QLabel(self.marco2_2)
        self.lbl_pb9.setObjectName(u"lbl_pb9")
        self.lbl_pb9.setMinimumSize(QSize(0, 9))
        self.lbl_pb9.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb9.setFont(font4)
        self.lbl_pb9.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.lbl_pb9, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco2_2, 1, 1, 1, 1)

        self.marco10_2 = QFrame(self.Marco_memoria)
        self.marco10_2.setObjectName(u"marco10_2")
        self.marco10_2.setMinimumSize(QSize(100, 20))
        self.marco10_2.setMaximumSize(QSize(160, 25))
        self.marco10_2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco10_2.setFrameShape(QFrame.StyledPanel)
        self.marco10_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.marco10_2)
        self.gridLayout_32.setSpacing(0)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.progressBar_17 = QProgressBar(self.marco10_2)
        self.progressBar_17.setObjectName(u"progressBar_17")
        self.progressBar_17.setMinimumSize(QSize(0, 9))
        self.progressBar_17.setMaximumSize(QSize(16777215, 14))
        self.progressBar_17.setValue(0)
        self.progressBar_17.setTextVisible(False)

        self.gridLayout_32.addWidget(self.progressBar_17, 1, 0, 1, 1)

        self.lbl_pb17 = QLabel(self.marco10_2)
        self.lbl_pb17.setObjectName(u"lbl_pb17")
        self.lbl_pb17.setMinimumSize(QSize(0, 9))
        self.lbl_pb17.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb17.setFont(font4)
        self.lbl_pb17.setAlignment(Qt.AlignCenter)

        self.gridLayout_32.addWidget(self.lbl_pb17, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco10_2, 1, 9, 1, 1)

        self.marco6_2 = QFrame(self.Marco_memoria)
        self.marco6_2.setObjectName(u"marco6_2")
        self.marco6_2.setMinimumSize(QSize(100, 20))
        self.marco6_2.setMaximumSize(QSize(160, 25))
        self.marco6_2.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.marco6_2.setFrameShape(QFrame.StyledPanel)
        self.marco6_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.marco6_2)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.lbl_pb13 = QLabel(self.marco6_2)
        self.lbl_pb13.setObjectName(u"lbl_pb13")
        self.lbl_pb13.setMinimumSize(QSize(0, 9))
        self.lbl_pb13.setMaximumSize(QSize(16777215, 9))
        self.lbl_pb13.setFont(font4)
        self.lbl_pb13.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.lbl_pb13, 0, 0, 1, 1)

        self.progressBar_13 = QProgressBar(self.marco6_2)
        self.progressBar_13.setObjectName(u"progressBar_13")
        self.progressBar_13.setMinimumSize(QSize(0, 9))
        self.progressBar_13.setMaximumSize(QSize(16777215, 14))
        self.progressBar_13.setValue(0)
        self.progressBar_13.setTextVisible(False)

        self.gridLayout_28.addWidget(self.progressBar_13, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.marco6_2, 1, 5, 1, 1)


        self.gridLayout_10.addWidget(self.Marco_memoria, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_6, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_7, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1592, 21))
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
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Procesos iniciales: ", None))
        self.pb_agregar_procesos.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.pb_re_iniciar.setText(QCoreApplication.translate("MainWindow", u"Reiniciar", None))
        self.pb_iniciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Quantum: ", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Pr\u00f3ximo proceso nuevo", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.le_siguiente_id_nuevo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o: ", None))
        self.le_siguiente_tam_nuevo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"P\u00e1ginas: ", None))
        self.le_siguiente_pag_nuevo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Pr\u00f3ximo proceso suspendido", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.le_siguiente_id_suspendido.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o: ", None))
        self.le_siguiente_tam_suspendido.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"P\u00e1ginas: ", None))
        self.le_siguiente_pag_suspendido.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Prioridad: ", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Procesos del sistema", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Nuevos: ", None))
        self.le_procesos_nuevos.setText("")
        self.le_procesos_nuevos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Listos: ", None))
        self.le_procesos_listos.setText("")
        self.le_procesos_listos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Bloqueados: ", None))
        self.le_procesos_bloqueados.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Suspendidos: ", None))
        self.le_procesos_suspendidos.setText("")
        self.le_procesos_suspendidos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Terminados: ", None))
        self.le_procesos_terminados.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
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
        self.groupBox_12.setTitle("")
        self.lb_pausa.setText(QCoreApplication.translate("MainWindow", u"Ejecuci\u00f3n", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Marcos libres:", None))
        self.le_marcos_libres.setPlaceholderText(QCoreApplication.translate("MainWindow", u"40/44", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Memoria en uso:", None))
        self.le_memoria_uso.setPlaceholderText(QCoreApplication.translate("MainWindow", u" 20 MB / 220 MB", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Memoria disponible:", None))
        self.le_memoria_restante.setPlaceholderText(QCoreApplication.translate("MainWindow", u"200 MB / 220 MB", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Espacio de Memoria", None))
        self.lbl_pb25.setText(QCoreApplication.translate("MainWindow", u"Marco 28", None))
        self.lbl_pb15.setText(QCoreApplication.translate("MainWindow", u"Marco 18", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Marco 3: SO", None))
        self.lbl_pb16.setText(QCoreApplication.translate("MainWindow", u"Marco 19", None))
        self.lbl_pb6.setText(QCoreApplication.translate("MainWindow", u"Marco 9", None))
        self.lbl_pb37.setText(QCoreApplication.translate("MainWindow", u"Marco 40", None))
        self.lbl_pb26.setText(QCoreApplication.translate("MainWindow", u"Marco 29", None))
        self.lbl_pb8.setText(QCoreApplication.translate("MainWindow", u"Marco 11", None))
        self.lbl_pb18.setText(QCoreApplication.translate("MainWindow", u"Marco 21", None))
        self.lbl_pb38.setText(QCoreApplication.translate("MainWindow", u"Marco 41", None))
        self.lbl_pb32.setText(QCoreApplication.translate("MainWindow", u"Marco 35", None))
        self.lbl_pb35.setText(QCoreApplication.translate("MainWindow", u"Marco 38", None))
        self.lbl_pb1.setText(QCoreApplication.translate("MainWindow", u"Marco 4", None))
        self.lbl_pb28.setText(QCoreApplication.translate("MainWindow", u"Marco 31", None))
        self.lbl_pb12.setText(QCoreApplication.translate("MainWindow", u"Marco 15", None))
        self.lbl_pb19.setText(QCoreApplication.translate("MainWindow", u"Marco 22", None))
        self.lbl_pb11.setText(QCoreApplication.translate("MainWindow", u"Marco 14", None))
        self.lbl_pb23.setText(QCoreApplication.translate("MainWindow", u"Marco 26", None))
        self.lbl_pb27.setText(QCoreApplication.translate("MainWindow", u"Marco 30", None))
        self.lbl_pb21.setText(QCoreApplication.translate("MainWindow", u"Marco 24", None))
        self.lbl_pb30.setText(QCoreApplication.translate("MainWindow", u"Marco 33", None))
        self.lbl_pb2.setText(QCoreApplication.translate("MainWindow", u"Marco 5", None))
        self.lbl_pb39.setText(QCoreApplication.translate("MainWindow", u"Marco 42", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Marco 2: SO", None))
        self.lbl_pb4.setText(QCoreApplication.translate("MainWindow", u"Marco 7", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Marco 1: SO", None))
        self.lbl_pb14.setText(QCoreApplication.translate("MainWindow", u"Marco 17", None))
        self.lbl_pb33.setText(QCoreApplication.translate("MainWindow", u"Marco 36", None))
        self.lbl_pb24.setText(QCoreApplication.translate("MainWindow", u"Marco 27", None))
        self.lbl_pb10.setText(QCoreApplication.translate("MainWindow", u"Marco 13", None))
        self.lbl_pb34.setText(QCoreApplication.translate("MainWindow", u"Marco 37", None))
        self.lbl_pb3.setText(QCoreApplication.translate("MainWindow", u"Marco 6", None))
        self.lbl_pb29.setText(QCoreApplication.translate("MainWindow", u"Marco 32", None))
        self.lbl_pb40.setText(QCoreApplication.translate("MainWindow", u"Marco 43", None))
        self.lbl_pb20.setText(QCoreApplication.translate("MainWindow", u"Marco 23", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Marco 0: SO", None))
        self.lbl_pb36.setText(QCoreApplication.translate("MainWindow", u"Marco 39", None))
        self.lbl_pb7.setText(QCoreApplication.translate("MainWindow", u"Marco 10", None))
        self.lbl_pb5.setText(QCoreApplication.translate("MainWindow", u"Marco 8", None))
        self.lbl_pb22.setText(QCoreApplication.translate("MainWindow", u"Marco 25", None))
        self.lbl_pb31.setText(QCoreApplication.translate("MainWindow", u"Marco 34", None))
        self.lbl_pb9.setText(QCoreApplication.translate("MainWindow", u"Marco 12", None))
        self.lbl_pb17.setText(QCoreApplication.translate("MainWindow", u"Marco 20", None))
        self.lbl_pb13.setText(QCoreApplication.translate("MainWindow", u"Marco 16", None))
    # retranslateUi

