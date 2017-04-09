import mysql.connector
from mysql.connector import errorcode

__author__ = 'Rashed'

connection = mysql.connector.connect(user='root', password='', host='localhost')
mycursor = connection.cursor()

try:
    mycursor.execute("CREATE DATABASE movieRatings  DEFAULT CHARACTER SET 'utf8'")
except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print("Database already exists.")
        else:
            print(err.msg)

mycursor.execute("USE movieRatings")
