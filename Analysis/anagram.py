# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 18:15:59 2015

@author: umesh
"""

def anagramSolution1(str1, str2):
    """ a check-off version to see if two strings are anagrams"""
    # make a list out of both stings    
    list1 = list(str1) 
    list2 = list(str2)
    N = len(list1) # assumed to be same len    
    
    foundAll = True # all characters found
    for pos1 in range(N):
        ch1 = list1[pos1] # reference character
        foundCh1 = False 
        for pos2 in range(N):
            if ch1 == list2[pos2]:
                list2[pos2] = None # so we don't compare again
                foundCh1 = True
                break # no need to continue comparisons in string2
        if foundCh1 == False:
            foundAll = False  # could not find a character; mark error
    
    return(foundAll) #return the answer
    

print(anagramSolution1('abcd','abcc'))    
                
                
                