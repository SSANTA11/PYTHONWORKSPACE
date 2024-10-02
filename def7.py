s=int(input())

def pi(s):
    i=0
    f=[0,1]
    if s!=1:
        while len(f)!=s:
            f.append(f[len(f)-2]+f[len(f)-1])
        return f
    elif s==1:
        return  [0]
    elif s==0:
        return []

print(pi(s))
