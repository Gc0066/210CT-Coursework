class Node(object):
    def __init__(self, value):
        #value passed when node is created
        self.value=value
        self.next=None
        self.prev=None


 
class List(object):
    
    def __init__(self):
        #initalises list with a head and a tail but does not assign a value to either
        #as no nodes yet.
        self.head=None
        self.tail=None
       # self.previousNode = None
        self.listOfNodes = []
        self.i = 0
        
    def insert(self,n,x):
        self.listOfNodes.append(x)


        #Not actually perfect: how do we prepend to an existing list?

        #n is referencing none or it is referencing the head node
        #x is referencing the node just initialised
        
        #runs for all nodes that are not the head
        if n!=None:
            #makes the next value of node currently being inserted = none
            #this is because it cannot point to anything as their is no next node after
            #the one being inserted right now.
            x.next=n.next
            #makes the node before the one currently being interserted.
            #Point to x aka. the current node being inserted.
            n.next=x
            #then makes the current node point to the node before it
            x.prev=n
            #htis if maybe stops the list?
            #print(x.next, "the next node to current one being initialsied")
            #print(n.next, "the next node for the one that was initalsied before the current one")
            #print(x.prev, "the previous node to the one currently being initialsied")
            
            
            if x.next!=None:
                x.next.prev=x
        #runs for first node 
        if self.head==None:
            #same way of writing self.head = x and then self.tail = x on two different lines.
            #Thus this makes the head and the tail the first node.

            self.head=self.tail=x
            #makes the previous and next node to the current node value = none
            x.prev=x.next=None
       

        #makes the tail the next element in the linked list
        #thus n which is the first node = the tail,
        #it then makes the new node the tail.
        elif self.tail==n:
            self.tail=x

            
    def display(self):
        #comment this
        values=[]
        n=self.head
        while n!=None:
            values.append(str(n.value))
            n=n.next
        print("List: ",",".join(values))

    def delete(self,deleteNode):
        
        nodeFound = False
        #sets the first node to be checked as the first node in the list
        searchNode = self.head
        #until node is found
        while nodeFound == False:
            
            print(searchNode)
            print(searchNode.value)

            #if the current node is the desired node to be
            #deleted.
            #if searchNode.value == deleteNode:
            if searchNode == deleteNode:

                #if it is not the head
                if searchNode.prev != None:
                    #make the previous node point to
                    #the node in front of the node being
                    #deleted.
                    searchNode.prev.next = searchNode.next
                #make the node that will be the first node
                #after deletion the head node.
                else:
                    l.head = searchNode.next

                #if it is not the tail
                if searchNode.next != None:
                    #make the next node point to
                    #the node previous to the node being
                    #deleted.
                    searchNode.next.prev = searchNode.prev
                    
                else:
                    #make the node that will be the last node
                    #after deletion the tail node.
                    l.tail = searchNode.prev
                    
                searchNode.del
                nodeFound = True
                
            #if at the end of the linked list and the
            #current node is not the desired delete node.
            elif searchNode.next == None:
                return False

            #otherwise go to next node
            else:
                searchNode = searchNode.next

     
##            
         
if __name__ == '__main__':
    l=List()
    #calls list function and withn the parameters it creates a node object and then passes that to the
    #insert function.

    #none given in first to make it the head of list.
    l.insert(None, Node(4))
    #after first node, .head is assigned to the first node thus l.head refernces the first node.
    l.insert(l.head, Node(5))
    l.insert(l.head,Node(6))
    l.insert(l.head,Node(8))
    l.insert(l.head, Node(10))

    #could either search for value.
    #or could search by node using dictionary.
    l.delete(l.listOfNodes[4])
    l.display()
