a=[None]*101
for n in range(1,100+1):
    if (n==1) or (n==2):
        a[n]=1
    else:
        a[n]=a[n-1]+a[n-2]

print(a)