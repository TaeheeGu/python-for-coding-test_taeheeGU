#퀵 정렬
def quick_sort(array, start, end):
  if start >= end: #원소가 1개인 경우 종료
    return

  pivot = start #피벗은 첫 번째 원소
  left = start + 1 #탐색할 범위의 가장 왼쪽
  right = end #탐색 할 범위의 가장 오른쪽

  while left <= right: #left(큰 값)과 right(작은 값)의 위치가 엇갈리기 전까지
    while left <= end and array[left] <= array[pivot]: #피벗보다 큰 값을 찾기까지 반복
      left += 1 #피벗보다 큰 값의 위치를 left로
    while right > start and array[right] >= array[pivot]: #피벗보다 작은 값을 찾기까지 반복
      right -= 1 #피벗보다 작은 값의 위치를 right로
    
    if left > right: #left(큰 값)과 right(작은 값)의 위치가 엇갈린 경우
      array[pivot], array[right] = array[right], array[pivot] #작은 값(right)와 피벗의 위치 교체
    else: #left(큰 값)과 right(작은 값)의 위치가 엇갈리지 않은 경우
      array[left], array[right] = array[right], array[left] #큰 값(left)와 작은 값(right)의 위치 교체
    
  #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행
  quick_sort(array, start, right-1) #왼쪽 부분
  quick_sort(array, right+1, end) #오른쪽 부분

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

quick_sort(array, 0, len(array)-1)

print(array)

#파이썬 문법활용 간단한 구현
def quick_sort2(array):
  if len(array) <= 1: #리스트가 하나 이하의 원소만을 담고 있다면 종료
    return array

  pivot = array[0] #피벗은 첫 번째 원소
  tail = array[1:] #피벗을 제외한 리스트

  left_side = [x for x in tail if x <= pivot] #피벗보다 작은 원소를 분할된 왼쪽 부분으로
  right_side = [x for x in tail if x > pivot] #피벗보다 큰 원소를 분활된 오른쪽 부분으로

  #분할 이후 왼쪽 부분과 오른쪽 부분에 대해 각각 정렬을 수행하고, 전체 리스트를 반환
  return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)


array1 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

print(quick_sort2(array1))