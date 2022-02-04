#선택 정렬
def selection_sort(array):
  for i in range(len(array)):
    min_index = i #정렬이 안된 가장 왼쪽의 원소
    for j in range(i+1, len(array)): #정렬이 된 원소 다음 부터
      if array[j] < array[min_index]: #가장 작은 원소를 찾는다
        min_index = j #가장 작은 원소의 인덱스
    array[min_index], array[i] = array[i], array[min_index]
    #가장 작은 원소와 정렬이 안된 가장 왼쪽의 원소와 교환
  
  return array

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

print(selection_sort(array))
      