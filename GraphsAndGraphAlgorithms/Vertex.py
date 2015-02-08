# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 09:27:43 2015
URL: http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html
@author: umesh
"""


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbrVertex, weight=0):
        self.connectedTo[nbrVertex] = weight

    def __str__(self):
        return str(self.id) + \
            " connected to " + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbrVertex):
        return self.connectedTo[nbrVertex]

if __name__== "__main__":
    v0 = Vertex('a')
    v1 = Vertex('b')
    v2 = Vertex('c')

    v0.addNeighbor(v1, 1)
    v0.addNeighbor(v2, 10)
    print(v0)

    v1.addNeighbor(v2, 1000)
    print(v1)
