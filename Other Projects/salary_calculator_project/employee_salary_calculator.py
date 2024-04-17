# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 17:40:36 2023

@author: leste
"""
import micropip
micropip.install("pandas") 
import pandas as pd
import sqlite3 as sql

#Connecting to employee database
employees_db = sql.connect('employee_database.db')
empl_cur = employees_db.cursor()
employee_info = pd.read_sql_query('SELECT empl_id, first_name, last_name FROM Employees', employees_db)
employee_info.index = employee_info['empl_id']

def employee_name(emplid):
    '''Finding corresponding name for emplid'''
    for index, row in employee_info.iterrows():
        if emplid == row['empl_id']:
            return str(row['first_name']) + ' ' + str(row['last_name'])
            

#Payroll for annual and biweekly overview

                                                #wages annual
def annual_regulartime(r, h = 40):
    '''calculates gross annual pay for 40 hour work week'''
    return((h*r)*2)*26

def annual_overtime(h,r):
    '''calculates overtime or reduction 
        if work week is less than 40 hours'''
    if h >= 40:
        return(((h-40)*(r*1.5))*2)*26
    else:
        return(((h-40)*r)*2)*26

def annual_salary(h,r):
    '''calculates total gross annual pay, including overtime or reduction'''
    return annual_regulartime(r)+ annual_overtime(h,r)

def wages_annual_total(h,r):
    '''returns gross annual pay with breakdown'''
    if h >= 40:
        wage = annual_salary(h,r)
        regular_time = annual_regulartime(r)
        over_time = annual_overtime(h,r)
        print(f'''Wages total accum: ${wage}
                Regular Time: ${regular_time}
                Overtime: ${over_time}
                
                  ''')      
                
    else:
        wage = annual_salary(h,r)
        regular_time = annual_regulartime(r) + annual_overtime(h,r)
        print(f'''Wages total accum: ${wage}
                Regular Time: ${regular_time}
                
                  ''')     
                
    
                                                #wages biweekly

def regulartime (r, h = 40):
    '''calculates gross biweekly pay for 40 hour work week'''
    return h * r
    
def overtime (h,r):
    '''calculates overtime or reduction 
        if work week is less than 40 hours'''
    if h>= 40:
        return (h-40)*(r*1.5)
    else:
        return(h-40)*r

def biweekly_pay(h,r):
    '''calculates total gross biweekly pay, including overtime or reduction'''
    return (regulartime(r) + overtime(h,r)) * 2 

def wages_total (h,r):
    '''returns gross biweekly pay with breakdown'''
    if h >= 40:
        wage = biweekly_pay(h,r)
        regular_time = regulartime(r)*2
        over_time = overtime(h,r)*2
        print(f'''Wages total accum: ${wage}
                Regular Time: ${regular_time}
                Overtime: ${over_time}
                
                  ''')         
    else:
        wage = biweekly_pay(h,r)
        regular_time = regulartime(r)*2 + overtime(h,r)*2
        print(f'''Wages total accum: ${wage}
                Regular Time: ${regular_time}
                
                  ''')         
    
              

        
                                                #deductions annual 

def ann_state_taxes(wage):
    '''calculates total state taxes'''
    return wage*0.06
    
def ann_retirement_funds(wage, overtime):
    '''calculates total retirement withholding'''
    if overtime > 0:
        return (wage-overtime)*0.045
    else:
        return (wage)*0.045
        
    
def ann_uniondues(wage, union):
    '''calculates total union dues'''
    if union == True:
        return wage*0.01
    else:
        return wage*0
        
    
def ann_federal_taxes(wage):
    '''calculates federal taxes in brackets'''
    if wage >= 10276 and wage <= 41775:
        return wage*0.12
    elif wage >= 41776 and wage <= 89075:
        return wage*0.22
    elif wage >= 89076 and wage <= 170050:
        return wage*0.24
    elif wage >= 170051 and wage <= 215950:
        return wage*0.32
    else:
        raise ValueError('Invalid value. Please ensure your salary is correct')
        
def ann_soc_security(wage):
    '''calculates social security withholding'''
    if wage*0.062 <= 147000:
        return wage*0.062
    else:
        return 147000

def ann_medicaid_taxes(wage):
    '''calculates medicaid taxes'''
    if wage*0.0145 <= 147000:
        return wage*0.0145
    else:
        return 147000

def ann_deduction_total(wage, overtime, union):
    '''calculates total deductions for net pay calculation'''
    state_tax = ann_state_taxes(wage)
    federal_tax = ann_federal_taxes(wage)
    union_dues = ann_uniondues(wage, union)
    retirement = ann_retirement_funds(wage, overtime)
    medicaid = ann_medicaid_taxes(wage)
    social_security = ann_soc_security(wage)
    return state_tax+ federal_tax+ union_dues+ retirement+ medicaid+ social_security 
    
def ann_deductions(wage, overtime, union):
    '''returns all deductions and their values, rounded for display'''
    state_tax = round(ann_state_taxes(wage), 2)
    federal_tax = round(ann_federal_taxes(wage), 2)
    union_dues = round(ann_uniondues(wage, union), 2)
    retirement = round(ann_retirement_funds(wage, overtime), 2)
    medicaid = round(ann_medicaid_taxes(wage) , 2)
    social_security = round(ann_soc_security(wage), 2)
    total_deductions = round(ann_deduction_total(wage, overtime, union), 2)
    print(f'''Deductions: ${total_deductions}
                Union Dues: ${union_dues}
                Retirement fund: ${retirement}
                State taxes: ${state_tax}
                Federal taxes: ${federal_tax}
                Social Security: ${social_security}
                Medicaid: ${medicaid}
                
                ''')


    
                                        #deductions biweekly

def state_taxes(wage):
    '''calculates total state taxes'''
    return wage*0.06
    
def retirement_funds(wage, overtime):
    return (wage-overtime)*0.045
    
    
def uniondues(wage, union):
    '''calculates total union dues'''
    if union == True:
        return wage*0.01
    else:
        return wage*0
        
    
def federal_taxes(wage):
    '''calculates federal taxes in brackets for biweekly values'''
    if wage >= (10276/26) and wage <= (41775/26):
        return wage*0.12
    elif wage >= (41776/26) and wage <= (89075/26):
        return wage*0.22
    elif wage >= (89076/26) and wage <= (170050/26):
        return wage*0.24
    elif wage >= (170051/26) and wage <= (215950/26):
        return wage*0.32
    else:
        raise ValueError('Invalid value. Please ensure your salary is correct')
        
def soc_security(wage):
    '''calculates social security withholding for biweekly values'''
    if wage*0.062 <= (147000/26):
        return wage*0.062
    else:
        return (147000/26)

def medicaid_taxes(wage):
    '''calculates medicaid taxes for biweekly values'''
    if wage*0.0145 <= (147000/26):
        return wage*0.0145
    else:
        return (147000/26)

def deduction_total(wage, overtime, union):
    '''calculates total biweekly deductions for net pay calculation'''
    state_tax = state_taxes(wage)
    federal_tax = federal_taxes(wage)
    union_dues = uniondues(wage, union)
    retirement = retirement_funds(wage, overtime)
    medicaid = medicaid_taxes(wage)
    social_security = soc_security(wage)
    return state_tax+ federal_tax+ union_dues+ retirement+ medicaid+ social_security

def deductions(wage, overtime, union):
    '''returns all deductions and their biweekly values, rounded for display'''
    state_tax = round(state_taxes(wage), 2)
    federal_tax = round(federal_taxes(wage), 2)
    union_dues = round(uniondues(wage, union), 2)
    retirement = round(retirement_funds(wage, overtime), 2)
    medicaid = round(medicaid_taxes(wage) , 2)
    social_security = round(soc_security(wage), 2)
    total_deductions = round(deductions(wage, overtime, union), 2)
    print(f'''Deductions: ${total_deductions}
                Union Dues: ${union_dues}
                Retirement fund: ${retirement}
                State taxes: ${state_tax}
                Federal taxes: ${federal_tax}
                Social Security: ${social_security}
                Medicaid: ${medicaid}
                
                ''')
    
    
    
                                            #display code annual 
def net_pay_accum(emplid,r,h,union):
    '''calculates and displays net pay with details'''
    name = employee_name(emplid)
    print(f''' Employee ID: {emplid}
               Name: {name}
            ''')
    wages_annual_total(h,r)
    ann_deductions(annual_salary(h,r), annual_overtime(h,r),union)
    netpay = annual_salary(h,r) - ann_deduction_total(annual_salary(h,r), annual_overtime(h,r),union)
    print('Net pay accumulated: $', round(netpay,2 ))


                                            #display code biweekly
def net_pay_biweekly(emplid,r,h,union):
    '''calculates and displays biweekly net pay with details'''
    name = employee_name(emplid)
    print(f''' Employee ID: {emplid}
               Name: {name}
            ''')
    wages_total(h,r)
    deductions(biweekly_pay(h,r), overtime(h,r),union)
    netpay = biweekly_pay(h,r) - deduction_total(biweekly_pay(h,r), overtime(h,r),union)
    print('Net pay accumulated: $', round(netpay,2 ))    
    
    #final code
def annual_or_biweekly(emplid,r,h,union,timeframe):
    
    if emplid not in employee_info['empl_id'].values :
        raise ValueError('Employee ID not found in our system.')
    elif union != True and union != False:
        raise ValueError('Please use True or False for union input.')
    elif(type(r) != float and type(r) != int) or (type(h) != float and type(h) != int):
        raise ValueError('Hours and rates should be numeric values.')
        
    if timeframe == 'annual':
        return net_pay_accum(emplid,r,h,union)
    elif timeframe == 'biweekly':
        return net_pay_biweekly(emplid,r,h,union)
    else:
        raise ValueError('Please choose one of the two provided options')


annual_or_biweekly(102, 35, 40, True, 'biweekly')

employees_db.close()
                                                