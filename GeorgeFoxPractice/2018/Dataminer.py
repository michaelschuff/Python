#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 22:13:29 2019

@author: eatdacarrot
"""
import os
path="/Users/eatdacarrot/ComputerScience/PythonSpyder/GeorgeFoxPractice/2018/"
file=open(os.path.join(path+"Dataminerinput.txt"),"r")
lines=file.read().splitlines()
del lines[0]
for x in lines:
    x=x.split("p:")[1]
    x=x.split(":p")[0]
    print(x)