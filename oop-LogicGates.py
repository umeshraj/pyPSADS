# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 08:31:15 2015

@author: umesh
"""

class LogicGate:
    """" a logic gate has a label and an output"""
    def __init__(self,name):
        self.label = name
        self.output = None
        
    def getLabel(self):
        return(self.label)
        
    def getOutput(self):
        self.output = self.performGateLogic() #a method for whom there is no code
        return(self.output)
        
class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pinA = None
        self.pinB = None
        
    def getPinA(self):
        aVal = input("Enter pinA input for " + self.getLabel() + ": " )
        return(int(aVal))
        
    def getPinB(self):
        bVal = input("Enter pinB input for " + self.getLabel() + ": " )
        return int(bVal)
        
class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pin = None
        
    def getPin(self):
        pinVal = input("Enter pin input for " + self.getLabel() + ": ")
        return(pinVal)
            
            
class AndGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)
        
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return a * b
             
        
a1 = AndGate("A1")
andRes = a1.performGateLogic() 
print "the result is ", andRes