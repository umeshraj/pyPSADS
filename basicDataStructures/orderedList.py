# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 08:27:28 2015

@author: umesh
"""

from unOrderedList import Node


class OrderedList:
    def __init__(self):
        self.head = None
        
    def search(self, item):
        found = False
        stop = False  # option to break if curData is > item
        cur = self.head
        while (cur is not None) and (not found) and (not stop):
            curData = cur.getData()
            if (curData == item):
                found = True  # item found
            elif (curData > item):
                stop = True  # item will not be found
            else:
                cur = cur.getNext()
        return(found)
        
    def add(self, item):
        
    