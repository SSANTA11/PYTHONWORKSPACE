inp=input().split()
a=int(inp[0])
b=int(inp[1])
while (a!=0 and b!=0):
    if a==0 and b==0:
        break
    elif a==0 or b==0:
        print("neither")
    elif b%a==0:
        print("factor")
    elif a%b==0:
        print("multiple")   
    else:
        print("neither")
    inp=input().split()
    a=int(inp[0])
    b=int(inp[1])    