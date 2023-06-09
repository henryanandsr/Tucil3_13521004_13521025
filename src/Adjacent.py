import math

class AdjacentB:
    def __init__(self, start, adjacent):
        # node
        self.start = start
        # list of nodes
        # [node, node, ...]
        self.adjacent = adjacent
    
    def getDistance(self, node):
        for adjacentIndex in range(len(self.adjacent)):
            if self.adjacent[adjacentIndex].name == node.name:
                return math.sqrt((self.start.X - self.adjacent[adjacentIndex].X)**2 + (self.start.Y - self.adjacent[adjacentIndex].Y)**2)    
    def display(self):
        print("===========================")
        self.start.display()
        print("List adjacent")
        for i in range (len(self.adjacent)):
            self.adjacent[i][0].display()
        print("===========================")
    def getName(self):
        return self.start.name
    
class Adjacent:
    def __init__(self, start, adjacent):
        # node
        self.start = start
        # list of nodes with weight/distance
        # [[node, distance], [node, distance], ...]
        self.adjacent = adjacent
    def display(self):
        print("===========================")
        self.start.display()
        print("List adjacent")
        for i in range (len(self.adjacent)):
            self.adjacent[i][0].display()
        print("===========================")