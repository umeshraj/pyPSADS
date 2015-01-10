# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 08:31:15 2015

@author: umesh
"""

class Logic:
    """" a logic gate has a label and an output"""
    def __init__(self,name):
        self.label = name
        self.output = None
        
    def getLabel(self):
        return(self.label)
        
    def getOutput(self):
        self.output = self.performGateLogic() #a method for whom there is no code
        return(self.output)