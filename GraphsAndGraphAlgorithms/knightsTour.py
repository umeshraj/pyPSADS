# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 08:35:42 2015

@author: umesh
"""

from pythonds.graphs import Graph


def knightGraph(bdSize):
    """ build possible locations for knight for all board locations"""
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for xy in newPositions:
                newNodeId = posToNodeId(xy[0], xy[1], bdSize)
                ktGraph.addEdge(nodeId, newNodeId)
    return ktGraph


def posToNodeId(row, col, bdSize):
    """ convert row/col to index"""
    nodeId = row * bdSize + col
    return nodeId


def genLegalMoves(row, col, bdSize):
    """ generate legal knight moves"""
    newMoves = []
    allOffsets = [(2, 1), (2, -1), (1, 2), (1, -2),
                  (-2, -1), (-2, 1), (-1, -2), (-1, 2)]
    for offset in allOffsets:
        newX = row + offset[0]
        newY = col + offset[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves


def legalCoord(x, bdSize):
    """ check if a coorinate is legal"""
    return (x > 0) and (x < bdSize)


def knightTour(n, path, u, limit):
    """ implementing knight tour"""
    u.setColor("white")
    path.appen(u)
    if n < limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1, path, u, limit)
            i += 1
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done

if __name__ == "__main__":
    myGraph = knightGraph(5)
    print(myGraph.vertices[0].getConnections())
