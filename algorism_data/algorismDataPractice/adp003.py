# 스택 클래스 활용
# 문자열 역순 프로그램


import sys
sys.path.append("C:/PYTHONWORKSPACE")  # algorism_data의 상위 폴더 경로

from algorism_data.algorismDataClass.algorism_data_structure_week4_0 import ArrayStack

s=ArrayStack(100)

msg=input("문자열 입력: ");
for c in msg:
    s.push(c)
print("문자열 출력: ", end='')
while not s.isEmpty():
    print(s.pop(), end=' ')
print()