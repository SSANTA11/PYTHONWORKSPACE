T=int(input())

for t in range(1,T+1):
    inp=input().split()
    A=int(inp[0])
    B=int(inp[1])
    print(f"Case #{t}: {A} + {B} = {A+B}")