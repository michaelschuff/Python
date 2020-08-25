a=[]
for x in range(4):
    a.append(input())
for x in a:
    s1=0
    b=x.split(", ")
    for x in range(3):
        s1+=float(b[x])
    s1/=3
    s1=str(round((90-s1*.75)*4,2))
    c=s1.split(".")
    del c[0]
    if(len(c[0])<2):
        s1=s1+"0"
    print(s1)