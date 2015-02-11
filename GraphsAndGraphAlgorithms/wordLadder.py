# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 18:36:17 2015

@author: umesh
"""

from pythonds.graphs import Graph

def buildGraph(wordFile):
    d = {}  # dictionary to collect bucket names
    
    wFile = open(wordFile, 'r')
    for line in wFile:
        word = line[:-1]  # ignore \n
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:  # bucket has been created already
                d[bucket].append(word)  # append current word to existing words
            else:  # bucket does not exists
                d[bucket] = [word]  #make a new list with the word
    
    g = Graph() # graph to store word links
    # now connect all words in one bucket with an edge
    for bucket in d.keys():
        for word1 in d[bucket]:  # could do d.values
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2, 0)
    return g  # return the grph
    
    