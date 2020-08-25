#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 20:19:46 2019

@author: eatdacarrot
"""

import os
path="/Users/eatdacarrot/ComputerScience/PythonSpyder/GeorgeFoxPractice/2019"
file=open(os.path.join(path+"OCRinput.txt"),"r")
lines=file.read().splitlines()
loop=int(lines[0])
del lines[0]
for x in range(0,loop*2,2):
    points=0
    a=[]
    b=[]
    for y in range(8):
        a.append(list(lines[0]))
        del lines[0]
    for y in range(8):
        b.append(list(lines[0]))
        del lines[0]
    for y in range(8):
        for z in range(8):
            if(b[y][z]!=a[y][z]):
                points+=1
    if(points<3):
        print("yes")
    else:
        print("no")