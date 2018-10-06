#!/usr/bin/python
import cgi 
print("Content-type: text/html\r\n\r\n") 
print("<html><body>") 
print("<h1> Welcome! </h1>") 
# Using the inbuilt methods 
  
 
  
# Using HTML input and forms method 
print("<form enctype='multipart/form-data' method='post' action='login.py'>")  
print("<p><input type = 'submit' value = 'Login' /></p>") 
print("</form>") 
print("<form enctype='multipart/form-data' method='post' action='signup.py'>")  
print("<p><input type = 'submit' value = 'Signup' /></p>") 
print("</form>")
print("</body></html>") 
