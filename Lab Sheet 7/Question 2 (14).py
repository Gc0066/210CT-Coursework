class Queue():
    def __init__(self):
        self.value = []                                                 #(1)

    def enqueue(self, visitedNode):
        self.value.append(visitedNode)                                  #(1)
        
    def dequeue(self):
        frontVertice = self.value.pop(0)                                #(n)
        return frontVertice                                             #(1)
        
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
            NodeOne.connectedTo.append(NodeTwo)
            NodeTwo.connectedTo.append(NodeOne)

    def insertNode(self, Value):
        '''takes input of self and an integer, creates a vertice.'''
        self.listOfNodes.append(Vertice(Value))                         #(1)

    def display(self, listOfNodes):
        neighbours = ""
        for n in listOfNodes:
            for nn in n.connectedTo:
                neighbours = neighbours + " " + str(nn.value)
            print(str(n.value) + ": " +  neighbours)
            neighbours = ""
            

    def DFS(self, startNode):
        stack = []                                                      #(1)
        visited = []                                                    #(1)
        stack.append(startNode)                                         #(1)
                    
        while len(stack) != 0:                                          #(n)
            x = stack.pop()                                             #(n)
            if x.value not in visited:                                  #(n)
                visited.append(x.value)                                 #(n)
                for i in x.connectedTo:                                 #(n^2)
                    stack.append(i)                                     #(n^2)
        returnString = str(visited[0])                                  #(1)
        for i in visited:                                               #(n)
            if i != visited[0]:                                         #(n)
                returnString = returnString + ", " + str(i)             #(n)
        return returnString                                             #(1)
    
    def BFS(self, startNode):
        queue = Queue()                                                 #(1)
        visited = []                                                    #(1)
        queue.enqueue(startNode)                                        #(1)
        while len(queue.value) != 0:                                    #(n)
            x = queue.dequeue()                                         #(n^2)
            if x.value not in visited:                                  #(n)
                visited.append(x.value)                                 #(n)
                for i in x.connectedTo:                                 #(n^2)
                    queue.enqueue(i)                                    #(n^2)
        returnString = str(visited[0])                                  #(1)
        for i in visited:                                               #(n)
            if i != visited[0]:                                         #(n)
                returnString = returnString + ", " + str(i)             #(n)
        return returnString                                             #(1)
        

g = Graph()

g.insertNode(5)
g.insertNode(10)
g.insertNode(1)
g.insertNode(3)
g.insertNode(6)
g.insertNode(8)
g.insertNode(9)

g.insertEdge(5,1)
g.insertEdge(5,3)
g.insertEdge(3,6)
g.insertEdge(1,8)
g.insertEdge(6,10)
g.insertEdge(10,9)

g.display(g.listOfNodes)

f = open("Search.txt", "w")
f.write("DFS" + ": " + str(g.DFS(g.listOfNodes[0])))
f.write("\nBFS" + ": " + str(g.BFS(g.listOfNodes[0])))
f.close()

#Runtime of BFS and DFS: 5n^2+13n+10
#Big O: O(n^2)
#n^2 due to having to loop through every neighbour of every node.
