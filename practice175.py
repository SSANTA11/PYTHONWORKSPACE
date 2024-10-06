# # 10월 6일 진도

# # 클래스: 함수(와 변수)를 묶어 놓은 것
# # -> 객체를 만들어내기 위한 설계도

# def creat_student(이름, 국어, 영어, 수학, 과학):
#     return {"이름":이름,"국어":국어,"영어":영어,"수학":수학,"과학":과학}

# 학생들=[
#     creat_student("인성",87,88,98,95),
#     creat_student("구름",92,98,97,98),
#     creat_student("별이",76,96,95,90),
# ]

# # 클래스 = 설계도
# class 학생:
#     # 클래스의 내용  
#     def 초기화(self, 이름, 국어, 영어, 수학, 과학):
#         self.이름=이름
#         self.국어=국어
#         self.영어=영어
#         self.수학=수학
#         self.과학=과학

# # 객체 = 인스터스
# 인성=학생()

# # 함수 호출 방법(1)
# 학생.초기화(인성, "인성",87,88,98,95)
# print(인성.이름, 인성.국어)

# # 함수 호출 방법(2)
# 인성.초기화("인성"87,88,98,95)



# # 변수 추가
# 인성.이름="인성"
# 인성.국어=87
# 인성.영어=88
# 인성.수학=98
# 인성.과학=95

# # 변수 사용
# print(인성.이름)
# print(인성.국어)

class lol:
    def 초기화(self,a,b,c,d,e):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e

laugh=lol()

lol.초기화(laugh,)
laugh.smile=100
laugh.funny_face=100

print(laugh.smile)