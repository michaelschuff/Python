infolist=[]
a3=[]
for i in range(int(input())):
    info=input()
    infolist=info.split("x")
    infolist.append(infolist[1].split(" - ")[0])
    infolist.append(infolist[1].split(" - ")[1])
    del infolist[1]
    w=int(infolist[0])
    h=int(infolist[1])
    d=int(infolist[2])
    a1=[]
    a2=[]
    for j in range(w):
        a2.append("")
    for x in range(h):
        a1.append(input())
    if(d==180):
        for x in range(h):
            a1[x]=a1[x][::-1]
        a1.reverse()
        a2=a1
    elif(d==90):
        for x in range(h):
            k=0
            for char in a1[h-x-1]:
                a2[k]+=char
                k+=1
    elif(d==270):
        for x in range(h):
            k=0
            for char in a1[x]:
                a2[k]+=char
                k+=1
        a2.reverse()
    elif(d==0):
        a2=a1
    a3.append(a2)
for x in range(len(a3)):
    for i in a3[x]:
        print(i)
    if(x<len(a3)-1):
        print()