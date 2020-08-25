bolts=[]
results=[]
num=int(input())
for i in range(num):
    results.append("z")
    newString=input()
    newList=newString.split(" ")
    for x in range(len(newList)):
        newList[x]=int(newList[x])
    del newList[0]
    bolts.append(newList)

for i in range(len(bolts)):
    while(True):
        boltCheck=True
        newBolt=[]
        for x in range(len(bolts[i])):
            newBolt.append(bolts[i][x])
        del newBolt[0]
        for x in range(len(newBolt)):
            newBolt[x]-=bolts[i][x]
            if(newBolt[x] != 0):
                boltCheck=False
        bolts[i]=newBolt
        if(boltCheck):
            results[i]+="ap!"
            break
        elif(len(newBolt) == 1):
            if(newBolt[0] > 0):
                results[i]="*fizzle*"
                break
            else:
                results[i]="*bunny*"
                break
        else:
            results[i]+="z"
    if(i==len(bolts)-1):
        print(results[i],end="")
    else:
        print(results[i])