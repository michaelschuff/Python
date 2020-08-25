#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:44:12 2019

@author: eatdacarrot
"""

import os
path="/Users/eatdacarrot/ComputerScience/PythonSpyder/GeorgeFoxPractice/2018/"
file=open(os.path.join(path+"StarStudentinput.txt"),"r")
lines=file.read().splitlines()
datasets=lines[0]
del lines[0]
for x in range(int(datasets)):
    imax=0
    smax=""
    a=lines[0]
    del lines[0]
    for y in range(int(a)):
        if(int(lines[0].split(" ")[1])>imax):
            imax=int(lines[0].split(" ")[1])
            smax=lines[0].split(" ")[0]
        del lines[0]
    print(smax)