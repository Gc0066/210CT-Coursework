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
        
    def insert(self,n,x):
        
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
            print(x.next, "the next node to current one being initialsied")
            print(n.next, "the next node for the one that was initalsied before the current one")
            print(x.prev, "the previous node to the one currently being initialsied")
            
            
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
        values=[]
        n=self.head
        while n!=None:
            values.append(str(n.value))
            n=n.next
        print("List: ",",".join(values))

    def delete(self,searchNode,deleteNode):
        #slide 65
        valueFound = False
        while valueFound = False:
            if searchNode.next == deleteNode.value:
                then delete searchNode.next
                valuefound = True
        #this bit will replace the "then delete search.next" bit in the loop
        if n != None:
            n.prev.next = n.next
        else:
            l.head = n.next
        if n.next != 0:
            n.next.prev = n.prev
        else:
            l.tail = n.prev
        
##            
         
if __name__ == '__main__':
    l=List()
    #calls list function and withn the parameters it creates the a node object and then passes that to the
    #insert function.

    #none given in first to make it the head of list.
    l.insert(None, Node(4))
    #after first node, .head is assigned to the first node thus l.head refernces the first node.
    l.insert(l.head,Node(6))
    l.insert(l.head,Node(8))
    l.insert(l.head, Node(10))
    #must have used the value somehow
    #searches from head to tail of the linked list for value and then deletes the node that has that value
    #could use the actual nodes name instead
    l.delete(10)
    l.display()
