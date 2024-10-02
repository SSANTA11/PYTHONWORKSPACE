num=input().split()
N=int(num[0])
M=int(num[1])

dict_a={}
a=0
for n in range(N):
    dict_a[n+1]=0

for i in range(M):
    nums=input().split()
    i=int(nums[0])
    j=int(nums[1])
    k=int(nums[2])
    for r in range(i,j+1):
        dict_a[r]=k

for h in range(N):
    print(dict_a[h+1], end=' ')