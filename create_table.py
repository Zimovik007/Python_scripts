#!/usr/bin/env python
import MySQLdb, sys, os

print "Content-Type: text/html; charset=UTF8\n\n"


#Enter the values for the four variables to connect to your database. 
#The fifth variable, enter the name of the table you want to create

db_server  = ""
db_login   = ""
db_pass    = ""
db_name    = ""
table_name = ""

try:
    dbh = MySQLdb.connect(db_server, db_login, db_pass, db_name)
    cursor = dbh.cursor()
    query = "CREATE TABLE `"+table_name+"` (`id` INT AUTO_INCREMENT, `reference` VARCHAR(255), `number` INT, `code` INT, `message` TEXT, `price` DOUBLE, `timestamp` DATETIME, `mccmnc` INT, `split` INT, PRIMARY KEY (`id`))"
    cursor.execute(query)
    dbh.commit()
except:
    print "failure to connect"
    exit()
print "The table created successfully"
