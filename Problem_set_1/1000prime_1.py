# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 12:20:58 2022

@author: Asus
"""
from math import *

#finds the 1000th prime
p=3; #inicializa el primer primo
primes=[2];
counter=1
isprime=True
while True:
    for i in range(3,ceil(sqrt(p))+1,2):
        if p%i==0 and i!=p:
            #print(p)
            isprime=False
            #print("%d No es primo" % p)
            continue
    if isprime:
        primes.append(p)
        counter+=1;
        p+=2
        isprime=True
    else:
        p+=2
        isprime=True
    if counter==10:
        break
print(primes)
print(primes[9])


def isThisNumPrime(N):
    from math import ceil,sqrt
    if N==2:
        return True
    isprime=True
    for i in range(3,ceil(sqrt(N))+1,2):
        if N%i==0 and i!=N:
            isprime=False
    return isprime

def sumLogPrimesTill(N):
    #adds the log of the primes til' N
    p=3; #inicializa el primer primo
    primes=[2];
    acum=log(2)
    isprime=True
    while True:
        for i in range(3,ceil(sqrt(p))+1,2):
            if p%i==0 and i!=p:
                #print(p)
                isprime=False
                #print("%d No es primo" % p)
                continue
        if p>N:
            return primes, acum, N/acum
            break
        if isprime:
            primes.append(p)
            acum+=log(p);
            p+=2
            isprime=True
        else:
            p+=2
            isprime=True
            
import matplotlib.pyplot as plt

ratios=[]
Ns=[]
for i in range(1,10000,2):
    primes, acum, ratio=sumLogPrimesTill(i)
    ratios.append(ratio)
    Ns.append(i)
    
plt.plot(Ns,ratios)
    
    

    
    

       
            
        
            
