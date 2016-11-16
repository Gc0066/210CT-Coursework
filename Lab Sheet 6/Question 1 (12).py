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
    stack = []
    treeEmpty = False
    stack.append(tree)
    while treeEmpty == False:
        if tree != None:
            stack.append(tree)
            tree = tree.left
            
        elif tree == None and len(stack)>0:
            x = stack.pop()
            print(x.value)
            tree = x.right
        else:
            treeEmpty = True
            
    
    
##    while bool = False:
####        stack.append(tree.value)
####        use stack to then navigate through tree
##
##        if tree.left == None:
##            printList.append(tree)
##            stack.pop()
##        else:
##            stack.append(tree.value)
##            tree = tree.left
##            if tree.right == None:
##                backtrack
##
##    if can go left then always go left
##    if cannot go left print
##    if can go right go right
##    if cannot go right then back track
##    repeat
##        
##        
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
