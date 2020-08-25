from math import sqrt
a=[]
for x in range(4):
    a.append(float(input()))
for x in a:
    print(round(sqrt(2*x/9.8),2),"second(s)")