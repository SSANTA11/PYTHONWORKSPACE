matrix=input().split()
col=int(matrix[0])
ro=int(matrix[1])

a=[]
b_1=[]
b_2=[]
b_3=[]
for i in range(col):
    num=input().split()
    for r in range(ro):
        a.append(num[r])
    b_1.append(a)
    a=[]

for i in range(col):
    num=input().split()
    for r in range(ro):
        a.append(num[r])
    b_2.append(a)
    a=[]

for i in range(col):
    b_3.append(a)

# 마지막 계산
for i in range(col):
    for r in range(ro):
       print(int(b_1[i][r])+int(b_2[i][r]), end=' ')
    if r==2:
        print()