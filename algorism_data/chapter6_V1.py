class LinkedStack :
    def __init__( self ):
        self.top = None

    def isEmpty( self ):
        return self.top == None

    def push( self, item ):
        self.top = Node(item, self.top)

    def peek( self ):
        if not self.isEmpty():
            return self.top.data

    def pop( self ):
        if not self.isEmpty():
            data = self.top.data
            self.top = self.top.link
            return data

    def size( self ):
        node = self.top
        count = 0
        while not node == None :
            node = node.link
            count += 1

    def __str__(self):
        arr = []
        node = self.top
        while not node == None :
            arr.append(node.data)
            node = node.link
        return str(arr)

class Node:
    def __init__ (self, elem, link=None):
        self.data = elem
        self.link = link
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
            node=self.getNode(0)
            while node is not None:# 이게 더 가독성 있는 듯한데... 내부에선 어떻게 굴러갈지 모르겠다... 막연히 효율 차이가 없다 가정하고 작성 중...
                print(node.data, end=" ")
                node=node.link



# 초안
# 상당 부분 printForward와 유사하게 가능할 것으로 예상...
# 1. 우선 임시로 담아둘곳이 필요할 수도... 그게 아니라면 가장 마지막 인덱스부터 확정해야하는데 이게 특정 불가능...
# 1-1. 아니다 가능하다.우선 인덱스 0부터 차례대로 link가 None이 나올 때까지 가서 마지막 인덱스를 특정한다. 여기까지 O(n)이 나온다...
# 2. 이후엔 반복문 -1로 반대로 출력한다
    def printReverse1(self):
        if self.isEmpty() is not True: # 당연히 가독성 때문에 표현한 방식...
            index=0
            node=self.getNode(index)
            while node is not None:
                node=node.link
                index+=1
            finalIndex=index-1
            for i in range(finalIndex,0-1,-1): # 인덱싱 헷갈려서 논리를 펼쳐 기입함. --> 0-1
                print(self.getEntry(i)) # 이런... 빅오가 아직 n^2이다...
# linkedStack활용
    def printReverse2(self):
        if not self.isEmpty():
            s=LinkedStack()
            node=self.getNode(0)
            while node is not None:
                s.push(node.data)
                node=node.link
            for i in range(s.size()):
                print(s.pop(), end="") # 빅오 해결!!! 이제는 O(n)이다!!


# 초안
# 기존의 작성한 필드 메서드를 응용하자. 예상하건데 아마 size()가 쓰일 듯....(하다보니 느낀건데 왜 앞선 메서드 작성에선 size를 안썼을까...? 의도와 무관하게 size의 원리를 성실히 공부해버렸다;;;)
# 1. 데이터 e를 가진 노드를 생성하자.
# 2. 최후방 노드를 특정해야한다. 이번에는 놓지지 말고 현명하게 size()를 사용하자
# 3. 기존의 최후방 노드의 링크가 앞서 생성한 노드를 가르키게 만들자.
    def append1(self, e):
        if self.isEmpty is not True:
            node=Node(e)
            tailNode=self.getNode(self.size()-1)
            tailNode.link=node
        else:
            self.head=Node(e)
# 수정안1 - 변수 최소화
    def append2(self, e):
        if self.isEmpty() is not True:
            node=self.getNode(self.size()-1) # 빅오가 n^2이 된다... 아마 tail이 있다면 줄일 수도
                                             # --> 그러나... 그렇게 한다면 몇몇 메서드들도 수정이 필요함으로 PASS!--> 아마 뒤에 18번을 구현하다면 해결될 문제...!
            node.link=Node(e)
        else:
            self.head=Node(e)

# 초안
# 앞서 제작한 메서드들을 잘 활용한다면 쉽게 풀릴 것을 예상된다.
# 고려해야하는 요소는 최종 길이이다. 합병 이후 늘어나는 A는 size가 늘어나야하고 B는 결국 0이된다.
# 또한 옮겨진 B리스트의 요소들은 순서가 뒤섞이면 안된다.
# 1. 우선 B 리스트의 길이를 구하자. 이는 후에 반복문에서 사용한다.( A도 구하자. 이는 B의 원소를 넣을 위치를 가르킬 때 사용한다.--> 아니다 어짜피 뒤에 이어 쓴다면 append로 해결가능!!)
# 2. 반복문을 돌려 0부터 n까지 리스트의 원소를 차례로 옮기자. 이때 A에는 append1이나 append2를 사용하고, 이후 곧바로 B는 최후방 노드에 delete를 사용한다.
# (tail을 넣어야하나;;하고 고민했지만 그럴 필요는 없을 듯! 개선해야되는 문제는 18번 문제의 조건에 따라 해소하자)
# 3. B의 size가 0이 될 때까지 반복한다면, A기준으로 merge() 작동완료!
    def merge(self,B):
        BSize=B.size()
        for i in range(BSize):
            self.append2(B.getEntry(0))
            B.delete(0)
