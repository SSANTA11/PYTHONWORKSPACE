# list 내포 예시


# 짝수열 나열
list_a=[2*i for i in range(1,10+1)]
print(list_a) # append. 메서드 대신에 사용가능하다.


# 환률 계산
dollar=[155.43,302.71,77.46,131.28]
won=[d*1399 for d in dollar]
print(won)

# 우선순위가 정해진 표현식 반복문 조건문 순의 리스트 내포
l=[2*i for i in range(1,10+1) if 2*i%3==0]
print(l)