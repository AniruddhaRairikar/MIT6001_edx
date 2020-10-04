# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 08:39:35 2020

@author: aniru
"""

# Logic number 1 : Convert characters into ascii and check if the subsequent
# character's ascii output is bigger. Continue till the chain breaks.

s = "barackobama"

#Submit from below.
final = s[0]
holder = final

for al in range(1, len(s)):
    if s[al] >= holder[-1]:
        holder += s[al]
        if len(holder) > len(final):
            final = holder
    else:
        holder = s[al]
            
print("Longest substring in alphabetical order is: " + final)