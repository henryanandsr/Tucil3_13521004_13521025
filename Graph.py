import Node as n

class Graph:
    def __init__(self, start, end, nodes):
        self.start = start
        self.end = end
        self.nodes = nodes
        self.cost = 0
        self.state = start
    
    def updateNodes(self, nodes):
        self.nodes.append(nodes)
    #graf sebagai array of adjacent
    def __init__(self, adjacent):
        self.list = []
        self.list.append(adjacent)
        self.cost = 0
        self.state = self.list[len(self.list)-1]
        # print("HAI")
    def setState(self, state):
        self.state = state
    #ctor graf dengan array of adjacent
    # def __init__(self, arr):
    #     self.list = []
    #     self.list.extend(arr)
    #     self.cost = 0
    def addAdjNode(self, node):
        self.list.append(node)
    def getCost(self):
        return self.cost
    def display(self):
        print("List of nodes")
        for i in range (len(self.list)):
            self.list[i].display()
    # def copy(self,other):
    #     self.list = other.list
    #     self.cost = other.cost
    #     self.state = other.state
