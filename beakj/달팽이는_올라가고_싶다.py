# snail
# advance
# branch
# reverse
# spend_day

info=input().split()

adv=int(info[0])
rev=int(info[1])
bran=int(info[2])

i=1

while True:
        # if bran//(adv-rev)>10:
        #      bran-=(adv-rev)*10
        #      i+=10
        # else:
    if bran-adv<=0:
        print(i)
        break
    else:
        bran-=(adv-rev)
        i+=1
        print(i)