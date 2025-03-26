list_a=[]
for i in range(9):
    a=int(input())
    list_a.append(a)
list_b=list_a.copy()
list_a.sort()

print(list_a[8])

for i in range(0,8+1):
    if list_b[i]==list_a[8]:
        print(i+1)
    else:
        None
