nums = input().split()
a = int(nums[0])
b = int(nums[1])

a_l = []
a1_l = []
b_l = []
a1 = 0
a2 = 0

for i in range(a + 1, 0, -1):
    if a % i == 0:
        a_l.append(i)

for i in range(b + 1, 0, -1):
    if b % i == 0:
        b_l.append(i)

for i in a_l:
    if i in b_l:
        a1 = i
        break
print(a1)

print(a*b//a1)