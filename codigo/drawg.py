import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
import pylab



class dGraph:

    def __init__(self,tree,key):
        self.key=key
        self.tree=tree
        self.niveles=0
        self.treeN={}
        self.initNiveles()
        self.initTreeN()
        self.treeN.clear()
        self.nodes=[]

    def llenarNivles(self):
        #print("entre")
        start = None
        aux_key = 1
        auxLista = self.tree.values()
        for n in auxLista:
            for nn in n:
                start = nn[0]
                self.addNodes(start)
                aux_index=1
                for nnn in nn:
                    if( (start != nnn) & (type(nnn)!= int)):
                        pareja = (start,nnn)
                        self.addNodes(nnn)
                        self.createNiveles(aux_index,pareja)
                        aux_index=aux_index+1
                        start=nnn
                    else:
                        pass

    def initTreeN(self):
        for nivel in range(self.niveles):
            self.createNiveles(nivel+1,[])

    def createNiveles(self,key,ruta):
        if(self.findD(key)):
            newRutas=[]
            newRutas = self.treeN.get(key)
            newRutas.append(ruta)
            self.treeN.update({key:newRutas})
        else:
            self.treeN.update({key:[ruta]})
    
    def findD(self,key):
        if(self.treeN.get(key)== None):
            return False
        else:
            return True

    def initNiveles(self):
        list=self.tree[self.key]
        for nivel in list:
            auxIndex = len(nivel)
            auxMax = nivel[auxIndex-1]
            if( self.niveles >=auxMax ):
                self.niveles = self.niveles
            else:
                self.niveles = auxMax-1

    def printTree(self):
        for key in self.treeN:
            print(key, ":",self.treeN[key])
    def addNodes(self,node):
        if(node in self.nodes):
            pass
        else:
            self.nodes.append(node)
    def crearDigra(self,canvas):
        g = nx.DiGraph()
        g.add_nodes_from(self.nodes)
        for key in self.treeN:
            g.add_edges_from(self.treeN[key], weight=key)
        #print(g.nodes())
        #print(g.edges())
        pox = nx.spiral_layout(g)
        nx.draw_networkx_nodes(g,pox)
        nx.draw_networkx_labels(g,pox)
        nx.draw_networkx_edges(g,pox,edge_color='b',arrows=True)
        canvas.draw()