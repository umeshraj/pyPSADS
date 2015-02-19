# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 08:50:40 2015
URL: http://interactivepython.org/runestone/static/pythonds/Graphs/DijkstrasAlgorithm.html
@author: umesh
"""

from pythonds.graphs import Graph, PriorityQueue, Vertex


def dijkstra(aGraph, start):
    start.setDistance(0)
    pq = PriorityQueue()
    pq.buildHeap([(v.getDistance(), v) for v in aGraph])
    while not pq.isEmpty():
        curVtx = pq.delMin()
        for nxtVtx in curVtx.getConnections():
            newDist = curVtx.getDistance() + curVtx.getWeight(nxtVtx)
            if newDist < nxtVtx.getDistance():
                nxtVtx.setDistance(newDist)
                nxtVtx.setPred(curVtx)
                pq.decreaseKey(nxtVtx, newDist)  # readjust the heap
    