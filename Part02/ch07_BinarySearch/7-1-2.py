#이진 탐색(재귀 함수)
def binary_search(array, target, start, end):
  if start > end:
    return None #시작점의 위치가 끝점의 위치를 벗어 날 때

  mid = (start + end)//2 #중간점의 위치

  if target == array[mid]: #타겟 값을 찾은 경우, 타겟 값의 위치가 중간점일 때
    return mid #중간점의 위치 반환
  
  elif target < array[mid]: #타겟 값이 중간점의 값보다 작을 때
    return binary_search(array, target, start, mid-1) #중간점의 왼쪽을 탐색
  
  else: #타겟 값이 중간점의 값보다 클 때
    return binary_search(array, target, mid+1, end) #중간점의 오른쪽을 탐색
  
array = [1, 3, 5, 7, 9, 11, 13, 15] #정렬된 리스트에 대한 탐색이 가능
target = 3

index = binary_search(array, target, 0, len(array)-1)

if index == None:
  print('존재하지 않습니다.')
else:
  print('타겟 값 : {}, 인덱스 : {}'.format(target, index))

#이진 탐색(반복문)
def binary_search2(array, target, start, end):
  while start <= end:
    mid = (start + end)//2 #중간점의 위치

    if target == array[mid]: #타겟 값을 찾은 경우, 타겟 값의 위치가 중간점일 때
      return mid
    
    elif target < array[mid]: #타겟 값이 중간점의 값보다 작을 때
      end = mid - 1 #중간점의 왼쪽을 탐색

    else:  #타겟 값이 중간점의 값보다 클 때
      start = mid + 1 #중간점의 오른쪽을 탐색

  return None  #시작점의 위치가 끝점의 위치를 벗어 날 때

array2 = [2, 4, 6, 8, 10, 12, 14, 16] #정렬된 리스트에 대한 탐색이 가능
target2 = 14

index2 = binary_search2(array2, target2, 0, len(array)-1)

if index2 == None:
  print('존재하지 않습니다.')
else:
  print('타겟 값 : {}, 인덱스 : {}'.format(target2, index2))