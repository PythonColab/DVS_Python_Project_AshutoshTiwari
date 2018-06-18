# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 06:19:59 2018

@author: Ashutosh
"""


# fetch the data from database
import pymysql
conn=pymysql.connect(host='localhost',user='root',password='',db='pyfirst')

a=conn.cursor() #go through with the context of database
sql='select * from pytone;'
a.execute(sql)

countrow=a.execute(sql)
print("No. of rows:",countrow)

#data=a.fetchall()
data=a.fetchmany(1)
print (data)

conn.commit()    
conn.close()      




#create table in database

import pymysql
conn=pymysql.connect(host='localhost',user='root',password='',db='pyfirst')

a=conn.cursor() #go through with the context of database

a.execute(""" create table new
          (
           id int primary key,
           name varchar(20),
           description varchar(100)
          )
""")
          
conn.commit()    
conn.close()      

#insert(uncomment the line) , delete(uncomment the line),update data into database


import pymysql
conn=pymysql.connect(host='localhost',user='root',password='',db='pyfirst')

a=conn.cursor()

#a.execute(""" insert into new values(1,'Ashutosh','He is ....')""")
#print("data inserted") 

#a.execute("delete from new where id=2")
#print("Data deleted")

#you can update the table in this same manner using cursour

         
conn.commit()    
conn.close()  



  
