#!/usr/bin/python3
import cgi
import cgitb
form=cgi.FieldStorage()
cgitb.enable()
wrong=''
#------------------------------------------------gets the input
username=form.getvalue('username','')
password=form.getvalue('password','')
#-------------------------------------------------gets all recorded usernames/passwords
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
for x in alluandp2:
    alluandp3.append(x.split(','))
for x in alluandp3:
    alluandp[x[0]]=x[1]
#------------------------------------------------errors
if username=='' or password=='':
    wrong='REMEMBER TO TYPE IN A USERNAME AND PASSWORD'
else:
    if username in alluandp:
        wrong='USERNAME ALREADY TAKEN'
if wrong=='':
    usernametxt='Histories/'+username+'.txt'
    g=open(usernametxt,'w')
    g.write('')
    g.close()
if wrong=='':
    fx=open("usernamesandpasswords.txt","a")
    fx.write('\n' + username + ',' + password + ', \n***')
    fx.close()
    file=open('unscramble (loggedin).html','r').read()
    print('Content-type: text/html\n')
    file=file.replace('***username***',username)
    print(file)
else:
    print('Content-type: text/html\n')
    fi=open('registererror.html','r').read()
    fi=fi.replace('***wrong***',wrong)
    print(fi)
