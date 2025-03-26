nums=input().split()

N=int(nums[0])
M=int(nums[1])

dict_a={i:i for i in range(1,N+1)}

for n in range(M):
    nums_1=input().split()
    i=int(nums_1[0])
    j=int(nums_1[1])
    dict_a[i],dict_a[j]=dict_a[j],dict_a[i]

for k in range(1,N+1):
    print(dict_a[k],end=' ')