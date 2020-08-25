#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 12:19:12 2019

@author: eatdacarrot
"""
def rectangle(r,c,filled):
    for x in range(r):
        if(filled or x==0 or x==r-1):
            print("#"*c)
        else:
            print("#"," "*(c-2),"#",sep="")
def left(x,filled):
    for z in range(1,x+1):
        if(filled or z==1 or z==x):
            print("#"*z)
        else:
            print("#"," "*(z-2),"#",sep="")
def right(x,filled):
    for z in range(1,x+1):
        if(filled or z==1 or z==x):
            print(" "*(x-z),"#"*z,sep="")
        else:
            print(" "*(x-z),"#"," "*(z-2),"#",sep="")
def diamond(w,filled):
    for x in range(1,w+1,2):
        print(" "*int((w-x)/2),end="")
        if(filled or x==1):
            print("#"*x)
        else:
            print("#"," "*(x-2),"#",sep="")
    for x in range(w-2,0,-2):
        print(" "*int((w-x)/2),end="")
        if(filled or x==1):
            print("#"*x)
        else:
            print("#"," "*(x-2),"#",sep="")
import os
path="/Users/eatdacarrot/ComputerScience/PythonSpyder/GeorgeFoxPractice/2018/"
file=open(os.path.join(path+"Drawinput.txt"),"r")
lines=file.read().splitlines()
del lines[0]
for x in lines:
    x=x.split(" ")
    if(x[1]=="triangle"):
        del x[1]
    for y in range(len(x)-2):
        x[y+1]=int(x[y+1])
    if(x[len(x)-1]=="y"):
        x[len(x)-1]=True
    else:
        x[len(x)-1]=False
    if(x[0]=="rectangle"):
        rectangle(x[1],x[2],x[3])
    elif(x[0]=="right"):
        right(x[1],x[2])
    elif(x[0]=="left"):
        left(x[1],x[2])
    elif(x[0]=="diamond"):
        diamond(x[1],x[2])