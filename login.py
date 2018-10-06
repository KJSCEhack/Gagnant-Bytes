#!/usr/bin/python
import cgi 
print("Content-type: text/html\r\n\r\n") 
print("<html><body>") 
print("<h1> Log in! </h1>") 
# Using the inbuilt methods 
  
 
  
# Using HTML input and forms method 
print("<form enctype='multipart/form-data' method='post' action='login_submit.py'>") 
print("<p>Enter your ID: <input type = 'number' name = 'id' /></p>")
print("<p>Name: <input type = 'text' name = 'name' /></p>")
print("<p><input type = 'submit' value = 'Upload' /></p>") 
print("</form>") 

print("</body></html>") 
