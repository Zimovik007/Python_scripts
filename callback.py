#!/usr/bin/env python
import os, sys, cgi
import MySQLdb

print "Content-Type: text/html; charset=UTF8\n\n"

def check_param(template):
    try:
        temp = form[template].value
    except:
        temp = None
    return temp

form = cgi.FieldStorage()
reference = check_param("reference")
message   = check_param("message")
code      = check_param("code")
number    = check_param("number")
price     = check_param("price")
timestamp = check_param("timestamp")
mccmnc    = check_param("mccmnc")
split     = check_param("split")

#the variables below need to fill out
#table_name - the variable in which to record the name of the table from the database

db_server  = ""
db_login   = ""
db_pass    = ""
db_name    = ""
table_name = ""  # the same name that you specified in the script create_table.

try:
    dbh = MySQLdb.connect(db_server, db_login, db_pass, db_name)
    cursor = dbh.cursor()
    query = "INSERT INTO `"+ table_name +"` VALUES(NULL, %s, %s, %s ,%s, %s ,%s, %s, %s)"
    cursor.execute(query, (reference, number, code, message, price, timestamp, mccmnc, split))
    dbh.commit()
except:
    print "Failure to connect"
print "New record successfully added to database"
