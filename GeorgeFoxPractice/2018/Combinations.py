#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 23:23:03 2019

@author: eatdacarrot
"""

def count(coins,coincount,target):
    if(target==0):
        return(1)
    if(target<0 or coincount<0):
        return(0)
    return(count(coins,coincount-1,target)+count(coins,coincount,target-coins[coincount-1]))

import os
path="/Users/eatdacarrot/ComputerScience/PythonSpyder/GeorgeFoxPractice/2018/"
file=open(os.path.join(path+"Combinationsinput.txt"),"r")
lines=file.read().splitlines()
datasets=int(lines[0])
del lines[0]
for x in range(datasets):
    target=int(lines[0].split(" ")[0])
    del lines[0]
    coins=lines[0].split(" ")
    del lines[0]
    for x in range(len(coins)):
        coins[x]=int(coins[x])
    print(count(coins,len(coins),target)-1)