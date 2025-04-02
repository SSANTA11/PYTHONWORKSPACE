
from algorism_data_structure_week4_0 import ArrayStack
st=ArrayStack(100)
word=input().upper().replace(" ","")
filtered=""
a=True
for ch in word:
    if ('A'<=ch<='Z'):
        st.push(ch)
        filtered+=ch
for ch in filtered:
    if ch!=st.pop():
        a=False
        break

print(a)

