# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 19:59:14 2015

@author: umesh
"""

def gapInsertionSort(aList, stIdx, gap):
    """ gap insertion sort for shell sort"""
    
    N = len(aList)
    for outIdx in range(1, N):
        curPos = outIdx
        curVal = aList[curPos]
        while (curPos >= 1) and (aList[curPos-1] > curVal):
            aList[curPos] = aList[curPos-1]
            curPos = curPos - 1
        aList[curPos] = curVal
    
    return aList
    
alist = [54,26,93,17,77,31,44,55,20]
gapInsertionSort(alist, 0, 1)
print(alist)

    