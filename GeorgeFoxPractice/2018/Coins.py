#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:54:44 2019

@author: eatdacarrot
"""

import os
path="/Users/eatdacarrot/ComputerScience/PythonSpyder/GeorgeFoxPractice/2018/"
file=open(os.path.join(path+"Coinsinput.txt"),"r")
lines=file.read().splitlines()
datasets=int(lines[0])
del lines[0]
for x in range(datasets):
    coins=0
    money=0
    target=int(lines[0].split(" ")[0])
    del lines[0]
    coins=lines[0].split(" ")
    for y in range(len(coins)):
        coins[y]=int(coins[y])
    coins.sort()
    coins.reverse()
    del lines[0]
    while(money<target):
        if(money+coins[len(coins)-1]>target):
            print("not possible")
            break
        for y in coins:
            if(money+y==target):
                money+=y
                print("possible")
                break
            if(money+y<target):
                money+=y
                break