#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 23:20:42 2019

@author: eatdacarrot
"""

import os
path="/Users/eatdacarrot/ComputerScience/PythonSpyder/GeorgeFoxPractice/2018/"
file=open(os.path.join(path+"Areasinput.txt"),"r")
lines=file.read().splitlines()
del lines[0]
for x in lines:
    x=x.split(" ")
    print(round(float(x[0])*float(x[1]),2))