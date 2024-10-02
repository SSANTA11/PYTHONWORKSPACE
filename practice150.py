year=int(input("12달 달력을 만들어드립니다\n원하시는 년도를 입력하세요!!>> "))
week='일월화수목금토'
days=0
category='nomal'
if year!=1:
    for days in range(1,year):
        if days%400==0:
            days+=366
        elif days%100==0:
            days+=365
        elif days%4==0:
            days+=366
        else:
            days+=365
    if year%400==0:
        category='leap'
    elif year%100==0:
        category="nomal"
    elif year%4==0:
        category='leap'
    else:
        category="nomal"
empty_space=days%7+1
for month in range(1,12+1):
    print()
    if month!=1:
        empty_space=(empty_space+days_in_month)%7        
    print('-'*20)
    print(f'{year}년 {month}월')                        
    for day in week:
        print(day, end=" ")
    print()
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days_in_month=31
    elif month in [4, 6, 9, 11]:
        days_in_month=30
    else:
        if category=='leap':
            days_in_month=29
        else:
            days_in_month=28                
    modify_num=empty_space        
    print(empty_space*"   ", end="")        
    for date in range(1,days_in_month+1):
        if date in [8-modify_num, 15-modify_num, 22-modify_num, 29-modify_num, 36-modify_num]:
            print()
        print('{0: >2}'.format(date),end=" ")

