#format함수 응용
print("제가 사용자님이 원하시는 값을 더해드릴게요!")
a=float(input("더하고자 하는 값을 입력해 주세요!"))
b=float(input("더하고자 하는 값을 입력해 주세요!"))
print("{}+{}={}".format(a, b, a+b))
print("-=-"*20)
print("제가 사용자님이 원하시는 값을 더해드릴게요!")
a=float(input("더하고자 하는 값을 입력해 주세요!"))
b=float(input("더하고자 하는 값을 입력해 주세요!"))
print(f"{a}+{b}={a+b}")
a="abcde"
a=a.find("e")
print(a)