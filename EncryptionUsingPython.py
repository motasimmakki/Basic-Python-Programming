myStr=input("Enter A String To Encrypt :")

i=0
encStr=""
decStr=""

def reverseString(x):
	return x[::-1]

#string encryption
while i<len(myStr) :
	if i%2==0 :
		ch=ord(myStr[i])+3
	else :
		ch=ord(myStr[i])+5

	encStr+=str(chr(ch))
	# print(ch,end=" ")
	i-=-1

encStr=reverseString(encStr)

print("\nEncrypted String Is : "+encStr)

#string decryption
i=0
encStr=reverseString(encStr)

while i<len(encStr) :
	if i%2==0 :
		ch=ord(encStr[i])-3
	else :
		ch=ord(encStr[i])-5

	decStr+=str(chr(ch))
	i-=-1

print("\nDecrypted String Is : "+decStr)

