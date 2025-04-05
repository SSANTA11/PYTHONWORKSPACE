
# 배열을 이용한 스택의 구조
cap=10
arr=[None]*10
top=-1

def isEmpty():
    if top==-1:
        return True
    else:
        return False
    
def isFull():
    return top==cap-1

def push(e):
    global top 
    if not isFull():
        top+=1
        arr[top]=e
    else:
        print("stack overflow")
        exit()
def pop(e):
    global top 
    if not isFull():
        top-=1
        return arr[top+1]
    else:
        print("stack underflow")
        exit()
# =======
a=[1,2,3]
print(a.pop(0))
