#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 15:23:36 2019

@author: eatdacarrot
"""
def isPrime(num1):
    for y in range(2,int(num1**.5)+1):
        if(num1%y==0):
            return False
    return True

def getprimefactors(num1):
    primefactors=[]
    x=2
    while(not isPrime(num1)):
        if(num1%x==0 and isPrime(x)):
            primefactors.append(x)
            num1=int(num1/x)
            x=x-1
        x=x+1
    primefactors.append(num1)
    return(primefactors)
import os
path ="/Users/eatdacarrot/ComputerScience/PythonSpyder/GeorgeFoxPractice/2019"
file = open(os.path.join(path+"Radicalinput.txt"),"r")
lines = file.read().splitlines()
for x in lines:
    outside=[]
    o=1
    i=1
    y=0
    p=getprimefactors(int(x))
    while(y<len(p)-1):
        if(p[y]==p[y+1]):
            outside.append(p[y])
            del p[y]
            del p[y]
            y=y-1
        y=y+1
    for j in outside:
        o*=j
    for j in p:
        i*=j
    if(o!=1):
        print(o,end="")
    if(i!=1):
        print(".",i,sep="",end="")
    print()