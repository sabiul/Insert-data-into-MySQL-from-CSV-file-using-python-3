# Insert-data-into-MySQL-from-CSV-file-using-python-3

## Introduction:
Our aim is to insert data into MySQL database from defferent CSV file.

## Prerequisites
To do this work we have to do first install python on our machine also have setup xampp and MySQL.

## How to run MySQL from python
To do this work first **open XAAMP & start MySQL**. Then got to this link: https://dev.mysql.com/downloads/connector/python/ & download the MySQL Connector/Python based on your opearating system & python version. Now install it. Thats it.

## Running the tests
 __init__.py in this file we are creating connection with MySQL database also we are creating database in this page name "movieRatings". Before run this page please be sure you must be change the connection based on your MySQL user,password & host.
 ```python
connection = mysql.connector.connect(user='root', password='', host='localhost')
```
Database will be create in this code bellow:
```python
mycursor.execute("CREATE DATABASE movieRatings  DEFAULT CHARACTER SET 'utf8'")
```

table_create.py in this python file we are creating tables on database.We are keeping our MySQL queries into a dictionary named"TABLES={}"
```python
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
```
By using for loop we are executing the queries into database for creating table.
```python
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
```
        
insert_movies.py in this python file we are creating 4 function for inserting data on 4 different  table from 4 different CSV file.In
the begining of function we are opening the CSV file.
```python
with open('./ml-latest-small/movies.csv', newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
```
Then using forloop we read the data from csv file and then inserting the data by query into database.
```python
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
```
 
## After inserting data the database screenshot
1. ![Movies](https://github.com/sabiul/Insert-data-into-MySQL-from-CSV-file-using-python-3/blob/master/screenshot/movies.JPG "Movies")

2. ![Links](https://github.com/sabiul/Insert-data-into-MySQL-from-CSV-file-using-python-3/blob/master/screenshot/links.JPG "Links")

3. ![Ratings](https://github.com/sabiul/Insert-data-into-MySQL-from-CSV-file-using-python-3/blob/master/screenshot/ratings.JPG "Ratings")

4. ![Tags](https://github.com/sabiul/Insert-data-into-MySQL-from-CSV-file-using-python-3/blob/master/screenshot/tags.JPG "Tags")


 ## Future Plan:
 We do this project on Postgre Database.
