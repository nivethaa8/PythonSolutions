#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 23:56:17 2020

@author: nivethaanesarajah
"""

#Initialize variables
r=0.04
semi_annual_period = 0.07
total_cost = 1000000
portion_down_payment = (0.25*(total_cost))
annual_salary = 150000
monthly_salary = (annual_salary)/12
epsilon = 100.00
current_savings_for_down_payment = 0
month = 0
num_of_guess = 0 

#First Guess and Associated Calculations
low=0.0
high=10000
guess=low
saving_rate = ((guess/10000))
yearly_saved_for_down_payment = (saving_rate)*(annual_salary)
monthly_salary_saved_for_down_payment = (yearly_saved_for_down_payment)/12
ROI_for_down_payment = monthly_salary_saved_for_down_payment * (r/12)
current_savings_for_down_payment  =  current_savings_for_down_payment + monthly_salary_saved_for_down_payment  + ROI_for_down_payment
month=1
num_of_guess=1

#First Guess and Associated Calculations Print
print("iteration 1 start")
print(month)
print(num_of_guess)
print(yearly_saved_for_down_payment)
print(monthly_salary_saved_for_down_payment)
print(ROI_for_down_payment)
print(current_savings_for_down_payment)
print("iteration 1 end")


def func (saving_rate):
    global current_savings_for_down_payment

    saving_rate = ((guess/10000))
    yearly_saved_for_down_payment = saving_rate * annual_salary
    monthly_salary_saved_for_down_payment = (yearly_saved_for_down_payment)/12
    ROI_for_down_payment = current_savings_for_down_payment  * (r/12)      
    current_savings_for_down_payment = current_savings_for_down_payment + monthly_salary_saved_for_down_payment  + ROI_for_down_payment
    
    print("Saving rate: ", saving_rate)
    print("yearly_saved_for_down_payment:", yearly_saved_for_down_payment)
    print("monthly_salary_saved_for_down_payment", monthly_salary_saved_for_down_payment)
    print("ROI_for_down_payment", ROI_for_down_payment)
    print("current_savings_for_down_payment", current_savings_for_down_payment)
    
    return current_savings_for_down_payment

     
#Bisection Search
while ((current_savings_for_down_payment - portion_down_payment) != epsilon):
    month=month+1
    print("month: ", month)
    
    if (month > 36):
        print("Not Possible")
        break
    
    elif (month <=36):    
         
        if ((month%6)==0):  
            print("divisible")
            annual_salary = annual_salary * (1+(semi_annual_period))
            continue
            
        if (func(guess) < portion_down_payment):
            low=guess
            print("func(guess) less than portion_DP, new current func(guess): ")
            print(func(guess))
            print("new low")
            print(low)
            
        elif (func(guess) > portion_down_payment):
            high=guess
            print("func(guess) greater than portion_DP, new current func(guess): ")
            print(func(guess))
            print("new high: ")
            print(high)
            
        guess = (high+low)/2.0
        
        print("new guess")
        print(guess)
        num_of_guess=num_of_guess+1
        print("Num of guess")
        print(num_of_guess)


            

print("END")
print ("Number of months %d" % (month))
print ("Best Saving Rate %f" % float((guess)/(10000)))
print("Steps in bisection search %d" % (int(num_of_guess)))



    
        