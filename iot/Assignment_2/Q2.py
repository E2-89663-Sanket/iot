import mysql.connector

def disp_all():
   connection = mysql.connector.connect(
        host="localhost",port="3306",user="root",password="password",database='IotPersonDb'
    )
   query="select * from employee;"
   cursor=connection.cursor()
   cursor.execute(query)
   employee=cursor.fetchall()
   print(employee)
   cursor.close()
   connection.close()
   
disp_all()

def disp_dept():
   connection = mysql.connector.connect(
        host="localhost",port="3306",user="root",password="password",database='IotPersonDb'
    )
   dept=input("enter the dept")
   query=f"select * from employee where dept='{dept}';"
   cursor=connection.cursor()
   cursor.execute(query)
   employee=cursor.fetchall()
   if(employee):
    print(employee)
   else:
        print("No emp found")
   cursor.close()
   connection.close()

disp_dept()

def max_salary():
   connection=mysql.connector.connect(
      host="localhost",port='3306',user="root",password="password",database='IotPersonDb'
   )

   query="Select MAX(salary) from employee;"
   cursor=connection.cursor()
   cursor.execute(query)
   employee=cursor.fetchone()
   print(employee)
   cursor.close()
   connection.close()

max_salary()


def min_salary():
   connection=mysql.connector.connect(
      host="localhost",port='3306',user="root",password="password",database='IotPersonDb'
   )

   query="Select MIN(salary) from employee;"
   cursor=connection.cursor()
   cursor.execute(query)
   employee=cursor.fetchone()
   print(employee)
   cursor.close()
   connection.close()
min_salary()