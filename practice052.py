#리스트명.append(요소)
#리스트명.insert(위치, 요소)

#리스트 생성
list_a=[1,2,3]

#리스트 뒤에 요소 추가하기
print("#리스트 뒤에 요소 추가하기")
list_a.append(4)
print(list_a)
list_a.append(5)
print(list_a)
print()

#리스트 중간에 요소 추가하기>>>>insert(위치, 요소)
print("#리스트 중간에 요소 추가하기")
list_a.insert(5,10)
print(list_a)