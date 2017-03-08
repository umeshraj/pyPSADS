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
        return int(input("Enter Pin A input for gate "+ self.getLabel() + "-->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate "+ self.getLabel() + "-->"))


class UnaryGate(LogicGate):
    """ Class for unary gate"""
    def __init__(self, gate_label):
        LogicGate.__init__(self, gate_label)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))


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


if __name__ == "__main__":
    b = BinaryGate('ur')
#    g1 = AndGate("G1")
#    print(g1.getOutput())
#    g2 = OrGate("G2")
#    print(g2.getOutput())
    g3 = NotGate("G3")
    print(g3.getOutput())