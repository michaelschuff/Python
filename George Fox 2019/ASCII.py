wordcount=0
asci=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
a = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for x in range(len(asci)):
    a.append(asci[x].lower())
b = input().split(" ")
c = input().split(" ")
d = input().split(" ")
for x in c:
    b.append(x)
for x in d:
    b.append(x)
for x in b:
    s=0
    for j in x:
        s+=a.index(j)+1
    if(len(x)%2==s%2):
        wordcount+=1
print("The provided text has",wordcount,"balanced word(s).")