# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 04:38:03 2020

@author: aniru
"""


s = input("Input:" )

#Submit from the line below.
vowels = ['a', 'e', 'i', 'o', 'u']

nvowels = 0

lno = 0

for letter in s:
    for vowel in vowels:
        if letter == vowel:
            nvowels += 1
            
print("Number of vowels:", nvowels)