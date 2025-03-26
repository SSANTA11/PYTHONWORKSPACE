# # 2주차 시작. 추상 자료형(ADT)
# ★추상 자료형(ADT)
    # 자료구조가 다루는 데이터와 연산의 종류를 정의한 것
    # 어떻게 다루는지는 실재로 자료구조를 구현하는 사람의 몫

# ★'가방'의 추상자료현
#     # 데이터: 중복된 항목을 허용하는 자료들의 모임, 자료들 사이에 순서는 없지만 서로 비교가능해야 함<가방이 다루는 자료들>
#     # 연산: insert(e), remove(e), contain(e), count(e) <물건 넣기, 물건 꺼내기, 내용물 확인하기 등>

# def insert(bag, e):
#     bag.append(e)

# def remove(bag, e):
#     bag.remove(e)

# def contain(bag, e):
#     return e in bag

# def count(bag, e):
#     return len(e)

# # myBag=[]

# # insert(myBag,"휴대폰")
# # insert(myBag,"손수건")
# # insert(myBag,"차키키")
# # insert(myBag,"도시락")
# # insert(myBag,"책")
# # insert(myBag,"시계계")
# # insert(myBag,"야구공")
# # print("가방에 뭐가 들어있을까?\n")
# # print("가방 속의 물건: ",myBag)
# # print()
# # print('-=-'*35)

# # myBag.remove("손수건")
# # print("가방 속의 물건: ",myBag)

# # ★알고리즘의 성능 분석
#     # 실행시간을 측정하는 방법
#         # 실제 실행시간을 측정-> 가장 확실
#         # 알고리즘을 실재로 구현해야함함
#         # 동일한 hw/sw환경 사용
#     # 알고리즘의 '복잡도'를 분석하는 방법
#         # 직접 구현하지 않고 수행시간 분석
#         # 연산의 횟수를 측정하여 비교-> ex)sum+=1-> 2번 연산
#               -> 왜냐하면 sum=sum+1 할당 한 번, 합 한 번(물론 각각의 속도는 다르지만, 차가 크고 고정된 값이 아니라 무시해도 된다.)
#         # 연산의 횟수는 입력의 크기 n의 함수
#             # '시간' 복잡도 분석: 수행 시간 분석
#             # '공간' 복잡도 분석: 필요한 메모리 공간 분석석

# import time
# myBag=[]
# start=time.time()

# insert(myBag, '축구공')

# end=time.time()
# print("실행시간: ", end-start)

# ★복잡도의 점근적 표기(빅오 표현법)
    # 계수 없이 최고차항만 취하여 단순하게 표현하는 방법
    # 상한(빅오: O(g(n)), 하안(빅오메가), 동급(빅 세타 표기법)
# ★입력 데이터에 따른 성능 차이
    # 최선: 수행시간이 가장 빠른 경우
    # 평균: 평균의 의미 의미가 모호함, 계산하기 어려움
    # 최악: 가장 늦은 경우-> 가장 널리 사용

# ★복잡도 분석의 예: 순차 캄색
    # 배열에서 어떤 값의 위치를 찾는 알고리즘
    # 기준연산?-> 가장 많이 수행되는 연산
    # 입력의 크기?

# def search(A,key):
#     n=len(A)
#     for i in range(n):
#         if A[i]==key:
#             return i
#     return -1

# 순환 알고리즘
    # 반복
    # 재귀
