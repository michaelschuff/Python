#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 15:15:24 2019

@author: eatdacarrot
"""

import os
path ="/Users/eatdacarrot/ComputerScience/PythonSpyder/GeorgeFoxPractice/2019"
file = open(os.path.join(path+"Vowelinput.txt"),"r")
lines = file.read().splitlines()
del lines[0]
vowels = ['a','e','i','o','u']

for w in lines:
    l=w.split(" ")
    a=l[0]
    b=l[1]
    aVowel = False
    bVowel = False
    andNumBin = []
    orNumBin = []
    xorNumBin = []
    
    for x in range(len(a)):
      andNumBin.append(0)
      orNumBin.append(0)
      xorNumBin.append(0)
      for y in range(5):
        if(a[x] == vowels[y]):
          aVowel = True
        if(b[x] == vowels[y]):
          bVowel = True
      if(aVowel and bVowel):
        andNumBin[x] = 1
        orNumBin[x] = 1
      elif(aVowel != bVowel):
        orNumBin[x] = 1
        xorNumBin[x] = 1
      aVowel = False
      bVowel = False
    andNum = 0
    orNum = 0
    xorNum = 0
    for x in range (len(a)):
      andNum += (andNumBin[len(a) - x - 1] * (2**x))
    print(andNum,end=" ")
    for x in range (len(a)):
      orNum += (orNumBin[len(a) - x - 1] * (2**x))
    print(orNum,end=" ")
    for x in range (len(a)):
      xorNum += (xorNumBin[len(a) - x - 1] * (2**x))
    print(xorNum)