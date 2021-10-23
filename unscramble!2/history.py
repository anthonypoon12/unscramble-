#!/usr/bin/python3
import cgi
import cgitb
cgitb.enable()
form=cgi.FieldStorage()
#-------------------getting input------------
username=form.getvalue('username2','')
usernametxt='Histories/'+username+'.txt'
#---------------getting all usernames and histories----------
f=open(usernametxt,'r').read().split('\n*****\n')
if f[-1]=='\n*****' or f[-1]=='\n*****\n'or f[-1]=='':
    f=f[:-1]
#--------------------------------------------------
    print('Content-type: text/html\n')
    file=open('history.html','r').read()
    file=file.replace('***historywords***','</center></td></tr><tr><td><center>'.join(f))
    file=file.replace('***username***',username)
    print(file)
else:
    print('Content-type: text/html\n')
    print('''
    <html>
    <body>
    Either you're not logged in or you don't have the correct hidden value for the username.
    <br>
    <b>
    It's name should be "username2".
    </b>
    <br>Either way it's saying that the python isn't taking in any input for the username so.....
<b>
<br>-----------------------------------------------------------------------------------------------------<br>
So, I checked it out and you made the history button a link to "history.html".<br>
I changed it to "history.py".<br>
 I need it to be able to take in the hidden value.<br>
 I THINK that you need to put it into a form cuz that's how we did it for the other ones.
<br>I would do it myself but I'm not sure if it might change how it looks so.... I'll leave it to you.
</b>
    </body>
    </html>
    ''')
