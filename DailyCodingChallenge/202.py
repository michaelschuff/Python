#Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.
num=7890987
numdigits=10
numofdigits=0
palindrome=True
while(num%numdigits!=num):
	numdigits*=10
while(numdigits!=1):
	numofdigits+=1
	numdigits/=10
for x in range(1,int(numofdigits/2)+1):
	if(((num%(10**x)-num%(10**(x-1)))/(10**(x-1)))!=((num%(10**(numofdigits-x+1)))-num%(10**(numofdigits-x)))/(10**(numofdigits-x))):
		palindrome=False
		break
if(not palindrome):
	print("Not a palindrome")
else:
	print("It is a palindrome!")