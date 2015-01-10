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
    """ AND gate functionality"""
    def __init__(self,n):
        BinaryGate.__init__(self,n)
        
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if (a == 1 and b==1):
            return 1
        else:
            return 0
             
class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if (a==0 and b==0):
            return 0
        else:
            return 1

class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n)
    
    def performGateLogic(self):
        a = self.getPin()
        if (a==1):
            return 0
        else:
            return 1
        
        
a1 = AndGate("A1")
andRes = a1.getOutput() 
print "the result is ", andRes

o1 = OrGate("O1")
orRes = o1.getOutput()
print "the result of the OR gate is: ", orRes

n1 = NotGate("n1")
notRes = n1.getOutput()
print "the result of the NOT gate is: ", notRes