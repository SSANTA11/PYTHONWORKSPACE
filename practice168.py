x=int(input())
s=1
if x==1:
    print('1/1')
else:
    for i in range(2,100000000+1):
        if s<x<=s+i:
            if i%2==0:
                print(f'{i-(s+i-x)}/{1+(s+i-x)}')
            else:
                print(f'{1+(s+i-x)}/{i-(s+i-x)}')
            break
        else:
            s+=i
            continue