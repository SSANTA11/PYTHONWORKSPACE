# 원형큐와 덱

# 큐의 특징
    # 선입 선출(FIFO)
    # 한번 enqueue할 때 앞선 요소들이 모두 움직여야 한다

# 큐의 발전형: 원형 큐
    # 나머지 연산자를 활용한 발전형인 원형 큐
    # 소프트웨어의 논리로 구현된 추상형이기에 당연히 실재론 일반 큐와 동일
        # 나머지 연산자를 활용한 원형 개념을 구현
    # 특징
        # 포화 상태와 오류 상태 구별하기
            # 포화 상태: 원형 큐의 한 칸이 비어 있을 때
            # 오류 상태: 모든 인덱스가 찼을 때

class CQue():
    def __init__(self, capacity=8):
        self.capacity=capacity
        self.array=[None]*capacity
        self.front=0
        self.rear=0
    def isEmpty(self):
        return self.front==self.rear
    def isFull(self):
        return self.front==(self.rear+1)%self.capacity
    def enqueue()