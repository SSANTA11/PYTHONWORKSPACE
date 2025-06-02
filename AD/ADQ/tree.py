# 이진트리의 노드 수 계산도 필요할 수도....
# 이진트리의 레벨 순회를 통해 이진 트리를 배열의 형태로 변환한다.
# 배열의 형에서 중간에 공란이 존재한다면, 이는 완전 이진트리가 아니다
class Node:
    def __init__(self, data, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right




# 18번
class CircularQueue:
    def __init__(self, capacity=100):
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
    l=[None] # 0인덱스 비워두기
    que=CircularQueue()
    que.enqueue(root)
    while not que.isEmpty():
        n=que.dequeue()
        l.append(n)
        if n is not None:
            que.enqueue(n.left)
            que.enqueue(n.right)
    return l



def isCompleteBinaryTree(root):
    l=levelOrder(root)
    binaryTree=True
    foundNone=False
    for i in range(1,len(l)):
        if l[i] is None:
            foundNone=True
        elif foundNone:
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
    if root is None:
        return 0
    elif root is node:
        return 1
    l=level(root.left, node)
    if l>0:
        return l+1
    r=level(root.right, node)
    if r>0:
        return r+1
    return 0

# 8.22: 이진트리의 경로의 길이(path depth)를 루트로부커 모든 자식 노드까지의 경로의 길이의 합이라고 하자.
# 경로의 길이를 구하는 다음 연산을 구현하라. 위의 트리에서 경로의 길이는0+1+1+2+2+2=8이다.
# 초안(문제점--> 빅오 n^2(level과 levelOrder 중첩))
def path_length(root):
    sum=0
    for i in levelOrder(root):
        sum+=level(root, i)
    return sum
# 개선안(빅오 문제 해결)
def path_length(root):
    if root is None:
        return 0
    que=CircularQueue()
    que.enqueue((root, 0))
    total=0
    while not que.isEmpty():
        node, depth=que.dequeue()
        if node is not None:
            total+=depth
            que.enqueue((node.left, depth+1))
            que.enqueue((node.right, depth+1))
        return total

def reverse(root):
    if root is not None:
        root.left, root.right = root.right, root.left
        reverse(root.left)
        reverse(root.right)

root = Node('A',Node('B',Node('D'),Node('E')), Node('C'))
# 레벨 3 형태 완전이진트리


print("완전 이진트리 여부 =", isCompleteBinaryTree(root))

print("레벨 순회 결과:")
level_list = levelOrder(root)

print("트리 전체 경로 길이 =", path_length(root))

print("트리 반전 수행")
reverse(root)