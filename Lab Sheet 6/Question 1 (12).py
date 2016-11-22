class BinTreeNode():

    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None


        
def tree_insert(tree, item):

    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                #.left points to only the first node on its right.
                #not all of the nodes on the right.
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print(tree.value)
  

def in_order(tree):
    '''takes input of the root node of the binary tree.
    Outputs the binary tree in order of value.'''
    
    stack = []                                                                                          #(1)
    treeEmpty = False                                                                                   #(1)

    while treeEmpty == False:                                                                           #(n)
        #If the node 'tree' currently points to IS NOT past the last node of the branch
        if tree != None:                                                                                #(n)
            
            #add the node to the end of the list(stack)
            stack.append(tree)                                                                          #(n)
            #move to next node on the left of the node previously pointed to,
            #this could be none if there is not a node
            tree = tree.left                                                                            #(n)

        #if node 'tree' points to IS past the last node of the branch
        #and their is still values to bracktrack too
        elif tree == None and len(stack)>0:                                                             #(n)
            
            #remove the last node in the stack
            x = stack.pop()                                                                             #(n)
            print(x.value)                                                                              #(n)
            #then make node point to the node on the right of the node that was just popped(removed)
            tree = x.right                                                                              #(n)
            #thus it will now go down right handside. if  no right hand side however then 'tree'
            #will equal none and thus the last appended node will be popped.

            #how backtracks:
            #if no right side tree will equal none, pop stack thus pops 5 in this case and then assigns
            #tree to equal 5.right, which equals none so thus it will then pop 6 and that does have right.
            #so will then go down that side.


        #if 'tree' equals none and there is no
        #nodes in the list, then have gone through all nodes
        #thus ends loop.
        else:                                                                                           #(1)
            treeEmpty = True                                                                            #(1)

 
   
##    if(tree.left!=None):
##        in_order(tree.left)
##    print(tree.value)
##    if(tree.right!=None):
##        in_order(tree.right)
        

if __name__ == '__main__':
    
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)


#runtime for In_Order: 8n+4
#Big O: O(n)
