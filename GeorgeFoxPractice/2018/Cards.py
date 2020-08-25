#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:38:05 2019

@author: eatdacarrot
"""

import os
path="/Users/eatdacarrot/ComputerScience/PythonSpyder/GeorgeFoxPractice/2018/"
file=open(os.path.join(path+"Cardsinput.txt"),"r")
lines=file.read().splitlines()
numbers=["0","1","2","3","4","5","6","7","8","9"]
del lines[0]
for x in lines:
    cards=0
    x=list(x)
    for y in x:
        if(y not in numbers):
            cards+=1
    print(52-cards)