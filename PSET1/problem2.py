# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:14:09 2020

@author: aniru
"""


s = input("Input:")

#Submit from the line below

times = 0

for let in range(len(s)):
    if (s[let : let + 3] == "bob"):
        times += 1
        
        
print ("Number of times bob occurs is: ", times)