# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 07:52:12 2015
URL: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
@author: umesh
"""


def mergeSort(aList):
    """ implementing the merge-sort algorithm"""
    N = len(aList)
    print "Splitting", aList
    if N > 1:
        midIdx = N//2
        leftArr = aList[:midIdx]
        rightArr = aList[midIdx:]
        mergeSort(leftArr)
        mergeSort(rightArr)
        
        i, j, k = 0, 0, 0
        #merge the left and right
        while(i < len(leftArr)) and (j < len(rightArr)):
            if leftArr[i] < rightArr[j]:
                aList[k] = leftArr[i]
                i += 1
                k += 1
            else:
                aList[k] = rightArr[j]
                j += 1
                k += 1
                
        #left/right might have values not yet filled in
        while (i < len(leftArr)):
            aList[k] = leftArr[i]
            i += 1
            k += 1
        while (j < len(rightArr)):
            aList[k] = rightArr[j]
            j += 1
            k += 1
    print "Merging", aList

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)            
            