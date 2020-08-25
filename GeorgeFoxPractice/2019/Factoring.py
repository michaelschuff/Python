#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 13:24:18 2019

@author: eatdacarrot
"""
import os
def printfactors(a1,b1,a2,b2):
    ab=[a1,b1,a2,b2]
    for x in range(0,2):
        if(ab[2*x+1]!=0):
            print("(",end="")
            if(ab[2*x]!=1):
                print(ab[2*x],end="")
            print("x",end="")
            if(ab[2*x+1]>0):
                print("+",end="")
            print(ab[2*x+1],")",end="",sep="")
        else:
            if(ab[2*x]!=1):
                print(ab[2*x],end="")
            print("x",end="")
    print()
path="/Users/eatdacarrot/ComputerScience/PythonSpyder/GeorgeFoxPractice/2019"
file=open(os.path.join(path+"Factoringinput.txt"),"r")
lines=file.read().splitlines()
del lines[0]
Cfctrs=[]
Afctrs=[]
for equation in lines:
    a=equation.split(" ")
    if(a[1]=="-"):
        a[2]="-"+a[2]
    del a[1]
    if(a[3]=="-"):
        a[4]="-"+a[2]
    del a[2]
    a[0]=int(a[0][:-2])
    a[1]=int(a[1][:-1])
    a[2]=int(a[2])
    for x in range(1,a[2]+1):
        if(a[2]%x==0):
            Cfctrs.append(x)
    for x in range(1,a[0]+1):
        if(a[0]%x==0):
            Afctrs.append(x)
    for A in Afctrs:
        for C in Cfctrs:
            if(A*C+(a[2]/C)*(a[0]/A)==a[1]):
                printfactors(A,int(a[2]/C),int(a[0]/A),C)
                Cfctrs=[]
                Afctrs=[]