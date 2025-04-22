class ArrayStack:
    def __init__(self, capacity=10):
        self.capacity=capacity
        self.array=[None]*self.capacity
        self.top=-1
    def isEmpty(self):
        return self.top==-1
    def isFull(self):
        return self.capacity-1==self.top
    def push(self, e):
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
        return str(self.array[0:self.top])

def evalPostFix(expr):
    s = ArrayStack()
    for token in expr:
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if token == "+": s.push(val1 + val2)
            elif token == "-": s.push(val1 - val2)
            elif token == "*": s.push(val1 * val2)
            elif token == "/": s.push(val1 / val2)
        else:
            s.push(float(token))
    return s.pop()
a=["1","1",'/']
print(evalPostFix(a))
