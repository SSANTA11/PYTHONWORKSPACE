#if조건문
#사용자가 입력한 숫자가
#양수 음수 0인지 판별하는 프로그램

raw_input=input("정수를 입력해주세요! : ")
raw_input=int(raw_input)

if raw_input>0:
    print("양수 입니다!")
if raw_input<0:
    print("음수입니다!")
if raw_input==0:
    print("0입니다!")