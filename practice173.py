# 힙과 스택
    # a=10
    # b=[1,2,3,4]
    # def fun_1(c,d):
    # 	c=20
    # 	d=[5,6,7,8]
    # fun_1(a,b)
    # print(a,b)
    # def fun_2(c,d):
    # 	c=20
    # 	d.extend([9,10])
    # fun_2(a,b)
    # print(a,b)

# 재귀함수

def factorial(n):
    output=1
    for i in range(1,n+1):
        output*=i
    return output

print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))