a=2

def mul(*values):
    global a
    a=1
    for i in values:
        a*=i
    return a
# 함수 스택에 새로운 변수를 만드는 경우에는 
# global을 사용하기 전까지 외부 선언과 무관하지만 
# 만약 함수 스택에 새로운 변수를 만드는 것이 아닌 
# extend의 경우에는 외부의 변수 선언의 연장 개념이 된다
#  
print(mul(5,7,9,10))

