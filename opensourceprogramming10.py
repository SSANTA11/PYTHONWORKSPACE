# 튜플은 수정이 불가능하다!!!!!
# 리스트는 수정이 가능하다!!
    # 그래서 copy가 존재한다


# 메소드는 파괴적: sort()
# 함수는 비파괴적: sorted()




# <list_reverseiterator object at 0x7bed1985e350>
    # 위 표시는 
    # a=[1,2,3,4,5,6]
    # a.reverse()
    # print(reversed(a))
    # 를 두고 iterator(반복가능한 것)임을 알려주고 있고 
    # iterator는 for문 뒤에서만 사용가능하다...

# 순서 정렬 메서드 .sort()
    # 숫자는 오름차순
    # 영어는 알파벳 순

# 원소의 위치 찾기 메서드 .index()
    # 서수 알려주기

# 모두 지우기 메서드 .clear()


# key 옵션의 사용(sort 고급)
    # list_a=[1,4,-1,2,3,4,-5,1,5]
    # list_a.sort(key=abs)
    # 크기 순으로 정렬
    

# sol1
    # from random import randint
    # list_a=[]
    # for i in range(500):
    #     num=randint(1,20)
    #     list_a.append(num)
    # for i in range(1,20+1):
    #     print(f"{i}:{list_a.count(i)}")

# sol2
    # from random import randint
    # d={}
    # for i in range(1,20+1):
    #     d[i]=0
    # for i in range(500):
    #     num=randint(1,20)
    #     d[num]+=1
    # for info in d:
    #     print(info)


# 30을 인덱스를 활용하여 지우기
    # a=[10,20,30,40,50]
    # num=a.index(30)
    # a.pop(num)

    # print(a)


# 띄어쓰기로 내림차순 나열
    # a="By accepting the erosion of our status and identity, we gain access to a broader spectrum of options in the long run."
    # a=a.split()
    # a.sort(key=len)
    # b=[]

    # for i in a:
    #     b.append(i)

    # print(b)    

    # from random import randint
    # lotto=[]
    # for i in range(6):
    #     num=randint(1,45)
    #     while num in lotto:
    #         num=randint(1,45)
    #     lotto.append(num)
    # lotto.sort()

    # print(lotto)




# 리스트 중첩
    # 이차원 리스트
        # 일차원리스트예시: [10,20,30]
        # 이차원리스트예시: [[1,2],[2,3],[3,4],[4,5],[5,6]]
            # 최외곽 대괄호가 끝나지 않는한 파이썬 인터프리터는 여러 줄의 코드라도 한 문장으로 취급한다.
            # 정방형 리스트: 정사각형 형태의 이차원 리스트(정방행렬)
            # 톱니형 리스트: 정방형이 아닌 것(그러나 드문 경우)
        # 이차원 리스트의 인덱싱은 [][]의 꼴로 사용한다.

# nums=[
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]]

# for i in range(3):
#     for r in range(4):
#         print("{0:<5}".format(nums[i][r]), end="")
#     print()

# 튜플
    # 읽기 전용 리스트
    # 단점: 수정, 삭제, 추가 불가(연결하기'+',복사하기'*'는 사용가능하다)
    # 장점: 메모리가 적고, 속도가 빠름, 데이터 안정성에 도움이 됨(수정이 불가 하기 때문)

    # 파이썬은 데이터나 나누어(',')져 있을 때, 괄호가 없어도 튜플로 본다.
        # 단, 튜플 내에 하나만 들어갈때는 쉼표만을 뒤에 붙이던지, 아니면 괄호 내에 넣은 뒤 뒤에 쉼표를 붙인다.
            # 하나짜리 튜플은 왜 필요할까?
                # 튜플을 요하는 함수에서 사용하기 위해서이다!
    #튜플의 메소드
        # count와 Index
        # sort()도 사용가능하다. 다만, 리스트 형태로 출력된다.





        # 튜플과 리스트 비교
                # 1
                # import time
                # a_list=list(range(10000000))
                # a_tuple=tuple(range(10000000))
                # sum1=0
                # sum2=0
                # start=time.time()
                # for value in a_list:
                #     sum1+=value
                # print("리스트 시간:", time.time()-start)

                # start=time.time()
                # for value in a_tuple:
                #     sum2+=value
                # print("튜플 시간:", time.time()-start)

                # 2
                # import time
                # start=time.time()
                # start=time.time()
                # for i in range(10000000):
                #     a_list=[1,2,3,4,5]
                # print("리스트 시간:",time.time()-start)

                # start=time.time()
                # for i in range(10000000):
                #     a_tuple=(1,2,3,4,5)
                # print("튜플 시간:",time.time()-start)

                # import sys
                # a_list=[1,2,3,4,5]
                # a_tuple=(1,2,3,4,5)
                # print('size of list:',sys.getsizeof(a_list))
                # print('size of tuple:',sys.getsizeof(a_tuple))

# 추가 문자열 메소드(숫자는 안됨을 유의하자)
    # replace
        # 형식: replace('기존 문자열','새 문자열')
        # 주의: 믄자열의 메소드는 객체 자체를 바꾸지 않는다!!
    # join
        # 형식: '문자열 구분자'.join(문자열 구분자로 나열된 문자열)
    # strip
        # 형식: strip([삭제할 문자들])-> []은 옵션!!
        # lstrip,rstrip,strip은 문자열 최외곽의 공백만을 없앤다. 그러므로 문자열 내부의 공백은 남아 있는다.
        # 만일 옵션에 "ab"가 들어간다면 ab만을 없앤다!(a,b 를 따로 고려하지는 않는다)
    # just: 줄 맞추기 기능!!
        # 형태: ljust,rjust,center
        # 형식: just([칸(?) 수])
        # 서식 지정자와 같은 기능을 한다.

