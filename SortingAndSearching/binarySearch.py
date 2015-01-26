# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 08:36:55 2015

@author: umesh
"""

def binarySearch(inList, item):
    """ binary search in an ordered list"""
    left = 0
    right = len(inList) - 1
    found = False
    while left <= right and not found:
        mid = (left + right)//2
        if inList[mid] == item:
            found = True
        elif inList[mid] < item:
            left = mid + 1
        else: # middle is greater than item
            right = mid - 1
    return found
    
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))    