s=input()

def re(s):
    return s[::-1]

print(re(s))

def re(s):
    s=list(s)
    s=reversed(s)
    return "".join(s)
print(re(s))

def re(s):
    s=list(s)
    s.reverse()
    return "".join(s)
print(re(s))
