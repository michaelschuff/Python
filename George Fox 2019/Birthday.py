num=int(input())
inputs=[]
for i in range(num):
    inputs.append(input())
dates=[]
for i in range(num):
    newlist=inputs[i].split(" - ")
    newintlist=[]
    newintlist.append(int(newlist[1]))
    dates.append(newintlist)
    newlist=newlist[0].split("/")
    for j in range(3):
        dates[i].append(int(newlist[j]))
for i in range(len(dates)):
    for x in range(dates[i][0]):
        dates[i][0]-=1
        dates[i][2]-=1
        if(dates[i][2]==0):
            dates[i][1]-=1
            if(dates[i][1]==0):
                dates[i][3]-=1
                dates[i][1]=12
                dates[i][2]=31
            elif(dates[i][1]==4 or dates[i][1]==6 or dates[i][1]==9 or dates[i][1]==11):
                dates[i][2]=30
            elif(dates[i][1]!=2):
                dates[i][2]=31
            else:
                if(dates[i][3]%400==0):
                    dates[i][2]=29
                elif(dates[i][3]%100==0):
                    dates[i][2]=28
                elif(dates[i][3]%4==0):
                    dates[i][2]=29
                else:
                    dates[i][2]=28
    for j in range(len(dates[i])):
        if(dates[i][j]<10):
            dates[i][j]="0"+str(dates[i][j])
    print(dates[i][1],"/",dates[i][2],"/",dates[i][3],sep="")