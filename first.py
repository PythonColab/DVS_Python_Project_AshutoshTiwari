# -*- coding: utf-8 -*-
"""
Created on Tue May 15 08:39:16 2018

@author: Ashutosh
"""
c=0

while(1):
    a=input()
    b=input()
    c=input()
    if(int(a)==0 & int(b)==0):
        break
    if(c=='+'):
        print(int(a)+int(b))
    if(c=='-'):
        print(int(a)-int(b))
    if(c=='*'):
        print(int(a)*int(b))
    if(c=='/'):
        print(int(a)/int(b))   
    else:
        print("Wrong input")         