#import statement
import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost', user='root', password='', db='week8')

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        cursor.execute(sql, ('Alaadin Addas', 'alaadinaddas@trentu.ca'))

    #When selecting we don't have to commit, but when manipulating the database in any way, we have to!
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM users WHERE `email`=%s"
        cursor.execute(sql, ('alaadinaddas@trentu.ca',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
