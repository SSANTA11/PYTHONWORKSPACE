height=int(input())

for l in range(1, height+1):
    print(f'{(height-l)*" "}{(l*2-1)*"*"}')