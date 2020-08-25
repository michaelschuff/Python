#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 15:06:25 2019

@author: eatdacarrot
"""
from math import *
import os
path ="/Users/eatdacarrot/ComputerScience/PythonSpyder/GeorgeFoxPractice/2019"
file = open(os.path.join(path+"Fenceinput.txt"),"r")
lines = file.read().splitlines()
del lines[0]
for x in lines:
    l=x.split(" ")
    print(ceil(int(l[0])*int(l[1])*2/150))