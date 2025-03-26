# break키워드
# 반복문 전체를 벗어날 때 사용하는 구문
i=0

while True:
    print(f'{i}번째 반복입니다.')
    i+=1
    a=input("종료하시겠습니까?(y/n)")
    if "y"or"Y"in a:
        break
    else:
        continue