grade_trans={"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0}

main_discipline_average_component_save=[]

grade_trans_save=[]
count=0

for i in range(20):
    info=input().split()
    if info[2]=="P":
        count+=1
    else:
        main_discipline_average_component_save.append(float(info[1]))
        grade_trans_save.append(grade_trans[info[2]])

s=0
for i in range(20-count):
    s+=(main_discipline_average_component_save[i]*grade_trans_save[i])
print(s/sum(main_discipline_average_component_save))
