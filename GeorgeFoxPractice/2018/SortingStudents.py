#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 23:45:06 2019

@author: eatdacarrot
"""

import os
path="/Users/eatdacarrot/ComputerScience/PythonSpyder/GeorgeFoxPractice/2018/"
file=open(os.path.join(path+"SortingStudentsinput.txt"),"r")
lines=file.read().splitlines()
datasets=int(lines[0])
del lines[0]
for x in range(datasets):
    a=int(lines[0])
    del lines[0]
    b=[]
    c=[]
    for i in range(a):
        b.append(lines[0].split(" "))
        c.append(int(lines[0].split(" ")[1]))
        del lines[0]
    c.sort()
    c.reverse()
    for x in range(len(c)):
        c[x]=str(c[x])
        for y in range(len(b)):
            if(c[x]==b[y][1]):
                print(b[y][0],b[y][1])
    if(x!=datasets-1):
        print()