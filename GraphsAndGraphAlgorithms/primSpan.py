# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 08:33:51 2015

@author: umesh
"""

from pythonds.graphs import PriorityQueue, Graph, Vertex


def prim(G, start):
    """ prim's min spanning tree """
    for v in G:
        v.setDistance(sys.maxSize)  # max dist for each node
        v.setPred(None)  # no predictors
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in G])  # make priority heap
    
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() +\
            currentVert.getWeight(nextVert)
            
            if nextVert in pq and newDist < nextVert.getDistance():
                nextVert.setPred(currentVert)
                nextVert.setDistance(newDist)
                pq.decreaseKey(nextVert, newDist)
    
        