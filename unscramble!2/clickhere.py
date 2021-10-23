#! /usr/bin/python3
import cgi
import cgitb
form=cgi.FieldStorage()
cgitb.enable
username=form.getvalue('username3','')
if username=='':
    f=open('missingword.html')
else:
    f=open('missingwordlog.html')
a=f.read()
f.close()
if username!='':
    logout='''
    <form name="lout" method="POST" action="unscramble.html">
    <input name="logout" type="submit" value="Logout">
    </form>'''
else:
    logout=''
a=a.replace('***username***',username)
a=a.replace('***logout***',logout)
print('Content-type: text/html\n')
print(a)
