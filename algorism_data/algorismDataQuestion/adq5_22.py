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
    def dequeue(self):
        if not self.isEmpty():
            self.front=(self.front+1)%self.capacity
            return self.arr[self.front]
        else:
            pass
    def peek(self):
        if not self.isEmpty():
            return self.arr[(self.front+1)%self.capacity]


class CircularDeque(CircularQueue):
    def __init__(self, capacity=10):
        super().__init__(capacity)

        # isEmpty(),isFull(),size(),__str__()
    def addRear(self,item):
        self.enqueue(item)
    def deleteFront(self):
        return self.dequeue()
    def getFront(self):
        return self.peek()

    # 새로 구현이 필요한 것들
    def addFront(self, item)    :
        if not self.isFull():
            self.arr[self.front]=item
            self.front=(self.front-1+self.capacity)%self.capacity
        else:
            pass
    def deleteRear(self):
        if not self.isEmpty():
            item=self.arr[self.rear]
            self.rear=(self.rear-1+self.capacity)%self.capacity
            return item
        else:
            pass
    def getRear(self):
        if not self.isEmpty():
            return self.arr[self.rear]
        else:
            pass

# 회문 검사기


def palindrome():
    st=CircularDeque(100)
    word=input().upper()
    a=0
    for ch in word:
        if ('A'<=ch<='Z'):
            st.enqueue(ch)
            a+=1
    for i in range(a//2):
        if (st.getFront()!=st.getRear()):
            return False
        st.deleteFront()
        st.deleteRear()
    return True
print(palindrome())
