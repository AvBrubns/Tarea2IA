import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
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
        self.colors=()
    """Pne el numero del arco entre los nodos"""
    """Limapia las estructuras"""
    def clearAll(self):
        self.nodes=[]
        self.colors=()
        self.key=None
        self.tree=None
        self.niveles=0
        self.treeN={}
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
    """inicializa el los nivels del diccionario"""
    def initTreeN(self):
        for nivel in range(self.niveles):
            self.createNiveles(nivel+1,[])
    """Rellena los niveles del diccionario con las rutas """
    def createNiveles(self,key,ruta):
        if(self.findD(key)):
            newRutas=[]
            newRutas = self.treeN.get(key)
            newRutas.append(ruta)
            self.treeN.update({key:newRutas})
        else:
            self.treeN.update({key:[ruta]})
    """Busca la llave en un diccionario devuelve true si exite, false en coso contrario"""
    def findD(self,key):
        if(self.treeN.get(key)== None):
            return False
        else:
            return True
    """Busca el numero maximo de niveles del arbol"""
    def initNiveles(self):
        list=self.tree[self.key]
        for nivel in list:
            auxIndex = len(nivel)
            auxMax = nivel[auxIndex-1]
            if( self.niveles >=auxMax ):
                self.niveles = self.niveles
            else:
                self.niveles = auxMax-1
    """Imprime el los nivels y las conexiones por nivel """
    def printTree(self):
        for key in self.treeN:
            print(key, ":",self.treeN[key])
    #agrega los nodos a una lista 
    def addNodes(self,node):
        if(node in self.nodes):
            pass
        else:
            self.nodes.append(node)
    """Crea el grafo general de plot recibe el canvas donde lo pinta"""
    def crearDigra(self,canvas):
        g = nx.DiGraph()
        g.add_nodes_from(self.nodes)
        for key in self.treeN:
            g.add_edges_from(self.treeN[key], weight=int(key))
        #print(g.nodes())
        #print(g.edges())

        pox = nx.spiral_layout(g)
        nx.draw_networkx_nodes(g,pox)
        nx.draw_networkx_labels(g,pox)
        nx.draw_networkx_edges(g,pox,edge_color='black',arrows=True)
        canvas.draw()
    """obtine la lista de color """
    def color_rutas(self):
        list=mcolors.CSS4_COLORS.items()
        return list
    """Pinta una ruta del grafo"""
    def drawRuta(self):
        g = nx.DiGraph()
        g.add_nodes_from(self.nodes)
        for key in self.treeN:
            g.add_edges_from(self.treeN[key], weight=key)
        #print(g.nodes())
        #print(g.edges())
        edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in g.edges(data=True)])

        pox = nx.spiral_layout(g)
        nx.draw_networkx_nodes(g,pox)
        nx.draw_networkx_edge_labels(g,pox,edge_labels=edge_labels)
        nx.draw_networkx_labels(g,pox)
        nx.draw_networkx_edges(g,pox,edge_color='red',arrows=True)
        plt.show()
        