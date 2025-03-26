######## c언어 스위치문?#########-> review!!
                                    # age,gender,height=22, "male", 181
                                    # if age>20:
                                    #     print("선배님은")
                                    #     if gender=="male":
                                    #         print("남자시구")
                                    #         if height>180:
                                    #             print("키가 크네요")
                                    # else:
                                    #     if age==20:
                                    #         print("친구야~")
                                    #     else:
                                    #         print("어...")  
# 대상이 하나일 때->elif 유리(c언어에선 스위치문 역할)
# 대상이 여러 개일 때->중첩 유리
# elif는 복잡성을 고려하여 논리적으로 감당 가능할 때만 사용하도록 하자!

# a=int(input("5와 비교하고자 하는 정수를 입력하세요."))
# if a>5:
#     print("a는 5보다 큽니다.")
# elif a==5:
#     print("a는 5입니다.")
# else:
#     print("a는 5보다 작습니다.")

# a, b=input("정수 두 개를 입력하세요").split()
# a=int(a)
# b=int(b)
# print(type(a))
# print(type(b))
#  map()함수
    # 형식: map(함수이름, 인수목록)
        # a,b,c=map(int,input().split() )
        # print(type(a))
        # print(type(b))
        # print(type(c))
# a=10
# print(f"a={a}")
# end와 sep:
# end는 뒤에 다음 줄 값을 붙이고, 디폴트 값은 '\n', sep은 seperate의 약자이고 괄호 內 문자열들을 쉼표를 기준으로 괄호 內 기준으로 나눈다
# 리스트에 대한 end 적용은 별개의 것이라 인식하기!

    # print('absxf',end='\n(디폴트 값)')
        # 응용: 
# print("a","b", end=" ")
# print("a")

# 옵션=[]

# 서식 지정자(format specifier)
    # '~~~%s~~'%(%s에 들어갈 내용 입력)
# print("%-10s"%12.33,"ㄴㄴㄴ")
    # %f: 실수 ,%(띄어쓰기 범위 정수)d: 정수 ,%(띄어쓰기 범위 정수)s: 변수
    # (띄어쓰기 범위 정수에 - 가 붙으면 왼쪽에서 적용)

#format과 f문자열(='%s')
    # a=input(" 뭐라고요 ???")
    
    # print('{} {} {}'.format('a','b')) -> 괄호 내는 서수이며 디폴트값은 순서대로이다

    # print(f"{a}라고 말씀하셨군요!!")
    
    # print(f'{"22"}                    {"111"}            {"s"} {"d"}asz')->포멧티드 스트링
    # 매개변수 값 지정-> review!!
    
    #format으로 문자열 지정
        # '{인덱스:<길이}'.format(문자열) 
        # -> 방향: <(왼쪽정렬), >(오른쪽정렬), 길이: 출력되는 전체 문자열의 길이
    # format 숫자 정렬
        # 정수:'{인덱스:<0개수d}'.format(숫자)
        # 실수:'{인덱스:<0개수.자릿수f}'.format(숫자)
    # format 종합표현
        # 형식: "{인덱스:[[채우기][정렬][길이][.자릿수][자료형]].format(값)}"
        # 포멧형 문자열 형식: f"{값:[[채우기][정렬][길이][.자릿수][자료형]]}"

# a=123
# print("{0:.>9d}".format(a))
# print(f"......{a}")
# print(f"{a}.0.....")

# print('{0:,}'.format(1000000)) -> 내장함수
# print(format(1000000,',')) -> 내장함수

# a=int(input("숫자를 맞춰보세요!!: "))
# while True:
    
#     if a>5:
#         print(f"{a}보다는 작습니다")

#     elif a<5:
#         print(f"{a}보다는 큽니다")

#     else:
#         print("정답입니다!!!")
# print("{0:.>20}".format("apple"))