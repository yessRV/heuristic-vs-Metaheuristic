# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1095, 747)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionID = QAction(MainWindow)
        self.actionID.setObjectName(u"actionID")
        self.actionDistancia = QAction(MainWindow)
        self.actionDistancia.setObjectName(u"actionDistancia")
        self.actionVelocidad = QAction(MainWindow)
        self.actionVelocidad.setObjectName(u"actionVelocidad")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(11, 11, 281, 343))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_generar = QPushButton(self.groupBox)
        self.pushButton_generar.setObjectName(u"pushButton_generar")

        self.gridLayout_2.addWidget(self.pushButton_generar, 1, 0, 1, 2)

        self.label_red = QLabel(self.groupBox)
        self.label_red.setObjectName(u"label_red")

        self.gridLayout_2.addWidget(self.label_red, 6, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)

        self.label_velocidad = QLabel(self.groupBox)
        self.label_velocidad.setObjectName(u"label_velocidad")

        self.gridLayout_2.addWidget(self.label_velocidad, 8, 0, 1, 1)

        self.spinBox_poblacion = QSpinBox(self.groupBox)
        self.spinBox_poblacion.setObjectName(u"spinBox_poblacion")
        self.spinBox_poblacion.setMaximum(500)

        self.gridLayout_2.addWidget(self.spinBox_poblacion, 4, 1, 1, 1)

        self.spinBox_iteraciones = QSpinBox(self.groupBox)
        self.spinBox_iteraciones.setObjectName(u"spinBox_iteraciones")
        self.spinBox_iteraciones.setMaximum(500)

        self.gridLayout_2.addWidget(self.spinBox_iteraciones, 2, 1, 1, 1)

        self.spinBox_vertices = QSpinBox(self.groupBox)
        self.spinBox_vertices.setObjectName(u"spinBox_vertices")
        self.spinBox_vertices.setMaximum(1000)

        self.gridLayout_2.addWidget(self.spinBox_vertices, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.pushButton_pso = QPushButton(self.groupBox)
        self.pushButton_pso.setObjectName(u"pushButton_pso")

        self.gridLayout_2.addWidget(self.pushButton_pso, 12, 0, 1, 2)

        self.spinBox_alfa = QDoubleSpinBox(self.groupBox)
        self.spinBox_alfa.setObjectName(u"spinBox_alfa")
        self.spinBox_alfa.setDecimals(1)
        self.spinBox_alfa.setMaximum(2.000000000000000)
        self.spinBox_alfa.setSingleStep(0.100000000000000)
        self.spinBox_alfa.setValue(0.900000000000000)

        self.gridLayout_2.addWidget(self.spinBox_alfa, 6, 1, 1, 1)

        self.spinBox_beta = QDoubleSpinBox(self.groupBox)
        self.spinBox_beta.setObjectName(u"spinBox_beta")
        self.spinBox_beta.setDecimals(1)
        self.spinBox_beta.setMaximum(2.000000000000000)
        self.spinBox_beta.setSingleStep(0.100000000000000)
        self.spinBox_beta.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.spinBox_beta, 8, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(11, 361, 280, 331))
        self.verticalLayout = QVBoxLayout(self.groupBox_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plainTextEdit = QPlainTextEdit(self.groupBox_5)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.pushButton_mostrar = QPushButton(self.groupBox_5)
        self.pushButton_mostrar.setObjectName(u"pushButton_mostrar")
        self.pushButton_mostrar.setEnabled(False)

        self.verticalLayout.addWidget(self.pushButton_mostrar)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(305, 11, 771, 681))
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit_tab = QLineEdit(self.tab_2)
        self.lineEdit_tab.setObjectName(u"lineEdit_tab")
        self.lineEdit_tab.setEnabled(False)

        self.gridLayout_4.addWidget(self.lineEdit_tab, 1, 0, 1, 1)

        self.pushButton_buscar = QPushButton(self.tab_2)
        self.pushButton_buscar.setObjectName(u"pushButton_buscar")
        self.pushButton_buscar.setEnabled(False)

        self.gridLayout_4.addWidget(self.pushButton_buscar, 1, 1, 1, 1)

        self.pushButton_mostrar_tab = QPushButton(self.tab_2)
        self.pushButton_mostrar_tab.setObjectName(u"pushButton_mostrar_tab")
        self.pushButton_mostrar_tab.setEnabled(False)

        self.gridLayout_4.addWidget(self.pushButton_mostrar_tab, 1, 2, 1, 1)

        self.tableWidget = QTableWidget(self.tab_2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(False)

        self.gridLayout_4.addWidget(self.tableWidget, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_ver = QPushButton(self.tab_3)
        self.pushButton_ver.setObjectName(u"pushButton_ver")

        self.gridLayout_5.addWidget(self.pushButton_ver, 2, 0, 1, 2)

        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addWidget(self.graphicsView, 1, 0, 1, 1)

        self.pushButton_dibujar = QPushButton(self.tab_3)
        self.pushButton_dibujar.setObjectName(u"pushButton_dibujar")

        self.gridLayout_5.addWidget(self.pushButton_dibujar, 4, 0, 1, 2)

        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1095, 26))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuOrdenar = QMenu(self.menubar)
        self.menuOrdenar.setObjectName(u"menuOrdenar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuOrdenar.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuOrdenar.addSeparator()
        self.menuOrdenar.addAction(self.actionID)
        self.menuOrdenar.addAction(self.actionDistancia)
        self.menuOrdenar.addAction(self.actionVelocidad)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionID.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.actionDistancia.setText(QCoreApplication.translate("MainWindow", u"Distancia", None))
        self.actionVelocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particula", None))
        self.pushButton_generar.setText(QCoreApplication.translate("MainWindow", u"Generar Random", None))
        self.label_red.setText(QCoreApplication.translate("MainWindow", u"Alfa:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 de vertices:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Poblacion", None))
        self.label_velocidad.setText(QCoreApplication.translate("MainWindow", u"Beta:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 Iteraciones", None))
        self.pushButton_pso.setText(QCoreApplication.translate("MainWindow", u"PSO", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Salida", None))
        self.pushButton_mostrar.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.lineEdit_tab.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identificador", None))
        self.pushButton_buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_mostrar_tab.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.pushButton_ver.setText(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.pushButton_dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Grafico", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuOrdenar.setTitle(QCoreApplication.translate("MainWindow", u"Ordenar", None))
    # retranslateUi

