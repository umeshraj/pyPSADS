# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 08:20:20 2015

URL: http://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html
@author: umesh
"""

def minCoinsRec(coinList, amount):
    """ get change for amount"""
    minCoins = amount  # pay all in pennies
    if amount in coinList:
        return 1
    else:
        # make new list with only coins less than amount
        newCoinList = [coin for coin in coinList if coin <= amount]
        for coin in newCoinList:
            numCoins = 1 + minCoinsRec(newCoinList, amount - coin)
            if numCoins < amount:  # incrementally find the min
                minCoins = numCoins
        return minCoins


coinList = [1, 5, 10, 25]
from time import time
t0 = time()
print(minCoinsRec([1,5,10,25], 63))
print time() - t0
