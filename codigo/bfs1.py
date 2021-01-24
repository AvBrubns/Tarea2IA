# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 17:28:32 2020

@author: Fernando
"""
graph = {'A': ['B', 'C','E'],
             'B': ['A','C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F','D'],
             'F': ['C']}
import sys
# a sample graph
class MyQUEUE: # just an implementation of a queue
	def __init__(self):
		"""Crea una lista vacia"""
		self.holder = []
		self.rutas = {}
		"""apendizar a la lista lo que llgue"""		
	def enqueue(self,val):
		self.holder.append(val)
		
	def dequeue(self):
		val = None
		try:
			val = self.holder[0]
			if len(self.holder) == 1:
				self.holder = []
			else:
				self.holder = self.holder[1:]	
		except:
			pass
			
		return val	
		
	def IsEmpty(self):
		result = False
		if len(self.holder) == 0:
			result = True
		return result
	
	def BFS(self,start,end):
		
		temp_path = [start]
		self.enqueue(temp_path)
		
		while self.IsEmpty() == False:
			tmp_path = self.dequeue()
			last_node = tmp_path[len(tmp_path)-1]
			#print (" ",tmp_path)
			if last_node == end:
				#print ("VALID_PATH : ",tmp_path)
				key = start+"-"+end
				tmp_path.append(len(tmp_path))
				self.createRutas(key,tmp_path)
			for link_node in graph[last_node]:
				if link_node not in tmp_path:
					new_path = []
					new_path = tmp_path + [link_node]
					self.enqueue(new_path)
		
		#for key in self.rutas:
		#	print(key, ":",self.rutas[key])

	def createRutas(self,key,ruta):
		if(self.findD(key)):
			newRutas = []
			newRutas = self.rutas.get(key)
			newRutas.append(ruta)
			self.rutas.update({key:newRutas})
		else:
			self.rutas.update({key:[ruta]})
	def findD(self,key):
		if(self.rutas.get(key)== None):
			return False
		else:
			return True
	def setTree(self):
		return self.rutas

	def setKey(self):
		key = None
		tree = self.rutas
		for k in tree.keys():
			key=k
		return key