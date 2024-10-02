# 서식지정자
    # 형식: 
        # 1) 한개 일 경우: "%s"%"문자열" 
            # print("%s"%("sssss"))
        # 2) 두 개일 경우: "%s %s"%("문자열1","문자열2")
            # print("%s %s"%("sssss","danke"))

# format
# f 문자열(포멧형 문자열)
    # print("{0:<02f}".format(123))
# print("{0:<010d}".format(123))
# print("{0:<.10}".format("아저씨"))
# import turtle
# turtle.pensize(10)
# turtle.shape('turtle')

# turtle.forward(200)
# turtle.right(144)
# turtle.pencolor("red")

# turtle.forward(100)
# turtle.right(144)
# turtle.pencolor("orange")

# turtle.forward(100)
# turtle.right(144)
# turtle.pencolor("yellow")

# turtle.forward(100)
# turtle.right(144)
# turtle.pencolor("green")

# turtle.forward(100)
# turtle.left(70)
# turtle.pencolor("blue")

# turtle.forward(100)
# turtle.right(144)
# turtle.pencolor("navy")

# turtle.forward(100)
# turtle.right(144)
# turtle.pencolor("purple")

# turtle.forward(100)
# turtle.right(144)
# turtle.pencolor("red")

# turtle.forward(100)
# turtle.right(144)
# turtle.pencolor("orange")

# import turtle
# turtle.shape("turtle")
# i=0
# while True: 
#     turtle.left(45+i)
#     turtle.forward(200+i)
#     i+=1

# a=int(input("숫자 1 ==>"))
# b=int(input("숫자 2 ==>"))
# print(f"{a} / {b} = {a/b}")
# print(f"{a} % {b} = {a%b}")
# print(f"{a} // {b} = {a//b}")
# print(f"{a} ** {b} = {a**b}")

# import turtle
# turtle_shape=input("거북이 모양(turtle, circle, square, rectangle) ==> ")
# pen_size=int(input("거북이의 선 두께 ==> "))
# turtle_color=input("거북이의 색상(red, blue, green, yellow, magenta) ==> ")
# turtle_angle=int(input("거북이의 회전 각도 ==> "))
# turtle_distance=int(input("거북이의 이동거리 ==> "))

# turtle.shape(turtle_shape)
# turtle.pensize(pen_size)
# turtle.pencolor(turtle_color)
# turtle.right(turtle_angle)
# turtle.forward(turtle_distance)

# import turtle
# turtle.penup()
# x=1
# y=1
# turtle.goto(x,y)

# import turtle
# pencolor=input("펜 색상(red, blue, green, yellow, magenta) ==>")
# X=int(input("X위치 ==>"))
# Y=int(input("Y위치 ==>"))
# write=input("쓰고 싶은 글자 (최대 4글자)==>").upper()
# turtle.pencolor(pencolor)
# turtle.goto(X,Y)
# turtle.write(write)

# 초이스는 리스트의 인덱스만을 사용한다.

# from random import choice

# a=choice(['가위','바위','보'])
# b=input("가위?바위?보?")

# if a=='가위':
#     if b=='가위':
#         print('비겼습니다')
#     elif b=='보':
#         print('졌습니다...')
#     else:
#         print(f"가위를 이겼습니다!!!")

# elif a=='바위':
#     if b=='바위':
#         print('비겼습니다')
#     elif b=='가위':
#         print('졌습니다...')
#     else:
#         print(f"바위를 이겼습니다!!!")

# elif a=='보':
#     if b=='보':
#         print('비겼습니다')
#     elif b=='바위':
#         print('졌습니다...')
#     else:
#         print(f"보를 이겼습니다!!!")
# print(f"상대방은 {a}를 제시했습니다!!")

# import random
# import turtle

# turtle.shape("turtle")
# turtle.pencolor("blue")
# turtle.pensize("5")

# turtle.screensize(300,300)
# turtle.setup(250,250)
# out=0

# while True:
#     a=random.randint(0,360)
#     b=random.randint(10,100)
#     turtle.right(a)
#     turtle.forward(b)
#     corX=turtle.xcor()
#     corY=turtle.ycor()
#     if (-150<=corX<=150) or (-150<=corY<=150):
#         print("goodboy")
#     else:
#         print("NONONONONO")
#         turtle.goto(0,0)
#         out+=1 
#         if out>=1:
#             turtle.pencolor("green")
#             if out>=2:
#                 turtle.pencolor("orange")
#             if out>=3:
#                 turtle.pencolor("red")
#                 break

# print("%s"%f"kdksnfdkl")