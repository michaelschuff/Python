#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 22:16:43 2019

@author: eatdacarrot
"""

import os
path="/Users/eatdacarrot/ComputerScience/PythonSpyder/GeorgeFoxPractice/2018/"
file=open(os.path.join(path+"Robberyinput.txt"),"r")
lines=file.read().splitlines()
datasets=int(lines[0])
del lines[0]
for data in range(datasets):
    money=0
    tempweight=[]
    tempmoney=0
    bestitems=[]
    sortedbest=[]
    maxweight=int(lines[0].split(" ")[0])
    numitem=int(lines[0].split(" ")[1])
    del lines[0]
    items=lines[0].split(" ")
    del lines[0]
    weight=lines[0].split(" ")
    del lines[0]
    for x in range(len(items)):
        items[x]=int(items[x])
        weight[x]=int(weight[x])
        bestitems.append(items[x]/weight[x])
    w=weight
    i=items
    b=bestitems
    for x in range(len(bestitems)):
        if(sum(tempweight)+w[b.index(max(b))]==maxweight):
            tempweight.append(w[b.index(max(b))])
            tempmoney+=i[b.index(max(b))]
            break
        if(sum(tempweight)+w[b.index(max(b))]<maxweight):
            tempweight.append(w[b.index(max(b))])
            tempmoney+=i[b.index(max(b))]
            del w[b.index(max(b))]
            del i[b.index(max(b))]
            del b[b.index(max(b))]
        else:
            del w[b.index(max(b))]
            del i[b.index(max(b))]
            del b[b.index(max(b))]
    print(tempmoney)