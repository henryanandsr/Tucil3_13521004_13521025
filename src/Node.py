import math

class NodeB:
    def __init__(self,name, previous = None):
        self.name = name
        self.previous = previous
        
    def setCoor(self,X,Y):
        self.X = X
        self.Y = Y

    def display(self):
        print(self.name)

    def setPrev(self, previous):
        self.previous = previous

    def getDistance(self, node):
        return math.sqrt((self.X - node.X)**2 + (self.Y - node.Y)**2)

class Node:

    def __init__(self, name, previous = None):
        self.name = name
        self.previous = previous

    def display(self):
        print(self.name)
    
    def setPrev(self, previous):
        self.previous = previous


    

    
    
    