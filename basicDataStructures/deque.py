# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 18:15:45 2015

@author: umesh
"""

class Deque:
    def __init__(self):
        self.items = []
        
    def addFront(self,item):
        self.items.append(item)
        
    def removeFront(self):
        return self.items.pop()
        
    def addRear(self, item):
        self.items.insert(0, item)
    
    def removeRear(self):
        return self.items.pop(0)
        
    def isEmpty(self):
        return self.items == []
        
    def size(self):
        retun len(self.items)