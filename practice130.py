num=int(input())
for i in range(num):
    if num!=1:
        word=input()
        a=len(word)
        print(f"{word[0]}{word[a-1]}")
    else:
        print(word*2)