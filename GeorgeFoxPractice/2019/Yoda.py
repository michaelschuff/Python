#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:45:32 2019

@author: eatdacarrot
"""

import os
path ="/Users/eatdacarrot/ComputerScience/PythonSpyder/GeorgeFoxPractice/2019"
file = open(os.path.join(path+"Yodainput.txt"),"r")
lines = file.read().splitlines()
del lines[0]
for x in lines:
    l=x.split(" ")
    l.append(l[0])
    l.append(l[1])
    del l[0]
    del l[0]
    for y in l:
        print(y," ",end="")
    print()