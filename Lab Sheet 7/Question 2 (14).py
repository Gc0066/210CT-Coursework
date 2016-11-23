class Vertice():
    def __init__(self, value):
        self.value = value
        #initalises list of nodes current node will be connected via edge to.
        self.connectedTo = []
        #self.conenctToLocation = []

class Graph():
    def __init__(self):
        self.listOfNodes = []

    def insertEdge(self, firstVertice, secondVertice):
        '''input of two integers and self. Returns false or connects input.'''
        
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

        #if input nodes not in graph.
        if NodeOne == None or NodeTwo == None:                          #(1)
            print("Node not in graph")                                  #(1)
            return False                                                #(1)
        else:                                                           #(1)
            ##NodeOne.connectedTo.append(secondVertice)                   #(1)
            ##NodeTwo.connectedTo.append(firstVertice)                    #(1)
            NodeOne.connectedTo.append(NodeTwo)
            NodeTwo.connectedTo.append(NodeOne)

    def insertNode(self, Value):
        '''takes input of self and an integer, creates a vertice.'''
        self.listOfNodes.append(Vertice(Value))                         #(1)

    def display(self, listOfNodes):
        for n in listOfNodes:
            print(n.value, n.connectedTo)

    def DFS(self, startNode):
        stack = []
        visited = []
        stack.append(startNode)
        #print(stack)

        while len(stack) != 0:
            #could do a loop here to turn int input into memory location of start node.
            x = stack.pop()
            #print(x.value,"x")
            #maybe use value
            if x.value not in visited:
                visited.append(x.value)
                #could now append it to the text file
                for i in x.connectedTo:
                    #print(i, "i")
                    stack.append(i)
        #or could now add all at once to a text file.
        return visited
    #currently works. However want it to display numbers rather than memory locations

    def BFS(self, startNode):
        Queue = #something
        #maybe import from linked list?
        visited = []
        Queue.enqueue(v)
        while len(Queue) != 0:
            x = Queue.dequeue()
            if x not in visited:
                visited.append(x)
                for i in x.connectedTo:
                    Queue.enqueue(i)
        return visited
                    
        

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
g.insertEdge(5,3)
g.insertEdge(3,6)
g.insertEdge(1,8)
#should give error
#g.insertEdge(10,0)

g.display(g.listOfNodes)

print(g.DFS(g.listOfNodes[0]))
