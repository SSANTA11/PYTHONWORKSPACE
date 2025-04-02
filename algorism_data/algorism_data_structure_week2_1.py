# 재귀함수와 팩토리얼 복잡도


def fac(num):
    if num==0:
        return
    for i in range(0,num):
        fac(num-1)
        print("a")
n=int(input())
print(fac(n))

# 두 결과 반환 가능한 파이썬
nums=input()
map(int,nums.split())
for i in range(len(nums)):
    print(f'{i}', end=' ')
print('\n')
for i in range(len(nums)):
    print(f'{type(i)}', end=' ')

# 지정된 범위의 수를 합한 결과를 반환하는 함수
def sum_range(begin, end, step=1):
    sum=0
    for n in range(begin, end, step):
        sum+=n
    return sum

def sum_recur(n):
    sum=0
    if n<1:
        return sum;
    else:
        sum=n+sum_recur(n-1)
    return sum

print(sum_recur(10))