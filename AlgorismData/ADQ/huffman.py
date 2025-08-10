# 최소힙의 삽입 알고리즘
def heappush(heap, n):
    heap.append(n)
    i = len(heap)-1
    while i != 1 :
        pi = i//2
        if not (n < heap[pi]):
            break
        heap[i] = heap[pi]
        i = pi
    heap[i] = n

    # 최대힙의 삭제 알고리즘
def heappop(heap) :
    size = len(heap) - 1
    if size == 0 :
       return None

    root = heap[1]
    last = heap[size]
    pi = 1
    i = 2

    while (i <= size-1):
        if i < size and heap[i] < heap[i+1]:
            i += 1
        if not (last > heap[i]):
            break
        heap[pi] = heap[i]
        pi = i
        i *= 2

    heap[pi] = last
    heap.pop()
    return root

class Node:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffmanTree(charFreq):
    heap = [None]
    for char, freq in charFreq:
        heappush(heap, Node(char, freq))

    while len(heap) > 2:
        left = heappop(heap)
        right = heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heappush(heap, merged)
    return heap[1]

def hCode(node, code=''):
    if node is None:
        return []

    if node.data is not None:
        return [(node.data, code)]

    return hCode(node.left, code + '0') + hCode(node.right, code + '1')

charFreq = [('A', 40), ('B', 30), ('C', 20), ('D', 10)]
root = huffmanTree(charFreq)
codes = hCode(root)

print("허프만 코드:")
for ch, c in codes:
    print(f"{ch}: {c}")
