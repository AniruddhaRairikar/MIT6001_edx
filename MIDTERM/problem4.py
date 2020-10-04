# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:37:06 2020

@author: aniru
"""


def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    
    # Your code here
    for lst in L:
        lst.reverse()
    L.reverse()
    

#CORRECT