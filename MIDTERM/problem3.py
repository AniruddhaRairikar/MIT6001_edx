# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:23:37 2020

@author: aniru
"""

# Equation: a1 * x1^2 + b1 * x1 + c1 + a2 * x2^2 + b2 * x2 + c2


def evalQuadratic(a, b, c, x):
   '''
   a, b, c: numerical values for the coefficients of a quadratic equation
   x: numerical value at which to evaluate the quadratic.
   '''
   return a*x*x + b*x + c


def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
  # Your code here
    print((evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2, c2, x2)))
    
    
#testcase:
twoQuadratics(2, 5, 3, 2, 2, 5, 3, 2)


#CORRECT