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
        self.tentWeight = None
        self.pathTo = None

class Graph():
    def __init__(self):
        self.listOfNodes = []
        self.weightedEdges = {}

    def insertEdge(self, firstVertice, secondVertice, weight):
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
            NodeOne.connectedTo.append(NodeTwo)                         #(1)     
            NodeTwo.connectedTo.append(NodeOne)                         #(1)
            #may store key as memory addresses.
            self.weightedEdges[NodeOne, NodeTwo] = weight               #(1)
            self.weightedEdges[NodeTwo, NodeOne] = weight               #(1)
            

    def insertNode(self, Value):
        '''takes input of self and an integer, creates a vertice.'''
        self.listOfNodes.append(Vertice(Value))                         #(1)

    def display(self, listOfNodes):
        '''takes input of list, list contains memory locations'''
        #for every node, gets its list of connected nodes.
        #prints them.
        neighbours = ""
        for n in listOfNodes:
            for nn in n.connectedTo:
                neighbours = neighbours + " " + str(nn.value) + "(" + str(self.weightedEdges[n,nn]) + ")"
                
            print(str(n.value) + ": " +  neighbours)
            neighbours = ""
            

    def DFS(self, startNode):
        
        stack = []                                                      #(1)
        visited = []                                                    #(1)
        #initalises stack with starting node
        stack.append(startNode)                                         #(1)

        #while not all nodes have been printed            
        while len(stack) != 0:                                          #(n)
            x = stack.pop()                                             #(n)
            #if end of stack has not been visited yet. visit it.
            #otherwise pop next item and repeat process.
            if x.value not in visited:                                  #(n)
                visited.append(x.value)                                 #(n)
                #get every node x is connected to.
                for i in x.connectedTo:                                 #(n^2)
                    #add to stack so next x value will be one of the
                    #edges of the current value of x.
                    stack.append(i)                                     #(n^2)
                    
        #formats output
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
            #gets from front of list
            x = queue.dequeue()                                         #(n^2)
            if x.value not in visited:                                  #(n)
                #visit it if haven't visited.
                visited.append(x.value)                                 #(n)
                #add all connections to queue
                for i in x.connectedTo:                                 #(n^2)
                    queue.enqueue(i)                                    #(n^2)

        returnString = str(visited[0])                                  #(1)
        for i in visited:                                               #(n)
            if i != visited[0]:                                         #(n)
                returnString = returnString + ", " + str(i)             #(n)
        return returnString                                             #(1)

    def dijkstra(self, startNode, destNode):
        '''takes input of graph, the starting node and the ending node.
        returns string of the path, shown by their node value,
        from end to start node.'''


        visited = []
        #used to backTrack
        stackOfNodes = []

        #sets all nodes tentative weight to infinity. So they can be updated later.
        for vertex in g.listOfNodes:
            vertex.tentWeight = float('inf')

        #as we are at start node. tentWeight is 0
        startNode.tentWeight = 0
        currentNode = startNode
        number = 0

        #appends to VISITED NEED TO SAY WHY
        visited.append(currentNode)

        
        while currentNode != destNode:
            
            for neighbour in currentNode.connectedTo:
                #updates weight of each of the nodes the current node
                #is connected to.
                #Thus will eventually find shortest path to each node.
                if currentNode.tentWeight+self.weightedEdges[currentNode, neighbour] < neighbour.tentWeight:
                    neighbour.tentWeight = currentNode.tentWeight+self.weightedEdges[currentNode, neighbour]
                    neighbour.pathTo = currentNode
                               
            #resets minimum to infinite so can find smallest path.
            minimum = float('inf')

            for neighbour in currentNode.connectedTo:
                #
                number = number + 1
                print(neighbour.value)
                #finds the neighbour with the smallest path
                #which has not been visited.
                #if tentWeight same as minimum it chooses first path.
                if neighbour not in visited and neighbour.tentWeight < minimum:
                    #
                    tempStore= neighbour
                    minimum = neighbour.tentWeight
                    number = 0
                    stackOfNodes.append(currentNode)
                    l = ""
                    for i in stackOfNodes:
                        l = l + "," + str(i.value)
                    print(l)
                    
                else:
                    #if all neighbours have been visited. Backtrack to node before
                    #current.
                    if len(currentNode.connectedTo) == number:
                        tempStore = stackOfNodes.pop()
                        print(tempStore.value, "popped")
                        number = 0
            
            number = 0
            currentNode = tempStore
            visited.append(currentNode)

        backTrack = destNode
        path = "Path from end to start node as being: "
        while backTrack != None:
            path = path + str(backTrack.value) + ","
            backTrack = backTrack.pathTo
        return path

        
        
        

g = Graph()

g.insertNode(5)
g.insertNode(10)
g.insertNode(1)
g.insertNode(3)
g.insertNode(6)
g.insertNode(8)
g.insertNode(9)
g.insertNode(20)
g.insertNode(21)
g.insertNode(22)

##g.insertEdge(5,1,6)
##g.insertEdge(5,20,4)
##g.insertEdge(5,3,8)
##g.insertEdge(3,6,2)
##g.insertEdge(1,8,4)
##g.insertEdge(6,10,9)
##g.insertEdge(10,9,8)
##g.insertEdge(8, 5, 1)

#test
g.insertEdge(5,1,6)
g.insertEdge(5,3,8)
g.insertEdge(3,6,2)
g.insertEdge(6,9, 8)
g.insertEdge(10,3,9)
g.insertEdge(1,8,4)
g.insertEdge(9,20,3)
g.insertEdge(21,9,2)
g.insertEdge(22,9,8)
g.insertEdge(8, 5, 1)


g.display(g.listOfNodes)

#opens file and writes result of dfs first then bfs on the next line, closes file.
f = open("Search.txt", "w")
f.write("DFS" + ": " + str(g.DFS(g.listOfNodes[0])))
f.write("\nBFS" + ": " + str(g.BFS(g.listOfNodes[0])))
f.close()

print(g.dijkstra(g.listOfNodes[0], g.listOfNodes[1]))

#Runtime of InsertEdge and insert Node: 5n + 9
#Big O: O(n)

#Runtime of BFS and DFS: 5n^2+13n+10
#Big O: O(n^2)
#n^2 due to having to loop through every neighbour of every node.
