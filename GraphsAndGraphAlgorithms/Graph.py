# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 09:44:02 2015
URL: http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html
@author: umesh
"""

from Vertex import Vertex

class Graph:
    def __init__(self):
        self.vertList = {}  # stoe the keys to the various Verticies
        self.numVertices = 0
        
    def addVertex(self, vertexKey):
        newVertex = Vertex(vertexKey)
        self.numVertices += 1
        self.vertList[vertexKey] = newVertex
        
    def getVertex(self, vertexKey):
        if vertexKey in self.vertList:
            return self.vertList[vertexKey]
        else:
            return None
            
    def __contains__(self, vertexKey):
        return vertexKey in self.vertList
        
    def addEdge(self, fromVertexKey, toVertexKey, weight):
        if fromVertexKey not in self.vertList:
            self.addVertex(fromVertexKey)
        if toVertexKey not in self.vertList:
            self.addVertex(toVertexKey)
        self.vertList[fromVertexKey].addNeighbor(self.vertList[toVertexKey], weight)
        
    def getVertices(self):
        return self.vertList.keys()
        
    def __iter__(self):
        return iter(self.vertList.values())
        
if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)
        
    #try out the iterator
    for vertex in g:  # using iterator here!
        for nbrVertex in vertex.getConnections():
            print ("%d, %d, %d") \
                %(vertex.getId(), nbrVertex.getId(), vertex.getWeight(nbrVertex))
