# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 08:23:33 2015

@author: umesh
"""

def orderedSequentialSearch(inList, item):
    """ list is ordered exit if larger item found """
    found = False
    for listItem in inList:
        if listItem == item:
            found = True
            break
        elif listItem > item:
            break
    return found
    
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(orderedSequentialSearch(testlist, 3))
print(orderedSequentialSearch(testlist, 13))