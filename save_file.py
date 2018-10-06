#!/usr/bin/python
import getdata
import random
import datetime
import cgi, os
import cgitb; cgitb.enable()
import mysql.connector
from mysql.connector import Error
from PIL import Image
from pytesser import *
def insert_blob(uid, givenname, filename):
    # read file
    data = Image.open(filename)
    blob_value = open(filename, 'rb').read()
    # prepare update query and data
    query = "Insert into final (id,name,img) values(%s,%s,%s)"
 
    args = (uid, givenname, blob_value)
 
    connection = mysql.connector.connect(host="localhost", user="root1", passwd="", database="college")
 
    try:
        cursor = connection.cursor()
        cursor.execute(query, args)
        connection.commit()
        #print("executed")
    except Error as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
def insert_data(uid,exname, address, dob, age):
    # read file
    
    # prepare update query and data
    query = "UPDATE final SET exname=%s, address=%s, dob=%s, age=%s WHERE id=%s"
 
    args = (exname, address, dob, age, uid)
 
    connection = mysql.connector.connect(host="localhost", user="root1", passwd="", database="college")
 
    try:
        cursor = connection.cursor()
        cursor.execute(query, args)
        connection.commit()
        #print("executed")
    except Error as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
def main():
    try: # Windows needs stdio set for binary mode.
        import msvcrt
        msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
        msvcrt.setmode (1, os.O_BINARY) # stdout = 1
    except ImportError:
        pass
    form = cgi.FieldStorage() 
    print("Content-type: text/html\r\n\r\n") 
    print("<html><body>") 

    if form.getvalue("name"):
         name = form.getvalue("name") 
    print("<h1>Hello " +name+"!!</h1><br />")


    fileitem=form['filename2']
    #print "---------"
    #print "filename",fileitem.filename
    #print "file",fileitem.file
#upload_dir = '/usr/lib/cgi-bin/osrtest'
#print(fileitem)
#print(fileitem.name)
# Test if the file was uploaded
    if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
         fn = os.path.basename(fileitem.filename)
         #print(fn)
         open(fn, 'wb').write(fileitem.file.read(250000))

         message = 'The file "' + fn + '" was uploaded successfully'
   
    else:
         message = 'No file was uploaded'
    print("<h1>" +message+"</h1>")
    print("</body></html>")
    flag=0
    while flag==0:
         a=random.randint(1000,10000)
         query = "Select id from image" 
         connection = mysql.connector.connect(host="localhost", user="root1", passwd="", database="college")
         cursor = connection.cursor()
         cursor.execute(query)
         rows=cursor.fetchall()
         connection.commit()
         #print("executed")
         cursor.close()
         connection.close()
         for row in rows:
              if row[0]!=a:
                   flag=1
                   break
    insert_blob(a,name,fn)
    abc=getdata.main(a)
    #print(abc)
    n1=abc.find("Name :")
    n1=n1+6
    n2=abc.find("S/D")
    #print(n1)
    #print(abc[n1:n2])
    s1=abc[n1:n2-1]
    n3=abc.find("Add .")
    n3=n3+8
    n4=abc.find("PIN")
    n4=n4+11
    n5=abc.find("DOB :")
    n5=n5+5
    
    #print(abc[n3:n4])
    s2=abc[n3:n4]
    #print(abc[n5:n5+11])
    s3=abc[n5:n5+11]
    n6=n5+7
    sub=abc[n6:n5+11]
    #print(sub)
    i=int(sub)
    now=datetime.datetime.now
    age=2018-i
    #print(age)
    #print(name)
    #print(s1)
    if name.replace(" ","").lower() == s1.replace(" ","").lower():
         print("<h1>Document Verified and Uploaded Sucessfully</h1>")
         print("<h1>Your Id is ")
         print(a)
         print("</h1>")
         insert_data(a,s1,s2,s3,age)
    else:
         print("<h1>Name does not match and your account was not created</h1>")
    
    print("<a href='final.py'>Home</a>")
 
if __name__ == '__main__':
    main()
