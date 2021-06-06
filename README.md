## WSGI Web App
Simple example of client-side POST request to WSGI Python web application  
Front to back and back to front ... end :)  

CLIENT --> WEBSERVER --> WSGI --> WEB APP

### Concept
1. Client submits a form which performs a POST request (vanilla Javascript and fetch)  
2. The web server request is handled by WSGI, which forwards to our Python web app  
3. Python receives request, and sends answer back to client  

### Requires
* Python (tested on >=3.9.1)
* Web server eg Apache

### Setup
* Apache web server: Create WSGIScriptAlias
```bash
cat /etc/httpd/conf.d/python-wsgi.conf
WSGIScriptAlias /webapp/app /var/www/html/webapp/app.py
```
* Restart web server
* Download index.html and api.py to /var/www/html/webapp/
* Open browser, open browser console (F12), and go to **localhost/webapp**

