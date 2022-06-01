from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'heroku_73c182f783c0a9'

db = mysql.connector.connect(
    host="eu-cdbr-west-02.cleardb.net",
    user="b2243985041ca4",
    passwd="24807411",
    database="heroku_73c182f783c0a9"
)

TABLES = {}

TABLES['titles'] = (
 "CREATE TABLE `titles` ("
 " `emp_no` int(11) NOT NULL,"
 " `title` varchar(50) NOT NULL,"
 " `from_date` date NOT NULL,"
 " `to_date` date DEFAULT NULL,"
 ") ENGINE=ClearDB")

mycursor = db.cursor()


def create_database(cursor):
    try:
        cursor.execute(
        "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
try:
    mycursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(mycursor)
        print("Database {} created successfully.".format(DB_NAME))
        db.database = DB_NAME
    else:
        print(err)
        exit(1)


for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        mycursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")
mycursor.close()



db.close()
