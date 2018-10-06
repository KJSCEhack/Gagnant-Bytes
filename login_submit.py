#!/usr/bin/python 
# Importing the 'cgi' module 
import cgi 
import cgitb
cgitb.enable()
import mysql.connector
from mysql.connector import Error
from PIL import Image
from pytesser import *
def read_data(uid):
    # select photo column of a specific author
    query = "Select * from final where id = %s;"
    args=(uid,)
    #args=(author_id)
    connection = mysql.connector.connect(host="localhost", user="root1", passwd="", database="college")
    try:
        # query blob data form the authors table
        
        cursor = connection.cursor()
        cursor.execute(query, args)
        rows = cursor.fetchall()
        print("<h1>Details of the document:</h1>")
        for row in rows:
             print("<h2>Exact Name as in Document : " +row[3]+"</h2><br />")
             print("<h2>Address : " +row[4]+"</h2><br />")
             print("<h2>Date : " +row[5]+"</h2><br />")
             print("<h2>Age : " +str(row[6])+"</h2><br />")
             #print(row[5])
        #print("photo name ")
        #print(photo)
        # write blob data into a file
        
      #  upload_file(author_id,filename,photo)
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        connection.close()
def main():
    form = cgi.FieldStorage() 
    print("Content-type: text/html\r\n\r\n") 
    print("<html><body>") 
    #print("<h1>Hello !!</h1><br />")
    if form.getvalue("id"):
         uid = form.getvalue("id")
    if form.getvalue("name"):
         name = form.getvalue("name")
    print("<h1>Hello " +name+"!!</h1><br />")
    read_data(uid)
    print("<a href='final.py'>Home</a>")
    print("</body></html>")
if __name__ == '__main__':
    main()
