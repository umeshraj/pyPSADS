# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 08:34:31 2015

@author: umesh
"""

from time import time


def sumOfN(n):
    """ sum of n integers"""
    theSum = 0
    t0 = time()
    for i in range(1,n+1):
        theSum += i
    runTime = time() - t0
    return theSum, runTime


def main():
    N = 10000
    for n in range(10, N+1, N/10):
        theSum, runTime = sumOfN(n)
        print "Sum of %d integers is %d. Runtime %f s" %(n, theSum, runTime)    


main()
        