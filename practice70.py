numbers=[1,1,2,2,3,3] #리스트 선언
counter={} #딕션너리 선언

for number in numbers: #리스트 요소에 대한 반복문 설정
    if number not in counter: #딕션너리에 숫자가 존재하지 않을 때
        counter[number]=0 #딕션너리에 들어가는 모든 리스트 요소에 0을 할당
    counter[number]+=1 #처리된 딕션너리를 리스트 요소의 갯수만큼 더한다
print(counter)