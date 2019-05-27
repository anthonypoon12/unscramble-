checker=''
def check(a,theinput1):
    checker=theinput1
    for y in a:
        if y in checker:
            checker=checker[:checker.find(y)]+checker[checker.find(y)+1:]
        else:
            return 0
    return 1
    checker=theinput1
theinput='aordef'
allwords=open('dictall.txt').read().split('\n')
allwords=allwords[:-1]
themaybewords=[]
for x in allwords:
    if len(x)<=len(theinput):
        themaybewords.append(x)
thewords=[]
for z in themaybewords:
    if check(z,theinput)==1:
        thewords.append(z)
print('Content-type: text/html\n')
print('''
<html>
<body>
%s
</body>
</html>''' % (','.join(thewords)))

