class Node:
    def __init__(self):
        self.data = 0
        self.next = None 



head = None 

while True:
    print("\n1 For Add\n2 For List")
    print("\nEnter choice")
    choice = int(input())
    
    if choice == 1: 
        if head == None:
            head = Node()
            head.data  =  int(input("enter number"))
            head.next =  None 
            last = head 
        else:
            tmp = Node() 
            tmp.data = int(input("Enter number"))
            tmp.next = None 
            last.next = tmp 
            last = tmp 
    elif choice == 2: 
        p = head 
        
        while p != None:
            print(p.data) # 30 
            p = p.next 
        
        
        
 

