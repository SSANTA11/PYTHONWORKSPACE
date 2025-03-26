string=input("인사말을 입력하세요!!")
print(string)
#input은 반드시 문자열 함수이기 때문에 별도의 float이나 int의 수식이 있어야 합니다!!
print("-"*60)
#방법1
a=int(input("첫 번째 정수를 입력하세요!"))
b=int(input("두 번째 정수를 입력하세요!"))
print("입력하신 두 정수의 합은", a+b, "입니다!")
print()
#방법2
a=int(a)
b=int(b)
a=int(input("첫 번째 정수를 입력하세요!"))
b=int(input("두 번째 정수를 입력하세요!"))
print("입력하신 두 정수의 합은", a+b, "입니다!")