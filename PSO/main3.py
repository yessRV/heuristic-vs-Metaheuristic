from PySide6.QtWidgets import QMainWindow, QApplication
from mainwindow import MainWindow
import sys

# Aplicacion de Qt
app = QApplication()
#Se crea un boton con la palabra Hola
window = MainWindow()
#Se hace visible el botón
window.show()
#Qt loop
sys.exit(app.exec_())