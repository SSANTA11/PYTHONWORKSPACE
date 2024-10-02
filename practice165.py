# 중앙 이동 알고리즘
f_num=2

T=int(input())

for t in range(T):
    num=f_num-1
    f_num=f_num+num

print(f_num**2)