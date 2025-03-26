while True:
    gr=int(input('뽑힌 점수 : '))
    if gr>=90 :
        print('장학생입니다!')
    elif gr>=60:
        print('합격입니다!')
    else:
        print('불합격입니다')
