
while True:
    n=input()
    if n=='0':
        break
    flag=0
    for i in range(len(n)):
        if n[i]!=n[len(n)-i-1]:
            flag=1
            break
    if flag==0:
        print('yes')
    else:
        print('no')