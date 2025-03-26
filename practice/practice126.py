num=input().split()
N=int(num[0])
M=int(num[1])
bask={}

for n in range(1,N+1):
    bask[n]=n

a=bask.copy()
for m in range(1,M+1):
    nums=input().split()
    i=int(nums[0])
    j=int(nums[1])
    while i<=j:
        bask[i],bask[j]=bask[j],bask[i]
        i+=1
        j-=1
for n in range(N):
    print(bask[n+1], end=' ')