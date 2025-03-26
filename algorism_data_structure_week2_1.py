# 재귀함수와 팩토리얼 복잡도


def fac(num):
    if num==0:
        return
    for i in range(0,num):
        fac(num-1)
        print("a")
n=int(input())
print(fac(n))

nums=input()
map(int,nums.split())
for i in range(len(nums)):
    print(f'{i}', end=' ')
print('\n')
for i in range(len(nums)):
    print(f'{type(i)}', end=' ')