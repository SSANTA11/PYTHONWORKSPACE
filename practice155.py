alpha=[
    'a','b','c','d',
    'e','f','g','h',
    'i','j','k','l',
    'n','m','o','p',
    'q','r','s','t',
    'u','v','w','x',
    'y','z'
        ]
cro_alpha=[
    'c=','c-','dz=',
    'd-','lj','nj',
    's=','z='
            ]

counter=0
cro_texts=input()

if 'dz=' in cro_texts:
    counter+=cro_texts.count("dz=")
    cro_texts=cro_texts.replace('dz=',' ')

for ch in cro_alpha:
    if ch in cro_texts:
        counter+=cro_texts.count(ch)
        cro_texts=cro_texts.replace(ch,' ')

for ch in alpha:
    if ch in cro_texts:
        counter+=cro_texts.count(ch)
print(counter)