# -*- coding: utf-8 -*-
"""
Created on Wed May 23 08:37:03 2018

@author: Ashutosh
"""

#function
def login(b):
    
    if(b=='admin'):
        print("you are admin you have these rights")
        print('1.update details')
        print('2.')
        
    elif(b=='student'):
        print("you are student you have these rights")
    
    elif(b=='faculty'):
        print("you are faculty you have these rights")
        
    else:
        print("No such type of user...")



#function
def newuser():
    n=input("\nEnter name:")
    phno=input("Enter phone number:")
    uname=input("Enter username:")
    email=input("Enter email:")
    passw1=input("Enter password:")
    passw2=input("Enter password Again:")
    

    if(passw1==passw2):
        with open('E:\\Games\\Internship\\python\\git\\m.txt','a+') as fp:
            fp.writelines('\n')
            fp.writelines(n+'\n')
            fp.writelines(phno+'\n')
            fp.writelines(uname+'\n')
            fp.writelines(email+'\n')
            fp.writelines(passw1+'\n')
            fp.writelines('\n')
        fp.close()
        print("Registered Sucessfully.......")
    else:
        print("Password dosent match re-enter your details...")
        newuser()
        


#function        
def euser():
    u=input("\nEnter username or email:")
    p=input("\nEnter password:")
    ty=input("\nUser Type(admin/student/faculty):")
    
    fp = open('E:\\Games\\Internship\\python\\git\\m.txt')
    lines = fp.read().split("\n") # Create a list containing all lines
    fp.close()
    #print(lines)
    i=int(3)
    j=int(5)
    l=0
    #for i in range(0,len(lines)):
    while(i<len(lines)):
        if(u==lines[i] and p==lines[j]):
            #print("You Rocked......")
            l=0
            break
        
        else:
            l=1
        i=i+7
        j=i+2     
            
        
            
    if l==0:
        print("You Rocked ...")
        print("Sucessfully login.....")
        print("Hello "+lines[i-2]+" How can i help you.....")
        login(ty)
        
        
        
    else:
        print("Try again later...")
            
   
print("---------------------Management system-------------------------------")
fp=open("E:\\Games\\Internship\\python\\git\\m.txt","w")
fp.write("--------------Management System-----------------")
fp.close()

print("Choose option::")

t='Y'
while(t.upper()=='Y'):
    print("\n1.New User\n2.Existing user")
    ch=int(input())
    if(ch==1):
        #print("Under construction")
        newuser();
        t=input("Do you want to continue(Y/N)")
    elif(ch==2):
        #print("Under construction")
        euser()
        t=input("Do you want to continue(Y/N)")
    else:
        print("Wrong choice")
        t=input("Do you want to continue(Y/N)")




        