# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 08:08:03 2015

@author: umesh
"""

def minCoinsRecCache(coinList, amount, knownVals):
    if amount in coinList:  # coin is in list
        knownVals[amount] = 1  # update known vals
        return 1
    elif knownVals[amount] > 0:  # we know the min coins for this
        return knownVals[amount]
    else:  # coin is not in list and not processed before
        # don't search if coin is greater than amount
        newCoinList = [c for c in coinList if c <= amount] 
        #find min combo of coins
        minCoins = amount
        for c in newCoinList:
            numCoins = 1 + minCoinsRecCache(newCoinList, amount-c, knownVals)
            if numCoins < minCoins:
                minCoins = numCoins
        knownVals[amount] = minCoins
        return minCoins
        
coinList = [1, 5, 10, 25]
from time import time
t0 = time()
minCoins = minCoinsRecCache([1,5,10,25], 63, [0]*64)
print time() - t0
print minCoins
        