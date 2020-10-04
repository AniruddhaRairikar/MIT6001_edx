# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:04:57 2020

@author: aniru
"""

#testCase:

t = (1112, (499, 21, 6, -1, 27), [9, 6000, [430, 6907]])

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t 
    """ 
    # Your code here
    v = []
    for i in t:
        if type(i) == int:
            v.append(i)
        else:
            v.append(max_val(i))

    return max(v)

print(max_val(t))