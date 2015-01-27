# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 10:36:39 2015

@author: umesh
"""

def insertionSort(aList):
    """ implementing insertion sort"""
    N = len(aList)
    for outIdx in range(1, N):
        curVal = aList[outIdx]
        curPos = outIdx

        while (curPos > 0) and (aList[curPos-1] > curVal):
            aList[curPos] = aList[curPos-1]  # move larger items to right
            curPos -= 1

        aList[curPos] = curVal
        print aList

    return aList

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)
