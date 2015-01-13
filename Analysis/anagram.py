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
    N = len(list1)  # assumed to be same len

    foundAll = True  # all characters found
    for pos1 in range(N):
        ch1 = list1[pos1]   # reference character
        foundCh1 = False
        for pos2 in range(N):
            if ch1 == list2[pos2]:
                list2[pos2] = None  # so we don't compare again
                foundCh1 = True
                break   # no need to continue comparisons in string2
        if foundCh1 is False:
            foundAll = False  # could not find a character; mark error

    return(foundAll)    # return the answer


def anagramSolution2(st1, str2):
    """ anagaram solution using sorted lists"""
    list1 = list(str1)
    list2 = list(str2)
    
    # sort the lists
    list1.sort()    # or list1 = sorted(list1)
    list2.sort()
    return (list1==list2)


def str2Dict(inStr):
    """ Function to count the number of times a character appears
    in a string """

    outDict = {}
    for ch in inStr:  # for each character
        outDict[ch] = outDict.get(ch, 0) + 1    # return 0 if key absent
    return outDict


def anagramSolution3(str1, str2):
    dict1 = str2Dict(str1)
    dict2 = str2Dict(str2)

    foundAll = True
    for key in dict1:
        val1 = dict1.get(key)   # using get instead of [key] to get None
        val2 = dict2.get(key, None)     # return None if key missing
        if(val1 != val2):
            foundAll = False
            break
    return foundAll


str1 = 'abcd'
str2 = 'abcd'
str3 = 'aads'

print(anagramSolution1(str1, str2))     # test anagram 1
print(anagramSolution1(str1, str3))     # test anagram 1

print(anagramSolution2(str1, str2))     # test anagram 2
print(anagramSolution2(str1, str3))     # test anagram 2

print(anagramSolution3(str1, str2))     # test anagram 3
print(anagramSolution3(str1, str3))     # test anagram 3
