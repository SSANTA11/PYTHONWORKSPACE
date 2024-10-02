num=int(input())
fnum=num*2-1
for i in range(1,num):
    print(f'{" "*((num-1)-(i-1))}{"*"*(2*i-1)}')
    
print("*"*fnum)

for i in range(1,num):
    print(f'{" "*i}{"*"*(2*(num-i)-1)}')