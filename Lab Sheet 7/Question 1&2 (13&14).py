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
            NodeOne.connectedTo.append(NodeTwo)                         #(1)
            NodeTwo.connectedTo.append(NodeOne)                         #(1)

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
                neighbours = neighbours + " " + str(nn.value)
                
            print(str(n.value) + ": " +  neighbours)
            neighbours = ""
            

    def DFS(self, startNode):
        '''Takes input of a memory location that contains a node. performs DFS
         on the graph. Returns a concatenated string of the values of the nodes,
         in the order they were visited.'''
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
        '''Takes input of a memory location that contains a node. performs BFS
         on the graph. Returns a concatenated string of the values of the nodes,
         in the order they were visited.'''
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

#opens file and writes result of dfs first then bfs on the next line, closes file.
f = open("Search.txt", "w")
f.write("DFS" + ": " + str(g.DFS(g.listOfNodes[0])))
f.write("\nBFS" + ": " + str(g.BFS(g.listOfNodes[0])))
f.close()

#Runtime of InsertEdge and insert Node: 5n + 9
#Big O: O(n)

#Runtime of BFS and DFS: 5n^2+13n+10
#Big O: O(n^2)
#n^2 due to having to loop through every neighbour of every node.
