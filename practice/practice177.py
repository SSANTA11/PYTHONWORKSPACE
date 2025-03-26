nums=input().split()

num_1=int(nums[0])
num_2=int(nums[1])

save=[]

for i in range(1,num_1+1):
    if num_1%i==0:
        save.append(i)

if num_2<=len(save):
    print(save[num_2-1])

else:
    print("0")