                # C언어를 제외하면 포인터라는 개념이 있다. 이 포인터가 가르킴을 참조(referencing)라고 한다.
                # 파이썬은 참조를 숨긴다.
# 할당과 복사
    # 사전 지식: 컴퓨터 메모리
        # 컴퓨터의 기억장치는 CPU가 사용하는 프로그램과 데이터를 저장하는 장치임
        # 메모리에는 워드라는 단위로 메모리를 구획지어 놓고 각 워드에 주소라는 정수값을 설정해 두고 있다. 모든 메모리에는 유일한 주소를 가짐
        # CPU는 이 주소를 이용하여 원하는 장소의 메모리에서 데이터를 가져오거나 저장함.

    # 할당
        # 할당한다는 10이라는 정수를 메모리에 두고 그 메모리의 주소를 a가 참조하느 것

    # 복사
    # 일차원은 단순 카피로 단순 해결 가능하다
        # a=[[1,2,3],[4,5,6]]
        # b=a.copy()
        # b[0][1]=200
        # print(b[0][1])
        # print(a[0][1])
    # 이차원 이상의 리스트는 카피 함수만으로는 해결불가
        # 해결방안은 deepcopy() 외장함수를 import해주고 사용하면 된다.

# 컴프리헨션(comprehension)->직역하지 마시오!!(이해로 해석하기 애매함)**************************************************************************************
    # 리스트 컴프리헨션(리스트 내포)
        # 변수=[표현식 반복문]
        # 변수=[표현식 조건문]

    # a=[i*10 for i in range(10)]
    # print(a)

    # ascii=[ord(ch) for ch in 'abcdef']
    # print(ascii)

    # a=[]
    # for i in range(10):
    #     a.append(i*10)
    # print(a)

    # ascii=[]
    # for ch in 'abcdef':
    #     ascii.append(ord(ch))
    # print(ascii)

    # # 컴프리헨션의 확장
    # c=[i for i in range(10) if i%2==0]
    # print(c)

    # # 두 개의 변수로 컴프리헨션 구성
    # v=[i*j for i in range(2,10) for j in range(1,10)]
    # print(v)

    # # 중첩 컴프리헨션
    # import pprint
    # b=[[i*j for i in range(1,10)] for j in range(2,10)]
    # pprint.pprint(b)

    # # 컴프리헨션과 반복하기 기능
    # a=[3 for i in range(3) for j in range(4)]
    # a[0]=5
    # print(a)

    # a1=[3]*12
    # a1[0]=5
    # print(a1)

    # # comprehension
    # b=[[3 for i in range(3)]for j in range(4)]
    # b[0][0]=5
    # print(b)

    # # 반복하기 문제점
    # # 이차원 이상부터는 문제가 된다
    # c=[[3]*3]*4
    # c[0][0]=5
    # print(c)

    # 중첩for문
    # range
    # 반복하기

# 튜플 컴프리헨션
    # 소괄호 안에 쓰는 것은 불가-> 제너레이터라는 고급함수
    # 그러므로 tuple=(comprehension)

# 딕션너리의 컴프리헨션
    # 세트는 중괄호 활용

# l=[i+j for i in range(1,7) if i%2==0 for j in range(1,7) if j%2==1]
# print(l)

# from random import randint

# b={randint(0,9) for i in range(10)}
# print(b)

# 함수 만들기
    # 함수를 만들지 않고 프로그램은 가능
    # 프로그램을 효율적으로 만들기 위해 구조적인 틀 필요
    # 더 체계적으로 프로그램을 만들려면->객체(class)->각자 공부!!!!!!!!!!!반드시!!!!!!!!!!!

    # 함수 호출 형식
    # 기본형
        # 함수이름()
            # 함수 내용이 시작하고 끝나는 형태
    # 변수=함수이름()
        # 함수 내용이 실행되고 반환값이 변수로 저장되는 형태

    # 함수이름(없거나or인수1,인수2,...)

    # print()는 리턴값이 없다.
        # ret=print()
        # print(ret)

# 함수 정의
    # def 함수이름(없거나or 매개변수1,매개변수2,....):
    #     함수내용
    # return 반환값
        # 반환할 값이 없다면 안써도 되고 
        # 함수를 끝내고 싶은 시점에 사용될 수 있따.

    # 매개변수(parameter)와 인수(argument)
        # 매개변수는 버스 터미널
        # 인수는 버스

# import turtle as t

# t.turtlesize(4)

# t.shape("turtle")

# def t_square(size):
#     for i in range(4):
#         t.forward(size)
#         t.right(90)

# t_square(100)
# def t_polygon(size,vertex):
#     if vertex<3:
#         print("최소한 삼각형 이상이 되어야 합니다")
#         return
#     for i in range(vertex):
#         t.forward(size)
#         t.left(360/vertex)

# t_polygon(100,5)

# def t_circle(size,angle):
#     for i in range(int(360/angle)):
#         t.circle(size)
#         t.left(angle)
# t_circle(50,60)
# t.clear()

# tkinter 색 사용
# PyQt6 색 사용

# 반환값(return value)
# 함수 반환값 유무
    # 합 구하기 함수

# 시험************************************************
# 이러이러한 결과가 나오는 함수를 만드시오

# 여러개의 반환값
    # 함수의 반환 값을 두 개 이상 지정할 수 있다.
    # 여러 개를 반환하는 것처럼 보이지만 사실 튜플 하나를 반환한다
    # ex)
def calc(a,b):
    return a+b,a-b,a*b,a/b
calc(10,5)
a,b,c,d=calc(10,5)

# 인수와 매개변수 
    # 매개변수 초기화
    # 함수 정의에서 매개변수에 default값 지정
    # 초기값이 있는 매개변수는 함수 사용에서 인수를 넣지 않으면 초기값으로 지정
    # 형식: def 함수명(매개변수1,매개변수=초기값):
def greeting(st,name='guest'):
    print(st,name)
# 초기화하는 매개변수를 뒤에 두어야 한다.

