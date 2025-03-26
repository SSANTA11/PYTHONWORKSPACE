nums_all=[]
nums_row=[]

for r in range(9):
    a=input().split()
    for c in range(9):
        nums_row.append(int(a[c]))
    nums_all.append(nums_row)
    nums_row=[]

num=0

for r in range(9):
    for c in range(9):
        if num <= nums_all[r][c]:
            num=nums_all[r][c]
            a=r
            b=c

print(num)
print(f"{a+1} {b+1}")