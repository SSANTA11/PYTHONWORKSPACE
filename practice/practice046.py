학점=float(input(">학점을 입력해주세요 :"))

print("당신의 명성은")
if 학점>4.5:
    print("신")
elif 학점>4.2:
    print("교수님의 사랑")
elif 학점>3.5:
    print("현 체제의 수호자")
elif 학점>2.8:
    print("일반인")
elif 학점>2.3:
    print("일탈을 꿈꾸는 소시민")
elif 학점>1.75:
    print("오락문화의 선구자")
elif 학점>1.0:
    print("불가촉천민")
elif 학점>0.5:
    print("자벌레")
elif 학점>0.0:
    print("플랑크톤")
else:
    print("시대를 앞서가는 혁명의 씨앗")

print("입니다!")