A= input()
counter={}
for a in A:
    if a not in counter:
        counter[a]=0
    counter[a]+=1

    # counter구문 암기!!!