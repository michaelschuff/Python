from math import sqrt

for x in lines:
    x=x.split(" ")
    print(round((-float(x[1])+sqrt(float(x[1])**2-4*float(x[0])*float(x[2])))/(2*float(x[0])),3),", ",end="",sep="")
    print(round((-float(x[1])-sqrt(float(x[1])**2-4*float(x[0])*float(x[2])))/(2*float(x[0])),3))