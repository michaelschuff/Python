#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 21:59:54 2019

@author: eatdacarrot
"""
import os
def solvemaze(x,y,maze,pathnum):
    directions=[[0,1],[1,0],[0,-1],[-1,0]]
    for d in directions:
        if(x+d[0]>=0 and x+d[0]<=19 and y+d[1]>=0 and y+d[1]<=19):
            if(maze[y+d[1]][x+d[0]]=="E"):
                pathnum+=1
                return(True,pathnum)
            if(maze[y+d[1]][x+d[0]]=="*"):
                pathnum+=1
                maze[y][x]="X"
                possible,pathnum=solvemaze(x+d[0],y+d[1],maze,pathnum)
                if(possible):
                    return(True,pathnum)
    return(False,pathnum-1)
path="/Users/eatdacarrot/ComputerScience/PythonSpyder/GeorgeFoxPractice/2018/"
file=open(os.path.join(path+"Lostinput.txt"),"r")
lines=file.read().splitlines()
datasets=int(lines[0])
del lines[0]
for x in range(datasets):
    pathnum=0
    size=int(lines[0].split(" ")[0])
    del lines[0]
    maze=[]
    for y in range(size):
        maze.append(list(lines[0]))
        del lines[0]
    for y in range(len(maze)):
        for z in range(len(maze)):
            if(maze[y][z]=="S"):
                startx=z
                starty=y
                maze[y][z]="*"
    a,pathnum=solvemaze(startx,starty,maze,pathnum)
    print(pathnum)