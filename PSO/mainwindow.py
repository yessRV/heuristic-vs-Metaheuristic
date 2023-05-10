from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem, QGraphicsScene
from PySide6.QtCore import Slot
from PySide6.QtGui import QPen, QColor, QTransform
from ui_mainwindow import Ui_MainWindow
from lista import Lista
from particula import Particula
from algoritmos import puntos_mas_cercanos
from pso.pso_main import *
import random
import time

class MainWindow(QMainWindow):
    def __init__(self):#reservar memoria para mostrar ventana
        super(MainWindow, self).__init__()#llama constructor de QMainWindow
        #lo anterior es una clase "Hija"

        self.lista = Lista()

        self.graph = Graph(amount_vertices=0, starting_vertex=0)

        self.nodos = []

        self.evolutions = []

        self.annotatedevolutions = []

        self.iteraciones = 10

        self.actual = 0


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        
        #self.ui.pushButton_agregar_final.clicked.connect(self.click_agregar)
        self.ui.pushButton_generar.clicked.connect(self.click_agregar_inicio)
        self.ui.pushButton_mostrar.clicked.connect(self.click_mostrar)
        #self.ui.pushButton_lista_adyacencia.clicked.connect(self.mostrar_lista_adyacencia)
        self.ui.actionAbrir.triggered.connect(self.action_Abrir_Archivo)
        self.ui.actionGuardar.triggered.connect(self.action_Guardar_Archivo)
        self.ui.pushButton_mostrar_tab.clicked.connect(self.mostrar_tabla)
        self.ui.pushButton_buscar.clicked.connect(self.buscar_id)
        self.ui.pushButton_dibujar.clicked.connect(self.dibuja)
        self.ui.pushButton_ver.clicked.connect(self.ver)
        self.ui.pushButton_pso.clicked.connect(self.mostrar_puntos_cercanos)
        self.ui.actionID.triggered.connect(self.action_Ordenar_ID)
        self.ui.actionDistancia.triggered.connect(self.action_Ordenar_Distancia)
        self.ui.actionVelocidad.triggered.connect(self.action_Ordenar_Velocidad)



    # @Slot()
    # def click_agregar(self):
    #     origen = dict()
    #     destino = dict()
    #     color = dict()
    #     id = self.ui.spinBox_id.value()
    #     origen["x"] = self.ui.spinBox_origen_x.value()
    #     origen["y"] = self.ui.spinBox_origen_y.value()
    #     destino["x"] = self.ui.spinBox_destino_x.value()
    #     destino["y"] = self.ui.spinBox_destino_y.value()
    #     velocidad = self.ui.spinBox_velocidad.value()
    #     color["red"] = self.ui.spinBox_red.value()
    #     color["green"] = self.ui.spinBox_green.value()
    #     color["blue"] = self.ui.spinBox_blue.value()

    #     particula = Particula(id, origen, destino, velocidad, color)
    #     self.lista.agregar_final(particula)

    @Slot()
    def click_agregar_inicio(self):
        amount = self.ui.spinBox_vertices.value()
        self.graph.set_amount(amount)
        for i in range(amount):
            coordenada = dict()
            coordenada["x"] = random.randint(0,500)
            coordenada["y"] = random.randint(0,500)
            self.nodos.append(coordenada)
        #print(nodos)
        for i in range(amount):
            for j in range(i+1,amount):
                id = i+j
                origen = dict()
                destino = dict()
                color = dict()
                origen["x"] = self.nodos[i]["x"]
                origen["y"] = self.nodos[i]["y"]
                destino["x"] = self.nodos[j]["x"]
                destino["y"] = self.nodos[j]["y"]
                velocidad = random.randint(0,400)
                color["red"] = random.randint(0,255)
                color["green"] = random.randint(0,255)
                color["blue"] = random.randint(0,255)

                particula = Particula(id, origen, destino, velocidad, color)
                self.lista.agregar_final(particula)
                self.graph.add_edge(i, j,particula.distancia)
                #print(nodos[i], nodos[j])
        # origen = dict()
        # destino = dict()
        # color = dict()
        # id = self.ui.spinBox_id.value()
        # origen["x"] = self.ui.spinBox_origen_x.value()
        # origen["y"] = self.ui.spinBox_origen_y.value()
        # destino["x"] = self.ui.spinBox_destino_x.value()
        # destino["y"] = self.ui.spinBox_destino_y.value()
        # velocidad = self.ui.spinBox_velocidad.value()
        # color["red"] = self.ui.spinBox_red.value()
        # color["green"] = self.ui.spinBox_green.value()
        # color["blue"] = self.ui.spinBox_blue.value()

        # particula = Particula(id, origen, destino, velocidad, color)
        # self.lista.agregar_inicio(particula)

    @Slot()
    def click_mostrar(self):
        self.limpia()
        self.ver()
        print(self.nodos)
        print(self.evolutions[self.actual])
        print(self.actual)
        for j in range(len(self.nodos)-1):
            self.scene.addLine(self.nodos[(self.evolutions[self.actual][j])]["x"],self.nodos[(self.evolutions[self.actual][j])]["y"],self.nodos[(self.evolutions[self.actual][j+1])]["x"],self.nodos[(self.evolutions[self.actual][j+1])]["y"])
            print(self.nodos[(self.evolutions[self.actual][j])]["x"],self.nodos[(self.evolutions[self.actual][j])]["y"],"-->",self.nodos[(self.evolutions[self.actual][j+1])]["x"],self.nodos[(self.evolutions[self.actual][j+1])]["y"])
        self.scene.addLine(self.nodos[self.evolutions[self.actual][len(self.nodos)-1]]["x"],self.nodos[self.evolutions[self.actual][len(self.nodos)-1]]["y"],self.nodos[self.evolutions[self.actual][0]]["x"],self.nodos[self.evolutions[self.actual][0]]["y"])
        pen = QPen()
        pen.setWidth(5)

        self.scene.addEllipse(self.nodos[self.evolutions[self.actual][0]]["x"],self.nodos[self.evolutions[self.actual][0]]["y"],5,5,pen)

        self.ui.plainTextEdit.insertPlainText(str(self.annotatedevolutions[self.actual])+"\n")

        self.actual = self.actual + 1
        if(self.actual == self.iteraciones):
            print("limite")
            self.ui.plainTextEdit.insertPlainText("Fin")
            self.ui.pushButton_mostrar.setEnabled(False)
            self.actual = self.actual-1
        # self.ui.plainTextEdit.clear()
        # self.ui.plainTextEdit.insertPlainText(str(self.lista))

    # @Slot()
    # def mostrar_lista_adyacencia(self):
    #     self.ui.plainTextEdit.clear()
    #     grafo = self.lista.lista_adyacencia()
    #     print(grafo)
    #     text = ""
    #     for key,value in grafo.items():
    #         text = text + str(key) + "-->[ " #+ str(value) + "\n"
    #         for a in value:
    #             text = text + str(a[0]) + " , "
    #         text = text[:-2]
    #         text = text + "]\n"
    #     self.ui.plainTextEdit.insertPlainText(text)


    @Slot()
    def action_Abrir_Archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.lista.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo abrir el archivo " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo abrir el archivo " + ubicacion
            )

    @Slot()
    def action_Guardar_Archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.lista.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )

    @Slot()
    def mostrar_tabla(self):
        self.ui.tableWidget.setColumnCount(6)
        headers = ["ID", "Origen", "Destino", "Velocidad", "Color", "Distancia"]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)

        self.ui.tableWidget.setRowCount(len(self.lista))
        row = 0
        for particula in self.lista:
            id_widget = QTableWidgetItem(str(particula.id))
            origen_widget = QTableWidgetItem("(" + str(particula.origen["x"]) + "," + str(particula.origen["y"]) + ")")
            destino_widget = QTableWidgetItem("(" + str(particula.destino["x"]) + "," + str(particula.destino["y"]) + ")")
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            color_widget = QTableWidgetItem("(" + str(particula.color["red"]) + "," + str(particula.color["green"]) + "," + str(particula.color["blue"]) + ")")
            distancia_widget = QTableWidgetItem(str(particula.distancia))


            self.ui.tableWidget.setItem(row, 0, id_widget)
            self.ui.tableWidget.setItem(row, 1, origen_widget)
            self.ui.tableWidget.setItem(row, 2, destino_widget)
            self.ui.tableWidget.setItem(row, 3, velocidad_widget)
            self.ui.tableWidget.setItem(row, 4, color_widget)
            self.ui.tableWidget.setItem(row, 5, distancia_widget)

            row += 1

    @Slot()
    def buscar_id(self):
        id = self.ui.lineEdit_tab.text()

        encontrado = False

        for particula in self.lista:
            if int(id) == particula.id:
                self.ui.tableWidget.clear()

                self.ui.tableWidget.setColumnCount(6)
                headers = ["ID", "Origen", "Destino", "Velocidad", "Color", "Distancia"]
                self.ui.tableWidget.setHorizontalHeaderLabels(headers)

                self.ui.tableWidget.setRowCount(1)

                id_widget = QTableWidgetItem(str(particula.id))
                origen_widget = QTableWidgetItem("(" + str(particula.origen["x"]) + "," + str(particula.origen["y"]) + ")")
                destino_widget = QTableWidgetItem("(" + str(particula.destino["x"]) + "," + str(particula.destino["y"]) + ")")
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                color_widget = QTableWidgetItem("(" + str(particula.color["red"]) + "," + str(particula.color["green"]) + "," + str(particula.color["blue"]) + ")")
                distancia_widget = QTableWidgetItem(str(particula.distancia))


                self.ui.tableWidget.setItem(0, 0, id_widget)
                self.ui.tableWidget.setItem(0, 1, origen_widget)
                self.ui.tableWidget.setItem(0, 2, destino_widget)
                self.ui.tableWidget.setItem(0, 3, velocidad_widget)
                self.ui.tableWidget.setItem(0, 4, color_widget)
                self.ui.tableWidget.setItem(0, 5, distancia_widget)

                encontrado = True
                return

        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f'La particula con el identificador {id} no fue encontrado'
            )

    @Slot()
    def dibuja(self):
        self.limpia()
        for particula in self.lista:
            pen = QPen()
            pen.setWidth(2)

            color = QColor(particula.color["red"],particula.color["green"],particula.color["blue"])
            pen.setColor(color)

            x_origen = particula.origen["x"]
            y_origen = particula.origen["y"]
            x_destin = particula.destino["x"]
            y_destin = particula.destino["y"]


            self.scene.addEllipse(x_origen,y_origen,6,6,pen)
            self.scene.addEllipse(x_destin,y_destin,6,6,pen)
            self.scene.addLine(x_origen+3,y_origen+3,x_destin+3,y_destin+3,pen)

    @Slot()
    def ver(self):
        self.limpia()
        for particula in self.lista:
            pen = QPen()
            pen.setWidth(2)

            color = QColor(particula.color["red"],particula.color["green"],particula.color["blue"])
            pen.setColor(color)

            x_origen = particula.origen["x"]
            y_origen = particula.origen["y"]
            x_destin = particula.destino["x"]
            y_destin = particula.destino["y"]


            self.scene.addEllipse(x_origen,y_origen,3,3,pen)
            self.scene.addEllipse(x_destin,y_destin,3,3,pen)


    @Slot()
    def mostrar_puntos_cercanos(self):
        self.limpia()
        self.ver()
        pso = PSO(self.graph, iterations=self.ui.spinBox_iteraciones.value(), size_population=self.ui.spinBox_poblacion.value(), beta=self.ui.spinBox_beta.value(), alpha=self.ui.spinBox_alfa.value())
        self.iteraciones = self.ui.spinBox_iteraciones.value()
        pso.run()
        self.evolutions = pso.evolutions
        self.annotatedevolutions = pso.annotatedEvolutions
        self.actual = 0
        self.ui.pushButton_mostrar.setEnabled(True)

    @Slot()
    def limpia(self):
        self.scene.clear()

    @Slot()
    def action_Ordenar_ID(self):
        self.lista.ordenar_id()


    @Slot()
    def action_Ordenar_Distancia(self):
        self.lista.ordenar_distancia()


    @Slot()
    def action_Ordenar_Velocidad(self):
        self.lista.ordenar_velocidad()

    def wheelEvent(self, event):
        print(event.delta())
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2,1.2)
        else:
            self.ui.graphicsView.scale(0.8,0.8)
