from random import randint

r1=randint(1,45)
r2=randint(1,45)
while r1==r2:
    r2=randint(1,45)
print(f"Lotto 숫자는{r1, r2} 입니다.")

i=1
r3=randint(1,45)
r4=randint(1,45)

while (r1!=r3) or (r2!=r4):
        r3=randint(1,45)
        r4=randint(1,45)
        print(f"{i} ({r3}, {r4})")
        i+=1

print(f"{i}번만에 당첨되었습니다!!")