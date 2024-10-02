i=1
while True:
    print(f"{i}번째 반복입니다.")
    i+=1
    a=input(">>>종료하시겠습니까?(y/n): ")
    if a in ["Y","y"]:
        print("반복문을 종료합니다.")
        break
    elif a in ["N","n"]:
        continue
    else:
         print("옳지 않은 입력입니다!")