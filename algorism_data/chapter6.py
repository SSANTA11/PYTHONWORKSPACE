class Node:
    def __init__ (self, elem, next=None):
        self.data = elem 
        self.link = next

class LinkedList:

    def __init__( self ):
        self.head = None
    
    def isEmpty( self ): 
        return self.head == None

    def isFull( self ): 
        return False

    def getNode(self, pos) :
        if pos < 0 : 
            return None
        node = self.head
        while pos > 0 and node != None :
            node = node.link
            pos -= 1
        return node

    def getEntry(self, pos) :
        node = self.getNode(pos)
        if node == None : 
            return None
        else : 
            return node.data

    def insert(self, pos, elem) :
        before = self.getNode(pos-1)
        if before == None :
            self.head = Node(elem, self.head)
        else :
            node = Node(elem, before.link)
            before.link = node

    def delete(self, pos) :
        before = self.getNode(pos-1)
        if before == None :
            if self.head is not None :
                self.head = self.head.link
        elif before.link != None :
            before.link = before.link.link

    def size( self ) :
        node = self.head
        count = 0
        while node is not None :
            node = node.link
            count += 1
        return count
    
    def __str__( self ) :
        arr = []
        node = self.head
        while node is not None :
            arr.append(node.data)
            node = node.link
        return str(arr)
    
    def replace(self, pos, elem) :
        node = self.getNode(pos)
        if node != None : 
            node.data = elem

    def find(self, val) :
        node = self.head
        while node is not None:
            if node.data == val : 
                return node
            node = node.link
        return node

# 초안
# 순서대로 출력하기 위해선...
# 1. 순서대로 담아서 반환하기 위해 리스트가 요구됨. 고로 일단 리스트 반환으로 생각 중... --> 대체 가능할 수도? void로 반환 없이 프린트 사용하여 반복문 돌리기
# 2. 리스트의 인덱스를 고려해야함. 일단 반복문 밖에 변수 0 초기화. 연결된 구조의 인덱스는 getNode를 응용가능
# 3. getNode를 통해 특정 노드를 가져오면, 해당 노드의 데이터필드를 의미하는 getEntry로 데이터 다루기..
    def printForward1(self):
        index=0
        if not self.isEmpty():
            while True:
                if not self.getNode(index)==None:
                    print(self.getEntry(index), end=" ")
                else:
                    break
                index+=1
# 수정안 1- 빅오 개선
    def printForward2(self):
        index=0
        if not self.isEmpty():
            while True:
                node=self.getNode(index)
                if not node==None:
                    print(node.data, end=" ")
                else:
                    break
                index+=1

# 수정안 2- 가독성 개선
    def printForward3(self):
        index=0
        if not self.isEmpty():
            node=self.getNode(index)
            while node is not None:
                print(node.data, end=" ")
                index+=1
                node=self.getNode(index)

# 수정안 3- 빅오 개선 O(n^2)-->O(n)
    def printForward4(self):
        if not self.isEmpty():
            index=0
            node=self.getNode(index)
            while node is not None:# 이게 더 가독성 있는 듯한데... 내부에선 어떻게 굴러갈지 모르겠다... 막연히 효율 차이가 없다 가정하고 작성 중...
                print(node.data, end=" ")
                index+=1
                node=node.link



# 초안
# 상당 부분 printForward와 유사하게 가능할 것으로 예상...
# 1. 우선 임시로 담아둘곳이 필요할 수도... 그게 아니라면 가장 마지막 인덱스부터 확정해야하는데 이게 특정 불가능...
# 1-1. 아니다 가능하다.우선 인덱스 0부터 차례대로 link가 None이 나올 때까지 가서 마지막 인덱스를 특정한다. 여기까지 O(n)이 나온다...
# 2. 이후엔 반복문 -1로 반대로 출력한다
    def printReverse(self):
        if self.isEmpty() is not True: # 당연히 가독성 때문에 표현한 방식...
            index=0
            node=self.getNode(index)
            while node is not None:
                node=node.link
                index+=1
            finalIndex=index-1
            for i in range(finalIndex,0-1,-1): # 인덱싱 헷갈려서 논리를 펼쳐 기입함. --> 0-1
                print(self.getEntry(i)) # 이런... 빅오가 아직 n^2이다...->수정예정
# 수정안- 빅오 개선
    def printReverse(self):
        if self.isEmpty() is not True:
            index=0
            node=self.getNode(index)
            while node is not None:
                node=node.link
                index+=1
            finalIndex=index-1
            for i in range(finalIndex,0-1,-1):
                print(self.getEntry(i)) 
    
            
            
            


    def append(self, e):