class Edge:
    def __init__(self) -> None:
        self.source =None  
        self.destionation=None
        self.cost=None
 



print("How many Edges You want to create") # 3 ->  6 
totalVertex = int(input())


list = [] 

for i in range(0,totalVertex):
    v = Edge() 
    print("Enter Source Destination and Cost")
    v.source = int(input())
    v.destionation = int(input())
    v.cost = int(input())
    list.append(v)
    
    s = Edge()
    s.source = v.destionation
    s.destionation=v.source
    s.cost = v.cost
    list.append(s)


print("Which Node You want to check?")
node = int(input())
for x in list:
    if x.source == node:
        print(x.destionation)