numbers=[1,2,3,4,5,6,7,8,9]
output=[[],[],[]]
for number in numbers:
    if number>=7:
        output[number-7].append(number)
    elif number>=4:
        output[number-4].append(number)
    elif number<=3:
        output[number-1].append(number)
print(output)