S=input()

alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(0,26):
    if alpha[i] in S:
        print(S.find(alpha[i]), end=' ')
    else:
        print(-1, end=' ')