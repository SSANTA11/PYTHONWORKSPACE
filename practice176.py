inp=input().split()
a=int(inp[0])
b=int(inp[1])

if b%a==0:
    print("factor")
elif a%b==0:
    print("multiple")
else:
    print("neither")