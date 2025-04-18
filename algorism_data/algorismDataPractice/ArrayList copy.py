class Arraylist:
    def __init__(self, capacity):
        self.capacity=capacity
        self.array=capacity*[None]
        self.size=0
    
    def isEmpty(self):
        return self.size==0
    
    def isFull(self):
        return self.size==self.capacity
    
    def get(self, pos):
        if 0<=pos<self.capacity:
            return self.array[pos]
        else:
            raise IndexError("저런~~ 인덱스 범위를 초과하셨네요")
    def insert(self, pos, e):
        if not self.isFull() and 0<=pos<self.capacity:
            for i in range(self.size, pos, -1):
                self.array[i]=self.array[i-1]
            self.array[pos]=e
            self.size+=1
        else:
            if self.isFull():
                 raise IndexError("앗! 리스트오버플로우;;")
            else:
                 raise IndexError("이런;; 인덱스 범위를 벗어나셨어요")
    def delete(self,pos):
        if not self.isEmpty() and 0<=pos<self.size:
            for i in range(pos, self.size -1):
                self.array[i]=self.array[i+1]
            self.array[pos]=None
            self.size-=1
        else:
            if self.isEmpty():
                 raise IndexError("앗! 리스트언더플로우;;")
            else:
                 raise IndexError("이런;; 인덱스 범위를 벗어나셨어요")
    def __str__(self):
        return str(self.array[0:self.size])