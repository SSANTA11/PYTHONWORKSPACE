numbers=[1,2,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
counter={}

for number in numbers:
    if number not in counter:
        counter[number]=0
    counter[number]+=1
print(counter)