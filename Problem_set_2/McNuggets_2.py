# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 12:21:35 2022

@author: Asus
"""
#Diophanes equation for mcnuggets

#you can only get packages for 6 9 and 20 mcnuggets

#6a+9b+20c=m m is the total of mcnuggts

#51, 52, 53,54,55 mcnugets is it possible?
from math import *
def isThisNumPrime(N):
    from math import ceil,sqrt
    if N==2:
        return True
    elif N%2==0:
            return False
    isprime=True
    for i in range(3,ceil(sqrt(N))+1,2):
        if N%i==0 and i!=N:
            isprime=False
    return isprime

def mcNuggets(N,a,b,c): #you can't make 43 nuggets, but you can make any number above or equal to 44.
    acum=0
    e=N**2;#number of iterations
    while True:
        #start with a=1,
        for i in range(ceil(N/a)+1):
            for j in range((ceil(N/b)+1)):
                for k in range((ceil(N/c)+1)):
                    if (a*i)+(b*j)+(c*k)==N:
                        print([i,j,k], i*a+j*b+k*c)
                        return True
                    elif acum>=e:
                        print("se alcanzó el número máximo de iteraciones")
                        print(("no es posible tener %d mcnuggets" % N))
                        return False
                    else:
                        acum+=1
                    

def maxMcNuggets(a,b,c): #you can't make 43 nuggets, but you can make any number above or equal to 44.
    seguidos=0
    i=1
    while True:
        if mcNuggets(i,a,b,c):
            seguidos+=1
            if seguidos==a:
                return "si los paquetes son de %d, %d y %d, el número máximo de mcNouggets que no pueden comprarse exactamente es %d" % (a,b,c,i-a)
            i+=1
        else:
            seguidos=0
            i+=1
            
            
        
        
            
        