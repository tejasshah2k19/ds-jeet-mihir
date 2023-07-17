#AVL -BST - Binary 

#AVL -> max 2 child min 0 child , left-> small , right-> big 
#node-> Balance Factor-> {-1, 0 ,1 } 
# rotate -> 

#bf = lh - rh 


class Node:
    def __init__(self):
        self.data = 0 
        self.left = None 
        self.right = None 
        self.height = 1

root = None 

 

def addNode(root,data): #100,200 
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
 
    root.height = 1 + calculateHeight(root)
 
    bf = calculateBF(root) 

    if bf < -1 and root.right.data < data :
        #RR 
        print("RR ",root.data)
    elif bf < -1 and root.right.data > data :
        #RL
        print("RL",root.data) 
    elif bf > 1 and root.left.data > data:
        #LL
        print("LL",root.data) 
    elif bf > 1 and root.left.data < data :
        #LR 
        print("LR",root.data)
     
    
    return root 

def calculateHeight(root):
    lh = 0 
    rh = 0
    if root.left != None :
        lh = root.left.height
    if root.right != None:
        rh = root.right.height; 
    if lh > rh  :
        return lh 
    else: 
        return rh
    
def calculateBF(root):
    lh = 0
    rh = 0 
    if root.left != None :
        lh = root.left.height
    if root.right != None:
        rh = root.right.height;
    return lh - rh 

def inOrder(root):
    if root != None:
        inOrder(root.left) #100  
        print(root.data," ",root.height," ",calculateBF(root))
        inOrder(root.right)
while True:
    print("\n\n1 For Add\n2 For Print\n0 Exit\n\nEnter choice")
    choice = int(input())

    if choice == 1 : 
        num = int(input())
        root = addNode(root,num) #100  200 
    elif choice == 2:
            inOrder(root)
    elif choice ==0 :
        exit(0)



