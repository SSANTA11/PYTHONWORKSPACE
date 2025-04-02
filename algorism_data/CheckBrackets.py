# 코드 4.4: 스택을 이용한 괄호검사 알고리즘 (참고 파일: ch04/CheckBrackets.py)
from ArrayStack import ArrayStack

def checkBrackets(statement):
    stack = ArrayStack(100)
    for ch in statement:
        # if ch in ('{', '[', '('):
        # if ch in '{[(':
        if ch=='{' or ch=='[' or ch=='(' :
            stack.push(ch)
        # elif ch in ('}', ']', ')'):
        # elif ch in '}])':
        elif ch=='}' or ch==']' or ch==')' :
            if stack.isEmpty() :
                return False
            else :
                left = stack.pop()
                if (ch == "}" and left != "{") or \
                   (ch == "]" and left != "[") or \
                   (ch == ")" and left != "(") :
                    return False

    return stack.isEmpty()


# 테스트 프로그램
s1 = "{ A[ (i+1) ] = 0; } "
s2 = "if( (i==0) && (j==0)"
s3 = "A[ ( i+1 ] ) = 0;   "
print(s1, " ---> ", checkBrackets(s1))
print(s2, " ---> ", checkBrackets(s2))
print(s3, " ---> ", checkBrackets(s3))


# 테스트 프로그램
filename = "ArrayStack.h"
infile = open(filename , "r")
str = infile.read()
infile.close()
print("소스파일", filename, " ---> ", checkBrackets(str))

# 테스트 프로그램
filename = "ArrayStack.h"
with open(filename , "r") as infile :
    str = infile.read()
    print("소스파일", filename, " ---> ", checkBrackets(str))
