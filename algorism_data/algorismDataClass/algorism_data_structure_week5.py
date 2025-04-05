# 4 장 스택
    # 전위 중위 후위 표기법??
        # 저번 주 진도....
    # 미로 탐색
        # 이번주 진도....

# 미로탐색
    # 이차원 배열을 이용하여 미로탐색 가능
        # 1.정방형 리스트 활용
        # 2.입구, 출구 생성
        # 3.벽과 경로 생성
    # 미로탐색에서 스택의 사용
        # 갈림길을 기록하고 번복을 위해 '후입 선출' 스택이 사용된다!!
    # 순서: DFS(깊이우선) 탐색
        # 1. 시작위치 스택에 입력
        # 2. 스택이 공백X-> 하나의 위치 꺼낸다. 방문 후에는 '.'표시
        # 3. 현재 위치 출구면 끝
        # 4. 스택에는 결국 올바른 경로의 원소들만 들어간다.
        # 5. 잘못된 길이면 후입을 선출하여 인전 위치로 복귀한다.
from algorism_data_structure_week4_0 import ArrayStack


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

def DFS():
    print("DFS: ")
    stack=ArrayStack(100)
    stack.push((0,1))

    while not stack.isEmpty():
        here=stack.pop()
        print(here,end='->')
        (x,y)=here
        if (map[y][x]=='x'):
            return True
        else:
            map[y][x]='.'
            if isValidPos(x,y-1):stack.push((x,y-1))
            if isValidPos(x,y+1):stack.push((x,y+1))
            if isValidPos(x-1,y):stack.push((x-1,y))
            if isValidPos(x+1,y):stack.push((x+1,y))
    print("현재 스택: ", stack)

    return False
result=DFS()
if result:
    print('-->미로탐색성공')
else:
    print('-->미로탐색실패')
# 의문:
    # 1. 스택에 아무것도 없다.->길이없다?
    # 2. size사용 이유?
    # 3. DFS 부분 통째로 이해 못함
    # 4. C언어 버전 ArrayStack에서 typedef과 구조체 미숙 element라는 이름?
        # 4-1. typedef A B;
        # 4-2. 단일 원소만을 받는 C언어 배열의 특징으로 인한 typedef의 element사용???
    # 5. 왜 작동 안하나?
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 5 장 큐와 덱

# 큐
    # 특징
        # 1. 선입 선출
        # 2. 전단과 후단으로 나뉨
        # 3. front가 최선방에 한칸 앞을, rear는 최후방을 가르킨다
        #   -> 원소가 없을 때 전후가 바뀌기 때문에 일부로 그렇게 설정

    # ADT
        # 1.enqueue(e): 요소 e를 큐의 맨 뒤에 추가
        # 2.dequeue(): 큐의 맨 앞에 있는 요소를 꺼내 반환
        # 3.isEmpty():큐가 비어있으면 True를 아니면 False를 반환
        # 4.isFull():큐가 가득 차있으면 True를 아니면 False를 반환
        # 5.peek(): 큐의 맨 앞에 있는 요소를 삭제하지 않고 반환***스택과 다르다

    # 큐의 구현 방법
        # 선형 큐
            # 큐 한개가 추가된다-> 기존 앞부분이 모두 밀림
        # 원형 큐
            # 큐 한개가 추가된다-> 나머지 연산을 고려하여 움직임 없이 추가 배치한다
            # 대신 꽉 차면 안된다
capacity=100

class CircularQueue:
    def __init__(self, capacity):
        self.capacity=capacity
        self.arr=[None]*capacity
        self.front=self.rear=0

        def isEmpty(self):
            return self.front==self.rear
        def isFull(self):
            return self.front==(self.rear+1)%self.capacity
        def enqueue(self, item):
            if not self.isFull():
                self.rear=(self.rear+1)%self.capacity
                self.arr[self.rear]=item
            else:
                pass
        def denqueue(self, item):
            if not self.isFull():
                self.front=(self.front+1)%self.capacity
                self.arr[self.front]=item
            else:
                pass
        def peek(self):
            if not self.isEmpty():
                return self.arr(self.front+1)


# 의문:
    # 1. 왜 peek이 스택과 다른가?-> 스택은 pop의 위치를 줄여서 ~~, front위치의 '다음'을 읽어내고 값을 바꾸지 않는다