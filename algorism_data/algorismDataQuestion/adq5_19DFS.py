import queue

map=[
    ['1','1','1','1','1','1'],
    ['e','0','0','0','0','1'],
    ['1','0','1','1','0','1'],
    ['1','1','1','1','0','1'],
    ['1','1','1','1','0','1'],
    ['1','1','1','1','0','x'],
    ['1','1','1','1','1','1'],
    ]
MAZE_SIZE=len(map)
def isValidPos(x,y):
    if 0<=x<MAZE_SIZE and 0<=y<MAZE_SIZE:
        if map[y][x]=='0' or map[y][x]=='x':
            return True
        return False


# 깊이우선탐색(DFS)
# 직접 구현 시...
# class ArrayStack:
#     def __init__(self, capacity=100):
# #         self.stack = [None]*capacity
# #         self.capacity = capacity
# #         self.top = -1

# #     def isEmpty(self):
# #         return self.top == -1

# #     def isFull(self):
# #         return self.top == self.capacity - 1

# #     def push(self, item):
# #         if not self.isFull():
# #             self.top += 1
# #             self.stack[self.top] = item
# #         else:
# #             print("스택이 가득 찼습니다.")

# #     def pop(self):
# #         if not self.isEmpty():
# #             item = self.stack[self.top]
# #             self.top -= 1
# #             return item
# #         else:
# #             print("스택이 비었습니다.")
# #             return None

# #     def peek(self):
# #         if not self.isEmpty():
# #             return self.stack[self.top]
# #         else:
# #             return None

# #     def __str__(self):
# #         return str(self.stack[:self.top + 1])


# # def DFS_1():
# #     print("DFS: ")
# #     stack=ArrayStack(100)
# #     stack.push((0,1))

# #     while not stack.isEmpty():
# #         here=stack.pop()
# #         print(here,end='->')
# #         (x,y)=here
# #         if (map[y][x]=='x'):
# #             return True
# #         else:
# #             map[y][x]='.'
# #             if isValidPos(x,y-1):stack.push((x,y-1))
# #             if isValidPos(x,y+1):stack.push((x,y+1))
# #             if isValidPos(x-1,y):stack.push((x-1,y))
# #             if isValidPos(x+1,y):stack.push((x+1,y))
# #     print("현재 스택: ", stack)

# #     return False
# # result=DFS_1()

# # if result:
# #     print('-->미로탐색성공')
# # else:
# #     print('-->미로탐색실패')

# # # 큐 모듈에서 제공하는 스택 사용 시...

def DFS_2():
    print("DFS: ")
    S=queue.LifoQueue(maxsize=100)
    S.put((0,1))

    while not S.empty():
        here=S.get()
        print(here,end='->')
        (x,y)=here
        if (map[y][x]=='x'):
            return True
        else:
            map[y][x]='.'
            if isValidPos(x,y-1):S.put((x,y-1))
            if isValidPos(x,y+1):S.put((x,y+1))
            if isValidPos(x-1,y):S.put((x-1,y))
            if isValidPos(x+1,y):S.put((x+1,y))
    print("현재 스택: ", S)

    return False

result=DFS_2()

if result:
    print('-->미로탐색성공')
else:
    print('-->미로탐색실패')
