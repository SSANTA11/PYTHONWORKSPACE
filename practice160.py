l_a=[]
l_b=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

for i in range(5):
    a=input()
    b=len(a)
    for r in range(b):
        l_b[r].append(a[r])

for i in range(15):
    for r in range(len(l_b[i])):
        print(l_b[i][r],end="")