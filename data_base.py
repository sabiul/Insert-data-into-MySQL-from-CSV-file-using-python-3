__author__ = 'Rashed'

import mysql.connector


class DbConnection:


    connection = mysql.connector.connect(user='root', password='', host='localhost')
    mycursor = connection.cursor()


    # mycursor.execute("CREATE DATABASE python")
    mycursor.execute("USE python")
    mycursor.execute("""CREATE TABLE customer(id int, name varchar(30))""")

