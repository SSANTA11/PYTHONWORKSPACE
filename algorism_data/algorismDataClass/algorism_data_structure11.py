# 정렬
# 탐색
# 순차탐색
# 코드 7.8: 이진 탐색  알고리즘(순환 구조)     참고 파일: ch07/basic_search.py
def binary_search(A, key, low, high) :
    if (low > high) :				# 종료 조건: 하나 이상의 항목이 있어야 함
        return -1        			# 탐색 실패

    middle = (low + high) // 2
    print(A[middle], end=' ')
    if (key == A[middle]) :	    # 탐색 성공
        return middle
    elif (key<A[middle]) :	# 왼쪽 부분리스트 탐색
        return binary_search(A, key, low, middle - 1)
    else :						# 오른쪽 부분리스트 탐색
        return binary_search(A, key, middle + 1, high)

# 이진 탐색(반복)
def binary_search_iter(A, key, low, high) :
    while (low <= high) :       	# 항목들이 남아 있으면(종료 조건)
        middle = (low + high) // 2
        print(A[middle], end=' ')
        if key == A[middle]:	    # 탐색 성공
            return middle
        elif (key > A[middle]):	# key가 middle의 값보다 크면
            low = middle + 1		# middle+1 ~ high 사이 검색
        else:						# key가 middle의 값보다 작으면
            high = middle - 1		# low ~ middle-1 사이 검색
    return -1   					# 탐색 실패

# 보간탐색
def interpolation_search(A, key, low, high) :
    while (low <= high) :       	# 항목들이 남아 있으면(종료 조건)
        mid = low + ((high - low) * (key - A[low])) / (A[high] - A[low])
        print(A[mid], end=' ')
        if key == A[mid]:	    # 탐색 성공
            return mid
        elif (key > A[mid]):	# key가 middle의 값보다 크면
            low = mid + 1		# mid+1 ~ high 사이 검색
        else:						# key가 middle의 값보다 작으면
            high = mid - 1		# low ~ mid-1 사이 검색
    return -1   					# 탐색 실패

# -----------------------------------------------------------------------------------------------------------------------------------------------
# 8장 

# 코드 8.1: 이진트리를 위한 노드 클래스

# CircularQueue.py
class CircularQueue :
    def __init__( self, capacity = 8 ) :
        self.capacity = capacity        # 용량(고정)
        self.array = [None] * capacity  # 요소들을 저장할 배열
        self.front = 0                  # 전단의 인덱스
        self.rear = 0                   # 후단의 인덱스

    def isEmpty( self ) :
       return self.front == self.rear

    def isFull( self ) :
       return self.front == (self.rear+1)%self.capacity

    def enqueue( self, item ):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item

    def dequeue( self ):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]

    def peek( self ):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]

    def size( self ) :
       return (self.rear - self.front + self.capacity) % self.capacity

    def __str__(self):
        if self.front < self.rear :
            return str(self.array[self.front+1:self.rear+1])
        else :
            return str(self.array[self.front+1:self.capacity] + \
                       self.array[0:self.rear+1] )


#======================================================================
if __name__ == "__main__":
    q = CircularQueue(8)
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    q.enqueue('D')
    q.enqueue('E')
    q.enqueue('F')
    print('A B C D E F 삽입: ', q)
    print('삭제 -->', q.dequeue())
    print('삭제 -->', q.dequeue())
    print('삭제 -->', q.dequeue())
    print('      3번의 삭제: ', q)
    q.enqueue('G')
    q.enqueue('H')
    q.enqueue('I')
    print('      G H I 삽입: ', q)

class TNode:
    def __init__ (self, elem, left, right):
        self.data = elem
        self.left = left
        self.right = right

    def isLeaf(self):
        return self.left is None and self.right is None

# 코드 8.2: 이진트리의 전위순회
def preOrder(n) :
    if n is not None :
        print(n.data, end=' ')
        preOrder(n.left)
        preOrder(n.right)

# 코드 8.3: 이진트리의 중위순회
def inOrder(n) :
    if n is not None :
        inOrder(n.left)
        print(n.data, end=' ')
        inOrder(n.right)

# 코드 8.4: 이진트리의 후위순회
def postOrder(n) :
    if n is not None :
        postOrder(n.left)
        postOrder(n.right)
        print(n.data, end=' ')

# 코드 8.5: 이진트리의 레벨순회

def levelOrder(root) :
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

# 코드 8.6: 이진트리의 노드 수 계산
def count_node(n) :
    if n is None :
        return 0
    else :
        return 1 + count_node(n.left) + count_node(n.right)

# 코드 8.7: 이진트리의 단말노드 수 계산
def count_leaf(n) :
    if n is None : return 0
    elif n.isLeaf() : return 1
    else : return count_leaf(n.left) + count_leaf(n.right)


# 코드 8.8: 이진트리의 트리의 높이 계산
def calc_height(n) :
    if n is None : return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight) : return hLeft + 1
    else: return hRight + 1


# 코드 8.9: 이진 트리 연산 테스트 프로그램
if __name__ == "__main__":
    print("\n======= 이진트리 테스트 ===================================")
    d = TNode('D', None, None)
    e = TNode('E', None, None)
    b = TNode('B', d, e)
    f = TNode('F', None, None)
    c = TNode('C', f, None)
    root = TNode('A', b, c)

    print('\n   In-Order : ', end='')
    inOrder(root)
    print('\n  Pre-Order : ', end='')
    preOrder(root)
    print('\n Post-Order : ', end='')
    postOrder(root)
    print('\nLevel-Order : ', end='')
    levelOrder(root)
    print()

    print(" 노드의 개수 = %d개" % count_node(root))
    print(" 단말의 개수 = %d개" % count_leaf(root))
    print(" 트리의 높이 = %d" % calc_height(root))
