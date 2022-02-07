#계수 정렬
def count_sort(array):
  sorted_array = []
  count = [0] * (max(array) + 1) #array의 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)

  for i in range(len(array)):
    count[array[i]] += 1 #각 데이터에 해당하는 인덱스의 값 증가

  for i in range(len(count)): #count 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
      sorted_array.append(i) #count 리스트의 등장 횟수만큼 기록
  
  return sorted_array

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8, 9, 1, 5, 7]

print(count_sort(array))