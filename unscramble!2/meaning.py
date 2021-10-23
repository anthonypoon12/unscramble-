#! /usr/bin/python3
import cgi
import cgitb
import requests
import time
form=cgi.FieldStorage()
cgitb.enable()
logout='''
<form name="lout" method="POST" action="unscramble.html">
<input name="logout" type="submit" value="Logout">
</form>'''
#----------------------------------------------------------getting all words and making dictionary
f=open('dictall.txt','r')
a=f.read()
f.close()
b=a.split('\n')
b=b[:-1]
word=''
message=''
file=open('definitions.txt','r')
re=file.read()
file.close()
ad=re.split('\n')
if ad[-1]=='':
    ad=ad[:-1]
ad2=[]
for x in ad:
    ad2.append(x.split(','))
ad3={}
for y in ad2:
    ad3[y[0]]=y[1]
file=open('synonyms.txt','r')
be=file.read()
file.close()
bd=be.split('\n')
if bd[-1]=='':
    bd=bd[:-1]
bd2=[]
for x in bd:
    bd2.append(x.split(','))
bd3={}
for z in bd2:
    bd3[z[0]]=z[1]
#-------------------------------------------------------------------missingword?
checking=form.getvalue('checking','')
if checking !='':
    try:
        word=form.getvalue('mword','')
        if word in b:
            int(a)
        url="https://twinword-word-graph-dictionary.p.rapidapi.com/definition/?entry=THEWORD"
        url=url.replace('THEWORD',word)
        response = requests.get(url,  headers={
            "X-RapidAPI-Host": "twinword-word-graph-dictionary.p.rapidapi.com",
            "X-RapidAPI-Key": "key"
          }
        )
        r=response.json()
        meaning2=r['meaning']
        meaning=[]
        for x in meaning2:
            if meaning2[x]!='':
                meaning.append(x + ':' + meaning2[x])
        meaning='***'.join(meaning)
        meaning=meaning.replace('\n','<br>')
        meaning=meaning.split('***')
        meaning='<br>'.join(meaning)
        meaning=meaning.replace('(nou)','')
        meaning=meaning.replace('(vrb)','')
        meaning=meaning.replace('(adj)','')
        meaning=meaning.replace('(adv)','')
        meaning=meaning.replace(',','&')
        message="WOAH! You found a word that we don't have! You're so cool!"
        a=a+word+'\n'
        w=open('dictall.txt','w')
        w.write(a)
        g=open('definitions.txt','r')
        re=g.read()
        g.close()
        re+=word+','+ meaning + '\n'
        g=open('definitions.txt','w')
        g.write(re)
        g.close()
        k=open('synonyms.txt','r')
        ke=k.read()
        k.close()
        ke+=word+','+ meaning + '\n'
        k=open('synonyms.txt','w')
        k.write(re)
        k.close()
    except:
        message="Sorry! Either you typed your word wrong, it isn't a real word, or we already have it."
        meaning=''
    print('Content-type: text/html\n')
    z=open('isitamissingword.html')
    o=z.read()
    z.close()
    username=form.getvalue('username','')
    meaning=meaning.replace('&',',')
    if username=='':
        logout=''
    if message[0]!='S':
        o=o.replace('***isitamissingword***',message + '<br>' + word + ':' + '<br>' + meaning)
        o=o.replace('***logout***',logout)
    else:
        o=o.replace('***isitamissingword***',message)
        o=o.replace('***logout***',logout)
    print(o)
#---------------------------------------------------------------------------synonyms
wanttogetsynonyms=form.getvalue('wanttogetsynonyms','')
if wanttogetsynonyms!='':
    url2="https://twinword-word-graph-dictionary.p.rapidapi.com/association/?entry=THEWORD"
    url2=url2.replace('THEWORD',word)
    response2 = requests.get(url2,  headers={
        "X-RapidAPI-Host": "twinword-word-graph-dictionary.p.rapidapi.com",
        "X-RapidAPI-Key": "key"
      }
    )
    r2=response2.json()
    synonyms2=r2['assoc_word']
    synonyms='&'.join(synonyms)
