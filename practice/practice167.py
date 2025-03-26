num=int(input())
a=1
if num==1:
    print(1)
else:
    for i in range(2,1000000000):
        if a<num<=a+6*(i-1):
            print(i)
            break
        else:
            a+=6*(i-1)
            continue

