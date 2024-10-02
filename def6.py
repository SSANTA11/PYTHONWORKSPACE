def ch(a):
    a=a.replace(' ','')
    a=a.replace('!','')
    a=a.replace('?','')
    a=a.replace('.','')
    a=a.replace(',','')
    a=a.replace(':','')
    a=a.replace(';','')
    b=a[::-1]
    if b==a:
        print(True)
    else:
        print(False)
a=input("...")
ch(a)
