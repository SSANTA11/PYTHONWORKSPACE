data_storage={"A":10,"B":11,"C":12,"D":13,
              "E":14,"F":15,"G":16,"H":17,
              "I":18,"J":19,"K":20,"L":21,
              "M":22,"N":23,"O":24,"P":25,
              "Q":26,"R":27,"S":28,"T":29,
              "U":30,"V":31,"W":32,"X":33,
              "Y":34,"Z":35}

a=set(data_storage.keys())

input_data=input().split()

N=input_data[0]
B=int(input_data[1])

save=[]
cal=[]
for n in N:
    if n not in a:
        n=int(n)
    else:
        n=int(data_storage[n])
    save.append(n)

save.reverse()
for i in range(len(save)):
    cal.append(save[i]*B**i)

print(sum(cal))