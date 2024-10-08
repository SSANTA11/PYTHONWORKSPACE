# 출력될 문자열을 좌측면에 붙이는 동시에 
# 스크립트에서 가독성을 높이는 방법

a=int(input("정수를 입력하세요!"))

# 방법 1('f 문자열'과 익스케이프 줄바꿈을 이용한 표현)
if a%2==0:
    print(
        f"입력하신 문자는 {a}입니다.\n"
        f"{a}는(은) 짝수입니다!"
        )
    print()
    print()
# 방법 2('" ".join' 함수 이용!)
else:
    print("\n".join([
        f"입력하신 문자는 {a}입니다.", 
        f"{a}는(은) 홀수입니다!"
        ]))


# 첨가: "~".join()에서 '~'에 들어가는 것은 
# 리스트 內의 서로 다른 요소를 구분하는 기호 등을 삽입한다.
# 예를 들어 '~'에 ','가 삽입된다면 리스트 內의 기존 ','으로 구분되던 
# 두 요소는 띄어쓰기 없이 ','만을 사이에 두고 구분되며, 
# 익스케이프문자 '\n'의 경우에는 리스트 內의 기존 ','으로 구분되던
# 두 요소는 띄어쓰기 없이 줄바꿈만이 일어난다.


# 이러한 함수는 알고리즘 문제에서 데카르트평면, 
# 즉 좌표평면에서 사용이 가능하다!