# -*- coding: utf-8 -*-
"""
Created on Tue May 15 08:39:16 2018

@author: Ashutosh
"""
                    """----------------Day 1-------------------"""

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
        
                    """----------------Day 2-------------------"""
                  
def fun():
    print("Hello")
    a=int(input("Enter element"))
    print(a*a)

fun() 

l=[123,1,33]
max(l)



a=[1,2]

while(1):
    print("Enter the operation \n")
    c=input()
    if(c=='1'):
        b=input("Enter element to append")
        a.append(b)
    if(c=='2'):
        b=input("Enter element index to remove")
        a.remove(b)
    else:
        break 
    
print(a)    
    

                  """---------------------Day 3----------------"""


#list 
l=[40,50,20,33]
for i in l:
    print (i)
l.append(10) 

#updating the tuple in a different manner   
l1=[]
t1=(10,20,30,11,"Ash,2.2")
for i in t1:
    if(i==20):
        l1.append(200)
    else:    
        l1.append(i)
print(t1)    
del t1
t1=(l1)
print(t1)    



#dictonary
st={"name":[1,2]}   
print(st["name"][0])
    
#updating list inside tuple    
t1=([1,2,3],10,20)
t1[0].append(10)
print(t1)




                  """---------------------Day 3----------------"""
"""
File handling

modes-->   for read = r,r+,rb,rb+
           for write = w,w+,wb,wb+ 
"""   

fo = open("E:\\Games\\Internship\\python\\A.txt", "w")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)

fo.write( "Python is a great language.\nYeah its great!!\n");
fo.close()


fo = open("E:\\Games\\Internship\\python\\A.txt", "r+")
a=fo.tell()
print(a)
str = fo.read()
print ("Read String is : ", str)
fo.close()                 


    











