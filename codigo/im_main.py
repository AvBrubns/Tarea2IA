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
from logs import Logs
import time

class MyApp(QtWidgets.QMainWindow, Ui_Busqueda):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_Busqueda.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Busqueda")
        self.txtMessage("clickee una opcion")
        self.btnDibujar.hide()
        self.inputArbol.hide()
        self.setFixedSize(self.size())
        self.menuBFS.triggered[QtWidgets.QAction].connect(self.BFS1)
        self.btnDibujar.clicked.connect(self.drawRuta)
        #Elementos
        self.figure = pylab.figure() 
        self.canvas = FigureCanvas(self.figure) 

        self.logs = Logs()
        self.arbolbsf1 = None
    """Funcion para activart la funcion de bfs1"""
    def BFS1(self,action):
        try:
            #print("Se dio clic:"+action.text())
            self.logs.writeLog("Se dio clic:"+action.text())
            #self.tituloArchivo.setText("Holi")
            #Canvas plot
            self.toolbar = NavigationToolbar(self.canvas, self)
            self.layout = QtWidgets.QVBoxLayout()
            self.figure.clear() 
            b1 = MyQUEUE()
            b1.BFS("A","D")
            self.logs.writeLog("Se crearon las rutas del nodo:[A] al [D]")
            self.arbolbsf1 = b1.setTree() #devuelve las rutas posibles de 'A' a 'D'
            key = b1.setKey()
            self.figure.clear()
            d=draw.dGraph(self.arbolbsf1,key)
            d.llenarNivles()
            
            d.crearDigra(self.canvas)
            self.layout.addWidget(self.toolbar)
            self.layout.addWidget(self.canvas)
            self.frameCanvas.setLayout(self.layout)
            """Termina craer canvas"""
            self.logs.writeLog("Numero de Rutas creadas:"+str(len(self.arbolbsf1.get('A-D'))))
            self.txtMessage("Las rutas del nodo:[A] al [D] son: "+str(len(self.arbolbsf1.get('A-D')))+". Ingrese un camino para dibujar")
            self.showbtnDraw()
                        

        except Exception as error:
            self.logs.erroLogs("Error en la funcion BFS1"+str(error))
    def drawRuta(self):
        aux_ruta = self.arbolbsf1.get('A-D')
        print(aux_ruta)
        ruta = aux_ruta[int(self.inputArbol.text())-1]
        print(ruta)
        aux_di = {'A-D':[ruta]}
        dR=draw.dGraph(aux_di,'A-D')
        dR.llenarNivles()
        dR.printTree()
        dR.drawRuta()
    def txtMessage(self ,text):
        self.tituloArchivo.setText(text)
        self.tituloArchivo.show()
    def showbtnDraw(self):
        self.btnDibujar.show()
        self.inputArbol.show()
    def closeEvent(self, event):
        close = QtWidgets.QMessageBox.question(self,
                                     "Cerrando",
                                     "¿Desea cerrar la aplicacion?",
                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            localtime = time.asctime( time.localtime(time.time()) )
            self.logs.writeLog("\tEl programa se cerro a las:"+str(localtime)+"\t")
            event.accept()

        else:
            event.ignore()
if __name__ == '__main__':
    try:
        app = QtWidgets.QApplication(sys.argv)
        app.setStyleSheet(qdarkstyle.load_stylesheet())
        logs = Logs()
        localtime = time.asctime( time.localtime(time.time()) )
        logs.writeLog("\tPrograma iniciado:"+str(localtime))
        window = MyApp()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print("Ocurrio un error"+str(e))

