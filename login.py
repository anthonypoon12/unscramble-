#!/usr/bin/python3
import cgi
import cgitb
form=cgi.FieldStorage()
cgitb.enable()
wrong=''
username=form.getvalue('username','')
password=form.getvalue('password','')
if username=='' or password=='':
    wrong='Remember to type in your username and password'
username=='***'+username+'***'
password=='***'+username+'***'
allusernames=''
allpasswords=''
f=open('usernames.txt','r')
allusernames=f.read()
f.close()
allusernames=allusernames.split('\n')
if allusernames[-1]=='':
    allusernames==allusernames[:-1]
f=open('passwords.txt','r')
allpasswords=f.read()
f.close()
allpasswords=allpasswords.split('\n')
if allpasswords[-1]=='':
    allpasswords==allpasswords[:-1]
if username in allusernames:
    if password==allpasswords[allusernames.index(username)]:
        wrong='IT WORKS'
    else:
        wrong='WRONG PASSWORD'
else:
    wrong='WRONG USERNAME/PASSWORD'
print('Content-type: text/html\n')
print('''
<html>
<body>
%s
</body>
</html>
''' % wrong)
    
