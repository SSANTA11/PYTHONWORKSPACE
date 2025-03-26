# parameter: 매개변수
def print_3_org(문자열): # 문자열 -> 매개변수
    print(문자열)
    print(문자열)
    print(문자열)

# argument: 인수
print_3_org("안녕") # 안녕 -> 인수

print("-=-="*4)
def print_3_ver1(문자열, 횟수): # 문자열 -> 매개변수
    for i in range(횟수):
        print(문자열)

# 가변 매개변수 
# : 투입되는 매개변수의 갯수가 가변인 매개변수 특성을 지칭
print_3_ver1("안녕",4)

def print_n_t(횟수,리스트):
    for i in range(횟수):
        for 요소 in 리스트:
            print(요소,end='')
print_n_t(2,['가','나','다','라'])
print("\n")
print("-=-="*4)
print("\n")
# 가변매개변수 EX)
def print_n_t_v1(횟수,*가변매개변수):
    for i in range(횟수):
            print(*가변매개변수,end='')
print_n_t_v1(2,*['가','나','다','라'])

a=[1,2,3,4]
print(*a)

def start_all(start,end):
    a=(start+end)*(end-start+1)/2
    return print(a)
s=int(input("시작 숫자"))
e=int(input("끝 숫자"))
start_all(s,e)