# -*- coding: utf-8 -*-
"""
Created on Mon May 21 08:25:52 2018

@author: Ashutosh
"""
a=691111111111.66
print(type(a))
t='Y'

fp=open("E:\\Games\\Internship\\python\\git\\ch.txt","w")
fp.write("108")
fp.close()

while(t.upper()=='Y'):
    print("Choose your operation:")
    print("\n1.BMI calculator\n2.currency converter\n3.calculator\nEnter choice:")
    ch=int(input())
    if(ch==1):
        h=int(input("Enter your height(in meter):"))
        w=int(input("Enter your weihght:"))
        print("Your BMI sucessfully store in bmi.txt file...")
        fp=open("E:\\Games\\Internship\\python\\git\\bmi.txt","w")
        fp.write(str(((h*h)/w)))
        fp.close()

        
        
    elif(ch==2):
        print("Currency converter::: your input is taken from the file:")
       
        fp = open('E:\\Games\\Internship\\python\\git\\ch.txt')
        lines = fp.read().split("\n")
        fp.close()
        print("\nRead from file:"+lines[0]+"\n")
        
        
        print("\nEnter the choice into which you want to convert:\n1.Rupee\n2.Dollar\n 3.Euro")
        cho=int(input())
        if(cho==1):
            print(float(lines[0]))
        elif(cho==2):
            
            print(float(lines[0])/61.06)
        elif(cho==3):
            print(float(lines[0])/79.88)
        else:
            print("Wrong choice...")
            
    elif(ch==3):
            a=input("Enter the first input:")
            b=input("\nEnter the second input:")
            c=input("\nSelect Operation (+,-,*,/):")
            if(c=='+'):
                print(int(a)+int(b))
            elif(c=='-'):
                print(int(a)-int(b))
            elif(c=='*'):
                print(int(a)*int(b))
            elif(c=='/'):
                print(int(a)/int(b))   
            else:
                print("Wrong input") 
        
        
        
    else:
        print("Wrong choice....Try again......")
    
    
    t=input('Do you want to continue(Y/N):')
    
    