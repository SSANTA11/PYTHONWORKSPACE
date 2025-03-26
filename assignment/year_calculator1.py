# 평년 유년 구분법
while True:
    year=int(input('연도를 입력하세요 ==> '))

    if (year%4==0):
        if (year%100==0):
            if (year%400==0):
                print('윤년입니다!')
            if (year%400!=0):
                print('평년입니다!')
        if (year%100!=0):
            print('윤년입니다!')
    if (year%4!=0)and(year%100!=0)and(year%400!=0):
        print('예년입니다!')
