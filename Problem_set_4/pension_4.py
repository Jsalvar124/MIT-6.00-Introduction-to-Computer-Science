# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 18:29:38 2022

@author: Asus
"""

# Problem Set 4
# Name: 
# Collaborators: 
# Time: 

#
# Problem 1
#

def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    # TODO: Your code here.
    fi=salary*save*0.01
    F=[fi]
    for i in range(1,years):
      fi=fi *(1 + 0.01 * growthRate) + salary * save * 0.01
      F.append(fi)
    return F

def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print (savingsRecord)
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    # TODO: Add more test cases here.


# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    # TODO: Your code here.
    
    
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    fi=salary*save*0.01
    F=[fi]
    for i in range(1,len(growthRates)):
      fi=fi*(1 + 0.01 * growthRates[i]) + salary * save * 0.01
      F.append(fi)
    return F
    
    
def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print(savingsRecord)
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.

#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    # TODO: Your code here.
# F[0] = savings * (1 + 0.01 * growthRates[0]) ??? expenses
# F[1] = F[0] * (1 + 0.01 * growthRates[1]) ??? expenses    
    
    fi=savings*(1 + 0.01 * growthRates[0])-expenses
    F=[fi]
    for i in range(1,len(growthRates)):
      fi=fi*(1 + 0.01 * growthRates[i])-expenses
      F.append(fi)
    return F
    
def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print(savingsRecord)
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.


# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    # TODO: Your code here.
    F1=nestEggVariable(salary, save, preRetireGrowthRates) #calcula ahorros totales de acuerdo a ingreso y tasa de crecimiento durante vida laboral
    savings=max(F1) #El valor del ahorro, es el acumulado del ??ltimo a??o. ambos valores son constantes, solo dependen del salario y de las tasas de crecimiento.
    expMax=savings+epsilon
    expMin=0
    expMid=(expMax+expMin)/2
    balance=min(postRetirement(savings, postRetireGrowthRates, expMid))
    while abs(balance)>epsilon:
        if balance>0: # if total is negative, average expenses is too low, solution is in the upper part of the space.
            expMin=expMid
            expMid=(expMax+expMin)/2
            balance=min(postRetirement(savings, postRetireGrowthRates, expMid)) #lo que se quiere averiguar es expenses, por lo que se debe iterar con un binary search.
        else: #average expense is too high, solution is in the lower part of the solution space.
            expMax=expMid
            expMid=(expMax+expMin)/2
            balance=min(postRetirement(savings, postRetireGrowthRates, expMid)) #lo que se quiere averiguar es expenses, por lo que se debe iterar con un binary search.
    return expMid, balance, savings
    

def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses,balance, savings = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print(expenses,balance,savings)
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.