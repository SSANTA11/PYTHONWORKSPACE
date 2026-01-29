while(True):
    n=input().split()
    if (n[0]==n[1]==n[2] and n[0]=='0'):
        break;
    l=[]
    for i in range(3):
       l.append(int(n[i]))
    l.sort()
    m=l.pop()
    sum=0
    for e in l:
        sum+=e**2
    if (m**2==sum):
        print("right")
    else:
        print("wrong")

