# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 08:31:15 2015

@author: umesh
"""


class LogicGate:
    """" a logic gate has a label and an output"""
    def __init__(self, name):
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
        if self.pinA is None:
            aVal = input("Enter pinA input for " + self.getLabel() + ": ")
        else: #a gate is connected to this
            aVal = self.pinA.getFrom().getOutput() #get output of gate connected to this pin
        return(int(aVal))

    def getPinB(self):
        if self.pinB is None:
            bVal = input("Enter pinB input for " + self.getLabel() + ": ")
        else:
            bVal = self.pinB.getFrom().getOutput()  # get output of gate connector
        return int(bVal)

    def setNextPin(self, source):
        """ attach a gate to this pin"""
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                raise RuntimeError("Non empty pins!!")


class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None

    def getPin(self):
        if self.pin is None:
            pinVal = input("Enter pin input for " + self.getLabel() + ": ")
        else:
            pinVal = self.pin.getFrom().getOutput()   # output from connector
        return(pinVal)

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError("Non empty pin!")


class AndGate(BinaryGate):
    """ AND gate functionality"""
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if (a == 1 and b == 1):
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if (a == 0 and b == 0):
            return 0
        else:
            return 1
            

class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPin()
        if (a == 1):
            return 0
        else:
            return 1


class Connector:
    def __init__(self, fGate, tGate):
        self.fromGate = fGate
        self.toGate = tGate
        tGate.setNextPin(self)  # connect next pin to this connector

    def getFrom(self):
        return(self.fromGate)

    def getTo(self):
        return(self.toGate)


def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())

main()
