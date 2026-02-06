n = int(input())
word = input()
sum = 0
r = 0
for i in word:
    tmp = ord(i) - 96
    sum += tmp * 31 ** r
    r += 1
print(sum % 1234567891)
