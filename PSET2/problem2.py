# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:16:36 2020

@author: aniru
"""


def finalBalance(balance, annualInterestRate, trialPayment):
    monthlyInterestRate = annualInterestRate / 12.0
    
    for j in range(12):
        monthlyUnpaidBalance =  balance - trialPayment
        balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    return balance 

lbound = balance / 12.0

rlbound = round(lbound, -1)

fin_bal = finalBalance(balance, annualInterestRate, rlbound)

while fin_bal > 0:    
    fin_bal = finalBalance(balance, annualInterestRate, rlbound)
    if fin_bal > 0:
        rlbound = rlbound + 10

print ("Lowest Payment: " + str(rlbound))