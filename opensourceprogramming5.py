# 연산자 간의 우선순위는 외워두자 3장
# 왜 일까?
    # a,b,c,d=1,2,3,4
    # a and b > not c
    # 인터프리터는 시야가 좁기 때문에 n을 보고 없는 변수로 취급한다
    # 비교 연산자 등장 시 True는 숫자 1로 바뀐다.
    # 애시당초 C언어는 True, False가 없다!
   
    # print(c != a < b)는 and의 의미가 숨겨져 있다!!
    # print(a==b<c)->False
    # e=a and b
    # print(e)
    # e=a > b and c
    # False


# 데이터 2장
    # 할당된 변수를 재할당하면 기존의 피할당이었던 대상은 
    # 메모리에서 'garbege'로 취급하고 이러한 조무래기는 가비지 콜랙터가 수시로 정리한다.
    # 변수는 그러므로 타입이 無

# 자료형
    # 기본 자료형
        # int, float, complex(복소수), string, bool, NoneType
        # C언어는 string 無 character有
        # Python언어는 string有  character無
        # 정수형
            # 크기 제한이 없다
            # 문자열로 면환 시 더 이상 숫자열이 아님
            # bin()과 hexadedimal()은 각각 이진수 표현법과 16진수 변환 함수
                # 위 함수의 출력물은 문자열이다
        # 실수형
            # 나누기 시 정수라도 실수형으로 나온다
        # 불형
            # True, False
        # 문자열형
            # 묶음형 데이터 타입->장 교수님 전용 표현
            # ""=빈 문자열
            
            # """ """ 응용법과 사용사례
                # a="""
                # 안녕하세요
                # 오늘은 날씨가 참 '좋습니다'.
                # 오르막길과 내리막길 "음치키"으치키"""
                # print(a)
                    # 
                # 할당하지 않으면 메모리의 가비지가 된다.
                # 독스티링(docstring): 클래스 등의 것을 부연 설명할 때 사용 -> ''' '''을 활용

                # 이스케이프 문자
                    # \, \n, \t, \\, \, \', \", \b(=backspace)
            # 문자열 연산
                # 더하기-> concatnate하여 하나늬 문자열로 만든다
                # 곱하기
            # len()
                # 문자열에서만 사용가능!!

# # i=0
# # while True:
    
# #     i+=1
# #     print("-=-"*i)
# a=12.34
# b=str(a)



# a="hello, world!"
# print(a.upper())
# print(a.isupper())
# print(a.lower())
# print(a.islower())
# print()
# print('-'*20)
# print(a.find("l",3))
# print('-'*20)
# print(a.split('or')) #->or처럼 split함수 괄호 안에 것을 '구분자'라고 한다.
# print(a[0],a[1])
# print('-'*20)
# print(a.count('p'))

            # 문자열 內 특정 문자를 검색: 인덱싱
                # 형태->문자열[숫자(=인덱스)]
                # 양수와 음수 주의!
            # 문자열 일부 선택: 슬라이스와 슬라이싱
                # 형태->문자열[시작:끝[:증가분]]->내부의 대괄호는 실표기가 아니라 option의 의미를 지니고 있다
# print(a[::-1])
# print(a[len(a):-1:-1])->볼 때마다 다시 한 번 이해하기

# 제어문
    # 조건문과 반복문
# 여기까지-=-=-=-=-=-==-==-==-=-==-=-=-=-=---------------------------------------------------------------------------