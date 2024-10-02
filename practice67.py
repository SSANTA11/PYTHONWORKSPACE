numbers=[1,2,6,8,3,2,3,4,3,2,1,2,2,2,3,4,5,8]
counter={}
numbers.sort()
for number in numbers:
    counter[number]=0  

for number in numbers:
    counter[number]=counter[number]+1

print(counter)