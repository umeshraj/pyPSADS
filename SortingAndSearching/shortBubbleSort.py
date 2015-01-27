# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 08:47:30 2015

@author: umesh
"""


def shortBubbleSort(aList):
    """ stop sorting if no exchanges """
    
    N = len(aList)
    passNum = N-1
    exchange = True

    while passNum > 0 and exchange:
        exchange = False
        print passNum
        for idx in range(passNum):
            if aList[idx] > aList[idx+1]:
                aList[idx], aList[idx+1] = aList[idx+1], aList[idx]
                exchange = True
        passNum -= 1
    return aList
    
alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)
    