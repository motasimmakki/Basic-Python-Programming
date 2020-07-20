firstNum=0
secondNum=1
i=0
print(firstNum,end=" ")
print(secondNum, end=" ")
while (i < 10):
    nextTerm=int(firstNum)+int(secondNum)
    print(nextTerm,end= " ")
    firstNum = int(secondNum)
    secondNum = int(nextTerm)
    i+=1