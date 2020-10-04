# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:22:49 2020

@author: aniru
"""


def finalBalance(balance, annualInterestRate, trialPayment):
    m_IntRate = annualInterestRate / 12.0
    for j in range(12):
        monthlyUnpaidBalance =  balance - trialPayment
        balance = monthlyUnpaidBalance + (m_IntRate * monthlyUnpaidBalance)
    return balance 

m_IntRate = annualInterestRate / 12.0
ubound = (balance * (1 + m_IntRate)**12) / 12.0

nconv = True

lbound = balance / 12.0
fin_bal_2 = finalBalance(balance, annualInterestRate, lbound)

TrialPayment = (ubound + lbound) / 2
shot = finalBalance(balance, annualInterestRate, TrialPayment)

fin_bal_3 = finalBalance(balance, annualInterestRate, ubound)

while nconv == True:
    if (ubound - lbound) < 0.002:
        nconv = False
    if shot < 0:
        ubound = TrialPayment
    if shot > 0:
        lbound = TrialPayment
    
    fin_bal_2 = finalBalance(balance, annualInterestRate, lbound)

    TrialPayment = (ubound + lbound) / 2
    shot = finalBalance(balance, annualInterestRate, TrialPayment)
    
    fin_bal_3 = finalBalance(balance, annualInterestRate, ubound)
    
print ("Lowest Payment: " + str(round(TrialPayment, 2)))