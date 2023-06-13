class Stack:
    def __init__(self):
        self.stack = [] # list() 
        self.top = -1 #empty  
        self.SIZE = 5
    
    def push(self,num):
        if self.top == self.SIZE - 1:
            print("STACK OVERFLOW")
        else:
            self.top = self.top + 1
            self.stack.append(num)

    def pop(self):
        if self.top == -1:
            print("STACK UNDERFLOW")
        else:
            print(self.stack[self.top]," poped")
            self.top = self.top - 1 
    
    def display(self):
        if self.top == -1 :
            print("STACK UNDERFLOW")
        else: 
            for i in range(self.top,-1,-1):
                print(self.stack[i])



stack = Stack()

while True:
    print("###################")
    print("1 For PUSH\n2 For POP\n3 For Display\n4 For Exit\nEnter Choice")
    choice = int(input())
    print("")
    if choice == 1 :
        num = int(input("Enter number"))
        stack.push(num)
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.display()
    else:
        exit(0)