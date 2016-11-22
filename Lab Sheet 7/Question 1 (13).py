class Vertice():
    def __init__(self, value):
        self.value = value
        #initalises list of nodes current node will be connected via edge to.
        self.connectedTo = []

class Graph():
    def __init__(self):
        self.listOfNodes = []

    def insertEdge(self, firstVertice, secondVertice):
        'input of two integers and self. Returns false or connects input.'
        
        NodeOne = None                                                  #(1)
        NodeTwo = None                                                  #(1)

        #for every node in graph
        for i in self.listOfNodes:                                      #(n)
            #if value of current node in list = inputted value
            #assign memory location to corresponding variable.
            if i.value == firstVertice:                                 #(n)
                NodeOne = i                                             #(n)
            if i.value == secondVertice:                                #(n)
                NodeTwo = i                                             #(n)

        #if input not nodes that are in graph.
        if NodeOne == None or NodeTwo == None:                          #(1)
            print("Node not in graph")                                  #(1)
            return False                                                #(1)
        else:                                                           #(1)
            NodeOne.connectedTo.append(secondVertice)                   #(1)
            NodeTwo.connectedTo.append(firstVertice)                    #(1)


    def insertNode(self, Value):
        'takes input of self and an integer'
        self.listOfNodes.append(Vertice(Value))                         #(1)

    def display(self, listOfNodes):
        for n in listOfNodes:
            print(n.value, n.connectedTo)

g = Graph()

g.insertNode(5)
g.insertNode(10)
g.insertNode(1)
g.insertNode(2)
g.insertNode(3)
g.insertNode(4)
g.insertNode(6)
g.insertNode(7)
g.insertNode(8)
g.insertNode(9)

g.insertEdge(5,1)
g.insertEdge(3,6)
#should give error
g.insertEdge(10,0)

g.display(g.listOfNodes)

#runtime: 5n + 9
#Big O: O(n)
