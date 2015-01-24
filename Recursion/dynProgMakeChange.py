# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 08:17:39 2015

@author: umesh
"""

def dpMakeChange(coinValueList, change, minCoins):
   for cents in range(change+1):
      coinCount = cents
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
      minCoins[cents] = coinCount
   return minCoins[change]
   

amnt = 23
cList = [1,5,10,21,25]

coinsUsed = [0]*(amnt+1)
print(dpMakeChange(cList, amnt, coinsUsed))