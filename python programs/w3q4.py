# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:03:51 2026

@author: CSD
"""

s = input("enter string: ")
for i in range(len(s)):
    if i%2==0:
        print(s[i],end=" ")
        