now_time=input()
C=input() #C=요리시간

now_time=now_time.split()
A=now_time[0] #A=시
B=now_time[1] #B=분

A=int(A)
B=int(B)
C=int(C)

if B+C<=59:
    print(A, B+C)
    
if (B+C>=60)and(0<=A<=23):
    if (60<=(B+C)<120):
        if (A<23):
            print(A+1, (B+C)-60)
        if (A==23):
            print(0, (B+C)-60)
    if 120<=(B+C)<180:
        if (A<22):
            print(A+2, (B+C)-120)
        if (A>=22):
            print(A-22, (B+C)-120)
    if 180<=(B+C)<240:
        if (A<21):
            print(A+3, (B+C)-180)
        if (A>=21):
            print(A-21, (B+C)-180)
    if 240<=(B+C)<300:
        if (A<20):
            print(A+4, (B+C)-240)
        if (A<=20):
            print(A-20, (B+C)-240)
    if 300<=(B+C)<360:
        if (A<19):
            print(A+5, (B+C)-300)
        if (A>=19):
            print(A-19, (B+C)-300)
    if 360<=(B+C)<420:
        if (A<18):
            print(A+6, (B+C)-360)
        if (A>=18):
            print(A-18, (B+C)-360)
    if 420<=(B+C)<480:
        if (A<17):
            print(A+7, (B+C)-420)
        if (A>=17):
            print(A-17, (B+C)-420)
    if 480<=(B+C)<540:
        if (A<16):
            print(A+8, (B+C)-480)
        if (A>=16):
            print(A-16, (B+C)-480)
    if 540<=(B+C)<600:
        if (A<15):
            print(A+9, (B+C)-540)
        if (A>=15):
            print(A-15, (B+C)-540)
    if 600<=(B+C)<660:
        if (A<14):
            print(A+10, (B+C)-600)
        if (A>=14):
            print(A-14, (B+C)-600)
    if 660<=(B+C)<720:
        if (A<13):
            print(A+11, (B+C)-660)
        if (A>=13):
            print(A-13, (B+C)-660)
    if 720<=(B+C)<780:
        if (A<12):
            print(A+12, (B+C)-720)
        if (A>=12):
            print(A-12, (B+C)-720)
    if 780<=(B+C)<840:
        if (A<11):
            print(A+13, (B+C)-780)
        if (A>=11):
            print(A-11, (B+C)-780)
    if 840<=(B+C)<900:
        if (A<10):
            print(A+14, (B+C)-840)
        if (A>=10):
            print(A-10, (B+C)-840)
    if 900<=(B+C)<960:
        if (A<9):
            print(A+15, (B+C)-900)
        if (A>=9):
            print(A-9, (B+C)-900)
    if 960<=(B+C)<1020:
        if (A<8):
            print(A+16, (B+C)-960)
        if (A>=8):
            print(A-8, (B+C)-960)
    if 1020<=(B+C)<1080:
        if (A<7):
            print(A+17, (B+C)-1020)
        if (A>=7):
            print(A-7, (B+C)-1020)