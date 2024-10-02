# 킹 퀸 룩 비숍 나이트 폰
fm=[1,1,2,2,2,8]
piece=input().split()
nums=[]

for i in range(6):
    nums.append(int(piece[i]))
final_num=[]
for i in range(6):
    final_num.append(fm[i]-nums[i])
for i in range(6):
    print(final_num[i],end=" ")