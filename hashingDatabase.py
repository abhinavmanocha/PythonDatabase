#Importing pymysql and bcrypt.
#Remember to run 'pip install bcrypt' to download/install that package.
import bcrypt
import pymysql

#def methodName(methodParameters): is how you define a method in Python.
#HashMyPassword accepts a string paramter password, and generates a salt/hashes it using the bcrypt password hashing function.
def hashMyPassword(password):

    #Using the Bcrypt package to utilize the Bcrypt password hashing algorithm.
    #We begin by generating a salt.
    salt = bcrypt.gensalt()
    #now we actually hash the password, given a salt.
    hashedPassword = bcrypt.hashpw(password.encode('utf8'), salt)
    #returning the hashedPassword
    return hashedPassword

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='week8')
try:
    with connection.cursor() as cursor:
        #Altering table if the column does not exist.
        sqlAlter = "ALTER TABLE users ADD IF NOT EXISTS password TEXT"
        cursor.execute(sqlAlter)
    connection.commit()

    with connection.cursor() as cursor:
        #inserting hashed password.
        sqlInsert = "INSERT INTO users (name, email, password) VALUES(%s, %s, %s)"
        hashedpassword = hashMyPassword('159159159')
        cursor.execute(sqlInsert, ('Some name', 'someemail@gmail.com', hashedpassword))
    connection.commit()

finally:
    connection.close()







