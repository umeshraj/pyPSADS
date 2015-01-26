# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 08:18:45 2015

@author: umesh
"""

def sequentialSearch(inList, item):
    found = False
    for listItem in inList:
        if listItem == item:
            found = True
            break
    return found
    
testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))