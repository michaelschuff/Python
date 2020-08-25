#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 17:01:21 2019

@author: eatdacarrot
"""

import os
path="/Users/eatdacarrot/ComputerScience/PythonSpyder/GeorgeFoxPractice/2019"
file=open(os.path.join(path+"Whaleinput.txt"),"r")
lines=file.read().splitlines()
del lines[0]
for z in lines:
    mylist,k,isWhale=[],0,False
    for char in z:
      mylist.append(char)
    for char in mylist:
      if(char=="*"):
        if(mylist[k-1]=="X" and mylist[k+1]=="X"):
          mylist[k] = "X"
      k+=1
    for x in range(2):
      k=0
      for char in mylist:
        if(char=="*"):
          if(mylist[k+1]=="*"):
            del mylist[k+1]
        k+=1
    mylist2=""
    for y in mylist:
      mylist2+=y
    newlist=mylist2.split("*")
    del newlist[len(newlist)-1]
    l,k=0,0
    for y in newlist:
      if(len(y)>8 and len(y)<12):
        l+=1
      k+=1
      if(l==4):
        isWhale=True
    if(isWhale):
        print("yes")
    else:
        print("no")