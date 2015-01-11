# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 15:10:22 2015

@author: umesh
"""


def findMinSlow(inList):
    """ an N^2 algo where we ask if each element is the smallest or not"""
    finalMin = inList[0]
    for i in inList:
        isSmallest = True
        for j in inList:
            if i > j:
                isSmallest = False
        if isSmallest:
            finalMin = i

    return finalMin

def findMinFast(inList):
    """ An order N algo"""
    minVal = inList[0]
    for val in inList:
        if val < minVal:
            minVal = val
    return minVal

import random
from time import time

val = findMinSlow([5, 4, 2, 0])
print "Smallest is %d" %val 

val = findMinSlow([0, 5, 4, 2, 1])
print "Smallest is %d" %val

#testing with a large collection of random numbers
for listSize in range(100, 5001, 1000):
    #generate random numbers via list comprehension
    randList = [random.randrange(listSize) for x in range(listSize)]
    begTime = time()
    minVal = findMinSlow(randList)
    runTime = time() - begTime
    print "min val of %d in list size of %d was found in %f s" \
    %(minVal, listSize, runTime)

    begTime = time()
    minVal = findMinFast(randList)
    runTime = time() - begTime    
    print "min val of %d in list size of %d was found in %f s" %(minVal, listSize, runTime)

