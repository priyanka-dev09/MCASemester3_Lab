# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 15:14:23 2026

@author: CSD
"""

list1 = [1,2,3,4,5]
list2= [9,8,7,6]

n = max(len(list1),len(list2))

for i in range(n):
    if i < len(list1):
        a=list1[i]
        
    else:
        a="None"
        
    if i <len(list2):
        b=list2[len(list2)-1-i]
        
    else:
        b="None"
        
    print(a,b)
        
    
    
    
    
    