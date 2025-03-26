year = int(input("12달 달력을 만들어드립니다\n원하시는 년도를 입력하세요!!>> "))

week = '일월화수목금토'

first_day = week[0]

if year % 400 == 0:
    category = 'leap'
elif year % 100 == 0:
    category = 'normal'
elif year % 4 == 0:
    category = 'leap'
else:
    category = 'normal'

for month in range(1, 12 + 1):
    print()
    print('-' * 20)
    print(f'{year}년 {month}월')

    for day in week:
        print(day, end=" ")
    print()

    # Calculate the number of days in the month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days_in_month = 31
    elif month in [4, 6, 9, 11]:
        days_in_month = 30
    else:
        if category == 'leap':
            days_in_month = 29
        else:
            days_in_month = 28

    # Calculate the day of the week for the 1st day of the month
    first_day_month = (week.index(first_day) + sum(range(1, month))) % 7
    
    # Print leading spaces if the 1st day of the month is not Sunday
    if first_day_month != 0:
        print(" " * 3 * first_day_month, end="")

    # Print the days of the month
    for day in range(1, days_in_month + 1):
        print('{0: >2}'.format(day), end=" ")

        # If the last day of the month is Saturday, start printing on a new line
        if (first_day_month + day) % 7 == 0:
            print()

print()
