#!/usr/bin/python 
# Importing the 'cgi' module 
import cgi 
import cgitb
cgitb.enable()
import mysql.connector
from mysql.connector import Error
from PIL import Image
from pytesser import *
def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
def read_blob(author_id, filename):
    # select photo column of a specific author
    query = "Select img from final where id = %s;"
    args=(author_id,)
    #args=(author_id)
    connection = mysql.connector.connect(host="localhost", user="root1", passwd="", database="college")
    try:
        # query blob data form the authors table
        
        cursor = connection.cursor()
        cursor.execute(query, args)
        photo = cursor.fetchone()[0]
        
        #print("photo name ")
        #print(photo)
        # write blob data into a file
        write_file(photo, filename)
      #  upload_file(author_id,filename,photo)
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        connection.close()
def main(uid):
    s="file"+str(uid)+".tif"
    read_blob(uid,s)
    image_file = s
    im = Image.open(image_file)
    text = image_to_string(im)
    text = image_file_to_string(image_file)
    text = image_file_to_string(image_file, graceful_errors=True)
    #print("Content-type: text/html\r\n\r\n") 
    print("<html><body>") 
    #print("<h1> Hello Program! </h1>") 
    return text
    #n1=text.find("Name :")
    #n1=n1+6
    #print(n1)
    #print(text[n1:11])
    print("</body></html>")
if __name__ == '__main__':
    main()
