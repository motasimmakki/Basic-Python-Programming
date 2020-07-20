mylist=[10,9,8,7,6,5,4,3,2,1]
i=0
while(i<len(mylist)):
    if mylist[i] % 2 == 0:
        print("{0}".format(mylist[i]))
    i+=1