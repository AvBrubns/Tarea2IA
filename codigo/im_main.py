"""Implementacion de interfaz main"""

import sys 
import qdarkstyle
import os

from PyQt5 import QtWidgets, QtCore, QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar 
from main import Ui_Busqueda 
import pylab
from canvas import mplCanvas
from bfs1 import MyQUEUE
import drawg as draw

class MyApp(QtWidgets.QMainWindow, Ui_Busqueda):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_Busqueda.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Busqueda")
        self.tituloArchivo.hide()
        self.setFixedSize(self.size())
        self.menuBFS.triggered[QtWidgets.QAction].connect(self.BFS1)
    def BFS1(self,action):
        print("se dio clic:"+action.text())
        #self.tituloArchivo.setText("Holi")
         #Canvas plot
        self.figure = pylab.figure() 
        self.canvas = FigureCanvas(self.figure) 
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.layout = QtWidgets.QVBoxLayout()
        self.figure.clear() 
        self.tituloArchivo.show()
        b1 = MyQUEUE()
        b1.BFS("A","D")
        tree = b1.setTree()
        key = b1.setKey()
        self.figure.clear()
        d=draw.dGraph(tree,key)
        d.llenarNivles()
        d.crearDigra(self.canvas)
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.canvas)
        self.frameCanvas.setLayout(self.layout)
        
    def closeEvent(self, event):
        close = QtWidgets.QMessageBox.question(self,
                                     "Cerrando",
                                     "¿Desea cerrar la aplicacion?",
                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
