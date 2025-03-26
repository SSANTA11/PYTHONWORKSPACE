print("------"*30)


# 초안

print("# 초안")
for i in range(1,9+1):
    for j in range(2,6+1):
        b=("{0:>3}".format(i*j))
        a=(f"{j} x {i} ={b}")
        print("{0:>15}".format(a), end="")
    print()
print()
for i in range(1,9+1):
    for j in range(7,11+1):
        b=("{0:>3}".format(i*j))
        a=(f"{j} x {i} ={b}")
        print("{0:>15}".format(a), end="")
    print()
print()
for i in range(1,9+1):
    for j in range(12,16+1):
        b=("{0:>3}".format(i*j))
        a=(f"{j} x {i} ={b}")
        print("{0:>15}".format(a), end="")
    print()
print()
for i in range(1,9+1):
    for j in range(17,19+1):
        b=("{0:>3}".format(i*j))
        a=(f"{j} x {i} ={b}")
        print("{0:>15}".format(a), end="")
    print()

print("------"*30)


# 수정안
print("# 수정안")
k=0
for r in range(1,4+1):
    for i in range(1,9+1):
        for j in range(2+k,6+k+1):
            if j<=19:
                b=("{0:>3}".format(i*j))
                a=(f"{j} x {i} ={b}")
                print("{0:>15}".format(a), end="")
        print()
    k+=5
    print()

print("------"*30)


