a=[None]
for n in range(1,1000+1):
    a_n=2*n-1
    a.append(a_n)

print(a)

print()

print("정수 n이 1 이상 1000 미만일 때, \n등차수열 2n-1을 계산해드립니다!")
print()

nat=int(input("n에 넣을 정수를 입력해주세요!\n>>>"))

def 함수(nat):
    ㅊ=a[nat]
    print(ㅊ)

함수(nat)