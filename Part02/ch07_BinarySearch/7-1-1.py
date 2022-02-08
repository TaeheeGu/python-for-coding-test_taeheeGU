#순차 탐색
def sequential_search(array, target):
  for i in range(len(array)): #각 원소를 하나씩 확인
    if array[i] == target: #각 원소와 찾고자 하는 값 비교
      return i #찾고자 하는 값의 인덱스 반환

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

index = sequential_search(array, 9)

print('타겟 값의 인덱스 : %d' %index)