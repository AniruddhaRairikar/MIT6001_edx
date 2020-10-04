# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:10:54 2020

@author: aniru
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    def spec_poly(x):
        
        opNums = 0
        
        for numIter in range(0, len(L)):
            k = (len(L)-1) - numIter 
            opNums += (L[numIter] * (x**k))
        
        return opNums
    
    return spec_poly

#testCase:
L = [1, 2, 3, 4]

print(general_poly(L)(10))