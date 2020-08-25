#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:23:17 2019

@author: eatdacarrot
"""

import os
from math import sqrt
path="/Users/eatdacarrot/ComputerScience/PythonSpyder/GeorgeFoxPractice/2018/"
file=open(os.path.join(path+"Quadraticsinput.txt"),"r")
lines=file.read().splitlines()
del lines[0]
for x in lines:
    x=x.split(" ")
    print(round((-float(x[1])+sqrt(float(x[1])**2-4*float(x[0])*float(x[2])))/(2*float(x[0])),3),", ",end="",sep="")
    print(round((-float(x[1])-sqrt(float(x[1])**2-4*float(x[0])*float(x[2])))/(2*float(x[0])),3))