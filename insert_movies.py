__author__ = 'Rashed'
#!/usr/bin/python3

from data import mycursor,connection
import csv
def insert_movies():
    with open('./ml-latest-small/movies.csv', newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            # Prepare SQL query to INSERT a record into the database.
            sql = "INSERT INTO movies(id,title, geners) VALUES ('%s', '%s', '%s' );" % (row[0], row[1], row[2])
            print(sql)
            try:
               # Execute the SQL command
               mycursor.execute(sql)
               # Commit your changes in the database
               connection.commit()
            except:
               # Rollback in case there is any error
               connection.rollback()


def insert_links():
    with open('./ml-latest-small/links.csv', newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            # Prepare SQL query to INSERT a record into the database.
            sql = "INSERT INTO links (id,imdbid, tmdbid,movie_id) VALUES ('%s','%s', '%s', '%s' );" % (row[0], row[1], row[2], row[2])
            print(sql)
            try:
               # Execute the SQL command
               mycursor.execute(sql)
               # Commit your changes in the database
               connection.commit()
            except:
               # Rollback in case there is any error
               connection.rollback()


def insert_ratings():
    with open('./ml-latest-small/ratings.csv', newline='',  encoding="utf8") as csvfile:
        next(csvfile)
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            # Prepare SQL query to INSERT a record into the database.
            sql = "INSERT INTO ratings(user_id,movie_id, ratings,timestapm) VALUES ('%s','%s', '%s', '%s' );" % (row[0], row[1], row[2], row[3])
            print(sql)
            try:
               # Execute the SQL command
               mycursor.execute(sql)
               # Commit your changes in the database
               connection.commit()
            except:
               # Rollback in case there is any error
               connection.rollback()


def insert_tags():
    with open('./ml-latest-small/tags.csv', newline='',  encoding="utf8") as csvfile:
        next(csvfile)
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            # Prepare SQL query to INSERT a record into the database.
            sql = "INSERT INTO tags(user_id,movie_id, tags,timestapm) VALUES ('%s','%s', '%s', '%s' );" % (row[0], row[1], row[2], row[3])
            print(sql)
            try:
               # Execute the SQL command
               mycursor.execute(sql)
               # Commit your changes in the database
               connection.commit()
            except:
               # Rollback in case there is any error
               connection.rollback()



insert_movies()
insert_links()
insert_ratings()
insert_tags()
# disconnect from server
connection.close()