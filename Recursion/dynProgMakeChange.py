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
   

def dpMakeChangeTrkCoins(coinValueList, change, minCoins, coinsUsed):
    """ changing dyn program to track coins used"""
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]
   
def printCoins(coinsUsed, amt):
    """ print list of coins used to make amt"""
    usedList = []
    while amt > 0:
        coin = coinsUsed[amt]
        print coin
        #usedList.append(coin)
        amt = amt - coin
    #return ",".split(usedList)
   
def main():
    amnt = 20
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChangeTrkCoins(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()
