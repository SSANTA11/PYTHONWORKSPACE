A=[1,2,3,4,1,2,3,1,4,1,2,3]
카운터={}
for a in A:
    if a not in 카운터:
        카운터[a]=0
    카운터[a]+=1

print(카운터)
print(f"사용된 숫자의 종류는 {len(카운터)}개입니다.")