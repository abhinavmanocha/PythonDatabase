#Importing pymysql, note this is a comment in Python (a number symbol or a hashtag :))
import pymysql


#Setting up connection variables.
host = 'localhost'
username= 'root'
password=''
dbName = 'week8'

#Connecting
conn = pymysql.connect(host, username, password, dbName)

#A database cursor is a control structure that enables traversal over the records in a database.
cursor = conn.cursor()

#SQL query we want to execute.
query = "SELECT * FROM users"

#Executing the query.
cursor.execute(query)

# data is a data structure that can hold the result of the query. cursor.fetchall() will return the entire table, cursor.fetchone() will return the first record (row).
data = cursor.fetchall()

#Printing to see the output.
print (data)

#Closing at the connection.
conn.close()

