# 변수를 선언합니다
미={"키a":"값a", "키b":"값b", "키c":"값c"}

# 딕션너리의 items() 함수 결과 출력하기
print("# 딕션너리의 items() 함수")
print("items():",미.items())
print()

# for 반복문과 items() 함수 조합해서 사용하기
print("# 딕션너리의 items() 함수의 반복문 조합하기")

for key, 값 in 미.items():
    print(f"dictionary[{key}]={값}")