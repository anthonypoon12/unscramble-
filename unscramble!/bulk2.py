#!/usr/bin/python3
import cgi
import cgitb
cgitb.enable()
form=cgi.FieldStorage()
def check(a,theinput1):
    checker=theinput1
    for y in a:
        if y in checker:
            checker=checker[:checker.index(y)]+checker[checker.index(y)+1:]
        else:
            return 0
    return 1
    checker=theinput1
theinput='awdhaow'#form.getvalue('theinput','')
f=open('dictall.txt','r')
allwords=f.read().split('\n')
f.close()
allwords=allwords[:-1]
themaybewords=[]
for x in allwords:
    if len(x)<=len(theinput):
        themaybewords.append(x)
thewords=[]
for z in themaybewords:
    if check(z,theinput)==1:
        thewords.append(z)
print('Content-Type: text/html\n')
print('''
<html>
<body>
%s
</body>
</html>''' % (','.join(thewords)))
