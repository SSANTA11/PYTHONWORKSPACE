#첫시도
pi=3.141592
print()
print("적어주신 구의 반지름을 통해 해당 구의 부피와 겉넓이를 계산해 드리겠습니다!")
print()
r=float(input("밑에 구의 반지름을 입력해주세요!\n"))
print("-"*50)
print("말씀하신 구의 부피는...\n ", 4/3*pi*r**3, "입니다!")
print()
print("말씀하신 구의 겉넓이는...\n", 4*pi*r**2, "입니다!")
print()
print("-=-=-"*3)

#모범 답안(과정과 절차가 눈에 보이는 정갈한 코드)
#입력 : 반지름 입력
r=input("반지름 :")
r=float(r)

#처리 : 부피 + 겉넓이
pi=3.141592
부피=(4/3)*pi*(r**3)
겉넓이=4*pi*(r**2)

#출력
print(f"부피 : {부피}")
print(f"겉넓이 : {겉넓이}")
print()