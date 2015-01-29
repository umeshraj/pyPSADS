# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 21:28:54 2015
URL: interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html
@author: umesh
"""


def partition(aList, first, last):
    """ partition function to find split point for quicksort """
    pivot = aList[first]
    leftIdx = first + 1
    rightIdx = last

    crossed = False
    while not crossed:  # left and right have not crossed
        while (leftIdx <= rightIdx) and (aList[leftIdx] <= pivot):
            leftIdx += 1

        while (rightIdx >= leftIdx) and (aList[rightIdx] >= pivot):
            rightIdx -= 1

        if leftIdx > rightIdx:
            crossed = True
        else:  # not crossed, swap the two values
            aList[leftIdx], aList[rightIdx] = aList[rightIdx], aList[leftIdx]

    # left/right have crossed swap right mark with pivot
    aList[first], aList[rightIdx] = aList[rightIdx], aList[first]

    return rightIdx

def quickSortHelper(aList, firstIdx, lastIdx):
    if firstIdx < lastIdx:
        splitPoint = partition(aList, firstIdx, lastIdx)
        quickSortHelper(aList, firstIdx, splitPoint-1)
        quickSortHelper(aList, splitPoint+1, lastIdx)


def quickSort(aList):
    quickSortHelper(aList, 0, len(aList)-1)


alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)

