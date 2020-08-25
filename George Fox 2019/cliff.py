def findheight(cliff,x):
    currentheight=0
    for i in range(len(cliff)-1,0,-1):
        if(cliff[i][x]=="C"):
            currentheight+=1
        else:
            break
    return(currentheight)
cliff=[]
for x in range(int(input())):
    cliff.append(input())
currentheight=findheight(cliff,0)
biggestdif=0
currentdif=0
nextheight=0
for i in range(1,len(cliff[0])):
    nextheight=findheight(cliff,i)
    currentdif=abs(currentheight-nextheight)
    if(currentdif>biggestdif):
        biggestdif=currentdif
    currentheight=nextheight
print(biggestdif,"units of rope are needed for this site.")