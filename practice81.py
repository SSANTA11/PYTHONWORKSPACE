import sys

input=sys.stdin.readline

T=int(input())

for t in range(T):
    input_a=input().split()
    A=int(input_a[0])
    B=int(input_a[1])
    print(A+B)