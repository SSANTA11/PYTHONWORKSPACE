# i=0
# for i in range(0,10):
#     i+=1
# print(i)
# dict={'a':1,'b':2}
# dict["a"]=2
# print(dict)
# print(dict.keys())


# 사용자 정의 함수

# 함수의 정의와 호출
def find_min_max(A):
    min=A[0]
    max=A[0]
    for i in range(1,len(A)):
        if max<A[i]:
            max=A[i]
        if min>A[i]:
            min=A[i]
    return min, max
data=[1,2,3,4,5,76,7000]
x,y=find_min_max(data)
print("(min, max)= ", (x, y))
