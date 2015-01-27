# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 08:29:18 2015

@author: umesh
"""


def bubbleSort(aList):
    """ function to sort data using bubble sort"""
    N = len(aList)
    for outIdx in range(N-1, 0, -1): #stop one below max; don't need to go -ve
        for inIdx in range(outIdx):
            if aList[inIdx] > aList[inIdx+1]:  # swap
                aList[inIdx], aList[inIdx+1] = aList[inIdx+1], aList[inIdx]
    return aList


mylist = [54,26,93,17,77,31,44,55,20]
bubbleSort(mylist)  # notice that the original list was modified!!
print(mylist)
