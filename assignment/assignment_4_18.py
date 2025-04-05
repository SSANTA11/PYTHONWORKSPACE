import sys
sys.path.append("C:/PYTHONWORKSPACE")  # algorism_data의 상위 폴더 경로

from algorism_data.algorismDataClass.algorism_data_structure_week4_0 import ArrayStack


# 1. 소스 파일을 읽어 괄호를 검사하는 프로그램을 완성하라. 임의의 파이썬 소스 코드(.py)를 입력하면 괄호검사가 되도록 해라
def checkBracket_1(statement):
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

filename=input()
with open(filename,"r") as infile:
    file_content=infile.read()
    print("소스파일", filename,"-->",checkBracket_1(file_content))


# 2. 괄호 매칭이 실패하면 조건 1~3 중에서 어떤 조건을 위반했는지를 출력할 수 있도록 소스코드를 수정하라. checkBrackets() 함수가 에러코드를 반환하도록 하면 될 것이다. 에러가 없으면 0을 반환하도록 하라.

def checkBracket_2(statement):
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

filename=input()
with open(filename,"r") as infile:
    file_content=infile.read()
    print("소스파일", filename,"-->",checkBracket_2(file_content))

# 3. 괄호 매칭이 실패하면 실패한  위치를  에러코드와 함께 반환할 수 있도록 수정하라. 실패한 위치는 (라인수, 문자수)로 나타낼 수 있을 것이다. 따라서 에러가 발생하면 (에러코드, 라인수, 문자수 )를 반환하면 될 것이다.