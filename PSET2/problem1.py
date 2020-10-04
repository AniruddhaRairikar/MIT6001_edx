# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:13:46 2020

@author: aniru
"""


monthlyInterestRate = annualInterestRate / 12.0

for j in range(12):
    minPayment = balance * monthlyPaymentRate
    monthlyUnpaidBalance = balance - minPayment
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

print ("Remaining balance: " + str(round(balance, 2)))