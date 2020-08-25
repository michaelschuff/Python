#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 14:18:06 2019

@author: eatdacarrot
"""
import os
path ="/Users/eatdacarrot/ComputerScience/PythonSpyder/GeorgeFoxPractice/2019"
file = open(os.path.join(path+"Drawinput.txt"),"r")
lines = file.read().splitlines()
line1=lines[0].split(" ")
circlex,circley,circleradius=int(line1[0]),int(line1[1]),int(line1[2])/2
del lines[0]
line1=lines[0].split(" ")
rectx,recty,rectw,recth=int(line1[0]),int(line1[1]),int(line1[2]),int(line1[3])
del lines[0]
for x in lines:
    y=x.split(" ")
    y[0],y[1]=int(y[0]),int(y[1])
    if((((y[0]-(circlex+circleradius))**2)+((y[1]-(circley+circleradius))**2))**.5<=circleradius):
        print("circle")
    elif(y[0]>=rectx and y[0]<=rectx+rectw and y[1]>=recty and y[1]<=recty+recth):
        print("rectangle")
    else:
        print("neither")