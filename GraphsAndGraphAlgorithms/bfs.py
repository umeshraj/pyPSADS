# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 08:11:16 2015

@author: umesh
"""


from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue


def bfs(g, startVert):
    """ breadth first search with word ladder """
    vertQ = Queue()
    startVert.color = 'gray'  # set the node color
    startVert.setDistance(0)  # distance to desired word is 0
    startVert.setPred(None)  # no predecessor
    vertQ.enqueue(startVert)  # push to queue

    while vertQ.size() > 0:
        curVert = vertQ.dequeue()
        for nbrVert in curVert.getConnections():  # for each connected vertex
            if nbrVert.getColor() == "white":
                nbrVert.setColor('gray')
                nbrVert.setDistance(curVert.getDistance() + 1)
                nbrVert.setPred(curVert)
                vertQ.enqueue(nbrVert)
        curVert.setColor("black")


def traverse(fromNode):
    """ traverse from end node to start node """
    x = fromNode
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())


