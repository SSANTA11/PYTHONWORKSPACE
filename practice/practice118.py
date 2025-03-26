# 1번 방식
N=int(input())

nums=input().split()

list_a=[int(nums[i]) for i in range(N)]

list_a.sort()

print(f"{list_a[0]} {list_a[N-1]}")


# 2번 방식
# N=int(input())

# nums=input().split()

# nums.sort()

# print(f"{nums[0]} {nums[N-1]}")

# 2번 방식은 문자열 정렬이기 때문에 숫자 오름차순 정리가 되지 않는다.