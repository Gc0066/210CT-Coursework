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
        self.listOfNodes = []
        
    def insert(self,n,x):

        #n is referencing none or it is referencing the head node
        #x is referencing the node just initialised
        
        #runs for all nodes that are not the head
        if n!=None:
            #makes the next value of node currently being inserted = none
            #this is because it cannot point to anything as there is no next node after
            #the one being inserted right now.
            x.next=n.next
            #makes the node before the one currently being interserted.
            #Point to x aka. the current node being inserted.
            n.next=x
            #then makes the current node point to the node before it
            x.prev=n          
            
            if x.next!=None:
                x.next.prev=x
        ##ALLOWS PREPEND
        if n==None and self.head != None:                                           #(1)
            #make the previous of the old head = the new head
            self.head.prev = x                                                      #(1)
            #makes the new heads next pointer, point at the old head.
            x.next = self.head                                                      #(1)
            #make the inserted node the head
            self.head = x                                                           #(1)
            #make the previous of the new head = none.
            x.prev = None                                                           #(1)
            
            
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
        
        values=[]
        n=self.head
        #goes from the head to the tail.
        #ending when it has gone past the tail.
        while n!=None:
            values.append(str(n.value))
            n=n.next
        print("List: ",",".join(values))

    def delete(self,deleteNode):
        
        nodeFound = False                                                   #(1)
        #sets the first node to be checked as the first node in the list
        searchNode = self.head                                              #(1)
        #until node is found
        while nodeFound == False:                                           #(n)
            
            #if the current node is the desired node to be
            #deleted.
            if searchNode.value == deleteNode:                              #(n)

                #if it is not the head
                if searchNode.prev != None:                                 #(1)
                    #make the previous node point to
                    #the node in front of the node being
                    #deleted.
                    searchNode.prev.next = searchNode.next                  #(1)
                #make the node that will be the first node
                #after deletion the head node.
                else:                                                       #(1)
                    l.head = searchNode.next                                #(1)

                #if it is not the tail
                if searchNode.next != None:                                 #(1)
                    #make the next node point to
                    #the node previous to the node being
                    #deleted.
                    searchNode.next.prev = searchNode.prev                  #(1)
                    
                else:                                                       #(1)
                    #make the node that will be the last node
                    #after deletion the tail node.
                    l.tail = searchNode.prev                                #(1)
                    
                del(searchNode)                                             #(1)
                nodeFound = True                                            #(1)
                
            #if at the end of the linked list and the
            #current node is not the desired delete node.
            elif searchNode.next == None:                                   #(1)
                return False                                                #(1)

            #otherwise go to next node
            else:                                                           #(n)
                searchNode = searchNode.next                                #(n)
        return True                                                         #(1)        
         
if __name__ == '__main__':
    l=List()
    #calls list function and withn the parameters it creates a node object and then passes that to the
    #insert function.

    #none given in first to make it the head of list.
    l.insert(None, Node(4))
    #after first node, .head is assigned to the first node thus l.head refernces the first node.
    l.insert(l.head, Node(5))
    l.insert(None,Node(6))
    l.insert(l.head,Node(8))
    l.insert(l.head, Node(10))
    l.insert(None, Node(1))
    boolean = False
    while boolean == False:
        try:
            number = int(input("Please enter a number to delete"))
            boolean = True
        except ValueError:
            print("Please enter an integer")
            
    print(l.delete(number))
    l.display()

#Runtime of Insert function and prepend code: 4n+20
#Big O: O(n)
