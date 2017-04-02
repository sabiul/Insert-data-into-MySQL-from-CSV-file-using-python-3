__author__ = 'Rashed'

from data import mycursor,connection
import mysql.connector
from mysql.connector import errorcode

TABLES = {}
TABLES['movies'] = (
    "CREATE TABLE `movies` ("
    "  `id` int(50) NOT NULL AUTO_INCREMENT,"
    "  `title` varchar(200) NOT NULL,"
    "  `geners` varchar(200) NOT NULL,"
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
    "  `timestapm`  varchar(250) NOT NULL"
    ") ENGINE=InnoDB")

TABLES['tags'] = (
    "CREATE TABLE `tags` ("
    "  `user_id` int(50) NOT NULL,"
    "  `movie_id` int(50) NOT NULL,"
    "  `tags` varchar(250) NOT NULL,"
    "  `timestapm` varchar(250) NOT NULL"
    ") ENGINE=InnoDB")


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