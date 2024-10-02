A,B,V=map(int,input().split())
a_1=0
a_2=0
while True:
    a_1+=A
    a_2+=1

    if a_1>=V:
        print(a_2)
        break
    a_1-=B