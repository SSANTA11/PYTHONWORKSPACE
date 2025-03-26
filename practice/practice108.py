list_a=[]
while True:
    inputs=input().split()
    a=(inputs[0])
    b=(inputs[1])
    list_a.append([a,b])

i=len(list_a)
for j in range(i):
    print(int(list_a[j][0])+int(list_a[j][1]))