#!/usr/bin/python3
import cgi
import cgitb
form=cgi.FieldStorage()
cgitb.enable()
text=''
wrong=''
#-------------------------------input-----------------------------
username=form.getvalue('username','')
password=form.getvalue('password','')
#------------------------------------------all usernames and passwords-------------------------
alluandp2=[]
f=open('usernamesandpasswords.txt','r')
alluandp2=f.read()
f.close()
alluandp2=alluandp2.split('\n***\n')
if alluandp2[-1]=='':
    alluandp2=alluandp2[:-1]
    if alluandp2[-1]=='\n***':
        alluandp2=alluandp2[:-1]
if alluandp2[0]=='':
    alluandp2=alluandp2[1:]
alluandp3=[]
alluandp={}
#----------------------------histories------------------------------
histories={}
for x in alluandp2:
    alluandp3.append(x.split(','))
for x in alluandp3:
    alluandp[x[0]]=x[1]
    histories[x[0]]=x[2]
history=''
#------------------------------errors------------------------------------------
if username=='' or password=='':
    wrong='Remember to type in your username and password'
else:
    if username in alluandp:
        if password==alluandp[username]:
            wrong='IT WORKS'
            history=histories[username][1:-1]
        else:
            wrong='WRONG PASSWORD'
    else:
        wrong='WRONG USERNAME/PASSWORD'
#-----------------------------------------------------------------------
print('Content-type: text/html\n')
if wrong!="IT WORKS":
    file2=open('loginerror.html','r').read()
    file2=file2.replace('**wrong**',wrong)
    print(file2)
else:
    file=open('unscramble (loggedin).html','r').read()
    file=file.replace('***username***',username)
    print(file)
