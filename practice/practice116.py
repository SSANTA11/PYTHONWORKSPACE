N=int(input())
num=input().split()
list_a=[]

for i in range(0,N):
    list_a.append(int(num[i]))
list_a.sort()

dict_a={}

for r in range(-100, 100+1):
    dict_a[r]=0

for i in range(0,N):
    dict_a[list_a[i]]+=1

v=int(input())

print(dict_a[v])