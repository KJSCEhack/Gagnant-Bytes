#!/usr/bin/python
import cgi 
print("Content-type: text/html\r\n\r\n") 
print("<html><body>") 
print("<h1> Sign Up! </h1>") 
# Using the inbuilt methods 
  
 
  
# Using HTML input and forms method 
print("<form enctype='multipart/form-data' method='post' action='save_file.py'>") 
print("<p>Name: <input type = 'text' name = 'name' /></p>")
print("<p>File POI: <input type = 'file' name = 'filename2' /></p>") 
print("<p>File Image: <input type = 'file' name = 'filename3' /></p>") 
print("<p><input type = 'submit' value = 'Upload' /></p>") 
print("</form>") 
print("</body></html>") 
