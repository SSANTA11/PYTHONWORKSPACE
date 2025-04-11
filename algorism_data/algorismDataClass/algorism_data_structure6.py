# 시험출제 포커스
    # 구조를 아느냐
    # 프로그래밍으로 구현 가능한가
    # 알고리즘을 쓰시오는 잘 안나옴 
    # '자료구조' 집중하여 준비하자
from algorism_data_structure_week5 import isValidPos
# 큐
    # 선입선출
    # 배열구조로 큐를 다루면 문제가 있다
        # 쉬프트가 연속으로 발생해야한다

class CircularQueue:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else:
            pass  # or return False

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else:
            return None

    def __str__(self):
        if self.isEmpty():
            return "[]"
        result = []
        i = (self.front + 1) % self.capacity
        while i != (self.rear + 1) % self.capacity:
            result.append(self.array[i])
            i = (i + 1) % self.capacity
        return str(result)


# 테스트 예제
q = CircularQueue(8)
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
print(q)            # ['A', 'B', 'C']
print(q.dequeue())  # A
print(q.peek())     # B
print(q)            # ['B', 'C']

def BFS():
    que = CircularQueue()
    que.enqueue((0, 1))  # 튜플로 삽입
    print('BFS: ')

    while not que.isEmpty():
        here = que.dequeue()
        print(here, end='->')
        x, y = here

        if map[y][x] == 'x':
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1): que.enqueue((x, y - 1))  # ← 튜플로
            if isValidPos(x, y + 1): que.enqueue((x, y + 1))
            if isValidPos(x - 1, y): que.enqueue((x - 1, y))
            if isValidPos(x + 1, y): que.enqueue((x + 1, y))

    return False  # ← 루프 끝난 뒤의 return


