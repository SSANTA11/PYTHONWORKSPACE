year=int(input("12달 달력을 만들어드립니다\n원하시는 년도를 입력하세요!!>> "))

week='일월화수목금토'

empty_space=0
category='nomal'
added_days=365
if year!=1:
    added_days=0
    for days in range(1, year):
        if days%4==0:
            if days%100==0:
                if days%400==0:
                    category='leap'
                    added_days+=366
                else:
                    category='nomal'
                    added_days+=365
            else:
                category='leap'
                added_days+=366
        else:
            category='nomal'
            added_days+=365

    # if added_days%7==0:
    #     empty_space=0
    # elif added_days%7==1:
    #     empty_space=1
    # elif added_days%7==2:
    #     empty_space=2
    # elif added_days%7==3:
    #     empty_space=3
    # elif added_days%7==4:
    #     empty_space=4
    # elif added_days%7==5:
    #     empty_space=5
    # elif added_days%7==6:
    #     empty_space=6

    empty_space%=7


for month in range(1,12+1):
    print()

    if month!=1:
        if (empty_space+days_in_month)%7==0:
            empty_space=0
        elif (empty_space+days_in_month)%7==1:
            empty_space=1
        elif (empty_space+days_in_month)%7==2:
            empty_space=2
        elif (empty_space+days_in_month)%7==3:
            empty_space=3
        elif (empty_space+days_in_month)%7==4:
            empty_space=4
        elif (empty_space+days_in_month)%7==5:
            empty_space=5
        elif (empty_space+days_in_month)%7==6:
            empty_space=6


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

    if empty_space==0:
        for date in range(1,days_in_month+1):
            if date in [8, 15, 22, 29]:
                print()
            print('{0: >2}'.format(date),end=" ")
    elif empty_space==1:
        print('   '*empty_space, end="")
        for date in range(1,days_in_month+1):
            if date in [7, 14, 21, 28]:
                print()
            print('{0: >2}'.format(date),end=" ")
    elif empty_space==2:
        print('   '*empty_space, end="")
        for date in range(1,days_in_month+1):
            if date in [6, 13, 20, 27]:
                print()
            print('{0: >2}'.format(date),end=" ")
    elif empty_space==3:
        print('   '*empty_space, end="")
        for date in range(1,days_in_month+1):
            if date in [5, 12, 19, 26]:
                print()
            print('{0: >2}'.format(date),end=" ")
    elif empty_space==4:
        print('   '*empty_space, end="")
        for date in range(1,days_in_month+1):
            if date in [4, 11, 18, 25]:
                print()
            print('{0: >2}'.format(date),end=" ")
    elif empty_space==5:
        print('   '*empty_space, end="")
        for date in range(1,days_in_month+1):
            if date in [3, 10, 17, 24, 31]:
                print()
            print('{0: >2}'.format(date),end=" ")
    elif empty_space==6:
        print('   '*empty_space, end="")
        for date in range(1,days_in_month+1):
            if date in [2, 9, 16, 23, 30]:
                print()
            print('{0: >2}'.format(date),end=" ")
