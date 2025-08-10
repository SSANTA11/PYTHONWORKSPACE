words_count={}
arr=[]
words,max_count=map(int,input().split())

for _ in range(words):
    word=input()
    if len(word)>=max_count:
        words_count[word]+=1

