# 세준이의 기말고사
N=int(input())
grades_input=input().split()
grades_list=[]

for i in range(N):
    grades_list.append(int(grades_input[i]))

max_num=int(max(grades_list))

trick=[]

for r in range(N):
    b=grades_list[r]/max_num*100
    trick.append(b)

print(sum(trick)/N)    
# 학습 포인트: 
# max() 함수의 산출물은 str이다(input()과 동일). 
# 고로, int() 처리해주자!