
class ArrayStack:
  def __init__(self, capacity):
    self.capacity = capacity
    self.array=[None]*self.capacity
    self.top=-1

  def isEmpty(self):
    return self.top==-1

  def isFull(self):
    return self.top==self.capacity-1

  def push(self,e):
    if not self.isFull():
      self.top+=1
      self.array[self.top]=e
    else:
      pass

  def pop(self):
    if not self.isEmpty():
      self.top-=1
      return self.array[self.top+1]
    else:
      pass

  def peek(self):
    if not self.isEmpty():
      return self.array[self.top]
    else:
      pass

  def __str__(self):
    return str(self.array[0:self.top+1])

  def newclear(self):
   while not self.isEmpty():
      self.pop()

# 1. 소스 파일을 읽어 괄호를 검사하는 프로그램을 완성하라. 임의의 파이썬 소스 코드(.py)를 입력하면 괄호검사가 되도록 해라
print("Q1")
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

filename=input("파일명: ")
with open(filename,"r") as infile:
    file_content=infile.read()
    print("소스파일:", filename,"-->",checkBracket_1(file_content))
print('-'*100)

# 2. 괄호 매칭이 실패하면 조건 1~3 중에서 어떤 조건을 위반했는지를 출력할 수 있도록 소스코드를 수정하라. checkBrackets() 함수가 에러코드를 반환하도록 하면 될 것이다. 에러가 없으면 0을 반환하도록 하라.
    # 조건1: 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야한다.
    # 조건2: 같은 타입의 괄호에서 왼쪽 괄호가 오른쪽 괄호보다 먼저 나와야 한다.
    # 조건3: 서로 다른 타입의 괄호쌍이 서로를 교차해선 안된다.
# 초안
print("Q2-v0.1")
print("""
    조건1: 왼쪽과 오른쪽의 괄호 개수가 동일 ---> 어길 시: f1
    조건2: 각 괄호가 왼쪽 괄호, 오른쪽 괄호 순 ---> 어길 시: f2
    조건3: 서로 다른 괄호쌍이 서로를 교차하면 안됨 ---> 어길 시: f3
    """

)
def checkBracket_2_1(statement):
    stack=ArrayStack(100)
    for ch in statement:
        if ch in "[{(":
            stack.push(ch)
        elif ch in "]})":
            if stack.isEmpty():
                return 'f2'
            else:
                left=stack.pop()
                if (ch=='}' and left!='{') or (ch==']' and left!='[') or (ch==')' and left!='('):
                    return 'f3'
    return 0

filename=input("파일명: ")
with open(filename,"r") as infile:
    file_content=infile.read()
    infile.close()
    print("소스파일:", filename,"-->",checkBracket_2_1(file_content))

# 문제점: f1 누락 문제, 중복 조건 누락


print('-'*100)
# 수정본(중복조건 가능, 파일 전체 검사 가능, 오류 흐름 확인 가능)
print("Q2-v1.0")
print("""
    조건1: 왼쪽과 오른쪽의 괄호 개수가 동일 ---> 어길 시: f1
    조건2: 각 괄호가 왼쪽 괄호, 오른쪽 괄호 순 ---> 어길 시: f2
    조건3: 서로 다른 괄호쌍이 서로를 교차하면 안됨 ---> 어길 시: f3
    """
)
def checkBracket_2_2(statement):
    stack=ArrayStack(100)
    l_count=0
    r_count=0
    error=ArrayStack(100)
    for ch in statement:
        if ch in "[{(":
            l_count+=1
            stack.push(ch)
        elif ch in "]})":
            r_count+=1
            if stack.isEmpty():
                error.push('f2')
            else:
                left=stack.pop()
                if (ch=='}' and left!='{') or (ch==']' and left!='[') or (ch==')' and left!='('):
                    error.push('f3')
    if l_count!=r_count:
        error.push('f1')
    if error.isEmpty():
        return 0
    else:
        return "발생 에러 코드", error.__str__()

filename=input("파일명: ")
with open(filename,"r") as infile:
    file_content=infile.read()
    infile.close()
    print("소스파일:", filename,"-->",checkBracket_2_2(file_content))

print('-'*100)

# 3. 괄호 매칭이 실패하면 실패한 위치를 에러코드와 함께 반환할 수 있도록 수정하라. 실패한 위치는 (라인수, 문자수)로 나타낼 수 있을 것이다. 따라서 에러가 발생하면 (에러코드, 라인수, 문자수)를 반환하면 될 것이다.

print("Q3")
print("""
    조건1: 왼쪽과 오른쪽의 괄호 개수가 동일 ---> 어길 시: f1
    조건2: 각 괄호가 왼쪽 괄호, 오른쪽 괄호 순 ---> 어길 시: f2
    조건3: 서로 다른 괄호쌍이 서로를 교차하면 안됨 ---> 어길 시: f3
    """
)
def checkBracket_3(statement):
    stack=ArrayStack(100)
    l_count=0
    r_count=0
    error=ArrayStack(100)
    character=ArrayStack(100000)
    line=1
    for ch in statement:
        if ch=="\n":
            character.newclear()
            line+=1
        else:
            character.push(ch)

        if ch in "[{(":
            l_count+=1
            stack.push(ch)
        elif ch in "]})":
            r_count+=1
            if stack.isEmpty():
                error.push('f2')
                print(f"{'='*10}\n에러 코드 f2\n\n에러 문자: '{character.peek()}'\n위치 --> 줄 수: {line}, 문자 수: {character.top+1}\n")
            else:
                left=stack.pop()
                if (ch=='}' and left!='{') or (ch==']' and left!='[') or (ch==')' and left!='('):
                    error.push('f3')
                    print(f"{'='*10}\n에러 코드f3\n\n에러 문자: '{character.peek()}'\n위치 --> 줄 수: {line}, 문자 수: {character.top+1}\n")
    if l_count!=r_count:
        error.push('f1')
        print("문서 내 f1 에러 존재")
    if error.isEmpty():
        return 0
    else:
        return "발생 에러 코드", error.__str__()

filename=input("파일명: ")

with open(filename,"r") as infile:
    file_content=infile.read()
    infile.close()
    print("소스파일:", filename,"-->",checkBracket_3(file_content))