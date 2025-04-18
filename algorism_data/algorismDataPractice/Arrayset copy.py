class ArraySet:
    def __init__(self, capacity=10):
        self.capacity=capacity
        self.array=[None]*capacity
        self.size=0
    def isEmpty(self):
        return self.size==0
    def isFull(self):
        return self.capacity==self.size
    def __str__(self):
        return str(self.array[0:self.size])

    def contains(self, e):
        for i in range(0,self.size):
            if e==self.array[i]:
                return True
        return False
    def insert(self, e):
        if not self.contains(e) and not self.isFull():
            self.array[self.size]=e
            self.size+=1
        else:
            return                
    def delete(self, e):
        if not self.isEmpty() and self.contains(e):
            for i in range(self.size):
                 if self.array[i]==e:
                     self.array[i]=self.array[self.size-1]
                     self.array[self.size]=None
                     self.size-=1
                     return
        else:
            return
    def union(self, setB):
        setC=ArraySet()
        for i in range(self.size):
            setC.insert(self.array[i])
        for i in range(setB.size):
            if not setC.contains(setB.array[i]):
                setC.insert(setB.array[i])
        return setC
        
    def intersect(self,setB):
        setC=ArraySet()
        for i in range(self.size):
            if setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC
    
    def difference(self, setB):
        setC=ArraySet()
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC