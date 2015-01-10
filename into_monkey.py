# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 07:59:11 2015

@author: umesh
"""

#function to simulate monkeys writing shakespeare
#make a random string  “this is a test of abcd”

import random

def mkRandString(strLen):
    """ generate a random string of length strLen """
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    NAlpha = len(alphabet)
    outStr = ''
    for i in range(strLen):
        outStr = outStr+alphabet[random.randrange(NAlpha)]
        
    return outStr

def updateRandString(goalString, thisString):
    """keep characters that match. change only 1 char"""
    if (goalString == thisString):
        return
    else:
        NGoal = len(goalString)
        #get a set of indicies that don't match
        mismatchIdx = []
        for i in range(NGoal):
            if (goalString[i] != thisString[i]):
                mismatchIdx.append(i)
                
        #randomly pick one of these mismatch idx and change
        Nmismatch = len(mismatchIdx)
        randomNum = random.randrange(Nmismatch)
        pickIdx = mismatchIdx[randomNum]
        
        #replace element in string by converting to list and back to string
        tmpList = list(thisString)
        tmpList[pickIdx] = mkRandString(1) #generate a random letter
        outStr = "".join(tmpList) #join the list back to a string
    return outStr

def score(goalString, thisString):
    NGoal = len(goalString)
    score = 0
    for i in range(NGoal):
        if goalString[i] == thisString[i]:
            score = score+1
    return float(score)/NGoal * 100

def main():
    goalString = 'this is a test of abcd'
    NGoal = len(goalString)
    
    bestScore = 0
    curStr = mkRandString(NGoal)
    while bestScore < 100:        
        curStr = updateRandString(goalString, curStr)
        curScore = score(goalString, curStr)       
        
        if curScore > bestScore:
            bestScore = curScore
            print ('%s :  %3.1f') %(curStr, curScore)
    
main()