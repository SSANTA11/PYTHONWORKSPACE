def long(s):
    h=""
    a=s.split()
    for i in a:
        if len(h)<len(i):
            h=i
    return h

print(long("오늘은 어쩌면 반환점이 되는 시기이지 않을까?"))