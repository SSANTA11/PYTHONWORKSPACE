# 전개연산자
# print(max(*a)) 전개를 해준다의 의미???

# a=reversed(range(0,10))
# for i in a:
#     print(i)
# for i in a:
#     print(i)
# 위의 반복문 중 하단의 반복문은 씹히게 된다. 이는 이터레이터라는 개념과 연관되어 있는데
# 이 개념은 이후에 클래스까지 배워야 알 수 있는 개념임으로 미루어 이해하자!
# reversed() 함수의 결과는 제너레이터이기 때문에 두번째가 출력이 안되는 것이다.

# enumerate() 함수

# fruits=["바나나","사과","포도"]
# a=enumerate(fruits)
# i=0
# for fruit in fruits:
#     print(f"{i}:{fruit}")
#     i+=1


# 튜플이 나오는 enumerate함수
# fruits=["banana","apple","grape"]
# a=enumerate(fruits)
# print(list(a))

# "for index, 값 in enumerate(리스트)" 반복문은 통으로 외우기!!

