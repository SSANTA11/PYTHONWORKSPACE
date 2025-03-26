a=10
b=[1,2,3,4]

print(a,b)

def function_a(c,d):
    c=20
    d=[5,6,7,8]
print(function_a(a,b))
print(a,b)

def function_b(c,d):
    c=30
    d.extend([9,10])
print(function_b(a,b))
print(a,b)
