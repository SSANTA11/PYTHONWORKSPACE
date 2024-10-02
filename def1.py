def pp(T, x, y):
    result = []
    for t in range(1, T+1):
        result.append(f"{x}\n{y}")
    return "\n".join(result)

i = input("""
횟수, 출력대상1, 출력대상2를 
순서대로 입력하고
각 입력 사항들은 
띄어쓰기로 구분하시오
""").split()

T = int(i[0])
x = i[1]
y = i[2]

print(pp(T, x, y))
# return문이 실행되면 함수는 그대로 종료된다
    # 반복문을 활용한다면 return을 반복하는 것은 불가하다