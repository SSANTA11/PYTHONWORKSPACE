a=input("a입력")
b=input("b입력")
a=int(a)
b=int(b)
if a>0:
    if b<0:
        print("a는 양수이고 b는 음수입니다!")
    if b>0:
        print("a는 양수이고 b도 양수입니다!")
    if b==0:
        print("a는 양수이고 b는 0입니다!")
if a<0:
    if b<0:
        print("a는 음수이고 b도 음수입니다!")
    if b>0:
        print("a는 음수이고 b는 양수입니다!")
    if b==0:
        print("a는 음수이고 b는 0입니다!")
if a==0:
    if b<0:
        print("a는 0이고 b는 음수입니다!")
    if b>0:
        print("a는 0이고 b는 양수입니다!")
    if b==0:
        print("a는 0이고 b도 0입니다!")
