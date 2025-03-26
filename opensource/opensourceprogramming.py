# 조건문...저번시간....
# 반복문
# for 반복문
    # for i in range(3):
    #     print("만세")
    # (iterable object) -> (반복가능한 객체)
    # 묶음 자료형은 거의 반복가능한 객체이다.
    # name='python'
    # for i in name:
    #     print(i, end='/ ') 
        # print(i) -> 위와 같은 반복문은 시험에 출제

# range 탐구 
    # 형태: range(시작, 끝, [증분])(=>슬라이싱과 유사하다->[ : : ])
        # 슬라이싱의 숫자 -> 인덱스
        # range의 숫자 -> 실재 숫자
    # 인덱싱, 슬라이싱
    # 증가분이 2이다 -> 나오는 숫자=1 3 5 7 9
    # print(type(range(1,10))) -> 클래스 range
    # 리스트는 중간고사 이후에 나온다...!
    # print(list(range(1,10)))
    #
    # for i in range(10000):
    #     print('만세')
    # C에서는 for 반복이 while과 별다른 차이가 없다
    # itch 반복문???***

                                                #3번의 기회를 주는 퀴즈 만들기 재도전************************ 
                                                    # a=int(input("숫자를 맞춰보세요!!: "))

                                                    # for i in range(3):
                                                    #     if a>5:
                                                    #         print(f"{a}보다는 작습니다")
                                                    #     elif a<5:
                                                    #         print(f"{a}보다는 큽니다")
                                                    #     else:
                                                    #         print("정답입니다!!")
# ANSI->utf8, cp949 -> 학습!


# 모듈(=라이브러리) 사용하기
    # import 모듈
    # from 패키지 import 모듈
            
        # from random import radiant, choice
        # radiant(1, 45)
            # from을 사용하게 되면 선택적인 기능을 수행할 수 있기 때문에 메모리 효율적이다

        # from random import * 
            # '*'은 모든 것을 의미함, 유용하지만 프로그램이 무거워짐

# install은 파이썬에 기본 설치되지 않은 모듈을 의미하고 이러한 모듈을 설치하는 것을 pip라고 지칭한다
# 기본함수 (0부터 1사이)
    # import random
# 특정범위의 무작위 
    # print(random.randint(1,45))
# 여러 개의 값 중에서 무작위로 하나 선택
    # random.choice('absdfsfrfsdfsdfasd')
                                    # from ppp.abc import func
                                        # ppp안에 abc라는 파일 안에서 func라는 기능을 사용한다
                                        # func는 다양하다(?)
# import numpy as np
# np.array()
# import pandas as pd
# import matplotlib.pyplot as plt
# plt.show()

# from random import randint

# b=randint(1,45)

# a=int(input())
# for i in range(1,3+1)
#     if b>5:
#         print(f"{a}보다는 작습니다")
#     elif b<5:
#         print(f"{a}보다는 큽니다")
#     else:
#         print("정답입니다!!!")


# 로또 출력물 만들기

# for i in range(6):
#     from random import randint
#     b=randint(1,45+1)
#     print(b, end=', ')
# print
# 중복 문제는 어떻게 해결하는가?

# 난수 초기화를 알아봅시다 -> 시험엔 안나오나 쳇 지피티로 공부하기
# randrange와 randint 차이점 쳇지피티 -> 시험엔 안나오나 쳇 지피티로 공부하기

# total=0
# for i in range(1,10+1):
#     total+=i
# print(total)

# 중첩 for 반복문

# 구구단 중 2단을 출력

# for i in range(1,19+1):
#     for j in range(1,19+1):
#         print(f'{i}x{j}={j*i}', end=' ')

# while True:
#     print("무한반복 가즈아", end=' ')

# 클라우드 리소스??

# 파이썬에선 for문이 무한루프를 돌기 힘들지만 돌릴 수는 있다

# i=0
# while True:
#     i+=1
#     print(f"반복: {i}")
#     if i>5:
#         break

#     for i in range(1,20):
#         if i%5==0:
#             print("%2d"%i)
#             continue
#         print()

import random
a=random.randint(1,45+1)

for i in range(1,10+1):
    num=int(input("숫자를 맞춰보세요"))
    if a<num:
        print(f"{num}보다 작습니다")
    elif a>num:
        print(f"{num}보다 큽니다")
    else:
        print("정답입니다!")