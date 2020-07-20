import math

str=input("Enter a String :")
i=0

while(str[i]==str[(len(str)-1)-i]) :
    if(i<(math.floor((len(str)/2))-1)) :
        i-=-1
    else:
        break

if(i==(math.floor((len(str)/2))-1)) :
    print("Entered String Is Palindrome.")
else :
    print("Entered String Is NOT Palindrome.")