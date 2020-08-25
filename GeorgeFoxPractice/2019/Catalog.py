#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:50:23 2019

@author: eatdacarrot
"""

import os
path ="/Users/eatdacarrot/ComputerScience/PythonSpyder/GeorgeFoxPractice/2019"
file = open(os.path.join(path+"Cataloginput.txt"),"r")
lines = file.read().splitlines()
del lines[0]
a=lines
a.sort()
n=[]
for x in lines:
    l=x.split(" ")
    n.append(int(l[len(l)-1]))
n.sort()
for x in n:
    for y in lines:
        l=y.split(" ")
        if(int(l[len(l)-1])==x):
            print(y)
print()
for x in a:
    print(x)
    