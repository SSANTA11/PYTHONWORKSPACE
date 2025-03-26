while True:
    inputs = input().split()
    a = int(inputs[0])
    b = int(inputs[1])
    if a == 0 and b == 0:
        break
    print(a + b)
