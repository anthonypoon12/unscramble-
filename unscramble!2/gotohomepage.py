#! /usr/bin/python3
import cgi
import cgitb
cgitb.enable()
form=cgi.FieldStorage()
username=form.getvalue('username3','')
if username!='***username***' and username!='':
	f=open('unscramble (loggedin).html')
	a=f.read()
	f.close()
	print('Content-type: text/html\n')
	a=a.replace('***username***',username)
	print(a)
else:
	f=open('unscramble.html')
	a=f.read()
	f.close()
	print('Content-type: text/html\n')
	print(a)
