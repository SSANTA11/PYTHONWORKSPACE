m = input().split()
N = int(m[0])
X = int(m[1])
nums=input().split()
list_a=[int(nums[i]) for i in range(N)]
a=0
list_b=[]
for i in range(N):
    if list_a[i]<X:
        list_b.append(list_a[i])
    else:
        continue

for lis in list_b:
    print(lis, end=' ')

# 기억할 점
    # 리스트 반복문
    # end 매개변수 사용법