# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 08:50:16 2015

@author: umesh
"""

def recBinarySearch(inList, item):
    """ recursive implementation of binary search"""
    if len(inList) == 0:  # no list
        return False
    else:  # valid list
        mid = len(inList)//2
        if inList[mid] == item:
            return True
        elif inList[mid] > item:  # items is to left of mid
            return recBinarySearch(inList[:mid], item)
        else: # item is to the right of mid
            return recBinarySearch(inList[mid+1:], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
        
