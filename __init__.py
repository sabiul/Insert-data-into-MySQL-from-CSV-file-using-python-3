import mysql.connector

__author__ = 'Rashed'

connection = mysql.connector.connect(user='root', password='', host='localhost')
mycursor = connection.cursor()


#mycursor.execute("CREATE DATABASE movieRatings  DEFAULT CHARACTER SET 'utf8'")
mycursor.execute("USE movieRatings")