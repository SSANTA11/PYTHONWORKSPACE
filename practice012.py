a=input("첫 번째 숫자를 입력해주세요>")
b=input("두 번째 숫자를 입력해주세요>")

print(a+b)
print(a, b)
#input은 문자열연결연산자로만 인식되어서 숫자를 입력할 경우 문자로 인식된다
#그러므로 inout 함수를 활용한 +연산자는 ','와 유사한 결과를 보여줍니다!
#만일 정수 계산을 원한다면 숫자가 문자가 아닌 정수로 인식되도록 int 함수를 input 함수에 적용시키면 해결됩니다.