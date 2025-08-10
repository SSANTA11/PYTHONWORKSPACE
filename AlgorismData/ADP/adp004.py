# 연산들의 추가: 화면출력

import sys
sys.path.append("C:/PYTHONWORKSPACE")  # algorism_data의 상위 폴더 경로
from algorism_data.algorismDataClass.algorism_data_structure_week4_0 import ArrayStack

s=ArrayStack(10)
for i in range(1,6):
    s.push(i)

#__str__()메소드 추가
    # 객체 정보 출력 (Class ArrayStack에 __str__ 메서드가 없을 경우)
print('push 5회: ', s )

# 스택 s의 배열 array를 직접 출력
print('push 5회: ', s.array)

# 스택의 응용: 괄호 검사
def checkBracket(statement):
    stack=ArrayStack(100)
    for ch in statement:
        if (ch=='['or ch=='{'or ch=='('):
            stack.push(ch)
        elif (ch==']'or ch=='}'or ch==')'):
            if stack.isEmpty():
                return False
            else:
                left=stack.pop()
                if (ch=='}' and left!='{') or (ch==']' and left!='[') or (ch==')' and left!='('):
                    return False
    return stack.isEmpty()

with open("algorism_data_structure_week4_0.py", 'r') as infile:
    file_content = infile.read()

print("소스파일",filename,"-->",checkBracket(str))