import mysql.connector
from datetime import datetime


def addfunct():
    connection = mysql.connector.connect(
        host="localhost",port="3306",user="root",password="password",database='IotPersonDb'
    )
    empid=int(input("Enter the employee id"))
    name=input("Enter the name of employee")
    department=input("Enter the dept")
    email=input("enter emailid")
    salary=float(input("Enter the salary"))
    year=int(input("Enter year"))
    month=int(input("Enter month"))
    day=int(input("Enter day"))
    hrs=int(input("Enter hrs"))
    min=int(input("Enter min"))
    sec=int(input("Enter sec"))
    date_of_joining= datetime(year, month, day, hrs, min, sec)

    query=f"insert into employee(empid,name,dept,email,salary,date_of_joining) value({empid},'{name}','{department}','{email}',{salary},'{date_of_joining}');"

    cursor=connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()


#addfunct()


def deletefunction():
  connection = mysql.connector.connect(
        host="localhost",port="3306",user="root",password="password",database='IotPersonDb'
    )
  empid=int(input("Enter user id to delete"))
  query=f"delete from employee where empid= {empid}"
  cursor=connection.cursor()
  cursor.execute(query)
  connection.commit()
  cursor.close()
  connection.close()

#deletefunction()

def updatefunct():
   connection = mysql.connector.connect(
        host="localhost",port="3306",user="root",password="password",database='IotPersonDb'
    )
   empid=int(input("Enter employee id to update"))
   name=input("Enter the name to update")
   query=f"update employee SET name = '{name}' where empid={empid}"
   cursor=connection.cursor()
   cursor.execute(query)
   connection.commit()
   cursor.close()
   connection.close()
#updatefunct()

print("1. add in the query\n2. delete in the query\n3. update in the query")
choice=int(input("Enter a choice"))
while choice !=0:
  if choice ==1:
   addfunct()
  elif choice ==2:
   deletefunction()
  elif choice==3:
   updatefunct()
  else:
   print("Invalid Choice entered")