#import mysql.connector
#print("MySQL Connector is installed successfully!")
import mysql.connector
#mydb = mysql.connector.connect(host="localhost", user="root", password="Anurag@2003")
mydb = mysql.connector.connect(host="localhost", user="root", password="Anurag@2003", database="order_management")
mycursor = mydb.cursor()
#mycursor.execute("show databases")
#print(mycursor)
#for i in mycursor:
#    print(i)
#mycursor.execute("show tables")
mycursor.execute("INSERT INTO dim_customer VALUES (3, 'Anurag Patil', '278 Madison Avenue', '101 Shipping Blvd', 'anuragpatil811@gmail.com'),  (4, 'Anil Kumar Sah', '279 Time Avenue', '100 Shipping Yard', 'anil@gmail.com')")
#mycursor.execute("INSERT INTO dim_customer VALUES (4, 'Anil Kumar Sah', '279 Time Avenue', '100 Shipping Yard', 'anil@gmail.com')")
mycursor.execute("select * from  dim_customer")
for i in mycursor:
    print(i)

mydb.commit()