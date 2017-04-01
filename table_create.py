__author__ = 'Rashed'

from data import mycursor,connection
# from __future__ import print_function
# from data.data_base import do_connect
#


import mysql.connector
from mysql.connector import errorcode


# from .data_base import do_connect

TABLES = {}
TABLES['movies'] = (
    "CREATE TABLE `movies` ("
    "  `id` int(50) NOT NULL AUTO_INCREMENT,"
    "  `title` varchar(100) NOT NULL,"
    "  `geners` varchar(100) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['links'] = (
    "CREATE TABLE `links` ("
    "  `id` int(50) NOT NULL,"
    "  `imdbid` int(50) NOT NULL,"
    "  `tmdbid` int(50) NOT NULL,"
    "  `movie_id` int(50) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['ratings'] = (
    "CREATE TABLE `ratings` ("
    "  `user_id` int(50) NOT NULL,"
    "  `movie_id` int(50) NOT NULL,"
    "  `ratings` float(50) NOT NULL,"
    "  `timestapm` TIMESTAMP DEFAULT 0"
    ") ENGINE=InnoDB")

TABLES['tags'] = (
    "CREATE TABLE `tags` ("
    "  `user_id` int(50) NOT NULL,"
    "  `movie_id` int(50) NOT NULL,"
    "  `tags` varchar(150) NOT NULL,"
    "  `timestapm` TIMESTAMP DEFAULT 0"
    ") ENGINE=InnoDB")


# connector = do_connect()
# connector.execute()
#mycursor.execute("CREATE DATABASE WWWython")

#mycursor.execute("USE python")

for name, ddl in TABLES.items():
    try:
        print("Creating table {}: ".format(name), end='')
        mycursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

mycursor.close()
connection.close()