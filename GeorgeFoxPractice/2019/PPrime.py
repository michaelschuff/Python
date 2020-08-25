b=int(input("Num of dataset"))
lines=[]
for x in range(b):  
    lines.append(input())
def isPrime(x):
    if(x>=2):
        for y in range(2,x):
            if(x%y==0):
                return False
    else:
        return False
    return True
for x in lines:
    if(x==x[::-1] and len(x)!=1 and isPrime(int(x))):
        print("yes")
    else:
        print("no")