
T=int(input())
for i in range(T):
    input_a=input().split()
    R=int(input_a[0])
    S=input_a[1]
    num=int(len(S))
    for n in range(num):
        print(S[n]*R, end='')
    print()
