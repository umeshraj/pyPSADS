# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 17:05:45 2015
URL: http://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html
@author: umesh
"""


class BinaryHeap:
    def __init__(self):
        self.list = [0]
        self.size = 0

    def percUp(self, idx):
        parIdx = idx//2  # parend idx
        while parIdx > 0:
            if self.list[idx] < self.list[parIdx]:
                self.list[idx], self.list[parIdx] = \
                    self.list[parIdx], self.list[idx]
            idx = parIdx
            parIdx = idx//2

    def insert(self, key):
        """ inserting a new element"""
        self.list.append(key)  # add to end of list
        self.size = self.size + 1
        self.percUp(self.size)  # percolate it up

    def delMin(self):
        minVal = self.list[1]  # min value
        # pick last element & keep heap structure
        self.list[1] = self.list.pop()  
        self.size = self.size-1
        # fix the heap property by moving min to right node
        self.percDown(1)
        return minVal

    def percDown(self, parIdx):
        """ move the node lower if needed """
        while 2*parIdx <= self.size:
            minChildIdx = self.getMinChildIdx(parIdx)
            if self.list[parIdx] > self.list[minChildIdx]:  # swap
                self.list[parIdx], self.list[minChildIdx] = \
                    self.list[minChildIdx], self.list[parIdx]
            parIdx = minChildIdx

    def getMinChildIdx(self, parIdx):
        """ get the idx of the min child """
        if 2*parIdx+1 > self.size:
            return(2*parIdx)
        else:
            if self.list[2*parIdx] < self.list[2*parIdx+1]:
                return 2*parIdx
            else:
                return 2*parIdx+1
                
    def buildHeap(self, inList):
        """ build heap from list """
        self.size = len(inList)
        self.list = [0] + inList              
        i = len(inList)//2
        while i > 0:
            self.percDown(i)
            i -= 1

if __name__ == "__main__":
    myHeap = BinaryHeap()
    myHeap.insert(10)
    myHeap.insert(11)
    myHeap.insert(4)
    print myHeap.list
    myHeap.delMin()
    print myHeap.list
    myHeap.buildHeap([9, 6, 5, 2, 3])
    print myHeap.list