#------------------------------------------------------------getting definitions
word=form.getvalue('word','')
username=form.getvalue('username','')
synonyms=''
if word!='':
    try:
        ad3[word]
        if ad3[word]!='':
             meaning=ad3[word]
             meaning=meaning.replace('&',',')
        else:
            try:
                url="https://twinword-word-graph-dictionary.p.rapidapi.com/definition/?entry=THEWORD"
                url=url.replace('THEWORD',word)
                response = requests.get(url,  headers={
                    "X-RapidAPI-Host": "twinword-word-graph-dictionary.p.rapidapi.com",
                    "X-RapidAPI-Key": "key"
                    }
                )
                r=response.json()
                meaning2=r['meaning']
                meaning=[]
                for x in meaning2:
                    if meaning2[x]!='':
                        meaning.append(x + ':' + meaning2[x])
                meaning='***'.join(meaning)
                meaning=meaning.replace('\n','<br>')
                meaning=meaning.split('***')
                meaning='<br>'.join(meaning)
                meaning=meaning.replace('(nou)','')
                meaning=meaning.replace('(vrb)','')
                meaning=meaning.replace('(adj)','')
                meaning=meaning.replace('(adv)','')
                meaning=meaning.replace(',','&')
                g=open('definitions.txt','r')
                re=g.read()
                g.close()
                re+=word+','+ meaning + '\n'
                re=re.replace('\n'+word+',\n','\n')
                g=open('definitions.txt','w')
                g.write(re)
                g.close()
            except:
                meaning='N/A'
    except:
        meaning="N/A"
    meaning=meaning.replace('&',',')
    if username!='':
        history=''
        history+=time.asctime()+'\n'
        history+='DEFINED:\n'
        history+=' ' + word + ': ' + meaning
        history+='\n*****\n'
        usernametxt='Histories/'+username+'.txt'
        file1=open(usernametxt,'r')
        e=file1.read()
        file1.close()
        file1=open(usernametxt,'w')
        file1.write(history+e)
        file1.close()
    try:
        bd3[word]
        if bd3[word]!='':
            synonyms=bd3[word]
        else:
            try:
                url2="https://twinword-word-graph-dictionary.p.rapidapi.com/association/?entry=THEWORD"
                url2=url2.replace('THEWORD',word)
                response2 = requests.get(url2,  headers={
                    "X-RapidAPI-Host": "twinword-word-graph-dictionary.p.rapidapi.com",
                    "X-RapidAPI-Key": "key"
                  }
                )
                r2=response2.json()
                synonyms2=r2['assoc_word']
                synonyms=''
                synonyms=','.join(synonyms2)
                if synonyms==[]:
                    int('a')
                u=open('synonyms.txt','r')
                ue=u.read()
                u.close()
                synonyms=synonyms.replace(',','&')
                if synonyms=='':
                    synonyms='N/A'
                ue+=word+','+ synonyms + '\n'
                ue=ue.replace('\n'+word+',\n','\n')
                u=open('synonyms.txt','w')
                u.write(ue)
                u.close()
            except:
                synoynms="N/A"
    except:
        synonyms='N/A'
    print('Content-type: text/html\n')
    if username=='':
        x=open('dictionary.html')
    else:
        x=open('dictionarylog.html')
    t=x.read()
    x.close()
    t=t.replace('***word***',word)
    meaning=meaning.replace('&',',')
    t=t.replace('***definition***',meaning)
    synonyms=synonyms.replace('&',',')
    if username=='':
        logout=''
    t=t.replace('***synonyms***',synonyms)
    t=t.replace('***logout***',logout)
    t=t.replace('***username***',username)
    print(t)
else:
    if form.getvalue('fback','')=='' and form.getvalue('checking','')=='':
        print('Content-type: text/html\n')
        if username=='':
            t=open('isitamissingword.html')
        else:
            t=open('isitamissingwordlog.html')
        u=t.read()
        if username=='':
            logout=''
        u=u.replace('***logout***',logout)
        u=u.replace('***isitamissingword***','Type Something in!')
        u=u.replace('***username***',username)
        print(u)
if form.getvalue('fback','')!='':
    h=open('messages.txt')
    hi=h.read()
    h.close()
    username=form.getvalue('username','')
    hi+=form.getvalue('fback','') + ',' + form.getvalue('username','') + '\n'
    u=open('messages.txt','w')
    u.write(hi)
    print('Content-type: text/html\n')
    if username=='':
        z=open('isitamissingword.html')
    else:
        z=open('isitamissingwordlog.html')
    o=z.read()
    z.close()
    if username=='':
        logout=''
    o=o.replace('***logout***',logout)
    o=o.replace('***isitamissingword***','Message Sent!')
    print(o)
