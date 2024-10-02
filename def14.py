# 문제1: 문자열 필터링
def filter_str(lst,word):
   save=[]
   for l in lst:
        if word in l:
           save.append(l)
   return save

# 문제2: 리스트 중첩 해제
def lst_flat(nested_list):
    a=[]
    for i in nested_list:
        if type(i)!=list:
            a.append(i)
        else:
            a.extend(lst_flat(i))
    return a
print(lst_flat([1,2,3,[4,5,7,10]]))

# # 문제3: 조건에 따른 리스트 필터링
# def filter_by_condition(lst, condition):
#     for ch in lst:
#         if condition(ch)==True:
#             return "good"
#         else:
#             return "bad"
# def condition(a):
#     if len(a)<10:
#         return False
#     else:
#         return True

" ".join(list)
# 문제4: 리스트의 평균 계산
def std(lst):
    return sum(lst)/len(lst)

# 문제5:문자열 길이의 합
def str_length(lst):
    a=0
    for st in lst:
        a+=len(st)
    return a