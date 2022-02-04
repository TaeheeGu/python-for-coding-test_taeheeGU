#삽입 정렬
def insertion_sort(array):
  #삽입 정렬은 두 번째 원소부터 시작
  for i in range(1, len(array)): #첫 번째 원소는 정렬이 되어 있다고 판단
    for j in range(i, 0, -1): #정렬이 안된 가장 왼쪽 원소부터 왼쪽의 정렬된 원소와 비교
      if array[j] < array[j-1]: #정렬이 안된 원소가 왼쪽의 원소보다 작으면 해당 원소의 왼쪽에 삽입
        array[j], array[j-1] = array[j-1], array[j]
      else:
        break #자기보다 작은 원소가 왼쪽에 있으면 정렬이 된 상태
  
  return array

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

print(insertion_sort(array))