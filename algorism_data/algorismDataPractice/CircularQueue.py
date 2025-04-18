class CirclularQueue:
    def __init__(self, capacity=8):
        self.capacity=capacity
        self.array=[None]*capacity
        self.front=0
        self.rear=0

    def isEmpty(self):
        return self.front==self.rear

    def isFull(self):
        return self.front==(self.rear+1)%self.capacity

    def enqueue(self, item):
        if not self.isFull():
            self.rear=(self.rear+1)%self.capacity #후단 갱신
            self.array[self.rear]=item #후단에 요소 추가
        else:
            pass

    def dequeue(self):
        if not self.isEmpty():
            self.front=(self.front+1)%self.capacity # 전단의 요소 삭제
            return self.array[self.front] # pop과 같이 요소 삭제 후 반환
        else:
            pass
    def peek(self): # 가장 전단의 요소를 찾아 반환한다
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else:
            pass
    def size(self): # 크기를 확인하고 반환한다
        return (self.rear-self.front+self.capacity)%self.capacity
