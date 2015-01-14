# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 07:46:44 2015

@author: umesh
"""

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,newItem):
        self.items.append(newItem)
        
    def pop():
        return(self.items.pop())
    
    def peek():
        return(self.items[-1])
    
    def isEmpty():
        return self.items == []
    
    def size():
        return len(self.items)