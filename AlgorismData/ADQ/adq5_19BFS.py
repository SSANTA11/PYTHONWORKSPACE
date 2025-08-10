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


# 너비우선탐색(BFS)
# 직접 구현할 시...

# class CircularQueue:
#     def __init__(self, capacity=100):
#         self.capacity=capacity
#         self.arr=[None]*capacity
#         self.front=self.rear=0
#     def isEmpty(self):
#         return self.front==self.rear
#     def isFull(self):
#         return self.front==(self.rear+1)%self.capacity
#     def enqueue(self, item):
#         if not self.isFull():
#             self.rear=(self.rear+1)%self.capacity
#             self.arr[self.rear]=item
#         else:
#             pass
#     def dequeue(self):
#         if not self.isEmpty():
#             self.front=(self.front+1)%self.capacity
#             return self.arr[self.front]
#         else:
#             pass
#     def peek(self):
#         if not self.isEmpty():
#             return self.arr[(self.front+1)%self.capacity]

# def BFS_1():
#     que=CircularQueue()
#     que.enqueue((0,1))
#     print('BFS:')
#     while not que.isEmpty():
#         here=que.dequeue()
#         print(here, end='->')
#         x,y=here
#         if (map[y][x]=='x'):
#             return True
#         else:
#             map[y][x]='.'
#             if isValidPos(x,y-1):que.enqueue((x,y-1))
#             if isValidPos(x,y+1):que.enqueue((x,y+1))
#             if isValidPos(x-1,y):que.enqueue((x-1,y))
#             if isValidPos(x+1,y):que.enqueue((x+1,y))

# result=BFS_1()

# if result:
#     print('-->미로탐색성공')
# else:
#     print('-->미로탐색실패')

#  큐 모듈을 사용할 시

def BFS_2():
    print('BFS:')
    Q=queue.Queue(maxsize=100)
    Q.put((0,1))
    while not Q.empty():
        here=Q.get()
        print(here, end='->')
        x,y=here
        if (map[y][x]=='x'):
            return True
        else:
            map[y][x]='.'
            if isValidPos(x,y-1):Q.put((x,y-1))
            if isValidPos(x,y+1):Q.put((x,y+1))
            if isValidPos(x-1,y):Q.put((x-1,y))
            if isValidPos(x+1,y):Q.put((x+1,y))

result=BFS_2()

if result:
    print('-->미로탐색성공')
else:
    print('-->미로탐색실패')