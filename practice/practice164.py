N=int(input())
l=[]
e={"q":[25,0],"d":[10,0],"n":[5,0],"p":[1,0]}
f=["q","d","n","p"]
g=[]

for n in range(N):
    a=int(input())
    l.append(a)

for n in range(N):
    b=l[n]
    for v in f:
        i=0
        while True:
            i+=1
            if b<e[v][0]*i:
                b=b-e[v][0]*(i-1)
                e[v][1]=i-1
                break
            else:
                continue
            break
    m=[e[v][1] for v in f]
    g.append(m)

for i in range(len(g)):
    for r in g[i]:
        print(r, end=" ")
    print()
        