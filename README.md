# Insert-data-into-MySQL-from-CSV-file-using-python-3

## Introduction:
Our aim is to insert data into MySQL database from defferent CSV file.

## Prerequisites
To do this work we have to do first install python on our machine also have setup xampp and MySQL.

## Running the tests
 __init__.py in this file we are creating connection with MySQL database also we are creating database in this page name "movieRatings"

table_create.py in this python file we are creating tables on database.We are keeping our MySQL queries into a dictionary named"TABLES={}"
By using for loop we are executing the queries into database for creating table.

insert_movies.py in this python file we are creating 4 function for inserting data on 4 different  table from 4 different CSV file.In
the begining of function we are opening the CSV file.
Then using forloop we read the data from csv file and then inserting the data by query into database.
 
## After inserting data the database screenshot
1. ![Movies](https://github.com/sabiul/Insert-data-into-MySQL-from-CSV-file-using-python-3/blob/master/screenshot/movies.JPG "Movies")

2. ![Links](https://github.com/sabiul/Insert-data-into-MySQL-from-CSV-file-using-python-3/blob/master/screenshot/links.JPG "Links")

3. ![Ratings](https://github.com/sabiul/Insert-data-into-MySQL-from-CSV-file-using-python-3/blob/master/screenshot/ratings.JPG "Ratings")

4. ![Tags](https://github.com/sabiul/Insert-data-into-MySQL-from-CSV-file-using-python-3/blob/master/screenshot/tags.JPG "Tags")


 ## Future Plan:
 We do this project on Postgre Database.
