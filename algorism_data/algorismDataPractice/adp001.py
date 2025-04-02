# 🧪 실습 문제 1. 기본 스택 구현

# [문제 설명]
    # 고정 크기의 스택을 직접 구현해보자. 다음 기능이 포함되어야 한다.
    # push(e): 정수를 스택에 삽입
    # pop(): 스택의 가장 위 값을 꺼내서 반환
    # peek(): 삭제 없이 맨 위 값만 확인
    # isEmpty(): 비었는지 확인
    # isFull(): 가득 찼는지 확인

# [요구사항]
    # 크기는 5로 고정
    # 사용자에게 숫자를 입력 받아 스택에 push
    # 숫자 0을 입력하면 pop 실행
    # 숫자 -1을 입력하면 종료
    # 종료 시 최종 스택 상태 출력

# 스택의 ADT
    # 1. 선입 후출
    # 2. 추가되거나 빠지면 전체 이동
    # 3. 스택안이 아무것도 없을 경우 -1로 표시
    #   -> 왜냐하면 1개라도 있다면 0이 top
    # 4. TOS는 생각
class ArrStack:
    def __init__(self,capacity):
        self.capacity=capacity
        self.arr=[None]*self.capacity
        self.top=-1
    def isEmpty(self):
        return self.top==-1
    def isFull(self):
        return self.top==self.capacity-1
