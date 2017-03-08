# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 08:31:15 2015

Inheritance using Logic Gate example
URL: https://goo.gl/AEpgFw
@author: umesh
"""

class LogicGate:
    def __init__(self, gate_label):
        self.label = gate_label
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, gate_label):
        LogicGate.__init__(self, gate_label)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA is None:
            return int(input("Enter Pin A input for gate "+ self.getLabel() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB is None:
            return int(input("Enter Pin B input for gate "+ self.getLabel() + "-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        """ set next available pin"""
        if self.pinA is None:
            self.pinA = source
        elif self.pinB is None:
            self.pinB = source
        else:
            raise RuntimeError('Error: NO EMPTY PINS')


class UnaryGate(LogicGate):
    """ Class for unary gate"""
    def __init__(self, gate_label):
        LogicGate.__init__(self, gate_label)

        self.pin = None

    def getPin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError('Error: NO EMPTY PIN')


class AndGate(BinaryGate):
    def __init__(self, gate_label):
        BinaryGate.__init__(self, gate_label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b == 1:
            out = 1
        else:
            out = 0
        return out

class OrGate(BinaryGate):
    """ OR gate"""
    def __init__(self, gate_label):
        BinaryGate.__init__(self, gate_label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==0 and b==0:
            out = 0
        else:
            out=1
        return out


class NotGate(UnaryGate):
    def __init__(self, gate_label):
        UnaryGate.__init__(self, gate_label)

    def performGateLogic(self):
        a = self.getPin()
        if a == 0:
            out = 1
        else:
            out = 0
        return out

class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


if __name__ == "__main__":
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())