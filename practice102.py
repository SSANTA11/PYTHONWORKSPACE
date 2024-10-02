# 1~100의 숫자에서 최대가 되는 경우는 어떤 숫자를 곱했을 때인가?

max_value=0
a=0
b=0
for i in range(1,100+1):
    j=100-i
    # 최댓값구하기
    
    a=j
    b=i

print(f"최대가 되는 경우: {a}*{b}={max_value}")