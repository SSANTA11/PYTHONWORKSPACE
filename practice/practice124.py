# 문자열과 리스트, 딕션너리의 len 함수의 결과 차이 인지하자
dict_a={}
for i in range(10):
    A=int(input())
    C=A%42
    dict_a[C]=0
print(len(dict_a))