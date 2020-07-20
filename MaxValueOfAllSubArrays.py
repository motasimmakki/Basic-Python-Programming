myList=[]
result=[]
n=int(input("Enter The Number Of Elements In An Array :"))
k=int(input("Enter The Length Of Sub Array :"))

for i in range(0,n):
    element=int(input())
    myList.append(element)

print("Input : ",myList)

def getGreatest(List):
    result.append(max(List))
    return

i=0
while((k+i)<=len(myList)): 
    getGreatest(myList[i:k+i])

    i-=-1

print("Result : ",result)