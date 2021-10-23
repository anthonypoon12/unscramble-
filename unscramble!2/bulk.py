#!/usr/bin/python3
import cgi
import cgitb
import time
cgitb.enable()
form=cgi.FieldStorage()
#---------------------------------------------------------------------------------
def check(a,theinput1):
    checker=theinput1
    for y in a:
        if y in checker:
            checker=checker[:checker.find(y)]+checker[checker.find(y)+1:]
        else:
            return 0
    return 1
def takeout(z):
    y=''
    for x in z:
        if ord(x)>=ord('0') and ord(x)<=ord('9'):
            y+=x
    return y
###################---------------------------getting the input----------------------------------------------------
theinput2=form.getvalue('theinput','').lower()
theinput=''
for l in theinput2:
    if ord(l) >= ord('a') and ord(l) <= ord('z'):
        theinput += l
#-----------------------------all english words--------------------------------------------------
f=open('dictall.txt','r')
allwords=f.read().split('\n')
f.close()
allwords=allwords[:-1]
#---------------------------------------------------------------------------
themaybewords=[]
for x in allwords:
    if len(x)<=len(theinput):
        themaybewords.append(x)
thewords=[]
for z in themaybewords:
    if check(z,theinput)==1:
        thewords.append(z)
#-------------------------------------------------------------------------
thewords1=[]
greaterthan=form.getvalue('great1','')
lessthan=form.getvalue('less1','')
only=form.getvalue('only1','')
if greaterthan=='':
    greaterthan=form.getvalue('greaterthan','')
if lessthan=='':
    lessthan=form.getvalue('lessthan','')
if only=='':
    only=form.getvalue('only','')
try:
    int(greaterthan)
    int(lessthan)
    int(only)
except:
    greaterthan=takeout(greaterthan)
    lessthan=takeout(lessthan)
    only=takeout(only)
if greaterthan != '':
    greaterthan=int(greaterthan)
    thewords1=thewords
    thewords=[]
    for word in thewords1:
        if len(word)>greaterthan:
            thewords.append(word)
if lessthan != '':
    lessthan=int(lessthan)
    thewords1=thewords
    thewords=[]
    for word in thewords1:
        if len(word)<lessthan:
            thewords.append(word)
if only != '':
    only=int(only)
    thewords1=thewords
    thewords=[]
    for word in thewords1:
        if len(word)==only:
            thewords.append(word)
range=''
if only=='' and greaterthan=='' and lessthan=='':
    range='All possible words'
elif only!='':
    range='words with length of' + ' ' + str(only)
else:
    if lessthan!='':
        range+='words with length less than' + ' ' + str(lessthan)
        if greaterthan!='':
            range+=' AND greater than' + ' ' + str(greaterthan)
    elif greaterthan!='':
        range='words with length greater than' + ' ' + str(greaterthan)
##############--------------------------------------------------------------------------
newuserpass=form.getvalue('newuserpass','')
if newuserpass!='':
        file2=open('usernamesandpasswords.txt','r')
        ab=file2.read().split('\n***\n')
        file2.close()
        if ab[-1]=='':
            ab=ab[:-1]
        if ab[-1]==' \n***':
            ab=ab[:-1]
        ab2=[]
        for z in ab:
            ab2.append(z.split(','))
        if '\n***' in ab2[-1][-1]:
            ab2[-1][-1]=ab2[-1][-1].replace('\n***','')
        theinput10=''
        for y in ab2:
            if y[0]==newuserpass:
                if theinput=='':
                    theinput10='(NothingTyped)'
                y[2]+= theinput10 + ' '
        ab3=[]
        for h in ab2:
            ab3.append(','.join(h))
        ab='\n***\n'.join(ab3)
        ab+='\n***'
        file2=open('usernamesandpasswords.txt','w')
        file2.write(ab)
        file2.close()
#-----------------------------------------------------------------------------
specifics3=''
specifics3=form.getvalue('specifics3','')
if specifics3=='':
    specifics3=form.getvalue('filter','')
    if specifics3=='':
        specifics3=form.getvalue('specifics','')
specifics2=[]
yep=thewords
try:
    if specifics3!='':
        specifics2=specifics3.split(',')
        specifics1=[]
        for x in specifics2:
            specifics1.append(x.split(':'))
        specifics={}
        for y in specifics1:
            specifics[int(y[0])]=y[1]
        badwords=[]
        for word in thewords:
            for i in specifics:
                try:
                    if word[i-1]!=specifics[i]:
                        if word not in badwords:
                            badwords.append(word)
                except:
                    if word not in badwords:
                        badwords.append(word)
        for word2 in badwords:
            if word2 in thewords:
                thewords.remove(word2)
    specificslist2=specifics2
    specificslist=[]
    for x in specificslist2:
        if x[x.find(':')-1]=='1':
            specificslist.append(x[:x.find(':')]+'st is '+x[x.find(':') + 1:])
        elif x[x.find(':')-1]=='2':
            specificslist.append(x[:x.find(':')]+'nd is '+x[x.find(':')+ 1:])

        elif x[x.find(':')-1]=='3':
            specificslist.append(x[:x.find(':')]+'rd is '+x[x.find(':') + 1:])
        else:
            specificslist.append(x[:x.find(':')]+'th is '+x[x.find(':') + 1:] )
except:
    thewords=yep
    specificslist=[]
#------------------------------------------------------------------------------
search=form.getvalue('search','').lower()
thewords3=thewords
if search!='':
    thewords=[]
    for x in thewords3:
        if search in x:
            thewords.append(x)
#---------------------------------------------------------------------------
if newuserpass=='':
  file=open('output.html','r').read()
else:
    file=open('outputlog.html','r').read()
thewords2=[]
for x in thewords:
    v='<input name="word" type="submit" ID="lkup" value=***>'
    v=v.replace('***',x)
    thewords2.append(v)
if newuserpass!='':
    logout='''
    <form name="lout" method="POST" action="unscramble.html">
    <input name="logout" type="submit" value="Logout">
    </form>'''
else:
    logout=''
count=len(thewords)
hiddenusername='''<input type="hidden" name="username" value="***username***">'''
hiddenusername=hiddenusername.replace('***username***',newuserpass)
#------------------------------history----------------------
history=''
history+=time.asctime()+': \n'
history+="UNSCRAMBLED:"
history+='\ninput: '+ theinput2
history+='\nrange: '+ range
history+='\nspecifics: ' + ('<br>'+ '<br>').join(specificslist)
history+='\ncount: ' + str(count)
history+='\nsearch: '+search
history+='\n*****\n'
usernametxt='Histories/'+newuserpass+'.txt'
file3=open(usernametxt,'r')
a=file3.read()
file3.close()
file3=open(usernametxt,'w')
file3.write(history+a)
file3.close()
#--------------------------------------------------------------
print('Content-Type: text/html\n')
file=file.replace('***range***',range)
file=file.replace('***greaterthan***',str(greaterthan))
file=file.replace('***lessthan***',str(lessthan))
file=file.replace('***only***',str(only))
file=file.replace('***specifics3***',specifics3)
file=file.replace('***count***',str(count))
file=file.replace('***input***',theinput2)
file=file.replace('***username***',newuserpass)
file=file.replace('***thewords***',(hiddenusername+'</form></center></td></tr><tr><td><center><form method="GET" action="meaning.py">').join(thewords2))
file=file.replace('***specifics***','<br>'+ '<br>'.join(specificslist))
file=file.replace('***unfilteredwords***',','.join(thewords))
file=file.replace('***logout***',logout)
print(file)
