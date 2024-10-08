# 파이썬이 이해하는 방식은 연속성이 요구된다
    # 새로운 변수가 등장한다고해서, 
    # 변수의 그 의미가 등장할 순간에 곧바로 정의되지는 않는다

# 코드 블록: 조건문이나 반복문에서 나타나는 들여쓰기
    # 대부분의 언어들은 들여쓰기 대신 중괄호를 사용한다
    # 때문에 파이썬은 에러의 위험성을 지니고 있다

# 파이썬의 문장은 한 줄이다
# 그러나 두 줄이 한 명령어인 것은 가능하다
    # ex) 조건문과 조건문의 코드 블록
# Enter를 누르더라도 괄호가 열린 채로 줄이 바뀌었으면 
# 괄호가 마무리 될 때까지 문장은 종료되지 않는다.
# conotation mark은 해당없음

# print("apple")

# print("app
# le") 
# 줄바꿈시 어려움


# 에약어==키워드
    # 모두 33개
    # 제어문(조건문, 반복문) 등의 것들이 포함되어 있다.

# 식별자 규칙
    # 흔히 알려진 아이디도 identifier(식별자)에서 나온 단어이다


    # 식별자
    #   ㄴ스네이크케이스 (apple_pie)
    #        ㄴ괄호有
    #             ㄴ함수 (apple_pie())
    #        ㄴ괄호無
    #             ㄴ변수 (apple_pie)
    #   ㄴ캐멀캐이스
    #        ㄴ클래스 (ApplePie)


# 항시 영어만을 사용하여 프로그래밍 하자
# 잘못된 변수나 함수의 네이밍(naming)은 정신건강에 해롭다
    # 상시 영어제목 작성을 연습하자

# 연산자
#   ㄴ산술
#   ㄴ대입(할당)
#   ㄴ비교
#   ㄴ논리
#   ㄴ연산자 우선순위: 비트 연산자 예){:d}.format(상수)

#   ㄴ종류
#       ㄴ(),**,(*,/),(+,-),% 등


# F=float(input("화씨로 변환하고 싶은 섭씨온도를 기입하세요"))
# C=(F-32)*5/9
# print(C)

# bill=int(input("1200원 음료수를 구매하기 위한 5만원 미만 지폐 한 장을 투입하세요\n>>>"))
# if bill==10000:
#     print("거스름돈 8800원입니다.")
# elif bill==5000:
#     print("거스름돈 3800원입니다.")
# elif bill==1000:
#     print("거스름돈 1000원입니다.")
# else :
#     print("단일 지폐만을 투입하세요!")
# # a=

# print(f"계산된 거스름돈은 {output}원입니다!")


# a=int(input("첫번째 점에 해당되는 x 좌표를 기입하세요!"))
# b=int(input("첫번째 점에 해당되는 y 좌표를 기입하세요!"))
# c=int(input("두번째 점에 해당되는 x 좌표를 기입하세요!"))
# d=int(input("두번째 점에 해당되는 y 좌표를 기입하세요!"))

# d=((a-c)**2+(b-d)**2)**0.5
# print(d)


# 대입연산자
    # l-value, r-value -> 왼쪽 항(변수 자리), 오른쪽항(값이 등장하는 자리)
# a,b,c=10,20,30
# print(a)
# print(b)
# print(c)

# 튜플
# a=10,20,30
# print(a)

# 복합 연산자 
    # 변수 연산자= 상수 등

# a=7
# a/=2
# print(a)


# 할당 연산자의 우선순위는 거의 최하위이다

# money=10000
# money=int(input("철수가 받은 용돈은..."))

# money-=3000
# money-=500
# money-=1900
# print(f"철수의 남은 용돈은 {money}원입니다!")



# 부등호 사이에 변수가 끼어있는 형태는 파이썬에서만 적용가능하다!

# s2="Iood morning, everybody!"
# s1="I pm a student."
# s1>s2
# -> ASCII코드 값이 더 크다

# 논리연산자
# and
# or
# not

# 논리값 False가 되는 것들
    # 정수
    # 실수
    # 빈 문자열
    # 비어있는 묶음자료형
    # None

# 심화: 효율적인 논리 판단
    # a and b: 둘 중 하나만 거짓이면 나머지는 알 필요가 없다 -> 당연히 거짓
    # a or b: 둘 중 하나만 참이면 나머지는 알 필요가 없다 -> 당연히 참


# print(a<b or c<d)
# # 파이썬은 논리 연산 결과를 논리값을 만들어서 내보내지 않는다

# ==,!=,=,복합연산자는 모두 동순위이다.

# # not >and >or 우선 순위 순
a,b,c,d=1,2,3,4
print(not a > b and c>d)
# print(a and b > not c)
# print(a>True)
# print(a!=b>c)
# result=2>1
# print(int(result))