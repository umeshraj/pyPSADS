# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 19:59:14 2015

@author: umesh
"""

def shellSort(aList):
    """ main function for shell sorting"""
    subListLen = len(aList)//2
    while subListLen > 0:
        for startIdx in range(subListLen):
            gapInsertionSort(aList, startIdx, subListLen)
        print aList
        subListLen = subListLen//2
    

def gapInsertionSort(aList, stIdx, gap):
    """ gap insertion sort for shell sort"""
    
    N = len(aList)
    for outIdx in range(stIdx+gap, N, gap):
        curPos = outIdx
        curVal = aList[curPos]
        while (curPos >= gap) and (aList[curPos-gap] > curVal):
            aList[curPos] = aList[curPos-gap]
            curPos = curPos - gap
        aList[curPos] = curVal
    
    return aList
    
alist = [54,26,93,17,77,31,44,55,20]
#gapInsertionSort(alist, 0, 3)
shellSort(alist)
print(alist)

    