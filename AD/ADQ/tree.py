# 이진트리의 노드 수 계산도 필요할 수도....
# 이진트리의 레벨 순회를 통해 이진 트리를 배열의 형태로 변환한다.
# 배열의 형에서 중간에 공란이 존재한다면, 이는 완전 이진트리가 아니다
class node:
    def __init__(self, data, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

# 18번
class CircularQueue:
    def __init__(self, capacity=10):
        self.capacity=capacity
        self.array=[None]*self.capacity
        self.front=0
        self.rear=0
    def isEmpty(self):
        return self.front==self.rear
    def isFull(self):
        return self.front==(self.rear+1)%self.capacity
    def enqueue(self, item):
        if not self.isFull():
            self.rear=(self.rear+1)%self.capacity
            self.array[self.rear]=item
        else:
            pass
    def dequeue(self):
        if not self.isEmpty():
            self.front=(self.front+1)%self.capacity
            return self.array[self.front]
        else:
            pass
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front+1)%self.capacity]
        else:
            pass
    def size(self):
        return (self.rear-self.front+self.capacity)%self.capacity

def levelOrder(root):
    l=[None]#0인덱스 비워두기
    que=CircularQueue()
    que.enqueue(root)
    while not que.isEmpty():
        n=que.dequeue()
        l.append(n)
        if n is not None:
            que.enqueue(n.left)
            que.enqueue(n.right)
    return l

def isCompleteBinaryTree(n):
    l=levelOrder(n)
    binaryTree=True
    foundNone=False# 예술적인 아이디어!
    for i in range(1,len(l)):
        if l[i] is None:
            foundNone=True
        elif foundNone:# 예술적인 아이디어!
            binaryTree=False
            return binaryTree
    return binaryTree

# 하단 함수의 노드 레벨 추정은 완전 이진트리일 때만 가능...
# def level(root, node):
#     l = levelOrder(root)
#     foundNode=0
#     for i in range(len(l)):
#         if l[i] is node:
#             while i!=1:
#                 i//=2
#                 foundNode+=1
#     return foundNode

# 개선. 트리구조이면 구할 수 있는 특정 노드의 레벨을 구할 수 있는 함수
def level(root, node):
    if root is node:
        return 1
    elif root is None:
        return 0