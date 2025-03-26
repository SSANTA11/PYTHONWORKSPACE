t_dict={}
t_list=[]
tt_list=[]
final=[]
texts=input().upper()

for text in texts:
    t_dict[text]=0
    
for text in texts:
    t_dict[text]+=1

for text in t_dict:
    t_list.append([text,t_dict[text]])

for i in range(len(t_list)):
    tt_list.append(t_list[i][1])
tt_list.sort(reverse=True)
max_num=tt_list[0]

for i in range(len(t_list)):
    if t_list[i][1]==max_num:
        final.append(t_list[i][0])
        continue
if len(final)!=1:
    print("?")
else:
    print(final[0])