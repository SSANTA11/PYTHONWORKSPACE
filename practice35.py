raw_input=input()

raw_input=raw_input.split()
A=raw_input[0]
B=raw_input[1]

A=int(A)
b=int(B)

if A>B:
    print(">")
if A<B:
    print("<")
if A==B:
    print("==")