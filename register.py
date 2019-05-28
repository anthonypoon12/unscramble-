#!/usr/bin/python3
import cgi
import cgitb
form=cgi.FieldStorage()
cgitb.enable()
wrong=''
username='ggg'#form.getvalue('username','')
password='aaa'#form.getvalue('password','')
allusernames=[]
allpasswords=[]
f=open('usernames.txt','r')
allusernames=f.read()
f.close()
allusernames=allusernames.split('\n')
if allusernames[-1]=='':
    allusernames==allusernames[:-1]
if allusernames[0]=='':
    allusernames==allusernames[1:]
f=open('passwords.txt','r')
allpasswords=f.read()
f.close()
allpasswords=allpasswords.split('\n')
if allpasswords[-1]=='':
    allpasswords==allpasswords[:-1]
if allusernames[0]=='':
    allusernames==allusernames[1:]
if username=='' or password=='':
    wrong='Remember to type in a username and password'
else:
    if username in allusernames:
        wrong='USERNAME ALREADY TAKEN'
if wrong=='':
    f=open("usernames.txt","a")
    f.write('\n' + username)
    f.close()
    f=open('passwords.txt','a')
    f.write('\n' + password)
    f.close()
    wrong='IT WORKS' + username + ' ' + password
print('Content-type: text/html\n')
print('''
<html>
<body>
%s
</body>
</html>
''' % wrong)
    
