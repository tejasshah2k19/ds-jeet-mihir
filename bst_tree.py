class Node:
    def __init__(self):
        self.data = 0 
        self.left = None 
        self.right = None 


root = None 


# root = Node()
# root.data = 30 
# root.left = None 
# root.right = None 

# tmp = Node() 
# tmp.data = 20 
# root.left = tmp 
# tmp.left = None
# tmp.right = None 

def addNode(root,data): #100,50 
    if root == None:
        root = Node()
        root.data = data 
        root.left = None
        root.right = None 
        return root 
    elif root.data > data:
        root.left = addNode(root.left,data)
    else:
        root.right = addNode(root.right,data)
    return root 

"""
    tree travesal -> 3
        1) inOrder    left:root:right {ascending order}
        2) preOrder   root:left:right 
        3) postOrder  left:right:root
"""

def inOrder(root):
    if root != None:
        inOrder(root.left) #100  
        print(root.data)
        inOrder(root.right)
while True:
    print("\n\n1 For Add\n2 For Print\n0 Exit\n\nEnter choice")
    choice = int(input())

    if choice == 1 : 
        num = int(input())
        root = addNode(root,num) #root{100},50
    elif choice == 2:
            inOrder(root)
    elif choice ==0 :
        exit(0)
