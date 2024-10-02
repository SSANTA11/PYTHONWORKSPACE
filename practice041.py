a=input()

a=a.split()

one=int(a[0])
two=int(a[1])
three=int(a[2])

if one==two==three:
    print(10000+100*one)
if one==two!=three:
    print(1000+two*100)
if one!=three==two:
    print(1000+two*100)
if one==three!=two:
    print(1000+100*one)
if (one>two>three) or (one>three>two):
    print(one*100)
if (two>one>three) or (two>three>one):
    print(two*100)
if (three>one>two) or (three>two>one):
    print(three*100)