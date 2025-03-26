y=int(input("당신이 태어나신 해를 입력해주세요!"))

if y%12==0:
    print("원숭이 띠입니다!")
elif y%12==1:
    print("닭 띠입니다!")
elif y%12==2:
    print("개 띠입니다!")
elif y%12==3:
    print("돼지 띠입니다!")
elif y%12==4:
    print("쥐 띠입니다!")
elif y%12==5:
    print("소 띠입니다!")
elif y%12==6:
    print("범 띠입니다!")
elif y%12==7:
    print("토끼 띠입니다!")
elif y%12==8:
    print("용 띠입니다!")
elif y%12==9:
    print("뱀 띠입니다!")
elif y%12==10:
    print("말 띠입니다!")
else:
    print("양 띠입니다!")

#print("원숭이 닭 개 돼지 쥐 소 범 토끼 용 뱀 말 양".split()[y%12] "띠입니다!")