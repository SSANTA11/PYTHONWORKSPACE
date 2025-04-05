# capacity=10
# array=[None]*capacity
# top=-1

# # 스택의 연산: 일반함수
# def isEmpty():
#     if top==-1:
#         return True
#     else:
#         return False

# def isFull():
#     return top==capacity-1

# def push(e):
#     if not isFull():
#         top+=1
#         array[top]=e



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


# capacity = 10
# array = [None] * capacity
# top = -1

# def isEmpty():
#     return top == -1

# def isFull():
#     return top == capacity - 1

# def push(e):
#     global top
#     if not isFull():
#         top += 1
#         array[top] = e  # Store the element directly
#     else:
#         print("Stack Overflow")
#         exit()

# def pop():
#     global top
#     if not isEmpty():
#         value = array[top]  # Get the value at the top
#         top -= 1  # Move the top pointer down
#         return value
#     else:
#         print("Stack Underflow")
#         exit()

# def peek():
#     if not isEmpty():
#         return array[top]
#     else:
#         return None  # If the stack is empty, return None

# # Input string from the user
# ch = input("입력: ")
# for i in ch:
#     push(i)

# print("문자열 출력: ", end='')
# while not isEmpty():
#     print(pop(), end=' ')
# print()



# s=ArrayStack(100)
# msg=input("문자열 입력:")
# for c in msg:
#   s.push(c)

# print("문자열 출력: ", end='')
# while not s.isEmpty():
#   print(s.pop(),end='')



# def checkbrackets(statement):
#   stack=ArrayStack(100)
#   for ch in statement:
#     if ch in ('(','[','{'):
#       stack.push(ch)
#     elif ch in (')',']','}'):
#       if stack.isEmpty():
#         return False
#       else:
#         left=stack.pop()
#         if (ch==')' and left!='(') or (ch==']'and left!='[') or (ch=='}' and left!='{'):
#           return False

#   return stack.isEmpty()



# checkbrackets(input())