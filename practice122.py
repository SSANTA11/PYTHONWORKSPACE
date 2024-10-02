stus={i:0 for i in range(1,30+1)}
for n in range(28):
    stu=int(input())
    stus[stu]+=1

for r in range(1,30+1):
    if stus[r]==0:
        print(r)
    else:
        continue