# 정렬
# 탐색
# 순차탐색
# 코드 7.8: 이진 탐색  알고리즘(순환 구조)     참고 파일: ch07/basic_search.py
def binary_search(A, key, low, high) :
    if (low > high) :				# 종료 조건: 하나 이상의 항목이 있어야 함
        return -1        			# 탐색 실패

    middle = (low + high) // 2
    print(A[middle], end=' ')
    if (key == A[middle]) :	    # 탐색 성공
        return middle
    elif (key<A[middle]) :	# 왼쪽 부분리스트 탐색
        return binary_search(A, key, low, middle - 1)
    else :						# 오른쪽 부분리스트 탐색
        return binary_search(A, key, middle + 1, high)

# 이진 탐색(반복)
def binary_search_iter(A, key, low, high) :
    while (low <= high) :       	# 항목들이 남아 있으면(종료 조건)
        middle = (low + high) // 2
        print(A[middle], end=' ')
        if key == A[middle]:	    # 탐색 성공
            return middle
        elif (key > A[middle]):	# key가 middle의 값보다 크면
            low = middle + 1		# middle+1 ~ high 사이 검색
        else:						# key가 middle의 값보다 작으면
            high = middle - 1		# low ~ middle-1 사이 검색
    return -1   					# 탐색 실패

# 보간탐색
def interpolation_search(A, key, low, high) :
    while (low <= high) :       	# 항목들이 남아 있으면(종료 조건)
        mid = low + ((high - low) * (key - A[low])) / (A[high] - A[low])
        print(A[mid], end=' ')
        if key == A[mid]:	    # 탐색 성공
            return mid
        elif (key > A[mid]):	# key가 middle의 값보다 크면
            low = mid + 1		# mid+1 ~ high 사이 검색
        else:						# key가 middle의 값보다 작으면
            high = mid - 1		# low ~ mid-1 사이 검색
    return -1   					# 탐색 실패

3445
15*34/45