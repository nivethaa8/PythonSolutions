#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:55:10 2020

@author: nivethaanesarajah
"""
r=0.04

current_savings_for_down_payment = 0
month = 0

total_cost = float (input("Enter the cost of your dream home: "))
portion_down_payment = float(0.25*(total_cost))

annual_salary = float(input("Enter your annual salary: "))
monthly_salary = (annual_salary)/12
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

#first month

monthly_salary_saved_for_down_payment = (portion_saved)*(monthly_salary)

ROI_for_down_payment = monthly_salary_saved_for_down_payment  * (r/12)

current_savings_for_down_payment  =  current_savings_for_down_payment + monthly_salary_saved_for_down_payment + ROI_for_down_payment 

month=month+1
    
    
while current_savings_for_down_payment < portion_down_payment:
    
    monthly_salary_saved_for_down_payment = (portion_saved)*(monthly_salary)
    ROI_for_down_payment = current_savings_for_down_payment  * (r/12)
    current_savings_for_down_payment  =  current_savings_for_down_payment + monthly_salary_saved_for_down_payment + ROI_for_down_payment 
    month=month+1
    
print (" \n Number of months %d" % (month))












