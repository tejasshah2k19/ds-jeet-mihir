class Node:
    def __init__(self):
        self.data = 0
        self.next = None 



head = None 

while True:
    print("0 For Exit\n1 For Add Node\n2 For List\n3 For DeleteNode\n\nEnter Your choice::")
    choice = int(input())

    if choice ==  1:
        if head == None: 
            head = Node()
            num = int(input("Enter number"))  
            head.data = num 
            head.next = None 
        else:
            num = int(input("Enter number"))  
            tmp = Node()
            tmp.data = num 
            tmp.next = None 
            p = head 
            while p.next != None: 
                p = p.next 
            p.next = tmp 

    elif choice == 2:
        p = head
        while p != None:
            print(p.data)
            p = p.next 

    elif choice == 3:
        p = head 
        while p.next !=None:
            p=p.next 

        q = head 
        while q.next != p:
            q=q.next    
        q.next = None 
        del p 

    elif choice == 0:
        exit(0)
    else:
        print("\nInvalid choice")