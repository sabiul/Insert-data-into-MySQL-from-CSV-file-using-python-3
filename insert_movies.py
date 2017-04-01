__author__ = 'Rashed'
import csv
from data import mycursor,connection
# LOAD DATA INFILE 'C:\Users\Rashed\PycharmProjects\database\data\ml-latest-small.csv'
# INTO TABLE discounts
# FIELDS TERMINATED BY ','
# ENCLOSED BY '"'
# LINES TERMINATED BY '\n'
# IGNORE 1 ROWS;

# def insert_movies():
#     header = ('title', 'geners')
#     with open('./ml-latest-small/movies.csv', newline='', encoding="utf8") as csvfile:
#         spamreader = csv.reader(csvfile)
#         for row in spamreader:
#             movie = dict(zip(header, row[1:]))
#             print(spamreader)
#             # Movie.objects.create(**movie)




with open('./ml-latest-small/movies.csv', newline='',  encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        # sql = "INSERT INTO testSmall VALUES (%s);" % ', '.join('?' for _ in row)
        # mycursor.execute (sql, row)

        # sql = "INSERT INTO `movies` (`title`, `geners`) VALUES ( ?, ?);"
        mycursor.execute("INSERT INTO `movies` (`id`, `title`, `geners`) VALUES ( %s, %s, %s);", row)
        #close the connection to the database.
        connection.commit()
        mycursor.close()
        # mycursor.execute (sql, (row[1], row[2]))
       # print(', '.join(row))