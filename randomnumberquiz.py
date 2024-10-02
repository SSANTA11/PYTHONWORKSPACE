import random
a=random.randint(1,45+1)

for i in range(1,10+1):
    num=int(input("숫자를 맞춰보세요"))
    if a<num:
        print(f"{num}보다 작습니다")
    elif a>num:
        print(f"{num}보다 큽니다")
    else:
        print("{26}! 정답입니다!")