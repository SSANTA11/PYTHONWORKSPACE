a=input()
a=a.split()

H=a[0]
M=a[1]

H=int(H)
M=int(M)

if M>=45:
    print(H, (M-45))
if (1<=H<=24)and(M<45):
    print(H-1, (60+(M-45)))
if (H==0)and(M<45):
    print((23), (60+(M-45)))