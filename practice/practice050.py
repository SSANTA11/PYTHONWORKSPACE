#practice49.py 응용 raise NotImplimentedError(=아직 구현되지 않음)을 사용하여 프로그램의 임시 실행과 미구현 영역에서의 반응을 살펴보자!!
i=input(">입력해주세요!:")
i=i.strip()

if i=="":
    raise NotImplementedError
else:
    print("입력한 내용:", i)