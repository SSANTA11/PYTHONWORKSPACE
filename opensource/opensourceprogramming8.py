# 오픈 소스 프로그래밍 중간고사
# 50점 반에서 6등

# 문제1
# 포인트
    # 부등호에세 등호를 사용하지말라
    # {1:}
# 감점요인
    # 마지막 줄에 경계선 누락 등
# info=input("영화제목과 나이를 입력하세요: ").split()

# name=info[0]
# old=int(info[1])

# print("-"*25)

# if 13>=old:
#     print("|{0:^10}|    9,000원 |".format("name"))

# elif old<=19:
#     print("|{0:^10}|   12,000원 |".format("name"))

# else:
#     print("|{0:^10}|   15,000원 |".format("name"))

# 문제2
# 문제점: map 함수 미숙, 마무리 멘트 누락
# years=input("시작년도 끝년도: ").split()

# sy=int(years[0])
# ey=int(years[1])

# a=0
# for i in range(sy, ey):
#     if i%4==0:
#         if i%100==0:
#             if i%400==0:
#                 a+=366
#             else:
#                 a+=365
#         else:
#             a+=366
#     else:
#         a+=365

# print(a)
# 다른방법1
    # years=input("시작년도 끝년도: ").split()

    # sy=int(years[0])
    # ey=int(years[1])

    # a=0
    # for i in range(sy, ey):
    #     if i%4!=0:
    #         a+=365
    #     elif i%100!=0:
    #         a+=366
    #     elif i%400!=0:
    #         a+=365
    #     else:        
    #         a+=366

    # print(a)
# 다른 방법2
    # years=input("시작년도 끝년도: ").split()

    # sy=int(years[0])
    # ey=int(years[1])

    # a=0
    # for i in range(sy, ey):
    #     if i%400==0:
    #         a+=366
    #     elif i%100==0:
    #         a+=365
    #     elif i%4==0:
    #         a+=366
    #     else:
    #         a+=365

    # print(a)
# 다른 방법3
    # years=input("시작년도 끝년도: ").split()

    # sy=int(years[0])
    # ey=int(years[1])

    # a=0
    # for i in range(sy, ey):
    #     day=0
    #     if i%400==0:
    #         day=1
    #     elif i%100==0:
    #         day=0
    #     elif i%4==0:
    #         day=1
    #     a+=365+day

    # print(a)
# ===================================================================================================================== #
# 진도
# 리스트
    # 데이터에게 아파트를 지어주자
        # 기본자료형: 단독주택, 자료구조: 아파트
        # 파이썬은 C보다 자료구조가 많다.
# 데이터가 반복적으로 나온다고 해서 iterable object(반복가능한 객체) 이라 칭한다.

# 자료구조의 종류
    # 시퀸스(sequence) 형(->순서가 있다!!)
        # 리스트, 튜플, 문자열, range
            # 리스트와 튜플은 거의 비슷하나 리스트는 수정이 가능하고 튜플은 수정이 불가하다.(시퀸스는 리스트를 제외하고 모두 수정불가!)
    # 특수형
        # 딕션너리
        # 세트
        