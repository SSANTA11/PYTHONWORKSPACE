바구니=input().split()

N=int(바구니[0])
M=int(바구니[1])

현황={}
for a in range(1,N+1):
    현황[a]=a

for b in range(1, M+1):
    입력=input().split()
    i=int(입력[0])
    j=int(입력[1])
print(i, j)