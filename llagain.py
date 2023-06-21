class Node:
    def __init__(self):
        self.data = 0
        self.next = None 



head = None 

while True:
    print("\n1 For Add\n2 For List\n3 For insert Any\n4 Fpr DeleteAny")
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
    elif choice == 3:
        source = int(input("Enter Source"))        
        num = int(input("Enter number"))

        p = head 
        while p.data != source: 
            p=p.next 
        q = p.next 

        tmp = Node()
        tmp.data = num 
        tmp.next = q
        p.next = tmp 

    elif choice == 4:
         source = int(input("Enter num that you want to delete"))

        p = head 
        while p.data != source: 
            p=p.next 
        r= p.next 

        q=head 
        while q.next != p 
            q=q.next 

        q.next = r
        del p 
