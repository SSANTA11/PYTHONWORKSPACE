table={}

for r in range(100):
    for c in range(100):
        table[f"{r}*{c}"]=0

paper_num=int(input())

for i in range(paper_num):
    st_point=input().split()
    r=int(st_point[0])
    c=int(st_point[1])
    for i in range(r,10+r):
        for n in range(c,10+c):
            table[f"{i}*{n}"]+=1

count=0

for r in range(100):
    for c in range(100):
        if table[f"{r}*{c}"]>0:
            count+=1

print(count)