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
    # def find_min_max(A):
    #     min=A[0]
    #     max=A[0]
    #     for i in range(1,len(A)):
    #         if max<A[i]:
    #             max=A[i]
    #         if min>A[i]:
    #             min=A[i]
    #     return min, max
    # data=[1,2,3,4,5,76,7000]
    # x,y=find_min_max(data)
    # print("(min, max)= ", (x, y))


# 두 결과 반환 가능한 파이썬
    # nums=input()
    # map(int,nums.split())
    # for i in range(len(nums)):
    #     print(f'{i}', end=' ')
    # print('\n')
    # for i in range(len(nums)):
    #     print(f'{type(i)}', end=' ')

# 지정된 범위의 수를 합한 결과를 반환하는 함수
    # def sum_range(begin, end, step=1):
    #     sum=0
    #     for n in range(begin, end, step):
    #         sum+=n
    #     return sum

def sum_recur(i):
    if i<1:
        return 0
    else:
        return i+sum_recur(i-1)

print(sum_recur(10))
