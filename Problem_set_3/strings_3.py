# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 01:13:58 2022

@author: Asus
"""
def countSubStringMatch(target, key):
    indexes=[]
    start=0
    idx=0
    idx=target.find(key,start)
    if idx==-1:
            return idx
    else:
        while start<len(target):
            idx=target.find(key,start)
            if idx==-1:
                return indexes
            indexes.append(idx)
            start=idx+len(key)    
        return indexes


def countSubStringMatchRecursive(target, key,acum=[]):
    idx=target.find(key)
    if idx==-1:
        return len(acum)
    else:
        acum.append(idx)
        #print(idx)
        #print("se encontro el key")
        return countSubStringMatchRecursive(target[(idx+len(key)):],key,acum)
    
target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'
#and four key strings:
key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

countSubStringMatchRecursive(target2,key11,[]) #count recursively
