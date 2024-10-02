num=int(input())

text_dict={}

counter=0

for l in range(num):
    
    texts=input()

    category=None
    
    for text in texts:
        text_dict[text]=0

    for text in texts:
        text_dict[text]+=1

    for key in text_dict:
        dispenser=texts.find(text_dict[key]*key)
        if dispenser!=-1:
            category="ok"
            continue
        else:
            category="out"
            break

    if category=='ok':
        counter+=1
    else:
        None
    text_dict.clear()

print(counter)