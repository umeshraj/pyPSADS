# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 09:59:28 2015

@author: umesh
"""

def selectionSort(inList):
    """ implements selection sort"""
    N = len(inList)
    for outIdx in range(N-1, 0, -1):
        maxIdx = 0
        for inIdx in range(0, outIdx+1):
            if inList[inIdx] > inList[maxIdx]:
                maxIdx = inIdx
        #put max value at the end
        inList[inIdx], inList[maxIdx] = inList[maxIdx], inList[inIdx]
    return inList
    
alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)