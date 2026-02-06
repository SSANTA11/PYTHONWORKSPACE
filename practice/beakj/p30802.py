N = input()
S, M, L, XL, XXL, XXXL = map(int, input().split())
T, P = map(int, input().split())

sum = S + M + L + XL + XXL + XXXL
Tsize=[ S, M, L, XL, XXL, XXXL]
TPackCount=0
for i in Tsize:
    if i/T>i//T:
        TPackCount += i//T+1
    else:
        TPackCount += i//T

Pcount = sum // P
Prest = sum - Pcount*P

print(f"{TPackCount}\n{Pcount} {Prest}")
