class Vertice():
    def __init__(self, value):
        self.value = value
        self.connectedTo = []

class Graph():
    def __init__(self):
        self.listOfNodes = []

    def insertEdge(self, firstVertice, secondVertice):
        firstBool = False
        secondBool = False
        for i in self.listOfNodes:
            if firstVertice == i:
                firstBool = True
            if secondVertice == i:
                secondBool = True
        if firstBool == True and secondBool == True:
            firstVertice.connectedTo.append(secondVertice)
            secondVertice.connectedTo.append(firstVertice)
        else:
            return False

    def insertNode(self, Value):
        self.listOfNodes.append(Vertice(Value))

g = Graph()

g.insertNode(5)
g.insertNode(10)
g.insertEdge(5,10)
print(g.listOfNodes[0].connectedTo)
print(g.listOfNodes)
##listl = []
##v = Vertice(5)
##listl.append(v)
##
##print(listl)
