x=int(input())
N=int(input())
list_a=[]
for n in range(N):
    input_a=input().split()
    a=int(input_a[0])
    b=int(input_a[1])
    c=a*b
    list_a.append(c)
all=sum(list_a)
if all==x:
    print("Yes")
else:
    print("No")