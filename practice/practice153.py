a=input()
counting=len(a)
l=[]
for i in range(counting):
    if a[i]==a[counting-1-i]:
        l.append(1)
    else:
        None

if len(l)==counting:
    print(1)
else:
    print(0)