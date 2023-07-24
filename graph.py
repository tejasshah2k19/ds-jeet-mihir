list = []

totalVertex = int(input("How many Vertex you have"))

while True:
    print("Enter Source - Destination - Cost ")
    source = int(input())
    destination = int(input())
    cost = int(input())
    list.append({"source":source,"destination":destination,"cost":cost})
    list.append({"source":destination,"destination":source,"cost":cost})

    choice = input("Do Yo want to add more ? Y")
 
    if choice != "Y" and choice != "y":
        break 


for i in range(0,totalVertex):# 0 1 2 3 4 5 
    print("\n",i,"is connected with : ")
    for edge in list:# source:0 destination:1 cost:5 
        if edge.get("source") == i:
            print(edge.get("destination"),end=" ") 
            
