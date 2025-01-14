ball_num=int(input())

x,y=list(map(int, input().split()))

min_row = x
min_colume = y
max_row = x
max_colume = y

for i in range(ball_num-1):
    x,y=list(map(int, input().split()))
    if min_row<x:
        min_row=x
    if min_colume<y:
        min_colume=y
    if max_row>x:
        max_row=x
    if max_colume>y:
        max_colume=y

print((max_row-min_row)*(max_colume-min_colume))